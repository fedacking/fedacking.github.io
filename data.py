from pickle import load

with open("data.pickle", "rb+") as data_file:
    dict_matchups = load(data_file)
