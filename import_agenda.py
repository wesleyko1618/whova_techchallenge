from db_table import db_table
import sqlite3
import pandas as pd
import sys

# using lookup columns for table schema columns {date, time_start, time_end, title, location, description, speaker} and adding the others

# Need to check for if they don't give a argv
if (len(sys.argv) != 2):
    print("Please enter a single Excel file")
    exit()

# take input of excel sheet
excelfile = sys.argv[1]   

# make sure it's an excel file 
if not excelfile.lower().endswith('.xls'):    
    print('Please enter a valid Excel file with the .xls file type')
    exit()

# get's all the data into a dataframe
dfs = pd.read_excel(excelfile, sheet_name="Agenda", header=14)           

#create a SQLite datatable with db_table with this schema
agenda = db_table("agenda", { 
    "id": "integer PRIMARY KEY", 
    "date": "text NOT NULL", 
    "time_start": "text NOT NULL", 
    "time_end": "text NOT NULL", 
    "session": "text NOT NULL",
    "title": "text NOT NULL", 
    "location": "text",
    "description": "text",
    "speaker": "text"})

#go through dataframe and insert all values into database
for d in range(len(dfs.index)):
    agenda.insert({
        "date": dfs.iat[d, 0], 
        "time_start": dfs.iat[d, 1], 
        "time_end": dfs.iat[d, 2], 
        "session": dfs.iat[d, 3], 
        "title": dfs.iat[d, 4], 
        "location": dfs.iat[d, 5], 
        "description": dfs.iat[d, 6], 
        "speaker": dfs.iat[d, 7]})

# agenda.select()
# for x in agenda.select():
#     print(x) 

agenda.close()