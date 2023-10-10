import pandas as pd
from color import bcolors

class BankApplication:
    def __init__(self, hash_func):
        self.database = pd.DataFrame(columns=['email', 'password_hash'])
        self.hash_function = hash_func
        self.password_length = 8
        
    def add_user(self, id, email, password):
        if len(password) == self.password_length:
            password_hash = self.hash_function(password)
            self.database.loc[id] = [email, password_hash]
        else:
            print(f"The length of password should be {self.password_length}")

    def withdraw(self, id, password, amount):
        password_hash = self.database.loc[id, 'password_hash']
        if len(password) != self.password_length:
            print(f"The length of password should be {self.password_length}")
        elif password_hash == self.hash_function(password):
            print(f"Good morning, {id}. {bcolors.OKGREEN}You are authenticated{bcolors.ENDC}")
            print(f"Here is {bcolors.OKGREEN}${amount}{bcolors.ENDC}")
        else:
            print(f"Your password is {bcolors.FAIL}not valid{bcolors.ENDC}")