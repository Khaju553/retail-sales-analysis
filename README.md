\# Retail Sales Performance Analysis



\## Project Overview



This project analyzes retail sales data to understand overall business performance, identify profitable and loss-making product areas, evaluate regional performance, and study the relationship between discounts and profit.



The analysis follows a complete data analyst workflow:



\*\*Raw Data → Data Cleaning → SQL Analysis → Power BI Visualization → Business Insights\*\*



The main goal of this project is to answer:



> \*\*Where is the business performing well, and where is profit being lost?\*\*



\---



\## Business Objectives



The main objectives of this analysis are to:



\- Measure total sales, total profit, and overall profit margin.

\- Compare sales and profitability across product categories.

\- Analyze regional sales and profit performance.

\- Identify profitable and loss-making sub-categories.

\- Study how different discount levels are associated with profitability.

\- Identify high-sales products that are generating losses.

\- Analyze yearly sales and profit trends.

\- Build an interactive Power BI dashboard for business decision-making.



\---



\## Dataset Overview



The project uses the \*\*Superstore retail sales dataset\*\*, containing \*\*9,994 transaction records\*\* and 21 original columns.



The dataset includes information related to:



\- Orders

\- Shipping dates

\- Customers

\- Customer segments

\- Geographic locations

\- Product categories

\- Product sub-categories

\- Sales

\- Quantity

\- Discounts

\- Profit



During data preparation, additional analytical columns were created:



\- `order\_year`

\- `order\_month`

\- `shipping\_days`

\- `profit\_margin`



After preprocessing, the cleaned dataset contains:



\*\*9,994 rows and 25 columns\*\*



\---



\## Tools and Technologies



\### Python



Python was used for:



\- Loading the raw dataset

\- Exploratory data analysis

\- Data cleaning

\- Data validation

\- Date conversion

\- Feature engineering

\- Exporting the cleaned dataset



Main Python library used:



\- Pandas



\---



\### SQL



SQL was used to answer business questions related to:



\- Overall sales and profit

\- Category performance

\- Regional performance

\- Sub-category profitability

\- Discount vs profit

\- Furniture profitability

\- Top-selling products

\- Loss-making products

\- Yearly sales and profit trends



\---



\### SQLite



SQLite was used as the local relational database.



The cleaned dataset was loaded into an `orders` table and analyzed using SQL queries.



\---



\### Power BI



Power BI was used to build an interactive business dashboard containing:



\- Total Sales KPI

\- Total Profit KPI

\- Profit Margin KPI

\- Sales and Profit by Category

\- Sales and Profit by Region

\- Yearly Sales and Profit Trend

\- Sub-Category Profitability

\- Discount vs Profit

\- Top 10 Loss-Making Products

\- Interactive Year filter

\- Interactive Region filter

\- Interactive Category filter



\---



\### Visual Studio Code



Visual Studio Code was used as the main development environment for:



\- Python scripts

\- SQL queries

\- Project documentation

\- Git and GitHub workflow



\---



\## Data Cleaning and Preparation



The raw dataset was cleaned and prepared using Python and Pandas before loading it into SQLite and Power BI.



The following steps were performed:



\- Loaded the raw CSV file using Pandas.

\- Checked the dataset shape.

\- Reviewed column names.

\- Checked data types.

\- Checked missing values.

\- Checked duplicate records.

\- Confirmed the dataset contained \*\*9,994 rows and 21 original columns\*\*.

\- Confirmed that there were no missing values.

\- Confirmed that there were no duplicate rows.

\- Converted `Order Date` into datetime format.

\- Converted `Ship Date` into datetime format.

\- Standardized all column names.

\- Converted column names to lowercase.

\- Replaced spaces with underscores.

\- Replaced hyphens with underscores.



Important numeric columns were validated:



\- `sales`

\- `quantity`

\- `discount`

\- `profit`



The analysis checked for:



\- Negative sales

\- Zero or negative quantities

\- Discounts outside the valid range

\- Negative-profit transactions



The dataset contained \*\*1,871 loss-making transaction rows\*\*.



These records were retained because they represent valid business outcomes rather than data-quality errors.



\---



\## Feature Engineering



Additional analytical columns were created using Python.



\### Order Year



Created from `order\_date` to support yearly analysis.



\### Order Month



Created from `order\_date` to support time-based analysis.



\### Shipping Days



Calculated using:



`ship\_date - order\_date`



This represents the number of days required to ship an order.



\### Profit Margin



Calculated using:



`Profit Margin = Profit / Sales × 100`



