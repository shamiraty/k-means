# K-MEANS CLUSTERING: CUSTOMER SEGMENTATION

## Live Demo
You can view the live demo of this project at:  
[**K-Means Clustering for Customer Segmentation**](https://k-means-algorithm.streamlit.app/)

## Technologies

| Technology     | Description                                                                                          |
|----------------|------------------------------------------------------------------------------------------------------|
| **Python**     | The core programming language used for implementing the algorithm and handling the data.            |
| **Streamlit**  | A framework used to create an interactive web application for visualizing the model's predictions and analytics. |
| **SQL Statements** | Used to interact with the MySQL database to read and write customer data.                           |
| **MySQL**      | A relational database management system used to store customer data for clustering and analytics.     |

## Applied Domains

| Role                                | Description                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------|
| **Statisticians**                   | Professionals who apply statistical techniques to collect, analyze, and interpret data for various purposes. |
| **Healthcare and Medicine**         | Medical professionals and researchers who use data analysis to improve patient care and medical research. |
| **Finance and Economics**           | Experts who use data and statistical models to make financial and economic decisions. |
| **Marketing and Customer Analytics**| Professionals who analyze consumer data to optimize marketing strategies and enhance customer experiences. |
| **Environmental Scientist**         | Scientists who apply data analysis, modeling, and statistical methods to study environmental changes, conservation efforts, and sustainability initiatives. |
| **Data Scientist**                  | Specialists in analyzing and interpreting complex data to provide actionable insights across various domains. |
| **Operational Research**            | Analysts who apply advanced mathematical and statistical models to help organizations solve complex problems. |

## Main Objective

The main objective of this project is to implement the **K-Means Clustering** algorithm to dynamically segment customers based on their **Age** and **Income** into distinct clusters. This segmentation helps businesses better understand their customer base and provides valuable insights for targeted strategies.

### Key Goals:
1. **Dynamic Segmentation**: Automatically group customers into clusters such as VIP, Regular, Gold, and Premium based on their data.
2. **Analytics**: Provide detailed insights into each cluster, including metrics like customer count, average income, and average age.
3. **Interactive Visualization**: Allow users to interact with the clustered data through a web-based interface.

---

## Simple Analytics and Cluster-Specific Insights

- **Cluster Analysis**: The project provides an analysis of the clustered dataset, focusing on key metrics within each segment:
    - **Cluster Distribution**: The number of customers assigned to each cluster, providing an overview of the customer base composition.
    - **Behavioral Insights**: Analysis of key behavioral metrics such as average income and age within each cluster to identify trends.
    - **Demographic Insights (If Available):** If demographic data (e.g., location) is available, analysis of these features within each cluster can provide additional insights.

- **Overall Customer Insights**: Basic statistics about the entire dataset, including the total number of unique customers and the distribution of key metrics like income and age.

These analytics help businesses identify and understand distinct customer groups for better decision-making.

---

## MySQL Database Connection and Data Handling

1. **MySQL Connection Setup**: Establishes a connection to the MySQL database to read and write customer data.
2. **Read Data**: Retrieves customer data (**Age**, **Income**, **Customer_Type**) from the database for clustering.
3. **Save Predictions**: Saves the predicted customer segments back into the database for future reference and analysis.

---

## Customer Analytics

The app groups the customer data by **Predicted Segment** and calculates the following metrics:
- **Customer Count**: The number of customers in each predicted segment.
- **Total Income**: The total income of customers in each segment.
- **Average Age**: The average age of customers in each segment.
- **Segment Percentage**: The percentage of customers in each segment relative to the total.

These analytics are displayed in an interactive table and visualized using charts.

---

## K-Means Clustering Process

1. **Feature Selection**: The features used for clustering are **Age** and **Income**.
2. **Cluster Initialization**: The number of clusters is dynamically determined based on distinct customer types in the database.
3. **K-Means Algorithm**: The K-Means model groups customers into clusters by minimizing the within-cluster sum of squares.
4. **Cluster Mapping**: The clusters are mapped to customer segments (VIP, Regular, Gold, Premium) for easier interpretation.

---

## New Customer Segmentation

A sidebar form allows users to input new records (**Age** and **Income**) for clustering. The model dynamically assigns the new customer to a predicted cluster, which is saved to the MySQL database.

---

## Displaying Results

1. **Original Dataset**: Displays the dataset retrieved from the database, including original customer types.
2. **Segmented Dataset**: Displays the dataset with predicted segments after clustering.
3. **Cluster Insights**: Provides detailed analytics and insights into each cluster, such as customer count, total income, and average age.

---

## Interpretation

1. **Clustered Dataset**: The dataset shows the predicted clusters for each customer. The column `Customer_Segment` contains the cluster assignment.
2. **Cluster Insights**: Key metrics for each cluster are displayed, providing actionable insights into customer groups.
3. **Interactive Visualization**: Users can interact with the segmented data and explore different clusters dynamically.

---

## Conclusion

This Streamlit application implements a **K-Means Clustering** model for customer segmentation based on age and income. It provides real-time insights into customer groups and enables businesses to make data-driven decisions for targeted marketing and personalized experiences.

**My Contacts**

**WhatsApp**  
+255675839840  
+255656848274

**YouTube**  
[Visit my YouTube Channel](https://www.youtube.com/channel/UCjepDdFYKzVHFiOhsiVVffQ)

**Telegram**  
+255656848274  
+255738144353

**PlayStore**  
[Visit my PlayStore Developer Page](https://play.google.com/store/apps/dev?id=7334720987169992827&hl=en_US&pli=1)

**GitHub**  
[Visit my GitHub](https://github.com/shamiraty/)
