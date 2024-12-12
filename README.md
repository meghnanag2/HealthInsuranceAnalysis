# HealthInsuranceAnalysis
Exploring Determinants of Healthcare Expenditures and Outcomes Using Statistical Analysis 

# Data Processing and Visualization Project

## Overview
This project focuses on processing and analyzing healthcare-related data using Python. The workflow involves cleaning and transforming raw datasets, mapping codes to meaningful labels, and performing visualizations to extract insights and test hypotheses.

## Files in This Repository

1. **`preprocessingCode.py`**
   - **Purpose**: Processes raw datasets from multiple years into a cleaned and unified format.
   - **Features**:
     - Combines multiple datasets.
     - Maps raw codes (e.g., gender, employment status) to human-readable labels.
     - Filters for relevant data (ages 18-64) and removes invalid values.
     - Outputs a combined CSV file: `combined_meps_data_new.csv`.

2. **`mapping.py`**
   - **Purpose**: Contains dictionaries to map coded values to descriptive labels.
   - **Features**:
     - Maps columns such as gender, health status, region, and more.
     - Example mappings:
       - `1 → "Male", 2 → "Female"` (Gender)
       -  1 → "Employed"`, `34 → "Unemployed" (Employment Status)
   - Designed to be imported and used during preprocessing or analysis.

3. **`dataViz.ipynb`**
   - **Purpose**: Jupyter Notebook for visualizing the processed data.
   - **Features**:
     - Generates plots to explore healthcare expenditures, regional trends, and demographic distributions.
     - Supports hypothesis testing using statistical methods.

4. **`visualizationAndHypothesisCode.ipynb`**
   - **Purpose**: Combines visualization and hypothesis testing for data insights.
   - **Features**:
     - Includes detailed visualizations for exploring data relationships.
     - Tests hypotheses such as differences in healthcare expenditures by region or vaccination status.
     - 

## Installation and Requirements

### Prerequisites
- Python 3.x
- Required Libraries:
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn`
  - `scipy`

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/meghnanag2/HealthInsuranceAnalysis.git
   ```
2. Install required Python packages:
   ```bash
   pip install pandas numpy matplotlib seaborn scipy
   ```

## Usage

1. **Preprocessing Data**:
   - Run `preprocessingCode.py` to process raw CSV files and generate a cleaned dataset:
     ```bash
     python preprocessingCode.py
     ```
   - Output: `combined_meps_data_new.csv`

2. **Mapping**:
   - Use `mapping.py` to convert raw codes into readable labels during data analysis.

3. **Visualization and Hypothesis**:
   - Open `dataViz.ipynb` or `visualizationAndHypothesisCode.ipynb` in Jupyter Notebook.
   - Execute the cells to generate plots and test hypotheses.


## Sample Workflow

1. Preprocess raw data:
   - Combine data from 2018-2022.
   - Filter and clean it.
2. Map codes to labels using `mapping.py`.
3. Analyze data in Jupyter Notebooks:
   - Generate visualizations.
   - Test statistical hypotheses.

## Contributions

This project was collaboratively developed by the following contributors:

Madhumitha Somasundaram
College of Engineering and Applied Science, Boulder, Colorado, USA
Madhumitha.Somasundaram@colorado.edu

Meghna Nag
College of Engineering and Applied Science, Boulder, Colorado, USA
Meghna.Nag@colorado.edu

Sathish Kumar Prabaharan
College of Engineering and Applied Science, Boulder, Colorado, USA
Sathishkumar.Prabaharan@colorado.edu

