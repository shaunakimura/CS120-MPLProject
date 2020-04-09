import bs4 as bs
import csv
import string
import sys
from time import sleep
import urllib.request
import webbrowser

# Store command line arguments in variables
title = sys.argv[1]
# Make title case insensitive
title = title.lower()
try:
    # Append titles from csv file to list
    filename = "netflix_titles.csv"
    reader = csv.reader(open(filename))

    netflix_data = {}
    for row in reader:
        key = row[2].lower()  # show/movie title
        # Store certain data from csv to dictionary
        netflix_data[key] = row[1], row[7], row[8], row[11]

    print()
    print("Scraping Netflix data...\n")
    sleep(3) # Just for effect

    # Display size of database
    print("Netflix currently has", format(len(netflix_data), ",d"), "TV shows and movies.\n")
    sleep(3) # Just for effect

    # Check for title in list
    if title in netflix_data:
        print(string.capwords(title), "is on Netflix!")
        print("------------------------------------------------")
        # TV/movie info
        print("* Type:", netflix_data[title][0])
        print("* Release Year:", netflix_data[title][1])
        print("* Rating:", netflix_data[title][2])
        print("* Description:", netflix_data[title][3])
        print()
        sleep(3)

        # Open Netlfix in browser
        print("Go check it out!")
        print("Launching Netflix...")
        sleep(10)
        webbrowser.open('https://www.netflix.com/browse', new=2)
    else:
        print(title, "is not on Netflix.")

    # Display top 10 Netflix series using web scraper
    print()
    print("Best Netflix Series and Shows to Watch Right Now")
    print("------------------------------------------------")
    source = urllib.request.urlopen('https://editorial.rottentomatoes.com/guide/best-netflix-shows-and-movies-to-binge-watch-now/')
    soup = bs.BeautifulSoup(source,'lxml')

    top = []
    for div in soup.find_all('div', class_='article_movie_title'):
        top.append(div.find('a').text)

    # Reverse list so #1 movie is first index
    top.reverse()
    for i in range(10):
        print("#", i + 1, ": ", top[i], sep='')

    print("Happy Netflixing!")


# Error opening file
except IOError:
    print("File not found.")
except:
    print("Unkown error.")
