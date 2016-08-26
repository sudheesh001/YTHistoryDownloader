import csv, sqlite3, os
from datetime import datetime, timedelta

# For windows finds the APPDATA folder and reads the chrome history
# [LATER]: Find default browser and fetch history
# [LATER]: Support history for Edge, IE, Firefox
connection = sqlite3.connect(os.getenv("APPDATA") + "\..\Local\Google\Chrome\User Data\Default\history")
connection.text_factory = str
cur = connection.cursor()
output_file = open('chrome_history.csv', 'wb')
csv_writer = csv.writer(output_file)

# Chrome stores its history as a SQLite database and using the sqlite3 allows us to read the data.
headers = ('URL', 'Title', 'Visit Count', 'Date (GMT)')
# Data structure of the SQLite DB

csv_writer.writerow(headers)
# Write the header data into the CSV file first.

epoch = datetime(1601, 1, 1)
for row in (cur.execute('select url, title, visit_count, last_visit_time from urls')):
	row = list(row)
	url_time = epoch + timedelta(microseconds=row[3])
	row[3] = url_time
	csv_writer.writerow(row)

# Finish writing all the data from chrome history to a file for furthur processing.
