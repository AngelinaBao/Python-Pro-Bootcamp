import random
from game_data import data, logo, vs

def clear():
  """clear screen."""
    import os
    return os.system("cls")

def pick_person():
    """Random returns a person from data library and print person info."""
    account = random.choice(data)
    return account

def person_info(role, account):
    """return account infomation."""
    return f"{role}: {account['name']}, a {account['description']}, from {account['country']}."

def compare_account(compare_a, aginst_b):
    """return winner.(string)"""
    if compare_a["follower_count"] >= aginst_b["follower_count"]:
        winner = "Compare A"
    else:
      winner = "Against B"
    return winner

def guess_higher():
    """guess higher game."""
    score = 0
    print(logo)
    against_b = pick_person()
  
    go_on = True
    while go_on:
      compare_a = against_b
      against_b = pick_person()
      while against_b == compare_a:
        against_b = pick_person()

      print(person_info("Compare A", compare_a))
      print(vs)
      print(person_info("Against B", against_b))
          
      guess = input("Who has more followers? Type 'A' or 'B': ").title()
      winner = compare_account(compare_a, against_b)

      clear()
      print(logo)
      if guess in winner:
        score += 1 
        print(f"You're right! Current score: {score}.")
      else:
        print(f"Sorry, that's wrong. Final score: {score}")
        go_on = False

if __name__ == "__main__":
  guess_higher()