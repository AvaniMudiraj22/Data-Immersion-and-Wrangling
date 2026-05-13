# TASK - 1 : DATA IMMERSION & WRANGLING
# Import Library
import pandas as pd
# STEP 1 : LOAD DATASET
print("====================================")
print(" DATA IMMERSION & WRANGLING PROJECT ")
print("====================================")

try:
    df = pd.read_csv("dataset.csv")
    print("\nDataset Loaded Successfully!\n")

except FileNotFoundError:
    print("\nERROR : dataset.csv file not found!")
    exit()

# STEP 2 : DISPLAY DATASET
print("------------- ORIGINAL DATASET -------------\n")
print(df)
# STEP 3 : DATASET INFORMATION

print("\n------------- DATASET INFO -------------\n")
print(df.info())

# STEP 4 : CHECK MISSING VALUES
print("\n------------- MISSING VALUES -------------\n")
print(df.isnull().sum())
# STEP 5 : CHECK DUPLICATES
print("\n------------- DUPLICATE ROWS -------------\n")

duplicate_count = df.duplicated().sum()

print("Number of Duplicate Rows :", duplicate_count)

# Remove duplicate rows
df = df.drop_duplicates()

print("\nDuplicate Rows Removed Successfully!")
# STEP 6 : CLEAN POSTAL CODE COLUMN
print("\n------------- CLEANING POSTAL CODE -------------\n")

# Fill missing postal codes with median
median_postal = df["Postal Code"].median()

df["Postal Code"] = df["Postal Code"].fillna(median_postal)

print("Missing Postal Codes Filled!")
# STEP 7 : STANDARDIZE DATE FORMAT
print("\n------------- STANDARDIZING DATE FORMAT -------------\n")

df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    errors="coerce"
)

df["Ship Date"] = pd.to_datetime(
    df["Ship Date"],
    errors="coerce"
)

print("Date Format Standardized!")
# STEP 8 : FEATURE ENGINEERING
print("\n------------- FEATURE ENGINEERING -------------\n")

# Create Sales Category Column
df["Sales_Category"] = df["Sales"].apply(
    lambda x: "High Sales" if x > 500 else "Low Sales"
)

print("New Column 'Sales_Category' Created!")
# STEP 9 : FINAL CLEANED DATASET
print("\n------------- CLEANED DATASET -------------\n")
print(df)
# STEP 10 : SAVE CLEANED DATASET
df.to_csv("cleaned_dataset.csv", index=False)

print("\nCleaned Dataset Saved Successfully!")
# STEP 11 : CREATE DATA DICTIONARY
dictionary_text = """
==============================
DATA DICTIONARY
==============================

Row ID            : Unique Row Identifier
Order ID          : Unique Order Identifier
Order Date        : Date of Order
Ship Date         : Shipping Date
Ship Mode         : Shipping Method
Customer ID       : Unique Customer ID
Customer Name     : Name of Customer
Segment           : Customer Segment
Country           : Country Name
City              : City Name
State             : State Name
Postal Code       : Postal Code
Region            : Region Name
Product ID        : Product Identifier
Category          : Product Category
Sub-Category      : Product Sub Category
Product Name      : Name of Product
Sales             : Sales Amount
Sales_Category    : High Sales or Low Sales
"""

with open("data_dictionary.txt", "w") as file:
    file.write(dictionary_text)

print("\nData Dictionary Created Successfully!")
# STEP 12 : COMPLETION MESSAGE
print("\n====================================")
print(" DATA CLEANING COMPLETED SUCCESSFULLY ")
print("====================================")