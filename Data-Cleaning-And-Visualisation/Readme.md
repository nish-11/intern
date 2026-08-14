\# Data Cleaning \& Visualization Project



\## Project Overview



This project focuses on cleaning, processing, analyzing, and visualizing a raw sales dataset using Python.



The dataset contains information about products, categories, quantities, prices, customer cities, and customer ratings.



\## Technologies Used



\- Python

\- Pandas

\- Matplotlib

\- Seaborn

\- Microsoft Excel



\## Data Cleaning



The following data-cleaning techniques were performed:



\- Identified and handled missing values.

\- Filled the missing customer city using the most frequent city.

\- Filled the missing rating using the average rating.

\- Identified and removed duplicate records.

\- Standardized inconsistent city names.

\- Detected an outlier using the IQR method.

\- Corrected an erroneous laptop price.



\## Data Visualization



The following visualizations were created:



1\. Total Quantity Sold by Product

2\. Total Revenue by Product

3\. Total Quantity Sold by City

4\. Customer Rating Distribution

5\. Correlation Heatmap



\## Key Findings



\- Mouse had the highest quantity sold.

\- Laptop generated the highest revenue.

\- Delhi had the highest total quantity sold among the cities.

\- Customer ratings were mainly concentrated around the higher rating values.

\- The correlation heatmap was used to examine relationships between numerical variables.



\## Project Structure



```text

Data-Cleaning-And-Visualisation/

│

├── sales\_dataset.xlsx

├── sales\_dataset.csv

├── data\_cleaning\_visualization.py

├── README.md

└── visualizations/

&#x20;   ├── product\_sales.png

&#x20;   ├── product\_revenue.png

&#x20;   ├── city\_sales.png

&#x20;   ├── rating\_distribution.png

&#x20;   └── correlation\_heatmap.png
 


### Save it

Press **Ctrl + S**.

Your final folder should look like:

```text
Data-Cleaning-And-Visualisation
│
├── sales_dataset.xlsx
├── sales_dataset.csv
├── data_cleaning_visualization.py
├── README.md
└── visualizations
    ├── product_sales.png
    ├── product_revenue.png
    ├── city_sales.png
    ├── rating_distribution.png
    └── correlation_heatmap.png
