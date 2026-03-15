# SQL Query Performance Benchmarking
### 📊 Comparative Latency Analysis Across Scaled SQLite Databases

This project features a performance engineering suite designed to stress-test the **SQLite3** engine. By automating query execution across three distinct data scales (1MB, 10MB, and 100MB), the project identifies performance bottlenecks and documents how SQL execution time scales with data volume in an embedded database environment.

## 🚀 Project Objective
The objective of this project is to develop an automated benchmarking program that measures and analyzes the execution time of complex SQL queries. This study provides a quantitative look at "Scaling Laws" for local data storage, identifying at which point data volume significantly impacts user experience and system latency.

## 🛠️ Technical Tech Stack
* **Language:** Python 3.x
* **Database Engine:** SQLite3
* **Libraries:** Matplotlib (Visual Analytics), Pandas, Time
* **Workflow:** Terminal-based bulk data ingestion and automated Python benchmarking.

---

## ⚙️ Technical Workflow & Implementation
# Database Design & Performance Analysis
### 📊 Comparative Latency Analysis Across Scaled SQLite Databases

This project features a performance engineering suite designed to stress-test the **SQLite3** engine. By automating query execution across three distinct data scales (1MB, 10MB, and 100MB), the project identifies performance bottlenecks and documents how SQL execution time scales with data volume in an embedded database environment.

---

## ⚙️ Technical Workflow & Implementation

### 1. Multi-Scale Data Ingestion & Schema Design
To observe performance degradation, I created three identical schemas across tiered datasets:
* **Datasets:** 1MB, 10MB, and 100MB versions of a salary tracking dataset.
* **Bulk Migration:** Utilized high-speed SQLite terminal commands for efficient data ingestion:
  ```bash
  sqlite3 salary_data_100MB.db
  sqlite> .mode csv
  sqlite> .import salary_tracker_100MB.csv salary_table (for other two datasets too)
####Automated Benchmarking Engine
Precision Tracking: Developed a Python test controller (query_performance_analysis.py) to interface with each database and capture execution latency at the microsecond level.

Independent Execution: Each query was measured independently to minimize the impact of database caching, ensuring "cold start" accuracy for every run.

3. Query Design & Stress Testing
Six standardized queries were engineered to test different computational complexities, ranging from standard filtering to complex memory-intensive aggregations. The resulting performance data captures the impact of data volume on query execution time.

###📈 Performance Analysis & Key Findings
Scaling Trends
Analysis of the benchmark results shows that standard selection queries follow a linear scaling path, where a 10x increase in data leads to a proportional increase in execution time. This indicates efficient indexing and retrieval for basic operations.

Aggregation Bottlenecks
Queries involving GROUP BY and conditional logic on the 100MB file showed non-linear growth. This suggests that as the dataset size increases, I/O and memory overhead become primary bottlenecks, requiring more sophisticated query optimization or hardware resources.

SQLite Efficiency
The results confirm that SQLite is an exceptionally robust choice for local applications, maintaining sub-second latency for most operations even at the 100MB threshold. This makes it an ideal solution for embedded systems and single-user applications with moderate data requirements.

###📂 Repository Structure
/scripts: query_performance_analysis.py - The main automation engine for performance measurement.

/notebooks: dbdesignproj.ipynb - Detailed step-by-step documentation and visualization code.

/visualizations: Performance comparison plots for each query (Query 1 through Query 6).

/data: Includes salary_tracker_1MB.csv for sample testing and local reproduction.

#Author: Hrushitha Darna

