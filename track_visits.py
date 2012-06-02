#!/usr/bin/env python
import urllib
import datetime
import re
import os
import bar_chart

input_file = "ip.txt"

# get data from remote server (optional, comment out if data stored locally)
os.spawnlp(os.P_WAIT, 'wget', 'wget', 'http://artax.karlin.mff.cuni.cz/~sotam0am/ip.txt', '-O', input_file)

# map ip to location (query free hostip database, not so great), extract country and city data
def map_ip(ip):
    response = urllib.urlopen('http://api.hostip.info/get_html.php?ip=%s&position=true' % ip).read()
    response_arr = response.split("\n");
    country = response_arr[0].split(":")[1].strip();
    city = response_arr[1].split(":")[1].strip();
    
    result = []
    result.append(country)
    result.append(city)
    return result

# build list of logs from textfie data
def construct_database():
    result = []
    f = open(input_file, "r")
    for line in f.readlines():
        line = line.split(" ");
        location = map_ip(line[0]);
        date = line[1].split(".");

        new_entry = { 'ip': line[0], 'country': location[0], 'city': location[1], 'year': date[2].strip(), 'month': date[0], 'day': date[1] }

        result.append(new_entry)
    
    f.close()
    return result

# main method
def filter_and_count():
    now = datetime.datetime.now()

    # simple interface
    year = raw_input("Year (press Enter if current): ")
    month = raw_input("Month (1-12, press Enter if all): ")
    day = raw_input("Day (1-31, press Enter if all): ")
    by_country = raw_input("By country (0)/By city (1): ")

    # final output
    data = {}

    database = construct_database()
    
    # group-by criterion
    if (by_country == "0"):
        criterion = "country"
    else: 
        criterion = "city"

    # if no year given, use current
    if (year == ""):
        year = str(now.year)

    # filter irrelevant entries
    filtered = []
    for entry in database:
        if (entry['year'] == str(year)):
            if (month == "" or entry['month'] == month):
                if (day == "" or entry['day'] == day):
                    filtered.append(entry)

    # group by
    for entry in filtered:
        key = entry.get(criterion)
        if key in data:
            data[key] += 1
        else: 
            data[key] = 1
    
    for key in data:
        print ("%s: %d" % (key, data[key]))

    # construct input for bar chart
    x_values = data.keys()
    y_values = []

    for key in x_values:
        y_values.append(data[key])
    
    # print bar chart
    bar_chart.print_bar_chart(x_values, y_values)
    
    return data 

filter_and_count()
