"""Restaurant rating lister."""

#Reads the ratings in from the file
rate_file = open("scores.txt")

#Prompt the user for a restaurant name
r_name = input("What's the restaurant name?")
#Prompt the user for a restaurant score
score = int(input("What's the restaurant score?"))

#Store the new restaurant/rating in the dictionary
rest_dict = {}

ratings = []
ratings.append([r_name, score])
#split each line up by ":" and put them in a list called ratings
for line in rate_file:
    line = line.rstrip()
    strip_line = line.split(":")
    ratings.append(strip_line)
#sorts them using sorted function
ratings_2 = sorted(ratings)

#Stores them in a dictionary
for elem in ratings_2:
    rest_dict[elem[0]] = elem[1]

#And finally, spits out the ratings in alphabetical order by restaurant
#Print all of the ratings in alphabetical order (including the new one, of course)

for key, value in rest_dict.items():
    print(f"{key} is rated {value}")
#return None