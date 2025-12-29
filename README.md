# Hospital Resource Optimization Pipeline

## Project Overview

This project implements an end-to-end **data engineering pipeline** for analyzing hospital appointment and admission data with the goal of supporting **hospital resource optimization and capacity planning**.

The pipeline follows standard data engineering stages:
- Data ingestion
- Data cleaning and preprocessing
- Feature engineering
- Analytical evaluation
- Conceptual orchestration using Apache Airflow

All outputs (tables and figures) are generated **automatically from Python code**, ensuring full reproducibility.

---

## Datasets

This project uses two real-world healthcare datasets:

1. **Hospital Appointment No-Show Dataset (Kaggle)**
   - Source: https://www.kaggle.com/datasets/joniarroba/noshowappointments
   - Description: Contains outpatient appointment information including patient demographics, appointment scheduling details, and no-show indicators.

2. **HDHI Admission Dataset**
   - Source: Provided as part of the course materials
   - Description: Contains detailed hospital admission records including clinical indicators, length of stay, ICU duration, and patient outcomes.

---

## Research Questions

**RQ1:** What are the basic statistics and demographic characteristics of hospital appointments?  
**RQ2:** What are the key clinical and operational characteristics of hospital admissions?  
**RQ3:** How do daily admissions and length of stay behave over time?  
**RQ4:** How can the hospital data pipeline be structured into reproducible stages?  
**RQ5:** Can simple forecasting support hospital capacity planning?

📌 **Each research question is supported by at least 4 automatically generated tables and/or figures.**

---

## Project Structure
```text
hospital-resource-optimization-pipeline/
│
├── dags/
│   └── hospital_pipeline_dag.py        # Apache Airflow DAG
│
├── src/
│   ├── data_ingestion/                 # Load raw datasets
│   ├── data_cleaning/                  # Cleaning & preprocessing
│   ├── feature_engineering/            # Derived features (LOS, trends)
│   └── evaluation/                     # Tables & figures for research questions
│
├── data/
│   └── *.csv                            # Cleaned datasets
│
├── tables/
│   └── *.xlsx                          # Generated tables
│
├── figures/
│   └── *.pdf                           # Generated figures
│
├── README.md
└── .gitignore
```
---

## How to Run the Code (Local Execution)

### 1. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```
### 2. Install required packages
```bash
pip install pandas numpy matplotlib seaborn scikit-learn openpyxl
```
### 3. Run pipeline steps manually 
```bash
python src/data_ingestion/convert_xlsx_to_csv.py
python src/data_cleaning/clean_hospital_data.py
python src/data_cleaning/clean_hdhi_data.py
python src/evaluation/rq1_basic_stats.py
```
All tables and figures will be saved automatically to the tables/ and figures/ folders.
Apache Airflow DAG

## This project includes one complete Apache Airflow DAG that conceptually represents the full pipeline.
```text
DAG Details
	•	DAG name: hospital_resource_optimization_pipeline
	•	Tasks reflect pipeline stages:
	•	Data ingestion
	•	Data cleaning
	•	Feature engineering
	•	Analytics and reporting
	•	Tasks use meaningful names
	•	Logical dependencies are defined
	•	DAG is runnable locally using Docker
```

## How to Run Airflow
```bash
docker compose up
Then open:
http://localhost:8080
```
Trigger the DAG manually from the Airflow UI.


## Reproducibility
```text
✔ All figures and tables are generated from Python code
✔ No manually created figures or tables
✔ Outputs are saved automatically
✔ Pipeline can be re-run end-to-end
```
This ensures full reproducibility of results.


Author
```text
Magomed Makhsudov
Data Engineering Project
```
