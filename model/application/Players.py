class Players:
    def __init__(self, players):
        self.players = players

    def get_players(self):
        return self.players

    def add(self, player):
        self.players.append(player)

    def remove(self, player):
        self.players.remove(player)

    def player(self, name):
        """
        The lookup pattern on the player list
        Parameters:
            name (String): The name of the player to search for
        Returns:
            The player object with the corresponding name, or null if not found
        """
        for player in self.players:
            if player.get_full_name() == name:
                return player
        return None

    def __str__(self):
        sb = ""
        for player in self.players:
            sb += player.get_full_name() + "\n"
        return sb