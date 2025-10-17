class Team:
    REQUIRED_TEAM_SIZE = 5

    def __init__(self, local_name, team_name, manager, all_players):
        self.local_name = local_name
        self.team_name = team_name
        self.manager = manager
        self.all_players = all_players
        self.current_team = []
        for i in range(Team.REQUIRED_TEAM_SIZE):
            self.current_team.append(None)

    def get_team_name(self):
        return self.team_name

    def get_manager(self):
        return self.manager

    def set_manager(self, manager):
        self.manager = manager

    def get_all_players(self):
        return self.all_players

    def __str__(self):
        return self.local_name + " " + self.team_name