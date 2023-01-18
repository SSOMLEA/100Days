import random

print("Fliiping the coin")
random_toss_coin = random.randint(0, 1)
if random_toss_coin == 0:
    print("Tails")
elif random_toss_coin == 1:
    print("Heads")


