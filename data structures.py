# """
# Author: Aldiana Kucevic
# Date: 27-12-2022
# Function: Datastructuren oefening
# """
#
"""
dictionaries
"""

#friend_birthday = {"Karlijn": "31-12-2000", "Maggy": "22-12-2001", "Kim": "21-06-2001"}

# if "Kim" in friend_birthday:
#     print(friend_birthday["Kim"])
# if "Iris" not in friend_birthday:
#     print("Iris not found")
 # met een in of not in statement kan je kijken of iemand in je dictionary zit

# num_friends = len(friend_birthday)
# print("Total amount of friends in dictionary:",num_friends)

# for key in friend_birthday:
#     print(key, friend_birthday[key])

 # je kan door dictionaries heen met loops en if-else statements
 # zoals hier boven te zien is


# phonebook = {}

# phonebook["chris"] = "0500-8899"
# phonebook["clara"] = "0500-9922"
# phonebook["ethan"] = "0500-8765"
# print(phonebook)

# methode hierboven heb je een lege dict, waarbij je dingen toevoegt

# del phonebook["chris"]
# print(phonebook)
# # met del kan je iets deleten

# nog extra methodes:

#test_scores = {"person 1": 98, "person 2": 100, "person 3": 97}
# clear methode:
# test_scores.clear()
# print(test_scores)
# output: een lege dictionary

# get methode:
# value_1 = test_scores.get("person 1", "person not found")
# print(value_1)
# value_2 = test_scores.get("person 4", "person not found")
# print(value_2)
# met get kan je iets uit een dictionary plukken
# de layout is .get(key, default message)
# default message is een bericht als de key die je zoekt er niet is zoals bij value 2

# for key in test_scores.keys():
#     print(key)
# print alleen de keys

# pop method:

# score = test_scores.pop("person 1", "person not found")
# print(score)
# score_2 = test_scores.pop("person 5", "person not found")
# print(score_2)
# bijna hetzelfde als .get alleen krijg je de value ipv de key

"""
sets
"""

# met een set kan je een lijst maken en dan kijken hoe deze overeenkomen of juist niet

groep_1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
groep_2 = set([7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

# zodra je groep_1. typt krijg je een lijst met opties wat je kan doen

# om 2 sets samen te voegen:
# groep_3 = groep_1.union(groep_2)
# print(groep_3)
#
# om verschillen te zien:
# print(groep_1.difference(groep_2))
# print(groep_2.difference(groep_1))

# om te kijke  wat gelijk is aan de sets:
# groep_4 = groep_1.intersection(groep_2)
# print(groep_4)

# er is ok iets genaamd subset en superset waarmee je booleans als output krijgt

# set_1 = set([1, 2, 3, 4, 5])
# set_2 = set([1, 2])
# question_1 = set_2.issubset(set_1)
# print(question_1)
#
# question_2 = set_1.issuperset(set_2)
# print(question_2)

# bovenste 2 dingen printen BOOLEANS uit: True of False

"""
Serializing objects (Pickles)
"""

import pickle

dictionary_test = {"Katie": 2, "Joanne": 5, "Chris": 3}
output_file = open("dictionary.dat", "wb")
pickle.dump(dictionary_test, output_file)
output_file.close()

# nu is dictionary_test in een file opgeslagen
