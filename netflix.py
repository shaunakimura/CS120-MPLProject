import csv
import sys
from time import sleep
import webbrowser

# Store command line arguments in variables
title = sys.argv[1]
print(title)
try:
    # Append titles from csv file to list
    filename = "netflix_titles.csv"
    reader = csv.reader(open(filename))

    netflix_data = {}
    for row in reader:
        key = row[2]  # show/movie title
        netflix_data[key] = row[1], row[7], row[8], row[11]


    print("Scraping Netflix data...")
    sleep(3) # Just for effect

    # Check for title in list
    if title in netflix_data:
        print(title, "is on Netflix!")
        print("-----------------------------")
        # TV/movie info
        print("Type:", netflix_data[title][0])
        print("Release Year:", netflix_data[title][1])
        print("Rating:", netflix_data[title][2])
        print("Description:", netflix_data[title][3])
        print("-----------------------------")

        # Open Netlfix in browser
        print("Go check it out!")
        sleep(10)
        webbrowser.open('https://www.netflix.com/browse', new=2)
    else:
        print(title, "is not on Netflix.")

# Error opening file
except IOError:
    print("File not found.")
except:
    print("Unkown error.")
