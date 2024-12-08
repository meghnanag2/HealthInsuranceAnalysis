import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Load dataset
data = pd.read_csv('combined_meps_data.csv')

# Clean the data
data['Current_Smoker_Status'] = data['Current_Smoker_Status'].fillna(data['Current_Smoker_Status'].mean())  # Handling missing values in 'Current_Smoker_Status'

# Hypothesis 1: Impact of Insurance Coverage on Healthcare Expenditure
print("\n1. Impact of Insurance Coverage on Healthcare Expenditure")
print("H₀: There is no significant difference in total healthcare expenditures between individuals with and without employer-provided health insurance.")
print("Hₐ: There is a significant difference in total healthcare expenditures between individuals with and without employer-provided health insurance.")
insured = data[data['Employer_Offers_Health_Insurance'] == 1]['Total_Expenditures']  # Assuming 1 means insured
uninsured = data[data['Employer_Offers_Health_Insurance'] == 0]['Total_Expenditures']  # Assuming 0 means uninsured

insured_mean = np.mean(insured)
uninsured_mean = np.mean(uninsured)

# T-test
stat, p_value = ttest_ind(insured, uninsured, equal_var=False)
print(f"Mean Expenditure (Insured): {insured_mean:.2f}, Mean Expenditure (Uninsured): {uninsured_mean:.2f}")
print(f"T-statistic: {stat:.2f}, P-value: {p_value:.5f}")

# Conclusion
if p_value < 0.05:
    print("Result: Reject H₀. There is a significant difference in healthcare expenditures between insured and uninsured individuals.")
else:
    print("Result: Fail to reject H₀. No significant difference in healthcare expenditures between insured and uninsured individuals.")

# Plotting the distributions of Total Expenditures for Insured vs. Uninsured
plt.figure(figsize=(10, 6))
plt.hist(insured, bins=50, alpha=0.5, label='Insured', color='blue')
plt.hist(uninsured, bins=50, alpha=0.5, label='Uninsured', color='red')
plt.title('Total Expenditures: Insured vs Uninsured')
plt.xlabel('Total Expenditures')
plt.ylabel('Frequency')
plt.legend(loc='upper right')
plt.show()

# Hypothesis 2: Effect of Family Income on Health Outcomes
print("\n2. Effect of Family Income on Health Outcomes")
print("H₀: There is no significant difference in general health status between individuals with high and low family income.")
print("Hₐ: There is a significant difference in general health status between individuals with high and low family income.")
# Group by Family Income
high_income = data[data['Family_Income'] > data['Family_Income'].median()]['General_Health']
low_income = data[data['Family_Income'] <= data['Family_Income'].median()]['General_Health']

high_income_mean = np.mean(high_income)
low_income_mean = np.mean(low_income)

# T-test
stat, p_value = ttest_ind(high_income, low_income, equal_var=False)
print(f"Mean Health Status (High Income): {high_income_mean:.2f}, Mean Health Status (Low Income): {low_income_mean:.2f}")
print(f"T-statistic: {stat:.2f}, P-value: {p_value:.5f}")

# Conclusion
if p_value < 0.05:
    print("Result: Reject H₀. There is a significant difference in general health status between high and low-income individuals.")
else:
    print("Result: Fail to reject H₀. No significant difference in general health status between high and low-income individuals.")

# Plotting the distributions of General Health for High vs Low Income
plt.figure(figsize=(10, 6))
plt.hist(high_income, bins=50, alpha=0.5, label='High Income', color='green')
plt.hist(low_income, bins=50, alpha=0.5, label='Low Income', color='orange')
plt.title('General Health: High Income vs Low Income')
plt.xlabel('General Health')
plt.ylabel('Frequency')
plt.legend(loc='upper right')
plt.show()

# Hypothesis 3: Regional Differences in Healthcare Access
print("\n3. Regional Differences in Healthcare Access")
print("H₀: There is no significant difference in healthcare access between different regions.")
print("Hₐ: There is a significant difference in healthcare access between different regions.")
# Group by Region
regional_visits = data.groupby('Region')['Outpatient_Visits'].mean()

print("\nAverage Outpatient Visits by Region:")
print(regional_visits)

# Conclusion
# Since the data is aggregated by region, we do not perform a t-test here.
# We can visually inspect the differences.
if regional_visits.var() > 0:
    print("Result: Reject H₀. There is a significant difference in healthcare access between regions.")
else:
    print("Result: Fail to reject H₀. No significant difference in healthcare access between regions.")

# Plotting Average Outpatient Visits by Region
regional_visits.plot(kind='bar', figsize=(10, 6), color='purple')
plt.title('Average Outpatient Visits by Region')
plt.xlabel('Region')
plt.ylabel('Average Outpatient Visits')
plt.xticks(rotation=45)
plt.show()

