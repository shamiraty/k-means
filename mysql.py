import streamlit as st
import pandas as pd
import mysql.connector
from sklearn.cluster import KMeans
import plotly.express as px

# Streamlit app setup
st.set_page_config(layout="wide")
st.title("K-MEANS CLUSTERING: CUSTOMER SEGMENTATION")
st.subheader("Dynamically Segment Customers Using K-Means and MySQL (Based on Age and Income)")

# MySQL connection setup
def get_mysql_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="knn"
    )

# Function to fetch data from MySQL
def read_data_from_database():
    connection = get_mysql_connection()
    query = "SELECT Age, Income, Customer_Type FROM large_customer_data"
    df = pd.read_sql(query, connection)
    connection.close()
    return df

# Function to fetch segment names dynamically from MySQL
def fetch_segment_names():
    connection = get_mysql_connection()
    query = "SELECT DISTINCT Customer_Type FROM large_customer_data"
    df_segments = pd.read_sql(query, connection)
    connection.close()

    # Map segment names dynamically based on sorted order
    segment_map = {i: segment for i, segment in enumerate(df_segments["Customer_Type"].sort_values().tolist())}
    return segment_map

# Fetch data and segment names
df = read_data_from_database()
segment_map = fetch_segment_names()

# Display dataset
with st.expander("Original Dataset"):
 st.dataframe(df, use_container_width=True)

# Extract features for clustering
X = df[["Age", "Income"]]

# Apply K-Means clustering
kmeans = KMeans(n_clusters=len(segment_map), random_state=42)
df["Customer_Segment"] = kmeans.fit_predict(X)

# Map clusters to segment names dynamically
df["Customer_Segment"] = df["Customer_Segment"].map(segment_map)

# Display segmented dataset, sorted by Customer Segment
with st.expander("Predicted Segmented Dataset"):
 df_sorted = df.sort_values(by="Customer_Segment")  # Sort by segment
 st.dataframe(df_sorted, use_container_width=True)

# Group by customer segments for detailed analytics
st.subheader("Customer Analytics by Predicted Segment")
analytics_df = df.groupby("Customer_Segment").agg(
    customer_count=("Customer_Segment", "count"),
    total_income=("Income", "sum"),
    avg_age=("Age", "mean"),
).reset_index()

# Calculate percentage for each segment
analytics_df["percent"] = (analytics_df["customer_count"] / analytics_df["customer_count"].sum()) * 100

# Sort the analytics data to get the segments with the highest count first
analytics_df = analytics_df.sort_values(by="customer_count", ascending=False)

# Display the analytics table
st.dataframe(analytics_df, use_container_width=True)

# Generate the summary text for the segments
highest_segment = analytics_df.iloc[0]
second_segment = analytics_df.iloc[1] if len(analytics_df) > 1 else None
last_segment = analytics_df.iloc[-1] if len(analytics_df) > 2 else None

# Construct the descriptive text
summary_text = f"""
- The most high-frequency predicted segment is **{highest_segment['Customer_Segment']}** with a percent of **{highest_segment['percent']:.2f}%** and a total of **{highest_segment['customer_count']}** customers. 

"""
if second_segment is not None:
    summary_text += f"""
- The next predicted segment is **{second_segment['Customer_Segment']}** with a percent of **{second_segment['percent']:.2f}%** and a total of **{second_segment['customer_count']}** customers. 
"""

if last_segment is not None:
    summary_text += f"""
- The last predicted segment is **{last_segment['Customer_Segment']}** with a percent of **{last_segment['percent']:.2f}%** and a total of **{last_segment['customer_count']}** customers.
"""

# Display the summary text
st.markdown(summary_text)

 

# Display additional insights
st.subheader("Segment Insights")
st.write("""
The table above provides key insights into the customer segments, including:
1. **Number of Customers in Each Segment**: The total count of customers assigned to each segment.
2. **Total Income**: The sum of income for customers within each segment.
3. **Average Age**: The mean age of customers in each segment.
4. **Percentage of Each Segment**: The percentage of total customers that belong to each segment, ordered from highest to lowest.
""")

# Sidebar for new record prediction
with st.sidebar.form("prediction_form"):
    st.subheader("Enter New Record for Prediction")
    age = st.number_input("Age", min_value=0)
    income = st.number_input("Income", min_value=0)
    submit_button = st.form_submit_button("Predict")

    if submit_button:
        # Predict segment for the new record
        new_record = [[age, income]]
        new_cluster = kmeans.predict(new_record)[0]
        new_segment = segment_map[new_cluster]
        
        # Show prediction result
        st.sidebar.success(f"The predicted Customer Segment is: {new_segment}")

        # Optionally save new record to the database
        connection = get_mysql_connection()
        cursor = connection.cursor()
        query = "INSERT INTO large_customer_data (Age, Income, Customer_Type) VALUES (%s, %s, %s)"
        cursor.execute(query, (age, income, new_segment))
        connection.commit()
        connection.close()

# Display model insights
st.subheader("Model Insights")
st.success(f"Number of Clusters: {len(segment_map)}")
st.success(f"Predicted Customer Segments: {', '.join(segment_map.values())}")

# Visualization of Customer Segments
st.subheader("Cluster Visualization")
if not df.empty:    
    # Group data by Customer Segment
    customer_count = df['Customer_Segment'].value_counts().reset_index()
    customer_count.columns = ['Customer_Segment', 'Count']    
    # Plotly Bar Chart
    fig = px.bar(
        customer_count,
        x="Customer_Segment",
        y="Count",
        color="Customer_Segment",
        title="Customer Segments Count",
        labels={"Customer_Segment": "Customer Segment", "Count": "Number of Customers"},
        text="Count"
    )
    
    fig.update_traces(textposition='outside')
    st.plotly_chart(fig)
else:
    st.warning("No data available in the database.")