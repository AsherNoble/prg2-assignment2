from model.application.Manager import Manager
from model.application.Player import Player
from model.application.Players import Players
from model.application.Team import Team
from model.application.Teams import Teams
from model.enums.Position import Position

class SeedData:
    def __init__(self):
        self.players = []
        self.teams = []
        self.managers = []

    def seed(self):
        self.populate_players()
        self.populate_teams()
        self.populate_managers()
        self.assign_team_members()
        return self

    def populate_players(self):
        self.players.extend([
            Player("Ethan", "Lockyer", None, Position.Fullback),
            Player("Lucas", "Inglis", None, Position.Wing),
            Player("Max", "Thurston", None, Position.Centre),
            Player("Noah", "Smith", None, Position.Halfback),
            Player("Kai", "Fittler", None, Position.Forward),
            Player("Leo", "Tallis", None, Position.Wing),
            Player("Isaac", "Slater", None, Position.Centre),
            Player("Owen", "Minichiello", None, Position.Fullback),
            Player("Liam", "Hodges", None, Position.Forward),
            Player("Caleb", "Hayne", None, Position.Halfback),
            Player("Ryan", "Burgess", None, Position.Centre),
            Player("Mason", "Carney", None, Position.Wing),
            Player("Zac", "Marshall", None, Position.Forward),
            Player("Nathan", "Gasnier", None, Position.Fullback),
            Player("Finn", "Gallen", None, Position.Wing),
            Player("Jake", "Civoniceva", None, Position.Centre),
            Player("Connor", "Watmough", None, Position.Forward),
            Player("Daniel", "Kennedy", None, Position.Halfback),
            Player("Aiden", "Meninga", None, Position.Wing),
            Player("Xavier", "Webcke", None, Position.Forward),
            Player("Elijah", "Pearce", None, Position.Centre),
            Player("Arlo", "Williams", None, Position.Fullback),
            Player("Hunter", "Johns", None, Position.Halfback),
            Player("Thomas", "Lewis", None, Position.Forward),
            Player("Jayden", "Chambers", None, Position.Wing),
            Player("Blake", "Walker", None, Position.Centre),
            Player("Joshua", "Stewart", None, Position.Forward),
            Player("Cooper", "Morris", None, Position.Wing),
            Player("Eli", "Lane", None, Position.Halfback),
            Player("Jordan", "Jennings", None, Position.Centre),
            Player("Tyler", "Barrett", None, Position.Fullback),
            Player("Jaxon", "Boyd", None, Position.Wing),
            Player("Luca", "Douglas", None, Position.Forward),
            Player("Riley", "Martin", None, Position.Centre),
            Player("Nathaniel", "Reynolds", None, Position.Fullback),
            Player("Charlie", "Morgan", None, Position.Wing),
            Player("Isaiah", "Baker", None, Position.Halfback),
            Player("Miles", "Ferguson", None, Position.Forward),
            Player("Zane", "Bryant", None, Position.Centre),
            Player("Archie", "Wade", None, Position.Wing),
            Player("Sebastian", "Day", None, Position.Halfback),
            Player("Grayson", "Hancock", None, Position.Forward),
            Player("Leon", "Preston", None, Position.Centre),
            Player("Ezekiel", "Rowe", None, Position.Fullback),
            Player("Jude", "Doyle", None, Position.Wing),
            Player("Asher", "Fleming", None, Position.Centre),
            Player("Carter", "O'Connor", None, Position.Forward),
            Player("Anthony", "Hughes", None, Position.Halfback),
            Player("Joel", "King", None, Position.Fullback),
            Player("Micah", "Sutton", None, Position.Wing),
            Player("Reuben", "Armstrong", None, Position.Forward),
        ])

    def populate_teams(self):
        self.teams.extend([
            Team("Ultimo", "Eels", None, Players([
                self.players[0], self.players[1], self.players[2],
                self.players[3], self.players[4], self.players[5], self.players[6]
            ])),
            Team("Chippendale", "Panthers", None, Players([
                self.players[7], self.players[8], self.players[9],
                self.players[10], self.players[11], self.players[12]
            ])),
            Team("Haymarket", "Storm", None, Players([
                self.players[13], self.players[14], self.players[15],
                self.players[16], self.players[17], self.players[18], self.players[19]
            ])),
            Team("Town Hall", "Titans", None, Players([
                self.players[20], self.players[21], self.players[22],
                self.players[23], self.players[24], self.players[25],
                self.players[26], self.players[27]
            ])),
            Team("Surry Hills", "Sharks", None, Players([
                self.players[28], self.players[29], self.players[30],
                self.players[31], self.players[32]
            ])),
            Team("Broadway", "Bulldogs", None, Players([
                self.players[33], self.players[34], self.players[35],
                self.players[36], self.players[37]
            ])),
            Team("Wynyard", "Warriors", None, Players([
                self.players[38],
                self.players[41], self.players[43],
                self.players[44], self.players[45], self.players[46],
                self.players[47], self.players[48], self.players[49]
            ]))
        ])
        for team in self.teams:
            for player in team.get_all_players().get_players():
                player.set_team(team)

    def populate_managers(self):
        self.managers.extend([
            Manager(12345, "Davey", "Dyer", None),
            Manager(1, "Aziz", "Shavershian", None),
            Manager(34896, "Head", "Hunterz", None),
            Manager(678, "Lee", "Yeoreum", None),
            Manager(912, "Dahyun", "Kim", None)
        ])

    def assign_team_members(self):

        index_pairs = [
            (0, 0),
            (1, None),
            (2, None),
            (3, 1),
            (4, 2),
            (5, None),
            (6, 3)
        ]

        for team_index, manager_index in index_pairs:
            team = self.teams[team_index]
            if manager_index is None:
                continue

            manager = self.managers[manager_index]
            if manager is not None:
                team.set_manager(manager)
                manager.assign_team(team)

    def get_players(self):
        return Players(self.players)

    def get_teams(self):
        return Teams(self.teams)

    def get_managers(self):
        return self.managers

seeded_data = SeedData().seed()