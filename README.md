# E-commerce RFM Customer Segmentation

### Table of Contents
- [Project Overview](#project-overview)
- [Data Sources](#data-sources)
- [Recommendation](#recommendation)
  
### Prorject Overview
This analysis aims to segment customers into groups, focusing on identifying the segments that contribute to 80% of revenue. The goal is to enhance decision-making and drive strategic improvements in our business.

<img width="625" alt="image" src="https://github.com/Huy24vt/Portfolio-Projects/assets/130732635/ad934769-34f0-4b58-a213-6750025c5463">

### Data Sources
Online Retail: This is a transnational data set which contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail. [Download here](https://archive.ics.uci.edu/dataset/352/online+retail)

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
 EDA involved explore Sales data to answers few key questions:

 - What is the overall sales?
   
<img width="336" alt="image" src="https://github.com/Huy24vt/RFM-Segmentation/assets/130732635/61671bad-2104-4da4-91c4-467346656d74">

 - How do sales vary on a weekly and monthly basis?
 - How do sales vary on an hourly basis?

<img width="389" alt="image" src="https://github.com/Huy24vt/RFM-Segmentation/assets/130732635/e8caf20a-a4ab-4372-9459-5cc74ca3dadd">

   
 - Which days of the week have the highest sales performance?

<img width="401" alt="image" src="https://github.com/Huy24vt/RFM-Segmentation/assets/130732635/ddef3ccc-af2d-4ef5-80e9-b09fcec51703">


 ### Data Analysis
I created an RFM table by calculating the Recency (how recently a customer made a purchase), Frequency (how often a customer makes a purchase), and Monetary value (the monetary amount spent by a customer) for each customer. Afterward, I assigned scores based on the RFM values to create segments.

<img width="290" alt="image" src="https://github.com/Huy24vt/Portfolio-Projects/assets/130732635/73ca218f-6b47-4192-8369-a73a8ff46a94">

### Results
 [You can view the dashboard here](https://app.powerbi.com/view?r=eyJrIjoiYTI3ZjM1YTItZjlhOS00MzY3LWFkMzQtMzA2ZTIzNjYzNGQyIiwidCI6IjJmODVkYzc0LWI2YjQtNDU4NC1iZWVlLWNjZGE3MTQ0NDk3MCIsImMiOjZ9)
 
 The analysis results are summarized as follow:
 1. A very good metric is that the top 20% of customers contribute to nearly 80% of the revenue.
 2. To reach the 80-20 gold metric, our target should be these customers.
 3. The business is experiencing positive momentum and is prepared to expand its customer base.

 ### Recommendation
 1. Invest in understanding customers' needs, preferences, and behaviors.
 2. Identify new opportunities and potential threats in the market.
 3. Strategic alliances can open up new markets or enhance product/service offerings.
