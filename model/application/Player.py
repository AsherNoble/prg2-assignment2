class Player:
    def __init__(self, first_name, last_name, team, position):
        self.first_name = first_name
        self.last_name = last_name
        self.team = team
        self.position = position

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_team(self):
        return self.team

    def set_team(self, team):
        self.team = team

    def get_position(self):
        return self.position

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.position.__str__()})"