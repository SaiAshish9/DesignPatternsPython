from abc import ABC, abstractmethod

class Game(ABC):
    @abstractmethod
    def initialize(self):
        pass
    @abstractmethod
    def start_play(self):
        pass
    @abstractmethod
    def end_play(self):
        pass
    def play(self):
        self.initialize()
        self.start_play()
        self.end_play()

class Cricket(Game):
    def end_play(self):
        print("Cricket Game Finished!")

    def initialize(self):
        print("Cricket Game Initialized! Start playing.")

    def start_play(self):
        print("Cricket Game Started. Enjoy the game!")

class Football(Game):
    def end_play(self):
        print("Football Game Finished!")

    def initialize(self):
        print("Football Game Initialized! Start playing.")

    def start_play(self):
        print("Football Game Started. Enjoy the game!")

if __name__ == "__main__":
    game = Cricket()
    game.play()
    print()
    game = Football()
    game.play()
