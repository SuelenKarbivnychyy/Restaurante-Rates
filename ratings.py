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

        restaurante_from_user = input("Enter a Restaurante name: ").title()       
        

        while True:
            restaurante_rate_from_user = input("Enter a rate between 1 and 5 for this restaurante: ")
                        
            if restaurante_rate_from_user.isdigit() != True:
                print("not valid Rate")
                continue    

            restaurante_rate_from_user_int = int(restaurante_rate_from_user)

            if restaurante_rate_from_user_int <= 0 or restaurante_rate_from_user_int > 5:
                print("not valid Rate: ")
                continue  
            
            break  

        ratings[restaurante_from_user] = restaurante_rate_from_user

        for line in restaurante_ratings.readlines():
            restaurante = line.replace("\n" , "")
            restaurante_list = restaurante.split(':')
            restaurante_name = restaurante_list[0]
            restaurante_rates = restaurante_list[1]        
            ratings[restaurante_name] = restaurante_rates

    sort_dict = ratings.items()
    new_sort_dict = sorted(sort_dict)

    # print(*new_sort_dict, sep="\n")
    return new_sort_dict

rates_from_restaurante = restaurantes_rates("scores.txt")
print(*rates_from_restaurante, sep="\n")    


