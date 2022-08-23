"""Restaurant rating lister."""


# pseudocode
#open the file
#reads the ratings from the file
#save the rates to a dictionary
#plit out the ratings in alphabetic order

from curses.ascii import isdigit


def restaurantes_rates(file_name):

    ratings = {}

    with open(file_name) as restaurante_ratings:     

        for line in restaurante_ratings.readlines():
            restaurante = line.replace("\n" , "")
            restaurante_list = restaurante.split(':')
            restaurante_name = restaurante_list[0]
            restaurante_rates = restaurante_list[1]        
            ratings[restaurante_name] = restaurante_rates
   
    return ratings


def restaurante_from_user_to_dict(restaurante_ratings):

        restaurante_from_user = input("Enter a Restaurante name: ").title()          

        while True:
            restaurante_rating_from_user = input("Enter a rate between 1 and 5 for this restaurante: ")
                        
            if restaurante_rating_from_user.isdigit() != True:
                print("not valid Rate")
                continue    

            restaurante_rating_from_user_int = int(restaurante_rating_from_user)

            if restaurante_rating_from_user_int <= 0 or restaurante_rating_from_user_int > 5:
                print("not valid Rate: ")
                continue  
            
            break  

        restaurante_ratings[restaurante_from_user] = restaurante_rating_from_user



def print_ratings(ratings):

    sort_dict = ratings.items()
    new_sort_dict = sorted(sort_dict)
    print(*new_sort_dict, sep="\n")   






ratings_for_restaurantes = restaurantes_rates("scores.txt")
restaurante_from_user_to_dict(ratings_for_restaurantes)
print_ratings(ratings_for_restaurantes)
 

