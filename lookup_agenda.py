import pandas as pd
import sqlite3
import sys
from db_table import db_table

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

listofcol = ['date', 'time_start', 'time_end', 'title', 'location', 'description', 'speaker']

col = sys.argv[1]
val = sys.argv[2]

if col not in listofcol:
    exit()

info = agenda.select(where = {col:val})
for x in info:
    print(x)

agenda.close()