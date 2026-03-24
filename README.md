# Health Insurance and Socioeconomic Data Analysis



## Overview

This project analyzes large-scale healthcare data to understand how socioeconomic and demographic factors influence healthcare utilization, costs, and outcomes. Using multi-year data from the Medical Expenditure Panel Survey (MEPS), the objective is to uncover patterns that explain disparities in healthcare access and expenditure across different population groups.

Rather than focusing solely on data processing, the project is structured around a central analytical question:

**How do income levels, age, gender, and insurance coverage impact healthcare costs and health outcomes?**

To answer this, the work combines multi-year data integration, structured preprocessing, categorical mapping, and exploratory analysis to build a clean and interpretable dataset for downstream analysis.



## Data

<p align="left">
  <img src="images/health-data-icon-in-logotype-vector.jpg" width="60">
</p>

The analysis is based on MEPS datasets spanning multiple years, including 2018 through 2022. These datasets provide detailed individual-level information across several dimensions:

- Demographics (age, gender, race, region)  
- Socioeconomic attributes (income, employment, education)  
- Healthcare utilization (expenditures, prescriptions, visits)  
- Insurance coverage and access  
- Health indicators (chronic conditions, general health, smoking status)  

A key challenge in this project was the variation in schema across different years. Column names and formats differed, requiring careful alignment and standardization to create a unified dataset suitable for analysis.



## Methodology

<p align="center">
  <img src="images/Health_Insurance_Pipeline.png" style="max-width: 200px; width: 50%;">
</p>

The pipeline follows a structured sequence of steps designed to transform raw multi-year data into a clean and interpretable dataset.

The process begins with loading multiple yearly datasets and identifying corresponding variables across different schemas. Pattern-based matching and dynamic column selection were used to extract consistent features despite naming differences across years.

Data cleaning and filtering were then applied to remove invalid entries, handle missing values, and ensure consistency. The analysis was restricted to a working-age population to maintain comparability across variables.

Once cleaned, the datasets were merged into a single integrated dataset, enabling cross-year comparisons and longitudinal analysis.

A critical step in the pipeline is categorical mapping. Many MEPS variables are encoded numerically, making interpretation difficult. These values were systematically converted into human-readable categories, improving interpretability and enabling meaningful analysis.

Finally, exploratory analysis and visualization were conducted to identify relationships, trends, and patterns across demographic and socioeconomic factors.



## Implementation

The data processing pipeline was implemented in Python with a focus on modularity, scalability, and reproducibility.

Key components of the implementation include:

- Multi-year dataset loading and schema alignment  
- Dynamic column extraction using pattern matching  
- Data cleaning and filtering  
- Categorical mapping for improved interpretability  
- Consolidation into a unified dataset  

The final output is a cleaned and structured dataset ready for analysis:



## Results and Insights

<p align="left">
  <img src="images/user_doc.png" width="55">
</p>

The analysis reveals several consistent patterns across the dataset.

Socioeconomic variables such as income and employment status show a strong relationship with healthcare expenditures. Individuals in higher income brackets tend to have greater access to healthcare services, while lower-income groups often exhibit reduced utilization despite potential need.

Insurance coverage plays a central role in determining access to care. Individuals with stable insurance coverage demonstrate more consistent healthcare usage patterns compared to uninsured populations.

Behavioral factors, including smoking status and vaccination history, are also associated with differences in health outcomes and healthcare utilization.

Temporal analysis across multiple years highlights shifts in healthcare patterns, suggesting the influence of broader factors such as policy changes, economic conditions, or external events.

Overall, the results emphasize that healthcare outcomes cannot be analyzed in isolation and must be understood within a broader socioeconomic context.



## Conclusion

This project demonstrates how large-scale healthcare datasets can be integrated, cleaned, and analyzed to uncover meaningful relationships between socioeconomic factors and healthcare outcomes. By combining data engineering, feature interpretation, and exploratory analysis, the work provides a strong foundation for deeper analytical and predictive studies.