The cleaned dataset was saved as:



`data/superstore\_clean.csv`



The final cleaned dataset contains:



\*\*9,994 rows and 25 columns\*\*



\---



\## Database Preparation



The cleaned CSV dataset was loaded into SQLite using Python.



The SQLite database file is:



`retail\_sales.db`



The main database table is:



`orders`



The table contains all cleaned retail transaction records used for SQL analysis.



\---



\## SQL Analysis



The SQL analysis focused on nine major business questions.



\### 1. Overall Business Performance



The overall business generated approximately:



\- \*\*Total Sales: $2.30M\*\*

\- \*\*Total Profit: $286.40K\*\*

\- \*\*Profit Margin: 12.47%\*\*



This indicates that the business is profitable overall.



\---



\### 2. Category Performance



Category-level analysis produced the following results:



| Category | Sales | Profit |

|---|---:|---:|

| Technology | $836.15K | $145.45K |

| Furniture | $742.00K | $18.45K |

| Office Supplies | $719.05K | $122.49K |



\### Key Finding



\*\*Technology\*\* generated both the highest sales and the highest profit.



\*\*Furniture\*\* generated strong revenue but relatively low profit.



This demonstrates that:



> High sales do not automatically mean high profitability.



\---



\## Regional Performance



Regional analysis produced:



| Region | Sales | Profit |

|---|---:|---:|

| West | $725.46K | $108.42K |

| East | $678.78K | $91.52K |

| Central | $501.24K | $39.71K |

| South | $391.72K | $46.75K |



\### Key Finding



The \*\*West\*\* region was the strongest-performing region.



The \*\*Central\*\* region generated more sales than South but produced less profit.



This indicates weaker profitability in Central relative to its sales volume.



\---



\## Sub-Category Profitability



Sub-category analysis identified several loss-making areas.



Major loss-making sub-categories included:



\- \*\*Tables:\*\* approximately \*\*-$17.73K\*\*

\- \*\*Bookcases:\*\* approximately \*\*-$3.47K\*\*

\- \*\*Supplies:\*\* approximately \*\*-$1.19K\*\*



The largest loss was generated by the \*\*Tables\*\* sub-category.



Other highly profitable sub-categories included:



\- Copiers

\- Phones

\- Accessories

\- Paper

\- Binders

\- Chairs



\### Key Finding



The profitability problem within Furniture is mainly concentrated in:



\- Tables

\- Bookcases



\---



\## Discount vs Profit Analysis



Discount-level analysis showed a strong relationship between increasing discounts and declining profitability.



Important observations included:



\- 0% discount generated strong positive profit.

\- 10% discounts remained profitable.

\- 20% discounts remained profitable overall.

\- 30% discounts generated negative aggregate profit.

\- Higher discount levels generally produced larger losses.



Discount levels of approximately \*\*30% and above were associated with negative aggregate profitability\*\*.



This finding represents an association within the dataset and does not necessarily prove that discounts alone caused the losses.



\---



\## Furniture Profitability Analysis



Further analysis was performed on Furniture sub-categories.



Approximate average discount levels showed:



\- Tables: 26.13%

\- Bookcases: 21.11%

\- Chairs: 17.02%

\- Furnishings: 13.83%



Tables had both:



\- The highest average discount among the major Furniture sub-categories

\- The largest overall loss



This suggests that aggressive discounting may be one contributing factor to Furniture profitability issues.



\---



\## Product-Level Analysis



The analysis also examined individual products.



Several products generated high sales but negative profit.



Examples include:



\- Cisco TelePresence System EX90 Videoconferencing Unit

\- GBC DocuBind P400 Electric Binding System

\- High Speed Automatic Electric Letter Opener



This demonstrates that:



> Revenue alone is not sufficient for evaluating product performance.



Profitability must also be considered.



\---



\## Top Loss-Making Products



Some of the largest loss-making products included:



\- Cubify CubeX 3D Printer Double Head Print

\- Lexmark MX611dhe Monochrome Laser Printer

\- Cubify CubeX 3D Printer Triple Head Print

\- Chromcraft Bull-Nose Wood Oval Conference Tables \& Bases

\- Bush Advantage Collection Racetrack Conference Table

\- GBC DocuBind P400 Electric Binding System

\- Cisco TelePresence System EX90 Videoconferencing Unit

\- Martin Yale Chadless Opener Electric Letter Opener

\- Balt Solid Wood Round Tables

\- BoxOffice By Design Rectangular and Half-Moon Meeting Room Tables



Several of these products belong to the \*\*Tables\*\* sub-category, supporting the sub-category-level profitability finding.



