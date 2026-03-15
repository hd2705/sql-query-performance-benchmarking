# Database Design & Performance Analysis
### 📊 Comparative Latency Analysis Across Scaled SQLite Databases

This project features a performance engineering suite designed to stress-test the **SQLite3** engine. By automating query execution across three distinct data scales (1MB, 10MB, and 100MB), the project identifies performance bottlenecks and documents how SQL execution time scales with data volume in an embedded database environment.

---

## 🚀 Project Objective
The objective of this project is to develop an automated benchmarking program that measures and analyzes the execution time of complex SQL queries. This study provides a quantitative look at "Scaling Laws" for local data storage, identifying at which point data volume significantly impacts system latency.

## 🛠️ Technical Tech Stack
* **Language:** Python 3.x
* **Database Engine:** SQLite3
* **Libraries:** Matplotlib (Visual Analytics), Pandas, Time
* **Workflow:** Terminal-based bulk data ingestion and automated Python benchmarking.

---

## ⚙️ Technical Workflow & Implementation

### 1. 3NF Schema Normalization
To ensure data integrity and minimize redundancy, the dataset was normalized into a **Third Normal Form (3NF)** relational schema consisting of the following entities:
* **Persons Table:** `PersonID` (PK), `PersonName`, `BirthDate`.
* **Schools Table:** `SchoolID` (PK), `SchoolName`, `SchoolCampus`.
* **Departments Table:** `DepartmentID` (PK), `DepartmentName`, `SchoolID` (FK).
* **Jobs Table:** `JobID` (PK), `JobTitle`, `DepartmentID` (FK).
* **Earnings Table:** `EarningsID` (PK), `PersonID` (FK), `JobID` (FK), `Earnings`, `EarningsYear`, `StillWorking`.

### 2. Multi-Scale Data Ingestion
Identical schemas were created across tiered datasets to observe performance degradation:
* **Datasets:** 1MB, 10MB, and 100MB SQLite databases.
* **Bulk Migration:** Utilized high-speed SQLite terminal commands for efficient ingestion:
    ```bash
    sqlite3 salary_data_100MB.db
    sqlite> .mode csv
    sqlite> .import salary_tracker_100MB.csv salary_table
    ```

### 3. Automated Benchmarking Engine
* **Precision Tracking:** Developed a Python test controller (`query_performance_analysis.py`) to capture execution latency at the microsecond level.
* **Independent Execution:** Each query was measured independently to ensure "cold start" accuracy and eliminate the impact of database caching.

### 4. Query Design & Stress Testing
Six standardized queries were engineered to test computational complexities, including **complex 5-table JOINs** involving filtering, multi-level aggregations, and conditional logic.

---

## 📈 Performance Analysis & Key Findings

### Scaling Trends
Analysis of the benchmark results shows that standard selection queries follow a **linear scaling path**. For example, Query 1 execution time scaled from **0.0087s (1MB)** to **0.2928s (100MB)**. This indicates efficient indexing for basic filtering operations.

### Aggregation Bottlenecks
Queries involving `GROUP BY` and multi-table joins on the 100MB file showed **non-linear growth**. This suggests that as the dataset size increases, I/O and memory overhead for joining normalized tables become primary bottlenecks, requiring more sophisticated query optimization at scale.

### SQLite Efficiency
The results confirm that SQLite is exceptionally robust for local applications, maintaining sub-second latency for most operations even at the 100MB threshold.

---

## 📂 Repository Structure
* **/scripts**: `query_performance_analysis.py` - The main automation engine.
* **/notebooks**: `dbdesignproj.ipynb` - Detailed documentation and visualization code.
* **/visualizations**: Performance comparison plots (Q1-Q6) and final comparison summary (`output_11_1.png`).
* **/docs**: `dbdesignproj.pdf` (Final Project Report) and `queries.txt` (SQL logic for 3NF schema).
* **/data**: Includes `salary_tracker_1MB.csv` for sample testing and local reproduction.

---
**Author:** Hrushitha Darna   
**Project:** Database Design & Performance Analysis
