import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
import pymysql
from tkcalendar import Calendar
import tkinter as tk
# Connect to your MySQL database
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="travelmanagement",
#     database="crud"
# )
con=pymysql.connect(host='localhost',user='root',password='travelmanagement')
mycursor= con.cursor()
    
query='use crud'
mycursor.execute(query)
# Create a cursor object to execute SQL queries
# mycursor = mydb.cursor()

# Execute a query to fetch data from the 'graph' table
# mycursor.execute("SELECT date, nos FROM graph")
query='SELECT date, nos FROM graph'
mycursor.execute(query)
# Fetch all rows from the result set
result = mycursor.fetchall()

# Extract dates and corresponding numbers from the result
dates = [row[0] for row in result]
nos = [row[1] for row in result]

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(dates, nos, marker='o', linestyle='-')
plt.title('Number of No Of Sales over Time')
plt.xlabel('Date')
plt.ylabel('Number of NOS')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()
