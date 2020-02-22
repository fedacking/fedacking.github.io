from data import dict_matchups

print("Welcome to Feda's matchup searcher!")
dict_list_matchup = dict()
for champion in dict_matchups:
    opponent_list = []
    for opponent in dict_matchups[champion]:
        opponent_list.append((dict_matchups[champion][opponent], opponent))
    opponent_list = sorted(opponent_list, key=lambda tup: tup[0])
    dict_list_matchup[champion] = opponent_list
print("Input the camp you want to counter")

champ = input()
try:
    for counter in dict_list_matchup[champ]:
        print(counter)
except KeyError:
    print("Write correctly chimp")