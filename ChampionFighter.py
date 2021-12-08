"""
Champion Fighter
Takes data on Champion's stats from Riot Games' League of Legends
and pits two random champions against each other to see
who would win.
"""

print("Welcome to Champion Fighter by John Lang! Two random champions will fight.")
from urllib.request import urlopen
import json
import random

class Character:
    def __init__(self, name, hp, dmg,):
        self.name = name
        self.hp = hp
        self.dmg = dmg

    def status(self):
        print(self.name, ": ", self.hp, "hp")
        
    def attack(self, opponent):
        opponent.hp-=self.dmg
        print(self.name, "deals", self.dmg ,  "damage to", opponent.name, ".")

#Grabs the champion data from Riot and puts it into data_json        
url = "http://ddragon.leagueoflegends.com/cdn/11.23.1/data/en_US/champion.json"
response = urlopen(url)
data_json = json.loads(response.read())

champlist = []
for i in data_json["data"]:
    fullname = i + ", " + data_json["data"][i]["title"]
    health = data_json["data"][i]["stats"]["hp"]
    damage = data_json["data"][i]["stats"]["attackdamage"]
    champlist.append(Character(fullname, int(health), int(damage)))
    
champ1 = random.choice(champlist)
champ2 = random.choice(champlist)
print("Our Champions today are: ", champ1.name, "and", champ2.name, ". Press the enter key to start. ")
input()

while(champ1.hp > 0 and champ2.hp > 0):
    print("")
    champ1.status()
    champ2.status()
    print("")
    champ1.attack(champ2)
    print("")
    champ1.status()
    champ2.status()
    print("")
    champ2.attack(champ1)

if(champ1.hp > champ2.hp):
    print(champ1.name, "wins!")
else:
    print(champ2.name, "wins!")

input("Press enter to exit.")
