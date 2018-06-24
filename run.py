import sc2, sys
from __init__ import run_ladder_game
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer

from hackerbot import hackerbot
bot = Bot(Race.Protoss, hackerbot())

# Start game
if __name__ == '__main__':
    if "--LadderServer" in sys.argv:
        # Ladder game started by LadderManager
        print("Starting ladder game...")
        run_ladder_game(bot)
    else:
        # Local game
        print("Starting local game...")
        sc2.run_game(sc2.maps.get("(2)AcidPlantLE"), [
            bot,
            Computer(Race.Random, Difficulty.VeryHard)
        ], realtime=False)
