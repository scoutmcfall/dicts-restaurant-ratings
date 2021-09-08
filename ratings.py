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
    full_list = list1.append(list2)
    full_list.sort()
    
    return full_list
    
def print_alph_ratings(rest_dict):
    """print an alphabetized and formatted list of ratings"""
    for key, value in rest_dict.items():
        print(f"{key} is rated {value}")


initial_ratings = lst_from_file(rate_file)

sorted_list = sorted(initial_ratings)

ratings_dict = list_into_dict(sorted_list)
#print(ratings_dict)
new_r_data = add_user_input()
merged_lists = merge_lists(sorted_list, new_r_data)
final_dict = list_into_dict(merged_lists)
print_alph_ratings(final_dict)

