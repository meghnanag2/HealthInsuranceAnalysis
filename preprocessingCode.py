import pandas as pd
import numpy as np
import re  # For regex

# File paths for the datasets
file_paths = [
    "meps_ins_data_2018.csv",
    "meps_ins_data_2019.csv",
    "meps_ins_data_2020.csv",
    "meps_ins_data_2021.csv",
    "meps_ins_data_2022.csv"
]

# Placeholder for processed data
data_list = []

# Columns to combine across years
combined_columns = [
    "TOTEXP", "TOTSLF", "FAMINC", "RXEXP", "OPTOTV", "DVTEXP",
    "DDNWRK", "ASTHAGED", "REGION", "FAMINC"
]

# Selected columns to extract and process
selected_columns = {
    "DUPERSID": "DUPERSID",
    "AGELAST": "AGELAST",
    "SEX": "SEX",
    "EMPST53H": "EMPST53H",
    "INDCT53H": "INDCT53H",
    "OFREMP53": "OFREMP53",
    "OCCCAT53": "OCCCAT53",
    "DSFLNV53": "DSFLNV53",
    "CVVACCINE53": "CVVACCINE53",
    "BOOSTERSHOT53": "BOOSTERSHOT53",
    "OFTSMK53": "OFTSMK53",
    "ADGENH42": "ADGENH42",
    "RACETHX": "RACETHX",
    "HIDEG": "HIDEG",
    "HIBPDX": "HIBPDX",
    "DIABAGED": "DIABAGED",
    "DIABDX_M18": "DIABDX_M18",
    "HIBPAGED": "HIBPAGED",
    "ENDRFY": "ENDRFY"
}

# Column renaming for final output
rename_columns = {
    "FAMINC22": "Family Income",
    "DUPERSID": "Person_ID",
    "AGELAST": "Age",
    "SEX": "Gender",
    "REGION": "Region",
    "TOTEXP": "Total_Expenditures",
    "TOTSLF": "Total_Self_Payment",
    "FAMINC": "Family_Income",
    "RXEXP": "Total_Prescription_Expenditures",
    "OPTOTV": "Outpatient_Visits",
    "DVTEXP": "Dental_Care_Expenditures",
    "DDNWRK": "Days_Missed_Work",
    "DIABAGED": "Age_of_Diabetes_Diagnosis",
    "DIABDX_M18": "Diabetes_Diagnosis",
    "HIBPAGED": "Age_of_High_Blood_Pressure_Diagnosis",
    "HIBPDX": "High_Blood_Pressure_Diagnosis",
    "ASTHAGED": "Age_of_Asthma_Diagnosis",
    "EMPST53H": "Employment_Status",
    "INDCT53H": "Industry_Group",
    "OFREMP53": "Employer_Offers_Health_Insurance",
    "OCCCAT53": "Occupation_Group",
    "CVVACCINE53": "COVID_Vaccine",
    "BOOSTERSHOT53": "COVID_Booster_Shot",
    "OFTSMK53": "How_Often_Smoke_Cigarettes",
    "ADGENH42": "General_Health",
    "RACETHX": "Race_Ethnicity",
    "HIDEG": "Highest_Education",
    "DSFLNV53": "Never_Got_Flu_Shots",
    "ENDRFY": "Year"
}

# Invalid values for removal
invalid_values = [-15]

# Load and process each year's data
for file in file_paths:
    # Extract year from the filename
    year = re.search(r'\d{4}', file).group(0)
    year_suffix = year[-2:]  # Last two digits of the year

    # Load the dataset
    df = pd.read_csv(file)

    # Add year-specific columns to the selected columns
    selected_columns_year = {f"{col}{year_suffix}": f"{col}{year_suffix}" for col in combined_columns}
    selected_columns.update(selected_columns_year)

    # Match available columns in the dataset
    matched_columns = {new_name: col_name for new_name, col_name in selected_columns.items() if col_name in df.columns}
    missing_columns = [col_name for col_name in selected_columns.values() if col_name not in df.columns]

    # Print missing columns
    if missing_columns:
        print(f"File: {file} | Missing Columns: {missing_columns}")

    # Rename and filter columns
    if matched_columns:
        df = df.rename(columns=matched_columns)[list(matched_columns.keys())]
    else:
        continue

    # Combine year-specific columns into unified columns
    for col in combined_columns:
        year_specific_cols = [c for c in df.columns if re.match(f"{col}(21|22|18|19|20)", c)]
        if year_specific_cols:
            df[col] = df[year_specific_cols].bfill(axis=1).iloc[:, 0].astype(float)
            df.drop(columns=year_specific_cols, inplace=True)

    # Fill missing values for vaccine and booster shot columns
    if "CVVACCINE53" in df.columns:
        df["CVVACCINE53"] = df["CVVACCINE53"].fillna(-1)
    else:
        df["CVVACCINE53"] = -1  # Add column with default value if missing

    if "BOOSTERSHOT53" in df.columns:
        df["BOOSTERSHOT53"] = df["BOOSTERSHOT53"].fillna(-1)
    else:
        df["BOOSTERSHOT53"] = -1  # Add column with default value if missing

    # Add a "Year" column
    df["Year"] = int(year)

    # Rename columns according to the new naming convention
    df.rename(columns=rename_columns, inplace=True)

    # Filter for valid age range (18-64)
    df = df[(df["Age"] >= 18) & (df["Age"] <= 64)]

    # Remove rows with invalid values
    df = df[~df["Days_Missed_Work"].isin(invalid_values)]

    # Append the processed DataFrame to the list
    data_list.append(df)

# Combine all years of data into a single DataFrame
all_data = pd.concat(data_list, ignore_index=True)
all_data = all_data.drop('Outpatient_Visits', axis=1, errors='ignore')

# Save the final combined dataset
output_file = "combined_meps_data_new.csv"
all_data.to_csv(output_file, index=False)
print(f"Final combined data saved to {output_file}")
print(all_data.columns)
