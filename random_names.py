# A simple program that takes a txt file (check line 22) of names (make sure that
# each name is on a new line), and selects a random number of names from that file.
# To change number of winning names go to line 33 and change the while condition.
# This program is useful for selcting a random winner or winners from a group 
# of people. Line 38-41 just prints the winners in a neat format.

from random import randint
from pathlib import Path

names = {}
chosen = []
key = 0
cycles = 0
place = 1

# load file with names
path = Path("Muntogi Day Raffle entries.txt")
contents = path.read_text()

# convert the txt file into a dictionary
lines = contents.splitlines()
for line in lines:
    names[key] = line
    key += 1

# change this value to change number of winners
while cycles < 3:
    number = randint(0, max(names))

    for name in names:
        name = names.get(number)
        if name not in chosen:
            chosen.append(name)
            cycles += 1
        else:
            continue
        break

for name in chosen:
    print(f"{place}. {name}")
    place += 1