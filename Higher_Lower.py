# Higher Lower Game with web scraped database for names and follower count
import random

# Code for importing a list of the top 100 Twitter accounts from a website
import requests
from bs4 import BeautifulSoup

url = 'https://www.socialtracker.io/toplists/top-100-twitter-users-by-followers/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table')
rows = table.find_all('tr')

database = []
for row in rows:
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    database.append([cols[2:4]])
database = database[1:]

print("Higher Lower Game in Python")

points = 0


def game():
    """ Recursive function that runs the game """

    global points

    first_acc_list = random.choice(database)
    database.remove(first_acc_list)
    second_acc_list = random.choice(database)
    database.remove(second_acc_list)
    first_acc = [item for sublist in first_acc_list for item in sublist]
    first_acc_name = first_acc[0]
    first_acc_followers = first_acc[1]
    second_acc = [item for sublist in second_acc_list for item in sublist]
    second_acc_name = second_acc[0]
    second_acc_followers = second_acc[1]
    highest_acc = highest_follower_acc(first_acc, second_acc)

    user_choice = input(f"Who has a higher follower count {first_acc_name} or {second_acc_name} ?. Type A for the first Account and B for the second: " )
    if user_choice == "A" and highest_acc == first_acc_name:
        print("Correct Answer")
        points += 1
        print(f"You have {points} points\n")
        game()
    elif user_choice == "B" and highest_acc == second_acc_name:
        print("Correct Answer")
        points += 1
        print(f"You have {points} points\n")
        game()
    else:
        print("Wrong Answer\nGame Over")
        print(f"You managed to get {points} points")
        return


def highest_follower_acc(acc_1, acc_2):
    """ Function to determine which of two accounts has the highest followers"""

    if int(acc_1[1].replace(",", "")) > int(acc_2[1].replace(",", "")):
        return acc_1[0]
    else:
        return acc_2[0]


game()