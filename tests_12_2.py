from unittest import TestCase


class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance = 0

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def run(self):
        self.distance += self.speed

    def walk(self):
        self.distance += self.speed / 2


class Tournament:
    def __init__(self, distance, runners):
        self.distance = distance
        self.runners = runners

    def start(self):
        finished = {}
        place = 1

        while len(finished) < len(self.runners):
            for runner in self.runners:
                if runner.name not in finished.values():
                    runner.run()
                    if runner.distance >= self.distance:
                        finished[place] = runner.name
                        place += 1

        return finished


class TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    def test_race_usain_nick(self):
        self.usain.distance = 0
        self.nick.distance = 0

        tournament = Tournament(90, [self.usain, self.nick])
        result = tournament.start()
        self.all_results[1] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    def test_race_andrey_nick(self):
        self.andrey.distance = 0
        self.nick.distance = 0

        tournament = Tournament(90, [self.andrey, self.nick])
        result = tournament.start()
        self.all_results[2] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    def test_race_all(self):
        self.usain.distance = 0
        self.andrey.distance = 0
        self.nick.distance = 0

        tournament = Tournament(90, [self.usain, self.andrey, self.nick])
        result = tournament.start()
        self.all_results[3] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    @classmethod
    def tearDownClass(cls):
        for key in sorted(cls.all_results.keys()):
            print(cls.all_results[key])







