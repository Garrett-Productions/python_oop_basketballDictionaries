class Player:
    
    players = []
    
    def __init__(self,attributes):
        self.name = attributes['name']
        self.age = attributes['age']
        self.position = attributes['position']
        self.team = attributes['team']

    def __repr__(self):
        return f"Player: {self.name}, {self.age} years old, {self.position}, on {self.team}"
    
    @classmethod
    
    def get_team(cls, team_list):
        new_team = []
        
        for every_team in team_list:
            new_team.append(cls(every_team))
        return new_team

players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "brooklyn nets"
    },
    {
        "name": "kyrie irving",
        "age": 32,
        "position": "point guard",
        "team": "brooklyn nets"
    
    }
]
print(Player.get_team(players))

new_team = []

for player_obj in players:
    player = Player(player_obj)
    new_team.append(player)
    

print(new_team)

kevin = {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "brooklyn nets"
    }

player_kevin = Player(kevin)
print(player_kevin)