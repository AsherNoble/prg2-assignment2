class Manager:
    def __init__(self, id, first_name, last_name, team):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.team = team

    def has_id(self, id):
        return self.id == id

    def get_team(self):
        return self.team

    def assign_team(self, team):
        self.team = team

    def __str__(self):
        return f"{self.first_name} {self.last_name}"