# Mapping dictionaries

gender_mapping = {
    1: "Male",
    2: "Female"
}

employment_status_mapping = {
    -1: "Inapplicable",
    1: "Employed",
    2: "Job To Return",
    34: "Not Employed"
}


industry_group_mapping = {
    -15: "Inapplicable",
    -8: "Inapplicable",
    -1: "Inapplicable",
    1: "Natural Resources",
    2: "Mining",
    3: "Construction",
    4: "Manufacturing",
    5: "Wholesale and Retail Trade",
    6: "Transportation and Utilities",
    7: "Information",
    8: "Financial Activities",
    9: "Professional and Business Services",
    10: "Education, Health, and Social Services",
    11: "Leisure and Hospitality",
    12: "Other Services",
    13: "Public Administration",
    14: "Military",
    15: "Unclassifiable Industry"
}

occupation_group_mapping = {
    -15: "Inapplicable",
    -2: "Inapplicable",
    -1: "Inapplicable",
    1: "Management, Business, and Financial Operations",
    2: "Professional and Related Occupations",
    3: "Service Occupations",
    4: "Sales and Related Occupations",
    5: "Office and Administrative Support",
    6: "Farming, Fishing, and Forestry",
    7: "Construction, Extraction, and Maintenance",
    8: "Production, Transportation, and Material Moving",
    9: "Military Specific Occupations",
    10: "Education, Health, and Social Services",
    11: "Unclassifiable Occupation"
}

never_got_flu_shots_mapping = {
    2: "No",
    1: "Yes",
    -8: "Inapplicable",
    -15: "Inapplicable",
    -1: "Inapplicable"
}

employer_offers_health_insurance_mapping = {
    2: "No",
    1: "Yes",
    -8: "Inapplicable",
    -1: "Inapplicable",
    -15: "Inapplicable",
    -7:"Inapplicable"
}

how_often_smoke_cigarettes_mapping = {
    -15: "Inapplicable",
    -8: "Inapplicable",
    -7: "Inapplicable",
    -1: "Inapplicable",
    1: "Every day",
    2: "Some days",
    3: "Not at all"
}

general_health_mapping = {
    -15: "Inapplicable",
    -8: "Inapplicable",
    -7: "Inapplicable",
    -1:"Inapplicable",
    1: "Excellent",
    2: "Very Good",
    3: "Good",
    4: "Fair",
    5: "Poor"
}

race_ethnicity_mapping = {
    -15: "Inapplicable",
    -8: "Inapplicable",
    -1: "Inapplicable",
    1: "Hispanic",
    2: "Non-Hispanic White Only",
    3: "Non-Hispanic Black Only",
    4: "Non-Hispanic Asian Only",
    5: "Non-Hispanic Other Race or Multiple Race"
}

highest_education_mapping = {
    -15: "Inapplicable",
    -8: "Inapplicable",
    -7: "Inapplicable",
    1: "No Degree",
    2: "GED",
    3: "High School Diploma",
    4: "Bachelor's Degree",
    5: "Master's Degree",
    6: "Doctorate Degree",
    7: "Other Degree",
    8: "Inapplicable"
}

high_blood_pressure_diagnosis_mapping = {
    -15: "Inapplicable",
    -8: "Inapplicable",
    -1: "Inapplicable",
    -7: "Inapplicable",
    2: "No",
    1: "Yes"
}

age_of_diabetes_diagnosis_mapping = {
    -1: "Inapplicable",
    -7: "Inapplicable",
    -8: "Inapplicable"
}

diabetes_diagnosis_mapping = {
    -15: "Inapplicable",
    -1: "Inapplicable",
    -8: "Inapplicable",
    -7: "Inapplicable", 
    1: "Yes",
    2: "No"
}

age_of_high_blood_pressure_diagnosis_mapping = {
    -1: "Inapplicable",
    -7: "Inapplicable",
    -8: "Inapplicable"
}

outpatient_visits_mapping = {
    0: "No",
    1: "Yes"
}

days_missed_work_mapping = {
    -15: "Inapplicable",
    -8: "Inapplicable",
    -7: "Inapplicable",
    -1: "Inapplicable"
}

region_mapping = {
    -1:"Inapplicable",
    1: "Northeast",
    2: "Midwest",
    3: "South",
    4: "West"
}

covid_vaccine_mapping = {
    -15: "Inapplicable",
    -8: "Inapplicable",
    -7:"Inapplicable",
    -1: "Inapplicable",
    1: "Yes",
    2: "No"
}

covid_booster_shot_mapping = {
    -15: "Inapplicable",
    -8: "Inapplicable",
    -7:"Inapplicable",
    -1: "Inapplicable",
    1: "Yes",
    2: "No"
}

# Example usage code:
# df['Gender'] = df['SEX'].map(gender_mapping)
# df['Employment_Status'] = df['EMPST53'].map(employment_status_mapping)
# df['Industry_Group'] = df['INDCT53H'].map(industry_group_mapping)
# df['Occupation_Group'] = df['OCCCAT53'].map(occupation_group_mapping)
# df['Never_Got_Flu_Shots'] = df['DSFLNV53'].map(never_got_flu_shots_mapping)
# df['Smoking_Frequency'] = df['OFTSMK53'].map(how_often_smoke_cigarettes_mapping)
# f['General_Health'] = df['ADGENH42'].map(general_health_mapping)
# df['Race_Ethnicity'] = df['RACETHX'].map(race_ethnicity_mapping)
# df['Highest_Education'] = df['HIDEG'].map(highest_education_mapping)
# df['High_Blood_Pressure_Diagnosis'] = df['HIBPDX'].map(high_blood_pressure_diagnosis_mapping)
# df['Age_of_Diabetes_Diagnosis'] = df['DIABAGED'].map(age_of_diabetes_diagnosis_mapping)
# df['Diabetes_Diagnosis'] = df['DIABDX_M18'].map(diabetes_diagnosis_mapping)
# df['Age_of_High_Blood_Pressure_Diagnosis'] = df['HIBPAGED'].map(age_of_high_blood_pressure_diagnosis_mapping)
# df['Outpatient_Visits'] = df['OPTOTV'].map(outpatient_visits_mapping)
# df['Days_Missed_Work'] = df['DDNWRK'].map(days_missed_work_mapping)
# df['Region'] = df['REGION'].map(region_mapping)
# df['COVID_Vaccine'] = df['CVVACCINE53'].map(covid_vaccine_mapping)
# df['COVID_Booster_Shot'] = df['BOOSTERSHOT53'].map(covid_booster_shot_mapping)
