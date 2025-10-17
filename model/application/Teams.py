class Teams:
    def __init__(self, teams):
        self.teams = teams

    def get_teams(self):
        return self.teams

    def add(self, team):
        self.teams.append(team)

    def remove(self, team):
        self.teams.remove(team)

    def team(self, local_name):
        for team in self.teams:
            if team.local_name == local_name:
                return team
        return None


    def __str__(self):
        sb = ""
        for team in self.teams:
            sb += team.__str__() + "\n"
        return sb
