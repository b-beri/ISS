"""
Author : Bhav Beri
Author Id : 2021111013
Author Github : bhavberi
Date : 05-2022

Stock Market Analysis for Given Data
"""


# Importing SqLite3 for database management
import sqlite3
import csv

# Emptying the Database file, and creating if not exists
with open("record.db", "w") as fp:
    pass

# Connecting with Databse & making an executable cursor instance with
# connection
mydb = sqlite3.connect("record.db")
cursor_obj = mydb.cursor()

# Creating Tables - Ticker and Metrics as per given format
cursor_obj.execute("""create table Ticker (
            "Date" datetime NOT NULL,
            "Company Name" TEXT,
            "Industry" TEXT,
            "Previous Day Price" TEXT DEFAULT 'NA',
            "Current Price"	TEXT,
            "Change in Price" TEXT DEFAULT 'NA',
            "Confidence" TEXT )"""
                   )

cursor_obj.execute("""create table Metrics (
            KPIs TEXT, Metrics TEXT )"""
                   )

# Reading the Controls File, so as to proceed as per it
control_list = list()
with open("./Control/control.csv", 'r') as fp:
    csv_reader = csv.reader(fp)
    next(csv_reader)

    for row in csv_reader:
        control_list.append(row)

# Dates & respective files array, for more dynamic nature
dates = ["2022-05-20", "2022-05-21", "2022-05-22", "2022-05-23", "2022-05-24"]
files = ["2021111013-20-05-2022.csv", "2021111013-21-05-2022.csv",
         "2021111013-22-05-2022.csv", "2021111013-23-05-2022.csv",
         "2021111013-24-05-2022.csv"
         ]

# Storing the 1st day data with assumption of no previous data
with open("./Record/" + files[0], "r") as fp:
    csv_reader = csv.reader(fp)
    next(csv_reader)

    for row in csv_reader:
        cursor_obj.execute("""insert into Ticker(
                    "Date","Company Name","Industry","Current Price",
                    "Confidence") values("%s", "%s", "%s", "%s", "%s")
                    """ % (dates[0], row[0], row[1], str(row[2]),
                           control_list[-1][2])
                           )

"""
Reading all except 1st File
After reading each entry, getting it's previous day data
And after computing the change/s, and operating upon data,
according to controls, pushing that data into the Ticker table,
for storing for future use/s.
"""

