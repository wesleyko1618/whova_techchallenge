import pandas as pd
import sqlite3
import sys
from db_table import db_table

#checking for subsessions when entering the session id number
def checksub(num):
    num += 1
    while agenda.select(where={'id':num})[0]['session'] == 'Sub':
        print(agenda.select(where={'id':num})[0])
        num += 1

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

if (len(sys.argv) != 3):
    print("Please only enter a colunn title and a value to search for (use " " when entering a string with spaces in it)")
    exit()

# inputs of column title and the value we are searching for
col = sys.argv[1]
val = sys.argv[2]

#testing without sys.argv
# col = "date"
# val = "6/16/2018" 

if col not in listofcol:
    print("Please give a valid column title: 'date', 'time_start', 'time_end', 'title', 'location', 'description', or 'speaker'")
    exit()

# want to check for the events that have multiple speakers or description
if col == 'speaker' or 'description':
    for x in agenda.select():
        if x[col] != None and val in x[col]:
            print(x)
            if x['session'] == 'Session':
                checksub(x['id'])
# every other event
else:
    info = agenda.select(where = {col:val})
    for x in info:
        print(x)
        #checking for sub sessions
        if x['session'] == 'Session':
            checksub(x['id'])


agenda.close()