//
// Created by Shauna Kimura on 4/7/20.
//

#include <fstream>
#include <iostream>
#include <string>
using namespace std;

// Different OSs use different CLI commands to run Python
#ifdef _WIN32
const string python = "python";
#else
const string python = "python3";
#endif

/*
 * Prompts the user for a movie or TV show title.
 * While the input is empty, prompt user again.
 * Return title name.
 */
string get_title();

/*
 * Call Python script to search for title in Netflix database.
 */
void search_netflix(string title);

int main() {
  cout << "Let's use the Netflix search tool!" << endl;
  string title_name = get_title();

  search_netflix(title_name);

  return 0;
}

string get_title() {
  string title_name;
  cout << "Enter the name of a TV show or movie title: ";
  // Validate string is not empty
  getline(cin, title_name);
  while (title_name.empty()) {
      cout << "Please enter a title name: ";
      getline(cin, title_name);
  }

  return title_name;
}

void search_netflix(string title) {
  string command = python + " netflix.py \"" + title + "\"";
  system(command.c_str());
}
