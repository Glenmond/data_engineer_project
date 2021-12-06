## Table of Contents
1. Project Description
2. Installation
3. Running Instructions
4. Code Description

## 1. Project Description
Our project aims to create an automated ETL pipeline solution to process data files on a regular interval. This project will be using cron (workflow tool) as a job scheduling component.

## 2. Installation
#### Libraries
Required libraries are described in requirements.txt. The code should run with no issues using Python versions 3.8+.

Using the requirements.txt file using Anaconda
```
conda create -n stash python=3.8 jupyter
conda activate stash
pip install -r requirements.txt
```

To verify that all packages are installed correctly, you can run: 
```
conda env list
```

## 3. Running Instructions
#### To Run ETL Pipeline
cd to the root directory, type in the command prompt:
```
python main.py
```

## 4. Code Description
We have 3 main classes in this project: namely DataLoader, DataPreprocessor (UsersPreprocessor, PerformancePreprocessor, GoalsPreprocessor) and DataExporter.
1. DataLoader: To load in data from inputs folder in csv format. (Future enhancements: load from database, pickle files)
2. DataPreprocessor: Is a parent class with 3 sub-classes: UsersPreprocessor, PerformancePreprocessor, GoalsPreprocessor
3. DataExporter: To export data to outputs folder as csv files (Future enhancements: export to database, pickle files)

**Note: For a more in-depth analysis, please refer to the detailed code annotation