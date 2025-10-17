from model.application import Team
from model.exception.UnauthorisedAccessException import UnauthorisedAccessException
from model.utils.SeedData import seeded_data
from model.application.Teams import Teams

class League:
    def __init__(self, seeded_teams, seeded_players, seeded_managers):
        self.teams = seeded_teams
        self.manageable_teams = Teams([team for team in self.teams.get_teams() if team.get_manager() is None])
        self.players = seeded_players
        self.managers = seeded_managers
        self.logged_in_manager = None

    def get_teams(self):
        return self.teams

    def get_manageable_teams(self):
        return self.manageable_teams

    def get_players(self):
        return self.players

    def get_logged_in_manager(self):
        return self.logged_in_manager

    def set_logged_in_manager(self, manager):
        self.logged_in_manager = manager

    def set_manager_for_team(self, manager, team):
        """
        Assigns a manager to a new team

        Parameters:
            manager (Manager.Manager): The manager to assign to the team
            team (Team.Team): The team to assign to the manager
        """
        if manager is None or team is None:
            raise Exception("Team and Manager cannot be null")
        if team.get_manager() is not None:
            raise Exception("Team already has a Manager. You should only be calling this method on a Team that is in the manageableTeams list")
        if manager.get_team() is not None:
            old_team = manager.get_team()
            old_team.set_manager(None)
            self.manageable_teams.add(old_team)
        manager.assign_team(team)
        team.set_manager(manager)
        self.manageable_teams.remove(team)

    def withdraw_manager_from_team(self, manager):
        """
        Withdraws a manager from the team they are currently assigned to
        Parameters:
            manager (Manager.Manager): The manager to be withdrawn
        """
        if manager is None:
            raise Exception("Manager cannot be null")
        if manager.get_team() is None:
            raise Exception("Manager is not assigned to any team")
        self.manageable_teams.add(manager.get_team())
        manager.get_team().set_manager(None)
        manager.assign_team(None)

    def validate_manager(self, id):
        """
        Confirms that the id is a valid manager id

        Parameters:
            id (int): The id to compare with
        Returns:
            The Manager object with that id
        Raises:
            UnauthorisedAccessException: If there is no manager in the League with the provided id
        """
        for manager in self.managers:
            if manager.has_id(id):
                return manager
        raise UnauthorisedAccessException("Invalid manager credentials")

league = League(seeded_data.get_teams(), seeded_data.get_players(), seeded_data.get_managers())
