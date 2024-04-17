# E-commerce RFM Customer Segmentation

### Table of Contents
- [Project Overview](#project-overview)
- [Data Sources](#data-sources)
- [Recommendation](#recommendation)
  
### Prorject Overview

In this analysis, we aim to segment customers into different categories to better understand their behavior and preferences. By doing so, we can tailor our marketing strategies and product offerings to meet the needs of each segment more effectively. The ultimate goal of this segmentation analysis is to identify the segments that contribute to 80% of our revenue, allowing us to focus our resources and efforts on the most profitable customer groups.

This approach is inspired by the Pareto principle, also known as the 80/20 rule, which suggests that roughly 80% of the effects come from 20% of the causes. In our context, we apply this principle to customer segmentation, recognizing that a relatively small percentage of customer segments may account for a significant majority of our revenue.

<img width="625" alt="image" src="https://github.com/Huy24vt/Portfolio-Projects/assets/130732635/ad934769-34f0-4b58-a213-6750025c5463">

### Data Sources
Online Retail: This is a transnational data set which contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail. [Source here](https://archive.ics.uci.edu/dataset/352/online+retail)

### Tools
 • Python: Data Cleaning and Analysis
 
 • PBI(PowerBi): Visualization

 ### Data Cleaning
 In the initial preperation phase, I perform following tasks:
 1. Load data.
 2. Handle missing data.
 3. Inspect data types.
 4. Engineer features.

 ### EDA (Explore Data Analysis)
 Exploratory Data Analysis (EDA) involves delving into sales data to uncover insights and answer key questions that can inform business decisions. Here are a few key questions:

 - What is the overall sales?
   
<img width="336" alt="image" src="https://github.com/Huy24vt/RFM-Segmentation/assets/130732635/61671bad-2104-4da4-91c4-467346656d74">

 - How do sales vary on a weekly and monthly basis?
 - How do sales vary on an hourly basis?

<img width="389" alt="image" src="https://github.com/Huy24vt/RFM-Segmentation/assets/130732635/e8caf20a-a4ab-4372-9459-5cc74ca3dadd">

   
 - Which days of the week have the highest sales performance?

<img width="401" alt="image" src="https://github.com/Huy24vt/RFM-Segmentation/assets/130732635/ddef3ccc-af2d-4ef5-80e9-b09fcec51703">


 ### Data Analysis
In order to gain deeper insights into customer behavior and segment our customer base effectively, I conducted an in-depth analysis using the RFM framework. RFM stands for Recency, Frequency, and Monetary value, three key metrics that provide valuable insights into customer engagement and purchasing behavior.

To create the RFM table, I first calculated the Recency, which measures how recently a customer made a purchase. This involved analyzing the timestamp of each customer's most recent purchase and calculating the time elapsed since then. Next, I calculated the Frequency, which measures how often a customer makes a purchase. This required analyzing the entire purchase history of each customer and determining the number of transactions they've made over a given period of time. Lastly, I calculated the Monetary value, which represents the monetary amount spent by each customer. This involved summing up the total spending of each customer across all transactions.

Once I had calculated the RFM values for each customer, I assigned scores to create segments. For Recency, customers who made a purchase more recently received a higher score, indicating higher engagement. Similarly, for Frequency, customers who made more frequent purchases received a higher score, indicating greater loyalty. For Monetary value, customers who spent more money received a higher score, indicating higher value.

<img width="412" alt="image" src="https://github.com/Huy24vt/RFM-Segmentation/assets/130732635/e51b279e-2cdc-4a8e-9efb-f273bd64e9df">


### Results
 [You can view the dashboard here](https://app.powerbi.com/view?r=eyJrIjoiYTI3ZjM1YTItZjlhOS00MzY3LWFkMzQtMzA2ZTIzNjYzNGQyIiwidCI6IjJmODVkYzc0LWI2YjQtNDU4NC1iZWVlLWNjZGE3MTQ0NDk3MCIsImMiOjZ9)
 
The analysis of our sales data has provided valuable insights that can guide strategic decision-making for the business. One key finding is that the top 20% of customers contribute to nearly 80% of the revenue, highlighting the significance of focusing on high-value customer segments. To optimize revenue generation and achieve the coveted 80-20 gold metric, our primary target should be these top-performing customers. By prioritizing efforts to retain and grow relationships with these customers, we can maximize revenue and profitability.

<img width="425" alt="image" src="https://github.com/Huy24vt/RFM-Segmentation/assets/130732635/067bfbe7-30c2-4e5b-954a-b6b1b8ca0b21">

Moreover, the analysis indicates that the business is experiencing positive momentum and is well-positioned to expand its customer base. This presents an opportunity for growth and market expansion. To capitalize on this momentum and further enhance our competitive position, it is imperative to invest in understanding customers' needs, preferences, and behaviors. By gaining deeper insights into customer motivations and pain points, we can tailor our products and services to better meet their demands and drive customer satisfaction and loyalty.

 ### Recommendation
 1. Invest in understanding customers' needs, preferences, and behaviors.
 2. Identify new opportunities and potential threats in the market.
 3. Strategic alliances can open up new markets or enhance product/service offerings.

In conclusion, the analysis underscores the importance of prioritizing high-value customers, investing in market understanding, and embracing strategic partnerships to drive sustainable growth and success for the business.
