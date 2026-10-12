# CSV Cleaner

A Python utility built with Pandas to clean, standardize, and prepare messy CSV files for data analysis and processing.

## Overview

CSV Cleaner simplifies common data-cleaning tasks by providing options to handle inconsistent column names, unnecessary whitespace, duplicate records, empty rows, and missing values. It allows users to inspect datasets, apply cleaning operations, generate a final report, and export the cleaned data while keeping the original CSV file unchanged.

## Features

### 1. CSV Loading and Inspection
- Load CSV files using Pandas.
- Display dataset shape, column names, and basic information.
- Inspect the dataset before applying cleaning operations.

### 2. Column Name Standardization
- Convert column names to lowercase.
- Remove leading and trailing whitespace.
- Replace spaces with underscores.

**Example:**

| Original | Cleaned |
|---|---|
| Customer Name | customer_name |
| Product Price | product_price |
| Order Date | order_date |

### 3. Text Cleaning
- Remove leading and trailing whitespace from text values.
- Improve consistency across text-based columns.

### 4. Empty Row and Duplicate Removal
- Identify and remove completely empty rows.
- Detect duplicate records.
- Remove duplicate rows to improve dataset consistency.

### 5. Missing Value Handling
- Detect missing values and display their counts.
- Choose to leave missing values unchanged.
- Remove rows containing missing values.
- Fill missing numeric values using the column mean.
- Fill missing numeric values using the column median.

### 6. Cleaning Report
- Display the final dataset shape.
- Summarize the cleaning results.
- Review the dataset after applying the selected operations.

### 7. Export Cleaned Data
- Save the cleaned dataset as a new CSV file.
- Preserve the original file without overwriting it.
- Prepare the cleaned dataset for further analysis.

## Technologies Used

- Python
- Pandas

## Installation

Clone the repository:

```bash
git clone https://github.com/bhanuu-u/python-utilities.git
```

Navigate to the project directory:

```bash
cd python-utilities/csv_cleaner
```

Install the required library:

```bash
pip install pandas
```

## Usage

Run the Python script:

```bash
python main.py
```

1. Enter the path to the CSV file.
2. Inspect the dataset information.
3. Apply the required cleaning operations.
4. Select a missing value handling strategy, if needed.
5. Review the final cleaning report.
6. Export the cleaned dataset to a new CSV file.

## Project Structure

```text
csv_cleaner/
├── main.py
└── README.md
```

## What I Implemented

- CSV loading and dataset inspection using Pandas.
- Column name standardization and whitespace removal.
- Empty row and duplicate record removal.
- Missing value detection and handling strategies.
- DataFrame index resetting after cleaning.
- Final cleaning report generation.
- Export functionality that preserves the original dataset.

## Applications

- Preparing datasets for exploratory data analysis.
- Cleaning data before visualization.
- Preparing CSV files for machine learning workflows.
- Standardizing datasets collected from different sources.

## Author

**A. Revanth Bhanu**
