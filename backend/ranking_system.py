class Player:
    def __init__(self, name, points):
        self.name = name
        self.points = points

    def __str__(self):
        return f'{self.name}: {self.points} points'

class RankingSystem:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def calculate_ranking(self):
        self.players.sort(key=lambda player: player.points, reverse=True)
        return self.players

    def display_rankings(self):
        rankings = self.calculate_ranking()
        for index, player in enumerate(rankings, start=1):
            print(f'{index}. {player}')