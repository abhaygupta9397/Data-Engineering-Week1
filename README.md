# Data Engineering Mini Pipeline (Single-File ETL)

This repository contains a beginner-friendly data engineering project that demonstrates a complete ETL (Extract → Transform → Load) pipeline using Python. The project is intentionally kept simple to focus on understanding how data flows through a pipeline in code, which is the core responsibility of a data engineer.

The pipeline reads raw data from a CSV file, performs transformations using Pandas, loads the processed data into a SQLite database, and verifies the final output.

Pipeline Flow:
CSV → Extract → Transform → Load → SQLite Database

Project Structure:
.
├── pipeline_single.py    # Complete ETL pipeline implemented in one file
├── sales.csv             # Raw input data
├── sales.db              # Auto-generated SQLite database (not committed)
├── README.md
└── .gitignore

Technologies Used:
- Python 3.8+
- Pandas for data transformation
- SQLite for relational data storage (built into Python)
- Git and GitHub for version control
- Virtual Environment (venv) for dependency isolation

Installation and Setup:

1. Clone the repository
git clone <your-repository-url>
cd data-engineering-mini-pipeline

2. Create a virtual environment (recommended)
python -m venv venv

3. Activate the virtual environment (Bash on Windows)
source venv/Scripts/activate

To deactivate later:
deactivate

4. Install dependencies
pip install pandas

How to Run the Pipeline:
python pipeline_single.py

When executed, the pipeline will:
- Read raw data from sales.csv
- Clean and aggregate the data using Pandas
- Store the processed result in a SQLite database (sales.db)
- Print the final aggregated output to the terminal

Expected Output:
         city  amount
0  Bangalore     300
1      Delhi     500
2     Mumbai     250

Sample Input (sales.csv):
order_id,city,amount
1,Delhi,100
2,Mumbai,200
3,Delhi,150
4,Bangalore,300
5,Mumbai,50
6,Delhi,250

Data Engineering Concepts Demonstrated:
- ETL pipeline design and execution
- Batch data processing
- Deterministic data flow using Python functions
- Data transformation using Pandas
- Relational data storage using SQL
- Reproducible project setup using virtual environments

Git Ignore Rules:
The following files and folders should not be committed to GitHub:
venv/
sales.db
__pycache__/
*.pyc

What This Project Shows:
- Understanding of core data engineering fundamentals
- Ability to build an end-to-end ETL pipeline
- Clean and reproducible project setup
- Industry-aligned workflow for data engineering projects

Future Improvements:
- Add logging and error handling
- Externalize configuration using YAML or JSON
- Replace SQLite with PostgreSQL
- Add Airflow DAG for scheduling
- Scale transformations using Apache Spark

Resume Line:
Built a single-file ETL data pipeline using Python, Pandas, and SQLite to demonstrate end-to-end data flow, transformation logic, and reproducible data engineering practices.
