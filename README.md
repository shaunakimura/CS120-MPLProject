# SK-Final-Project-MPL

## Team Members
* Shauna Kimura

## Instructions
* Open project directory in Terminal
* Enter command 'g++ -std=c++1y main.cpp' to compile C++ project.
* Enter command './a.out' to execute program.
* Enter the title of a TV show or movie when prompted to search on Netflix. Input is case insensitive.
* If the given title exists in the Netflix database, a message is displayed to the user and information is provided (type, release year, rating, description). Netflix is opened in a new tab in the user's browser.
* If the given title is not in the database, a message is displayed to the user and the program ends.

## Summary
I created this project to search for existing movies and TV shows on Netflix.
The project is launched from a C++ program (main.cpp) where it prompts a user for
the title of a movie or TV show. Next, the program calls a Python script (netflix.py)
and sends the given title as a parameter. The Python script scrapes a dataset (netflix_titles.csv)
and stores all titles as keys in a dictionary. Each title in the dictionary contains a type (movie or TV show), release year, rating, and a description found from the dataset. If the title provided by the user
exists in the dictionary, a message is displayed and information is provided. The program then opens
up netflix.com in the user's browser. The dataset I used was found from kaggle.com and was updated 3 months ago.

# Sources
* Netflix Movies and TV Shows dataset - https://www.kaggle.com/shivamb/netflix-shows
* Referenced Lisa Dion's Image Manipulation example for calling Python script from C++
