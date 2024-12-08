 # Importing necessary libraries
import pandas as pd
import numpy as np
import re  # For regex

# Import mapping dictionaries
from mapping import (
    gender_mapping,
    employment_status_mapping,
    industry_group_mapping,
    occupation_group_mapping,
    never_got_flu_shots_mapping,
    how_often_smoke_cigarettes_mapping,
    general_health_mapping,
    race_ethnicity_mapping,
    highest_education_mapping,
    high_blood_pressure_diagnosis_mapping,
    diabetes_diagnosis_mapping,
    outpatient_visits_mapping,
    region_mapping,
    covid_vaccine_mapping,
    covid_booster_shot_mapping,
    employer_offers_health_insurance_mapping
    # Add other mappings as needed
)

# File paths for the datasets (update with actual paths)
file_paths = [
    "meps_ins_data_2018.csv",
    "meps_ins_data_2019.csv",
    "meps_ins_data_2020.csv",
    "meps_ins_data_2021.csv",
    "meps_ins_data_2022.csv"
]

# Placeholder for processed data
data_list = []

# Columns to combine across years (including new fields)
combined_columns = [
    "TOTEXP", "TOTSLF", "FAMINC", "RXEXP", "OPTOTV", "DVTEXP", 
    "DDNWRK", "ASTHAGED", "REGION"
]

# Selected columns to extract and process
selected_columns = {
    "DUPERSID": "DUPERSID",
    "AGELAST": "AGELAST",  # Person's age
    "SEX": "SEX",          # Gender
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
    "ENDRFY": "ENDRFY"  # Year of data
}

# Column renaming for final output
rename_columns = {
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

# Values to drop rows for
invalid_values = [-15]

# Load and process each year's data
for file in file_paths:
    # Extract year from the filename (assuming year is part of the filename)
    year = re.search(r'\d{4}', file).group(0)
    year_suffix = year[-2:]  # Get last two digits of the year (e.g., 21 for 2021)

    # Load the data
    df = pd.read_csv(file)

    # Dynamically select columns for the current year
    selected_columns_year = {f"{col}{year_suffix}": f"{col}{year_suffix}" for col in combined_columns}

    # Add selected columns to the DataFrame
    selected_columns.update(selected_columns_year)

    # Check which columns are available in the dataset
    matched_columns = {new_name: col_name for new_name, col_name in selected_columns.items() if col_name in df.columns}
    missing_columns = [col_name for col_name in selected_columns.values() if col_name not in df.columns]

    # Print debug information about missing columns
    if missing_columns:
        print(f"File: {file} | Missing Columns: {missing_columns}")

    # Proceed only with matched columns
    if matched_columns:
        df = df.rename(columns=matched_columns)[list(matched_columns.keys())]
    else:
        continue  # Skip this file if no matched columns exist

    # Combine year-specific columns into unified columns
    for col in combined_columns:
        year_specific_cols = [c for c in df.columns if re.match(f"{col}(21|22|17|18|19|20)", c)]
        if year_specific_cols:
            df[col] = df[year_specific_cols].bfill(axis=1).iloc[:, 0].astype(float)
            df.drop(columns=year_specific_cols, inplace=True)

    # Handle missing values for CVVACCINE53 and BOOSTERSHOT53
    if "CVVACCINE53" in df.columns:
        df["CVVACCINE53"].fillna(-1, inplace=True)
    else:
        df["CVVACCINE53"] = -1  # Add column with default value if missing

    if "BOOSTERSHOT53" in df.columns:
        df["BOOSTERSHOT53"].fillna(-1, inplace=True)
    else:
        df["BOOSTERSHOT53"] = -1  # Add column with default value if missing

    # Add a "Year" column for identification
    df["Year"] = int(year)

    # Rename columns according to the new naming convention
    df.rename(columns=rename_columns, inplace=True)

    # Apply mappings
    if "Gender" in df.columns:
        df["Gender"] = df["Gender"].map(gender_mapping)
    if "Employment_Status" in df.columns:
        df["Employment_Status"] = df["Employment_Status"].map(employment_status_mapping)
    if "Industry_Group" in df.columns:
        df["Industry_Group"] = df["Industry_Group"].map(industry_group_mapping)
    if "Occupation_Group" in df.columns:
        df["Occupation_Group"] = df["Occupation_Group"].map(occupation_group_mapping)
    if "Never_Got_Flu_Shots" in df.columns:
        df["Never_Got_Flu_Shots"] = df["Never_Got_Flu_Shots"].map(never_got_flu_shots_mapping)
    if "How_Often_Smoke_Cigarettes" in df.columns:
        df["How_Often_Smoke_Cigarettes"] = df["How_Often_Smoke_Cigarettes"].map(how_often_smoke_cigarettes_mapping)
    if "General_Health" in df.columns:
        df["General_Health"] = df["General_Health"].map(general_health_mapping)
    if "Race_Ethnicity" in df.columns:
        df["Race_Ethnicity"] = df["Race_Ethnicity"].map(race_ethnicity_mapping)
    if "Highest_Education" in df.columns:
        df["Highest_Education"] = df["Highest_Education"].map(highest_education_mapping)
    if "High_Blood_Pressure_Diagnosis" in df.columns:
        df["High_Blood_Pressure_Diagnosis"] = df["High_Blood_Pressure_Diagnosis"].map(high_blood_pressure_diagnosis_mapping)
    if "Diabetes_Diagnosis" in df.columns:
        df["Diabetes_Diagnosis"] = df["Diabetes_Diagnosis"].map(diabetes_diagnosis_mapping)
    if "Outpatient_Visits" in df.columns:
        df["Outpatient_Visits"] = df["Outpatient_Visits"].map(outpatient_visits_mapping)
    if "Region" in df.columns:
        df["Region"] = df["Region"].map(region_mapping)
    if "COVID_Vaccine" in df.columns:
        df["COVID_Vaccine"] = df["COVID_Vaccine"].map(covid_vaccine_mapping)
    if "COVID_Booster_Shot" in df.columns:
        df["COVID_Booster_Shot"] = df["COVID_Booster_Shot"].map(covid_booster_shot_mapping)
    if "Employer_Offers_Health_Insurance" in df.columns:
        df["Employer_Offers_Health_Insurance"] = df["Employer_Offers_Health_Insurance"].map(employer_offers_health_insurance_mapping)

    # Remove rows with invalid values for specific columns
   # df = df[~df["Age_of_Diabetes_Diagnosis"].isin(invalid_values)]
   # df = df[~df["Age_of_High_Blood_Pressure_Diagnosis"].isin(invalid_values)]
    df = df[~df["Days_Missed_Work"].isin(invalid_values)]

    # Append the processed DataFrame to the list
    data_list.append(df)

# Combine all years of data into a single DataFrame
all_data = pd.concat(data_list, ignore_index=True)
all_data = all_data.drop('Outpatient_Visits', axis=1)
# Save the final combined dataset
output_file = "combined_meps_data.csv"
all_data.to_csv(output_file, index=False)
print(f"Final combined data saved to {output_file}")
print(all_data.columns)