for i in range(1, len(files)):
    with open("./Record/" + files[i], "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)

        for row in csv_reader:
            # Getting Previous Day data
            cursor_obj.execute(
                """select "Current Price", "Company Name", Date from Ticker
                where "Company Name" = "%s" and "Date" = "%s"
                """ % (row[0], dates[i - 1])
            )
            result = cursor_obj.fetchone()
            if result is None:
                cursor_obj.execute("""insert into Ticker(
                    "Date","Company Name","Industry","Current Price",
                    "Confidence") values("%s", "%s", "%s", "%s", "%s")
                    """ % (dates[i], row[0], row[1], str(row[2]),
                           control_list[-1][2])
                )
                continue

            last_price = float(result[0])
            curr_price = float(row[2])
            percent_change = (curr_price - last_price) / last_price * 100
            confidence = "NA"

            percent_change = float(format(percent_change, '.8f'))
            # Rounding off the value as Python adds some very \
            # less significant digits in calculations, \
            # which may cause error in comparisons

            # Opertaing upon data according to controls file
            for control_line in control_list:
                if control_line[0] == row[1]:
                    if control_line[1][0] == '<':
                        percentage = float(control_line[1].strip()[1: - 1])
                        if percent_change < percentage:
                            confidence = "Low"
                            break
                    elif control_line[1][0:2] == '>=':
                        percent_list = control_line[1].split('&')
                        bottom = float(percent_list[0].strip()[2: - 1])
                        above = float(percent_list[1].strip()[2: - 1])
                        if bottom <= percent_change <= above:
                            confidence = "Medium"
                            break
                    elif control_line[1][0] == '>':
                        percentage = float(control_line[1].strip()[1: - 1])
                        if percent_change > percentage:
                            confidence = "High"
                            break

            cursor_obj.execute("""insert into Ticker values
            ("%s", "%s", "%s", "%s", "%s", "%s", "%s"
                )""" % (dates[i], row[0], row[1], str(last_price),
                        str(curr_price), str(percent_change), confidence))

# Set the Best Listed Industry in table Metrics a/c to max Highs
cursor_obj.execute("""select "Industry",
            sum(case when Confidence='High' Then 1 else 0 end) as count_HIGH
            from Ticker group by "Industry"
            order by count_HIGH desc"""
                   )
result = cursor_obj.fetchone()
cursor_obj.execute(
    "insert into Metrics values('Best Listed Industry', \"%s\");" % result[0])

# Set the Worst Listed Industry in table Metrics a/c to max Lows
cursor_obj.execute("""select "Industry",
            sum(case when Confidence='Low' Then 1 else 0 end) as count_LOW
            from Ticker group by "Industry"
            order by count_LOW desc"""
                   )
result = cursor_obj.fetchone()
cursor_obj.execute(
    "insert into Metrics values('Worst Listed Industry', \"%s\");" % result[0])

# ON PER DAY BASIS

# Getting the relative order of companies based on the 3 criterias given
cursor_obj.execute("""select "Company Name","Change in Price" from Ticker
            where "Change in Price" != "NA"
            order by cast("Change in Price" as decimal) desc,
            (cast("Current Price" as decimal)
            - cast("Previous Day Price" as decimal)) desc,
            "Company Name" asc"""
                   )
result = cursor_obj.fetchall()

# Set the Best Company & it's Gain % in table Metrics
cursor_obj.execute("insert into Metrics values('Best Company', \"%s\");" %
                   result[0][0])
cursor_obj.execute(
    "insert into Metrics values('Gain %%', \"%s\");" %
    format(
        float(
            result[0][1]),
        '.8f'))

# Set the Worst Company & it's Gain % in table Metrics
cursor_obj.execute("insert into Metrics values('Worst Company', \"%s\");" %
                   result[-1][0])
cursor_obj.execute("insert into Metrics values('Loss %%', \"%s\");" %
                   format(float(result[-1][1]), '.8f'))

# ON OVERALL BASIS

cursor_obj.execute("select distinct \"Company Name\" from Ticker")
companies = cursor_obj.fetchall()

best = [0, 0, ""]  # [Change, %age Change, Company name]
worst = [0, 0, ""]  # [Change, %age Change, Company name]

# Getting stats for all companies
for i in companies:
    company = i[0]
    cursor_obj.execute(""" select "Current Price" from Ticker
            where "Company Name" = "%s"
            order by "Date" """ % company
                       )
    result = cursor_obj.fetchall()

    # Getting overall gain/loss percentage
    change = float(result[-1][0]) - float(result[0][0])
    percent_change = change * 100 / float(result[0][0])

    percent_change = float(format(percent_change, '.8f'))
    # Rounding off the value as Python adds some very \
    # less significant digits in calculations, \
    # which may cause error in comparisons

    # Updating value/s of best/worst according to given parameters
    if best[1] < percent_change or (
            best[1] == percent_change and best[0] < change) or (
            best[1] == percent_change and best[0] == change
            and best[2] > company):
        best = [change, percent_change, company]

    if worst[1] > percent_change or (
            worst[1] == percent_change and worst[0] > change) or (
            worst[1] == percent_change and worst[0] == change
            and worst[2] < company):
        worst = [change, percent_change, company]

# Set the Best Company & it's Gain % in table Metrics (For Overall)
cursor_obj.execute(
    "insert into Metrics values('Best Company(Overall)', \"%s\");" %
    best[2])
cursor_obj.execute(
    "insert into Metrics values('Gain %%(Overall)', \"%s\");" % best[1])

# Set the Worst Company & it's Gain % in table Metrics (For Overall)
cursor_obj.execute(
    "insert into Metrics values('Worst Company(Overall)', \"%s\");" %
    worst[2])
cursor_obj.execute(
    "insert into Metrics values('Loss %%(Overall)', \"%s\");" % worst[1])


# Commiting all of the operations done, for some external use
mydb.commit()

# Thanks.............
