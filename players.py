import json
from dataclasses import dataclass

@dataclass
class Players:
	"""
	A class for Player
	"""

	name: str
	player_hands: list[str]


	def getName(self):
		"""
		Getter for name
		"""
		return self.name


	def getPlayerHands(self):
		"""
		Getter for list of player's hands
		"""
		return self.player_hands


	def objtToDict(self):
		"""
		Convert object to dict
		"""
		output = {
			"Name": self.getName(),
			"players_hands": self.getPlayerHands()
		}
		return output
