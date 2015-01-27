# Blackjack

import random

def calculate_score(cards):
  value = 0
  aces_number = 0
  for card in cards:
    face = card[:-1] 
    if face in ['J', 'Q', 'K']:
      points = 10
    elif face == 'A':
      points = 11
      aces_number = aces_number + 1
    else:
      points = int(face)
    value = value + points
  if value > 21 and aces_number>0:
    value = value - (10*aces_number)
  return value

import time

def main():
  SUITS = "\u2663 \u2665 \u2666 \u2660".split()
  FACES = "A 2 3 4 5 6 7 8 9 10 J Q K".split()

  deck = []
  for suit in SUITS:
    for face in FACES:
      deck.append(face+suit)

  random.shuffle(deck)

  # deal two cards
  hand = [deck.pop(0), deck.pop(0)]
  score = calculate_score(hand)

  print("Your hand:", " ".join(hand))

  while score < 21 and input("Do you want another card? (y/n) ") == 'y':
    hand.append(deck.pop(0))
    score = calculate_score(hand)
    print("Your hand:", ", ".join(hand))

  if score > 21:
    print("You're busted!")
  elif score == 21:
    print("You win!")
  else:
    print("You have %s points." %score)
    print("\n")

    time.sleep(2)
    dealer_hand = [deck.pop(0), deck.pop(0)]
    dealer_score = calculate_score(dealer_hand)
    print("Dealer has", " ".join(dealer_hand))
    while dealer_score < 17:
      print("The dealer will take another card...")
      time.sleep(5)
      dealer_hand.append(deck.pop(0))
      dealer_score = calculate_score(dealer_hand)
      print("Dealer now has", " ".join(dealer_hand))
      time.sleep(3)

    if dealer_score > 21:
      print("The dealer's busted! You win!")
    elif dealer_score == 21:
      print("The dealer got 21! You lose.")
    elif dealer_score > score:
      print("You lost.")
    elif dealer_score == score:
      print("It's a tie.... nobody wins this time.")
    else:
      print("You win!")

main()
