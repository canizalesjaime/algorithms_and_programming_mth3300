# Lecture Notes

## table of contents
1. pandas
2. In Class Assignments 


## What is Pandas?

Pandas is a Python library used for:
- working with tables of data
- analyzing datasets
- cleaning messy data
- computing statistics
- filtering/searching information

It is one of the most important libraries in:
- data science
- machine learning
- analytics
- scientific computing

Pandas is built on top of NumPy.

---

## Why Pandas Exists

Normal Python data structures like lists and dictionaries become difficult to manage when data gets large or structured like spreadsheets.

For example:

```python
students = [
    ["Alice", 92, "CS"],
    ["Bob", 81, "Math"],
    ["Charlie", 88, "CS"]
]
```

Problems:
- hard to search/filter
- awkward statistics
- messy indexing
- difficult to scale

Pandas solves this by providing table-like data structures.

---

## Core Pandas Data Structures

### 1. Series

A Series is a single labeled column.

Example:

```python
import pandas as pd

s = pd.Series([10, 20, 30])

print(s)
```

Output:

```text
0    10
1    20
2    30
dtype: int64
```

A Series is similar to:
- a NumPy array
- a spreadsheet column

but with labels/indexes.

---

### 2. DataFrame

A DataFrame is the main Pandas structure.

It is:
- a 2D table
- rows + columns
- similar to Excel spreadsheets or SQL tables

Example:

```python
import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Department": ["CS", "Math", "Physics"]
})

print(df)
```

Output:

```text
      Name  Age Department
0    Alice   25         CS
1      Bob   30       Math
2  Charlie   35    Physics
```

---

## Important Concepts

### Columns

You can access columns by name:

```python
df["Age"]
```

---

### Rows

Rows have indexes:

```text
0,1,2,...
```

You can access rows using:

```python
df.iloc[0]
```

---

### Filtering

Pandas allows SQL-like filtering.

Example:

```python
df[df["Age"] > 28]
```

---

### Statistics

You can compute statistics easily:

```python
df["Age"].mean()
df["Age"].max()
df["Age"].min()
```

---

## Why Pandas is Powerful

Pandas allows operations on entire columns at once.

Instead of writing loops:

```python
for row in data:
    ...
```

you operate directly on tables:

```python
df["Score"].mean()
```

This style is called:
- vectorized
- column-oriented computation

It is:
- faster
- cleaner
- easier to read

---

## Common Pandas Tasks

Pandas is commonly used for:

| Task | Example |
|---|---|
| Load data | CSV/Excel files |
| Clean data | remove missing values |
| Analyze data | averages/statistics |
| Filter data | select matching rows |
| Group data | averages by category |
| Save data | export processed CSV |

---

## Reading CSV Files

One of the most common operations:

```python
import pandas as pd

df = pd.read_csv("students.csv")
```

This loads a CSV file into a DataFrame.

---

## Small Project: Analyze Student Scores from a CSV File

In real projects, data usually comes from files such as:
- CSV
- Excel
- databases
- logs

CSV ("Comma-Separated Values") is one of the most common formats.

---

## Step 1 — Example CSV File

Suppose we have a file called:

```text
students.csv
```

Contents:

```csv
Student,Department,Score,Hours_Studied
Alice,CS,92,12
Bob,Math,81,8
Charlie,CS,88,10
David,Physics,95,15
Eva,Math,76,6
```

---

## Step 2 — Load the CSV with Pandas

```python
import pandas as pd

df = pd.read_csv("students.csv")

print(df)
```

Output:

```text
   Student Department  Score  Hours_Studied
0    Alice         CS     92             12
1      Bob       Math     81              8
2  Charlie         CS     88             10
3    David    Physics     95             15
4      Eva       Math     76              6
```

Now the CSV data is stored inside a Pandas DataFrame.

---

## Step 3 — Inspect the Dataset

### View first rows

```python
df.head()
```

---

### View dataset info

```python
df.info()
```

Example output:

