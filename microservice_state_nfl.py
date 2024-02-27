# Microservice for Russel Hueso's project
# Created by: Julian Peterson
# Purpose: Create a microservice that reads a request in the form of the name of a state
# written to a text file, then returns the team(s) in the text file if that state has
# an NFL team. Otherwise, it writes NO TEAM to the text file.

import time

# TODO: change the name of the file if it's different in your code

FILE_NAME = "state.txt"

state_dict = {
    "Alabama": None,
    "Alaska": None,
    "Arizona":	["Arizona Cardinals"],
    "Arkansas": None,
    "California": ["Los Angeles Rams", "Los Angeles Chargers", "San Francisco 49ers"],
    "Colorado":	["Denver Broncos"],
    "Connecticut": None,
    "Delaware": None,
    "Florida": ["Jacksonville Jaguars", "Miami Dolphins", "Tampa Bay Buccaneers"],
    "Georgia": ["Atlanta Falcons"],
    "Hawaii": None,
    "Idaho": None,
    "Illinois": ["Chicago Bears"],
    "Indiana": ["Indianapolis Colts"],
    "Iowa": None,
    "Kansas": None,
    "Kentucky": None,
    "Louisiana": ["New Orleans Saints"],
    "Maine": None,
    "Maryland":	["Baltimore Ravens", "Washington Commanders"],
    "Massachusetts": ["New England Patriots"],
    "Michigan":	["Detroit Lions"],
    "Minnesota": ["Minnesota Vikings"],
    "Mississippi": None,
    "Missouri":	["Kansas City Chiefs"],
    "Montana": None,
    "Nebraska": None,
    "Nevada": ["Las Vegas Raiders"],
    "New Hampshire": None,
    "New Jersey": ["New York Giants", "New York Jets"],
    "New Mexico": None,
    "New York":	["Buffalo Bills"],
    "North Carolina": ["Carolina Panthers"],
    "North Dakota": None,
    "Ohio":	["Cincinnati Bengals","Cleveland Browns"],
    "Oklahoma": None,
    "Oregon": None,
    "Pennsylvania":	["Philadelphia Eagles", "Pittsburgh Steelers"],
    "Rhode Island": None,
    "South Carolina": None,
    "South Dakota": None,
    "Tennessee": ["Tennessee Titans"],
    "Texas": ["Dallas Cowboys", "Houston Texans"],
    "Utah": None,
    "Vermont": None,
    "Virginia": None,
    "Washington": ["Seattle Seahawks"],
    "West Virginia": None,
    "Wisconsin": ["Green Bay Packers"],
    "Wyoming": None
}

while True:
    time.sleep(3)
    with open(FILE_NAME, 'r') as file:
        state_string = file.readline().strip()
        if state_string not in state_dict:
            continue

    team_list = state_dict[state_string]

    # no team in that state
    if team_list is None:
        with open(FILE_NAME, 'w') as file:
            print("This state does not have a team")
            file.write("NO TEAM")

    # state has a team(s)
    else:
        with open(FILE_NAME, 'w') as file:
            for team in team_list:
                print(team)
                file.write(f'{team}\n')
