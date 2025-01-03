import re
import csv
data_dictionary = {}
csv_file_location = 'E:/PythonProject/user_data.csv'
try: 
    with open(csv_file_location, mode='r') as file:
         reader = csv.DictReader(file)
         for row in reader: data_dictionary[row['email']] = {'username': row['username'], 'password': row['password']}
except FileNotFoundError: data_dictionary = {}

def save_user_data():
    """ 
    Save user data to the CSV file. 
    """
    with open(csv_file_location, mode='w', newline='') as file:
         fieldnames = ['email', 'username', 'password']
         writer = csv.DictWriter(file, fieldnames=fieldnames)
         writer.writeheader()
         for email, data in data_dictionary.items():
             writer.writerow({'email': email, 'username': data['username'], 'password': data['password']})
    



def login (email,password) :  
        """
            Log in a user by checking their email and password.
            Args: 
            email (str): The user's email.
            password (str): The user's password.
        """          
        if email in data_dictionary and data_dictionary[email]['password'] == password:
             print(f"Welcome back, {data_dictionary[email]['username']}!") 
        else:
            print("Invalid email or password.")     

         
def register(email,username,password,confirm_password):
    """ Register a new user by saving their email, username, and password. 
        Args: 
        email (str): The user's email.
        username (str): The user's username.
        password (str): The user's password.
        confirm_password (str): The user's password confirmation.
        Raises: ValueError: If the email is invalid, the password is too short, or the passwords do not match.
    """
    email_regular_expression = r'[A-z0-9\.]+@[A-z0-9]+\.[A-z]+'
    if re.match(email_regular_expression,email) :
        if len(password) < 8 :
            raise ValueError("Password must be at least 8 characters")
        else :
            if password != confirm_password :
                raise ValueError ("Please confirm password correctly")
            else :
                data_dictionary[email] = {"password": password, "username": username} 
                save_user_data()
                print(f"Welcome {username}, you successfully registered!")
    else :
        print("Please ener valid email")
    


option = input("Enter 'l' for login or 'r' for register :  ")

if option == "l" :
    email = input("Enter your email : ")
    password = input("Enter your password : ")
    login(email,password)

elif option == "r" :
    username = input("Please enter your username : ")
    email = input("Enter valid email : ")
    password = input("Enter your password : ")
    confirm_password = input("Confirm your password : ")
    register(email,username,password,confirm_password)

else :
    print("Please enter valid option")