\---



\## Yearly Sales and Profit Trend



Yearly performance was:



| Year | Sales | Profit |

|---|---:|---:|

| 2014 | $484.25K | $49.54K |

| 2015 | $470.53K | $61.62K |

| 2016 | $609.21K | $81.80K |

| 2017 | $733.22K | $93.44K |



\### Key Findings



\- Sales decreased slightly from 2014 to 2015.

\- Sales increased strongly in 2016.

\- Sales increased further in 2017.

\- Profit increased every year.

\- \*\*2017 was the strongest year\*\* in both sales and profit.



Overall business performance improved significantly during the analyzed period.



\---



\## Power BI Dashboard



An interactive Power BI dashboard was created to communicate the analytical findings.



The dashboard contains three major KPIs:



\- Total Sales

\- Total Profit

\- Profit Margin



The dashboard also includes:



\- Sales and Profit by Category

\- Sales and Profit by Region

\- Yearly Sales and Profit Trend

\- Sub-Category Profitability

\- Discount vs Profit

\- Top 10 Loss-Making Products



Interactive slicers allow users to filter the dashboard by:



\- Year

\- Region

\- Category



The KPI cards and charts automatically update according to the selected filters.



\---



\## Business Recommendations



Based on the analysis, the following recommendations could improve profitability.



\### Review High Discount Levels



Products receiving discounts of approximately \*\*30% or more\*\* should be reviewed carefully because these discount levels are associated with negative aggregate profit.



\---



\### Investigate the Tables Sub-Category



Tables generated the largest sub-category loss.



Management should review:



\- Pricing

\- Product costs

\- Discount policies

\- Supplier costs

\- Shipping costs

\- Product-level margins



\---



\### Review Loss-Making Products



High-sales products generating negative profit should be analyzed individually.



The company should determine whether losses are caused by:



\- Excessive discounts

\- High product costs

\- Shipping expenses

\- Pricing strategy

\- Low margins



\---



\### Improve Central Region Profitability



The Central region generates substantial sales but weaker profit compared with other regions.



Further analysis should investigate:



\- Product mix

\- Discount levels

\- Customer segments

\- Shipping costs

\- Regional pricing



\---



\### Continue Supporting Strong Categories



Technology generates both high sales and high profit.



The business could continue investing in profitable Technology products while monitoring product-level margins.



\---



\## Project Structure



```text

retail-sales-analysis/

│

├── data/

│   ├── superstore\_raw.csv

│   └── superstore\_clean.csv

│

├── scripts/

│   ├── 01\_explore\_data.py

│   ├── 02\_clean\_data.py

│   ├── 03\_load\_database.py

│   └── 04\_run\_sql.py

│

├── sql/

│   └── business\_analysis.sql

│

├── dashboard/

│   └── retail\_sales\_dashboard.pbix

│

├── retail\_sales.db

│

├── .gitignore

│

└── README.md

```



\---



\## Project Workflow



The complete project follows this workflow:



`Raw CSV Data`



↓



`Python Data Exploration`



↓



`Python Data Cleaning`



↓



`Feature Engineering`



↓



`Cleaned CSV`



↓



`SQLite Database`



↓



`SQL Business Analysis`



↓



`Power BI Dashboard`



↓



`Business Insights and Recommendations`



\---



\## Key Business Insights



The main findings from the project are:



1\. The business generated approximately \*\*$2.30M in sales\*\* and \*\*$286.40K in profit\*\*.

2\. Overall profit margin was approximately \*\*12.47%\*\*.

3\. Technology was the strongest category in terms of profit.

4\. Furniture generated high sales but relatively low profit.

5\. Tables were the largest loss-making sub-category.

6\. West was the strongest-performing region.

7\. Central generated relatively high sales but weaker profitability.

8\. Discount levels of approximately 30% and above were associated with negative aggregate profit.

9\. Some high-revenue products were still loss-making.

10\. Profit increased every year between 2014 and 2017.

11\. 2017 was the strongest year in both sales and profit.



\---



\## Conclusion



This project demonstrates an end-to-end data analytics workflow using Python, SQL, SQLite, and Power BI.



The project transforms raw retail transaction data into actionable business insights by combining:



\- Data cleaning

\- Data validation

\- SQL analysis

\- Business-focused visualization

\- Interactive dashboard development

\- Business recommendations



The analysis shows that strong sales alone do not guarantee strong profitability.



Product-level profitability, discount strategy, regional performance, and category-level margins all need to be monitored together when making business decisions.

