# # #ALL NOTES FROM SLIDES BELOW. ASSIGNMENT IS FIRST with soime already made corrections from our  solution video

from webbrowser import get

class Player:

    players = []
    
    def __init__(self, attributes):
        self.name = attributes['name']
        self.age = attributes['age']
        self.position = attributes['position']
        self.team = attributes['team']
        
    def __repr__(self): #this function will reproduce how our info is printed to the console, we used an f statement 
        return f"Player: {self.name}, {self.age} y/o, pos: {self.position}, team: {self.team}"

    @classmethod
    def get_team(cls, team_list):
        new_team = []
        for every_index in team_list:
            new_team.append(cls(every_index))
        return new_team


#3 prompt Finally, given the example list of players at the top of this module (the one with many players)
#write a for loop that will populate an empty list with Player objects from the original list of dictionaries.

#were gonna do a for loop over a list of dictionaires,
#each time we loop through a new dict in our list,
#use that dictionary info to create a new Player instance

players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
},
{
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
},
{
    "name": "Kyrie Irving", 
    "age":32, 
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
},
{
    "name": "Damian Lillard", 
    "age":33, "position": "Point Guard", 
    "team": "Portland Trailblazers"
},
{
    "name": "Joel Embiid", 
    "age":32, "position": "Power Foward", 
    "team": "Philidelphia 76ers"
},
{
    "name": "", 
    "age":16, 
    "position": "P", 
    "team": "en"
}
]
print(Player.get_team(players))

new_team = []

for player_dict in players:   #this for loop goes into my list of dictionaries, so we created a var called "player_dict" that's inside our list we called Players
    player = Player(player_dict)
    new_team.append(player)


print(new_team)

kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"} 

print(kevin["name"])
player_kevin = Player(kevin) #in order to store the info created on line 51 we create an instanxe of kevin so we can call upon and use it.
print(player_kevin)


# jason = {"name": "Jason Tatum", "age":24, "position": "small forward", "team": "boston celtics"}

# print (jason['name'])
# player_jason = Player(jason)
# print(player_jason)

# kyrie ={"name": "Kyrie Irving", "age":32, "position": "Point Guard", "team": "Brooklyn Nets"}

# print (kyrie['name'])
# player_kyrie = Player(kyrie)
# print(player_kyrie)

# damian = {"name": "Damian Lillard", "age":33, "position": "Point Guard", "team": "Portland Trailblazers"}

# print(damian['name'])
# player_damian = Player(damian)
# print(player_damian)

# joel = {"name": "Joel Embiid", "age":32, "position": "Power Foward", "team": "Philidelphia 76ers"}

# print(joel['name'])
# player_joel = Player(joel)
# print(player_joel)


#Making Object Instances from Dictionary Data

# kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}

# class Player:
#     def __init__(self, name, age, position, team):
#         self.name = name
#         self.age = age
#         self.position = position
#         self.team = team

#Okay, now that we have a class defined, let's take our dictionary info to make a Player instance.

# kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}

# # Pass in all the values from the dictionary by their keys

# player_kevin = Player(kevin["name"], kevin["age"], kevin["position"], kevin["team"])
# print(player_kevin.position) # prints small forward

# class Player:
#     def __init__(self, attr_dict):
#         self.attr_dict = {
#             "name": "name",
#             "age": "age",
#             "position": "position",
#             "team": "team"
#         }

# kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}

# Uncomment the line below to test
#player_kevin = Player(kevin)

#They are widely used, extremely powerful and considered fundamental for one primary reason:
#"They provide constant-time lookup, insertion and deletion on average"

#Many extremely common problems are best solved with the key-value pair data structure (commonly called a hash table in computer science.) 

#Here are some of the names you will hear them called.

# Dictionaries	Python
# Objects (misleadingly!)	JavaScript, JSON
# Maps, Hash Maps	Java, C++
# Hash Table	C#
# Associative Array	PHP