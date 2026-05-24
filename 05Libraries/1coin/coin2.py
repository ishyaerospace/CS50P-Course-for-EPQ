from random import choice, randint, shuffle

coin = choice(["heads", "tails"]) #no longer need to specify random.choice
print(coin)

number = randint(1, 10) # random integer from 1 to 10 inclusive
print(number)

cards = ["jack", "queen", "king"]
shuffle(cards) # shuffles items in the list
for card in cards:
    print(card)