# from pip._internal import main as pipmain
# pipmain(['install', 'pandas'])

import players, playTexas
import pandas as pd
import argparse

def setUsers(args):
	"""
	Load roles configuration from Input folder
	"""
	users_input = None
	try:
		config_path = Path(args.users).resolve(strict=True)
		with open(config_path) as csv_file:
			df = pd.read_csv(csv_file)
		players_objs = []
		df = df.reset_index()  # make sure indexes pair with number of rows
		for index, row in df.iterrows():
			listCards = []
			listCards.append(row["Card1"])
			listCards.append(row["Card2"])
			players_obj = players.Player(name=row["Player"], player_hands=listCards)
			players_objs.append(players_obj)

	except FileNotFoundError:
		print(f"\n\nPlayers file could not be found: {args.user}")
		parser.print_help(sys.stderr)
		sys.exit(2)
	return players_objs


def process(args):
	"""
	Instantiate our two classes
	"""
	players_objs = setUsers(args)
	community_cards = arg.community
	winner = playTexas.make_the_winner(players_objs, community_cards)

	return winner

if __name__ == "__main__":

	# Setup argparser to get input from users
	parser = argparse.ArgumentParser()
	parser.add_argument(
		"-c",
		"--community",
		help="input a list of 3 community cards",
	)
	parser.add_argument(
		"-u",
		"--users",
		help="the path to the users csv file",
	)    
	args = parser.parse_args()

	winner = process(args)