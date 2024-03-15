import pandas
import random


class PasswordManager():

    def __init__(self, website, username, password):
        self.website = website
        self.username = username
        self.password = password

    def show_dict(self):   # for dewelopment only
        my_dict = pandas.read_csv("secret_dict.csv")
        print(my_dict)

    def save_new_password(self, website, username, password, path):
        new_row = {"website" : [website], "username" : [username], "password" : [password]}
        data_frame = pandas.DataFrame(new_row)
        data_frame.to_csv(path, mode="a", index=False, header=False)
    
    def generate_random_password(self):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
        
        psw_letters = [random.choice(letters) for x in range(random.randint(7, 10))]
        psw_numbers = [random.choice(numbers) for x in range(random.randint(4, 6))]
        psw_symbols = [random.choice(symbols) for x in range(random.randint(2, 3))]
        
        password_list = psw_letters + psw_numbers + psw_symbols
        random.shuffle(password_list)
        joined_password = "".join(password_list)
        return joined_password
    
    