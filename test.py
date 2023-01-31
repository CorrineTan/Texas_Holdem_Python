import pandas as pd
with open("players.csv") as csv_file:
	df = pd.read_csv(csv_file)
df = df.reset_index()  # make sure indexes pair with number of rows
for index, row in df.iterrows():
	print(row["Player"])
	listCards = []
	listCards.append(row["Card1"])
	listCards.append(row["Card2"])
	print(listCards)