```text
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 4 columns):
 #   Column          Non-Null Count  Dtype
---  ------          --------------  -----
 0   Student         5 non-null      object
 1   Department      5 non-null      object
 2   Score           5 non-null      int64
 3   Hours_Studied   5 non-null      int64
```

---

## Step 4 — Basic Statistics

### Average score

```python
print(df["Score"].mean())
```

---

### Highest score

```python
print(df["Score"].max())
```

---

### Full statistics summary

```python
print(df.describe())
```

---

## Step 5 — Filter Data

### Students scoring above 90

```python
top_students = df[df["Score"] > 90]

print(top_students)
```

---

## Step 6 — Multiple Conditions

Students in CS with score above 85:

```python
cs_students = df[
    (df["Department"] == "CS") &
    (df["Score"] > 85)
]

print(cs_students)
```

---

## Step 7 — Create a New Column

Suppose we define efficiency as:


$\text{Efficiency} = \frac{\text{Score}}{\text{Hours Studied}}$

```python
df["Efficiency"] = df["Score"] / df["Hours_Studied"]

print(df)
```

---

## Step 8 — Sort the Data

Sort by highest score:

```python
sorted_df = df.sort_values(by="Score", ascending=False)

print(sorted_df)
```

---

## Step 9 — GroupBy Analysis

Average score per department:

```python
department_avg = df.groupby("Department")["Score"].mean()

print(department_avg)
```

This is similar to SQL:

```sql
SELECT Department, AVG(Score)
FROM students
GROUP BY Department;
```

---

## Step 10 — Handle Missing Data

Suppose a score is missing.

Example CSV:

```csv
Student,Department,Score,Hours_Studied
Alice,CS,92,12
Bob,Math,81,8
Charlie,CS,,10
David,Physics,95,15
Eva,Math,76,6
```

Notice Charlie's score is empty.

---

### Detect missing values

```python
print(df.isna())
```

---

### Remove missing rows

```python
clean_df = df.dropna()
```

---

### Fill missing values

Replace missing score with average score:

```python
mean_score = df["Score"].mean()

df["Score"] = df["Score"].fillna(mean_score)
```

---

## Step 11 — Save Processed Data

```python
df.to_csv("processed_students.csv", index=False)
```

This creates a new cleaned CSV file.

---

## Complete Example Script

```python
import pandas as pd

# Load CSV
df = pd.read_csv("students.csv")

# View dataset
print(df.head())

# Statistics
print("Average score:", df["Score"].mean())

# Filter students
top_students = df[df["Score"] > 90]
print(top_students)

# Add efficiency column
df["Efficiency"] = df["Score"] / df["Hours_Studied"]

# Group by department
department_avg = df.groupby("Department")["Score"].mean()
print(department_avg)

# Save processed file
df.to_csv("processed_students.csv", index=False)
```


## In Class Assignments
You are given a dataset of robot sensor logs stored in a CSV file called:

```text
robot_logs.csv
```

### CSV Contents:

```csv
Timestamp,RobotID,Distance_cm,MotorSpeed,Battery_V
10:00,R1,20,0.5,7.2
10:01,R2,18,0.6,7.1
10:02,R1,15,0.7,6.9
10:03,R3,200,0.2,7.0
10:04,R2,17,0.6,6.8
10:05,R1,14,0.8,6.7
10:06,R3,210,0.1,6.5
```

---

## Tasks

### 1. Load the CSV into a Pandas DataFrame

---

### 2. Find all rows where:
- Distance_cm is greater than 100

What might these represent in a real robot system?

---

### 3. Compute the **average motor speed per RobotID**

(Hint: use `groupby()`)

---

### 4. Find the robot that has the **lowest average battery voltage**

---

### 5. Create a new column:

```text
Power_Usage_Index = MotorSpeed / Battery_V
```

---

### 6. Sort the dataset by:
- Battery_V (lowest first)

---

### 7. Detect “danger events” defined as:
A row is dangerous if:

- Distance_cm > 100 OR
- Battery_V < 6.8

Return only those rows.

---

### 8. Count how many logs each robot has generated
