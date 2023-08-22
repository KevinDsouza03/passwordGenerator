#Author: KevinDsouza03
#Desc: Password generator using random number generation and a user inputted length.
import secrets
import string
import keyring as kr

def gen_password(length: int):
    allowed_chars: str = string.ascii_letters + string.digits + string.punctuation
    password: str = ''.join(secrets.choice(allowed_chars) for i in range(length))
    return password


def store_password(application_name: str, username: str, password: str):
    kr.set_password(application_name,username,password)

def generate_store_workflow():
    app_N = str(input("What application are you generating a password for? ")).lower()
    user_N = str(input(f"What is your username for {app_N} "))
    password = gen_password(32)
    try:
        store_password(app_N,user_N,password)
        print(f"Your password has been created and stored with your provided Application Name({app_N}) and Username({user_N}). ")
    except:
        print("Password was not successfully generated nor stored.")

def retrieve_pass_workflow():
    app_N = str(input("For what application are you retrieving info? ")).lower()
    #user_N = str(input(f"What is your username for {app_N}"))
    try:
        credentials = kr.get_credential(service_name=app_N,username=None)
        print(f"Application: {app_N}\nUsername: {credentials.username}\nPassword: {credentials.password}")
    except:
        print("Could not retrieve password.")

def deleting_pass_workflow():
    app_N = str(input("For what application are you deleting the password? "))
    user_N = str(input(f"What is your username for {app_N} "))
    try:
        kr.delete_password(service_name=app_N,username=user_N)
        print("Successfully deleted password.")
    except:
        print("Password was not deleted.")
