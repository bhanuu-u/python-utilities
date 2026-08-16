import pandas as pd


# ============================================================
# 1. LOAD THE CSV FILE
# ============================================================

df = pd.read_csv("csv_cleaner_test.csv")

# Store original row count for the final report
original_rows = len(df)


# ============================================================
# 2. INSPECT THE DATA
# ============================================================

print("\n========== CSV INFORMATION ==========")

# Check the number of rows and columns
print("Shape:")
print(df.shape)

# Display the column names
print("\nColumns:")
print(df.columns)

# Display information about columns, data types and missing values
print("\nInformation:")
df.info()


# ============================================================
# 3. CLEAN COLUMN NAMES
# ============================================================

# Get all the original column names
col = df.columns

# Create an empty list to store cleaned column names
clean_columns = []

# Clean each column name
for column in col:

    # Remove spaces from the beginning and end
    column = column.strip()

    # Convert the column name to lowercase
    column = column.lower()

    # Replace spaces between words with underscores
    column = column.replace(" ", "_")

    # Add the cleaned column name to the list
    clean_columns.append(column)

# Replace the original column names with the cleaned names
df.columns = clean_columns


# ============================================================
# 4. REMOVE WHITE SPACE FROM TEXT DATA
# ============================================================

# Find columns that contain text
text_columns = df.select_dtypes(include="str").columns

# Go through each text column
for column in text_columns:

    # Remove leading and trailing spaces from text values
    df[column] = df[column].str.strip()


# ============================================================
# 5. REMOVE COMPLETELY EMPTY ROWS
# ============================================================

# Count completely empty rows before removing them
empty_rows = df.isnull().all(axis=1).sum()

# Remove a row only when ALL values in that row are missing
df = df.dropna(how="all")

print("\nCompletely empty rows removed:", empty_rows)


# ============================================================
# 6. DETECT DUPLICATES
# ============================================================

# Count the number of duplicate rows
duplicates = df.duplicated().sum()

print("Duplicate rows found:", duplicates)


# ============================================================
# 7. REMOVE DUPLICATES
# ============================================================

# Remove duplicate rows
df = df.drop_duplicates()

print("Duplicate rows after cleaning:", df.duplicated().sum())


# ============================================================
# 8. CHECK AND HANDLE MISSING VALUES
# ============================================================

# Count missing values in each column
null_values = df.isnull().sum()

# Calculate total number of missing values
total_missing = null_values.sum()


if total_missing == 0:

    print("\nNo missing values found.")

else:

    print("\n========== MISSING VALUES ==========")
    print(null_values[null_values > 0])

    print("\nChoose how to handle missing values:")
    print("1. Leave them unchanged")
    print("2. Remove rows containing missing values")
    print("3. Fill numeric missing values with mean")
    print("4. Fill numeric missing values with median")

    choice = input("\nEnter your choice: ")


    # --------------------------------------------------------
    # OPTION 1 — Leave missing values unchanged
    # --------------------------------------------------------

    if choice == "1":

        print("\nMissing values left unchanged.")


    # --------------------------------------------------------
    # OPTION 2 — Remove rows containing missing values
    # --------------------------------------------------------

    elif choice == "2":

        rows_before = len(df)

        # Remove rows containing at least one missing value
        df = df.dropna()

        rows_removed = rows_before - len(df)

        print("\nRows containing missing values have been removed.")
        print("Rows removed:", rows_removed)


    # --------------------------------------------------------
    # OPTION 3 — Fill numeric columns with MEAN
    # --------------------------------------------------------

    elif choice == "3":

        # Find numeric columns
        numeric_columns = df.select_dtypes(include="number").columns

        for column in numeric_columns:

            # Check whether this column contains missing values
            if df[column].isnull().sum() > 0:

                # Calculate the mean of the column
                mean_value = df[column].mean()

                # Fill missing values with the mean
                df[column] = df[column].fillna(mean_value)

        print("\nNumeric missing values filled using MEAN.")


    # --------------------------------------------------------
    # OPTION 4 — Fill numeric columns with MEDIAN
    # --------------------------------------------------------

    elif choice == "4":

        # Find numeric columns
        numeric_columns = df.select_dtypes(include="number").columns

        for column in numeric_columns:

            # Check whether this column contains missing values
            if df[column].isnull().sum() > 0:

                # Calculate the median of the column
                median_value = df[column].median()

                # Fill missing values with the median
                df[column] = df[column].fillna(median_value)

        print("\nNumeric missing values filled using MEDIAN.")


    # --------------------------------------------------------
    # INVALID OPTION
    # --------------------------------------------------------

    else:

        print("\nInvalid choice.")
        print("Missing values have been left unchanged.")


# ============================================================
# 9. RESET THE INDEX
# ============================================================

# Reset the index after ALL row-removing operations.
#
# drop=True means:
# Throw away the old index and create a fresh index.
#
# Example:
# 0, 2, 5, 7  →  0, 1, 2, 3

df = df.reset_index(drop=True)


# ============================================================
# 10. FINAL CHECK
# ============================================================

# Count remaining missing values
remaining_missing = df.isnull().sum().sum()

# Count remaining duplicates
remaining_duplicates = df.duplicated().sum()

# Final number of rows
final_rows = len(df)


print("\n========== FINAL REPORT ==========")

print("Original rows:", original_rows)
print("Final rows:", final_rows)

print("Empty rows removed:", empty_rows)
print("Duplicate rows removed:", duplicates)
print("Duplicates remaining:", remaining_duplicates)

print("Missing values remaining:", remaining_missing)


# ============================================================
# 11. DISPLAY CLEANED DATA
# ============================================================

print("\n========== CLEANED DATA ==========")
print(df)


# ============================================================
# 12. SAVE CLEANED CSV
# ============================================================

# Create the output filename
output_file = "csv_cleaner_test_cleaned.csv"

# Save the cleaned DataFrame
# index=False prevents Pandas from creating an extra index column
df.to_csv(output_file, index=False)

print("\nCleaned CSV saved as:", output_file)

print("\n========== CLEANING COMPLETE ==========")