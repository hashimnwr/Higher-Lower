import random
from gamedata import data


a = random.choice(data)
b = random.choice(data)
score = 0

end_game = False

while not end_game:
#     print(a['follower_count'])
#     print(b['follower_count'])
    print(f"\n{a['name']}, {a['description']} from {a['country']}.\n vs\n{b['name']}, {b['description']} from {b['country']}. ")
    y_n = input(f"\nDoes {a['name']} have more followers than {b['name']}?\nType 'y' if yes, 'n' if no: ").lower()

    if y_n == 'y':
        if a['follower_count'] > b['follower_count']:
            score += 1
        elif a['follower_count'] < b['follower_count']:
            end_game = True
    elif y_n == 'n':
        if a['follower_count'] > b['follower_count']:
            end_game = True
        elif a['follower_count'] < b['follower_count']:
            score += 1
    else:
        print("Typo")
        end_game = True

    a = b
    b = random.choice(data)
    print(f"Score: {score}")
