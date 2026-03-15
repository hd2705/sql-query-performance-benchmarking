import sqlite3
import time
import matplotlib.pyplot as plt

# Database paths for the three file sizes
db_files = {
    "1MB": "/Users/hrushitha/Desktop/dbdesignproj/salary_data_1MB.db",
    "10MB": "/Users/hrushitha/Desktop/dbdesignproj/salary_data_10MB.db",
    "100MB": "/Users/hrushitha/Desktop/dbdesignproj/salary_data_100MB.db"
}

# Corrected queries to execute and measure
queries = {
    # Query 1: Show the name of all people born before 1975 whose most recent earning is more than $130,000
    "Query 1": """SELECT PersonName
                  FROM salary_data
                  WHERE BirthDate < '1975-01-01'
                    AND Earnings > 130000
                    AND EarningsYear = (SELECT MAX(EarningsYear) 
                                        FROM salary_data 
                                        WHERE PersonID = salary_data.PersonID);""",
    
    # Query 2: Show the names and school names of all people who made more than $400,000 at any point in their career and are not active.
    "Query 2": """SELECT DISTINCT PersonName, SchoolName
                  FROM salary_data
                  WHERE Earnings > 400000
                    AND StillWorking = 'no';""",
    
    # Query 3: Show the names of all people who worked at the University of Texas as Lecturers and are not active.
    "Query 3": """SELECT DISTINCT PersonName
                  FROM salary_data
                  WHERE SchoolName = 'University of Texas'
                    AND JobTitle = 'Lecturer'
                    AND StillWorking = 'no';""",
    
    # Query 4: Show the University and campus pair that has the most active faculty members.
    "Query 4": """SELECT SchoolName, SchoolCampus, COUNT(*) AS active_count
                  FROM salary_data
                  WHERE StillWorking = 'yes'
                  GROUP BY SchoolName, SchoolCampus
                  ORDER BY active_count DESC
                  LIMIT 1;""",
    
    # Query 5: Search for the latest job details and earnings of a specific individual named "Hrushitha DARNA".
    "Query 5": """SELECT PersonName, JobTitle, DepartmentName, SchoolName, Earnings
                  FROM salary_data
                  WHERE PersonName = 'Hrushitha DARNA'
                  ORDER BY EarningsYear DESC
                  LIMIT 1;""",
    
    # Query 6: Show the department with the highest average earnings.
    "Query 6": """SELECT DepartmentName, AVG(Earnings) AS avg_earnings
                  FROM salary_data
                  GROUP BY DepartmentName
                  ORDER BY avg_earnings DESC
                  LIMIT 1;"""
}

# Dictionary to store the execution times for each query
results = {query_name: [] for query_name in queries}

# Measure execution time of each query on each database
for db_size, db_path in db_files.items():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"\nRunning queries on {db_size} database...")
    for query_name, query in queries.items():
        start_time = time.time()
        cursor.execute(query)
        cursor.fetchall()  # Ensure the query is fully executed
        execution_time = time.time() - start_time
        
        # Store the execution time for graphing
        results[query_name].append((db_size, execution_time))
        
        # Print the time taken for each query on each database
        print(f"{query_name} on {db_size}: {execution_time:.4f} seconds")
    
    conn.close()

# Plotting the results
for query_name, timings in results.items():
    file_sizes = [size for size, _ in timings]
    times = [time for _, time in timings]
    
    plt.figure()
    plt.plot(file_sizes, times, marker='o')
    plt.title(f"Execution Time for {query_name}")
    plt.xlabel("File Size")
    plt.ylabel("Time (seconds)")
    plt.show()