# Hypothesis 4: Impact of Hypertension Diagnosis Age on Healthcare Expenditure
print("\n4. Impact of Hypertension Diagnosis Age on Healthcare Expenditure")
print("H₀: There is no significant difference in total healthcare expenditures between individuals diagnosed with hypertension at different ages.")
print("Hₐ: There is a significant difference in total healthcare expenditures between individuals diagnosed with hypertension at different ages.")
if 'Age_of_Hypertension_Diagnosis' in data.columns:
    young_diag = data[data['Age_of_Hypertension_Diagnosis'] <= data['Age_of_Hypertension_Diagnosis'].median()]['Total_Expenditures']
    old_diag = data[data['Age_of_Hypertension_Diagnosis'] > data['Age_of_Hypertension_Diagnosis'].median()]['Total_Expenditures']

    young_diag_mean = np.mean(young_diag)
    old_diag_mean = np.mean(old_diag)

    # T-test
    stat, p_value = ttest_ind(young_diag, old_diag, equal_var=False)
    print(f"Mean Expenditure (Young Diagnosis): {young_diag_mean:.2f}, Mean Expenditure (Older Diagnosis): {old_diag_mean:.2f}")
    print(f"T-statistic: {stat:.2f}, P-value: {p_value:.5f}")

    # Conclusion
    if p_value < 0.05:
        print("Result: Reject H₀. There is a significant difference in healthcare expenditures between those diagnosed with hypertension at different ages.")
    else:
        print("Result: Fail to reject H₀. No significant difference in healthcare expenditures between those diagnosed with hypertension at different ages.")
else:
    print("Column 'Age_of_Hypertension_Diagnosis' not found in the dataset.")

# Hypothesis 5: Smoking Status and Healthcare Expenditures
print("\n5. Smoking Status and Healthcare Expenditures")
print("H₀: There is no significant difference in healthcare expenditures between smokers and non-smokers.")
print("Hₐ: Smokers incur significantly higher healthcare expenditures than non-smokers.")
smokers = data[data['Current_Smoker_Status'] == 1]['Total_Expenditures']
non_smokers = data[data['Current_Smoker_Status'] == 0]['Total_Expenditures']

smokers_mean = np.mean(smokers)
non_smokers_mean = np.mean(non_smokers)

# T-test
stat, p_value = ttest_ind(smokers, non_smokers, equal_var=False)
print(f"Mean Expenditure (Smokers): {smokers_mean:.2f}, Mean Expenditure (Non-Smokers): {non_smokers_mean:.2f}")
print(f"T-statistic: {stat:.2f}, P-value: {p_value:.5f}")

# Conclusion
if p_value < 0.05:
    print("Result: Reject H₀. Smokers incur significantly higher healthcare expenditures than non-smokers.")
else:
    print("Result: Fail to reject H₀. No significant difference in healthcare expenditures between smokers and non-smokers.")

# Plotting the distributions of Total Expenditures for Smokers vs. Non-Smokers
plt.figure(figsize=(10, 6))
plt.hist(smokers, bins=50, alpha=0.5, label='Smokers', color='red')
plt.hist(non_smokers, bins=50, alpha=0.5, label='Non-Smokers', color='blue')
plt.title('Total Expenditures: Smokers vs Non-Smokers')
plt.xlabel('Total Expenditures')
plt.ylabel('Frequency')
plt.legend(loc='upper right')
plt.show()

# Hypothesis 6: COVID Vaccine and Healthcare Expenditures
print("\n6. COVID Vaccine and Healthcare Expenditures")
print("H₀: There is no significant difference in healthcare expenditures between individuals who received the COVID vaccine and those who did not.")
print("Hₐ: There is a significant difference in healthcare expenditures between individuals who received the COVID vaccine and those who did not.")
vaccinated = data[data['COVID_Vaccine'] == 1]['Total_Expenditures']
not_vaccinated = data[data['COVID_Vaccine'] == 0]['Total_Expenditures']

vaccinated_mean = np.mean(vaccinated)
not_vaccinated_mean = np.mean(not_vaccinated)

# T-test
stat, p_value = ttest_ind(vaccinated, not_vaccinated, equal_var=False)
print(f"Mean Expenditure (Vaccinated): {vaccinated_mean:.2f}, Mean Expenditure (Not Vaccinated): {not_vaccinated_mean:.2f}")
print(f"T-statistic: {stat:.2f}, P-value: {p_value:.5f}")

# Conclusion
if p_value < 0.05:
    print("Result: Reject H₀. There is a significant difference in healthcare expenditures between vaccinated and non-vaccinated individuals.")
else:
    print("Result: Fail to reject H₀. No significant difference in healthcare expenditures between vaccinated and non-vaccinated individuals.")

# Plotting the distributions of Total Expenditures for Vaccinated vs Not Vaccinated
plt.figure(figsize=(10, 6))
plt.hist(vaccinated, bins=50, alpha=0.5, label='Vaccinated', color='green')
plt.hist(not_vaccinated, bins=50, alpha=0.5, label='Not Vaccinated', color='yellow')
plt.title('Total Expenditures: Vaccinated vs Not Vaccinated')
plt.xlabel('Total Expenditures')
plt.ylabel('Frequency')
plt.legend(loc='upper right')
plt.show()

# Hypothesis 7: Employment Status and General Health
print("\n7. Employment Status and General Health")
print("H₀: There is no significant difference in general health status between employed and unemployed individuals.")
print("Hₐ: There is a significant difference in general health status between employed and unemployed individuals.")
employed = data[data['Employment_Status'] == 1]['General_Health']
unemployed = data[data['Employment_Status'] == 0]['General_Health']

# T-test
stat, p_value = ttest_ind(employed, unemployed, equal_var=False)
print(f"Mean Health Status (Employed): {np.mean(employed):.2f}, Mean Health Status (Unemployed): {np.mean(unemployed):.2f}")
print(f"T-statistic: {stat:.2f}, P-value: {p_value:.5f}")

# Conclusion
if p_value < 0.05:
    print("Result: Reject H₀. There is a significant difference in general health status between employed and unemployed individuals.")
else:
    print("Result: Fail to reject H₀. No significant difference in general health status between employed and unemployed individuals.")
