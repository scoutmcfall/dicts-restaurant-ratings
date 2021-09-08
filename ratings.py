"""Restaurant rating lister."""

#Reads the ratings in from the file
rate_file = open("scores.txt")

def lst_from_file(file):
    """Get the data from the file and return a list"""
    ratings = []
    for line in file:
        line = line.rstrip()
        strip_line = line.split(":")
        ratings.append(strip_line)
    return ratings


def list_into_dict(lst):
    """Make the list into a dictionary"""
    rest_dict = {}
    for elem in lst:
        rest_dict[elem[0]] = elem[1] 
    return rest_dict #return this into a variable so that other fxns can use it

    
def add_user_input():
    """Get and add user input to the dictionary"""
    r_name = input("What's the restaurant name?")
    score = input("What's the restaurant score?")
    return [r_name, score]

def merge_lists(list1, list2):
    """Merge and sort two lists"""
    # full_list = list1 + list2
    full_list = [list1.append(list2)]
    #full_list.sort()#getting a none type error here
    return full_list
    
def print_alph_ratings(rest_dict):
    """print an alphabetized and formatted list of ratings"""
    for key, value in rest_dict.items():
        print(f"{key} is rated {value}")

#open the file and make a list of it
initial_ratings = lst_from_file(rate_file)

#sort the list
sorted_list = sorted(initial_ratings)

#make that list into a dictionary
ratings_dict = list_into_dict(sorted_list) #assigns rest_dict to ratings_dict

#print the dictionary
print(ratings_dict)

#get new user input and put it in a list
new_r_data = add_user_input()

#add the new user data list onto the prev list
merged_lists = merge_lists(initial_ratings, new_r_data)

#sort the list
sorted_merged_lists = sorted(merged_lists) #getting a none type object is not iterable error here

#make that sorted list into a dictionary
final_dict = list_into_dict(sorted_merged_lists) #none type object is not subscriptable

#print the final ratings list
print_alph_ratings(final_dict)

