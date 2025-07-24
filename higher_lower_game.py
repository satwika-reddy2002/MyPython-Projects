import random
from game_data import data
from art import logo,vs
# use variables to put the name, follower_count, description, country
def details(account):
    """takes the account data and gives in printable format"""
    account_name = account["name"]
    account_follower = account["follower_count"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description} from {account_country}"


def check_answer(user_guess,a_followers, b_followers):
     """take a users guess and follower count and returns if they got it right"""
     if a_followers > b_followers:
         return guess == "a"
     else :
         return guess == "b"

print(logo)
score = 0
continue_game = True
account_b = random.choice(data)
while continue_game:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
      account_b = random.choice(data)

    print(f"Compare A : {details(account_a)}")
    print(vs)
    print(f"Compare B : {details(account_b)}")

    #get user input
    guess = input("who has more followers? Type A or B :").lower()

    #check if user is correct
    #-get follower count
    # use if statement for problem is correct or no
    a_follower_account = account_a["follower_count"]
    b_follower_account = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_account,b_follower_account)

    #give user the feedback
    if is_correct:
     score += 1
     print(f"you're right and you're score is {score}")
    else:
     continue_game = False
     print(f"sorry you loose and you're final score is {score}")



    # loop the statements each time and increase the count of correct answers
