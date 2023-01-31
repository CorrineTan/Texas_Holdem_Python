from . import players, playTexas
import pandas

def loadPlayers(args):
	"""
	Load roles configuration from Input folder
	"""
	users_input = None
	try:
		config_path = Path(args.users).resolve(strict=True)
		with open(config_path) as csv_file:
			roles_config = json.load(json_file)
	except FileNotFoundError:
		print(f"\n\nTable config file could not be found: {args.roles}")
		parser.print_help(sys.stderr)
		sys.exit(2)
	return roles_config


def process(args):
	"""
	Instantiate our two classes
	"""
	players = loadRolesConfig(args)
	users = loadUsersConfig(args)

	hierarchy = usersHierarchy.Hierarchy()

	hierarchy.setRoles(roles)
	hierarchy.setUsers(users)

	return hierarchy


if __name__ == "__main__":

	# Setup argparser to get input from users
	parser = argparse.ArgumentParser()
	parser.add_argument(
		"-r",
		"--community",
		help="input a list of 3 community cards",
	)
	parser.add_argument(
		"-u",
		"--users",
		help="the path to the users csv file",
	)    
	args = parser.parse_args()

	hierarchy = process(args)

	# Simple test here
	print("Sample Test Below: ")
	print("{:=^50s}".format("Split Line"))
	print("Hierarchy for User 3: ")
	res = hierarchy.getSubOrdinates(3)
	print(res)
	print("{:=^50s}".format("Split Line"))

	print("Hierarchy for User 1: ")
	res = hierarchy.getSubOrdinates(1)
	print(res)
	print("{:=^50s}".format("Split Line"))

	print("Hierarchy for User 5: ")
	res = hierarchy.getSubOrdinates(5)
	print(res)