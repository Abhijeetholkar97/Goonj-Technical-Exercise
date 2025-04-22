# Data Processing Utilities

A collection of standalone Python scripts for common data‑processing tasks, including validation, API integration, testing, querying, and reporting.

---

## Table of Contents

- [Prerequisites](#prerequisites)  
- [Installation](#installation)  
- [Scripts & Usage](#scripts--usage)  
  - [Exercise 1: Data Validation & Transformation](#exercise-1-data-validation--transformation)  
  - [Exercise 2: REST API Integration & Processing](#exercise-2-rest-api-integration--processing)  
  - [Exercise 3: Debugging & Testing](#exercise-3-debugging--testing)  
  - [Exercise 4: Database Querying & Reporting](#exercise-4-database-querying--reporting)  
- [Notes & Configuration](#notes--configuration)  

---

## Prerequisites

- **Python** 3.7 or higher  
- **pip** package manager  

---

## Installation

Install all the third‑party dependencies with:

```bash
pip install pandas matplotlib requests python-dateutil pytest
```
Note:
The Exercise_3.py script uses only the standard library, so it has no extra requirements.

Scripts & Usage


## Exercise 1: Data Validation & Transformation
Script: DataValidationAndTransformation.py

Purpose:

-Validate phone, gender, and age fields in DistributorsData.csv

-Split rows into cleaned and invalid CSV files

-Print summary statistics

-Plot a bar chart of people per state

-Dependencies: pandas, matplotlib

# Run the script

```bash
python DataValidationAndTransformation.py
```
Defaults to DistributorsData.csv in the same folder as the script

Outputs:

cleaned_list.csv (valid rows)

invalid_list.csv (invalid rows)

people_per_state.png (bar chart)




## Exercise 2: REST API Integration & Processing
Script: RESTAPIIntegrationAndProcessing.py

Purpose:

-Fetch inventory data from a mock REST endpoint

-Filter items where quantity < 50

-Save a CSV report of low‑stock items

Dependencies: requests

# Run the script
```bash
python RESTAPIIntegrationAndProcessing.py
```
Output: low_quantity_report.csv

Columns: item_id, item_name, quantity, location


## Exercise 3: Debugging & Testing
Script: correct_script.py

Purpose:

-Load volunteer records from CSV

-Filter by city

-Calculate average volunteer hours

-Handle file‑ and data‑parsing errors

-Includes built‑in unit tests

Dependencies: Python standard library only



# Run the script
```bash
python correct_script.py 
```
# To run all test
```bash
python -m pytest
```

## Exercise 4: Database Querying & Reporting

Script: DatabaseQueryingAndReporting.py

Purpose:

-Analyze MockDonations.csv

-Identify donors with total donations > ₹10,000 in the last 3 months

-Summarize total donations by city

Dependencies: pandas, python-dateutil

# Run the script
```bash
python DatabaseQueryingAndReporting.py
```
Defaults to MockDonations.csv in the same folder as the script

Outputs:

donors_over_10000.csv (donor_name, TotalAmount)

city_donation_summary.csv (city, NumberOfDonors, TotalAmount)

## Notes & Configuration
    Make sure your are in the correct folder before running the script.

    All scripts print status messages and write outputs to the current working directory.

    Each script expects its input CSV file to be located in the same folder as the script.

    To customize file paths or numeric thresholds, edit the configuration block at the top of each script.

