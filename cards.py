# cards.py


# Functions
def CardName(abbrev):
  # Bonus 1
  if abbrev[:2] == "10":
    abbrev = "T" + abbrev[2:]
  
  if len(abbrev) != 2:
    print("Wrong length; try two characters.")
    return None

  values = {
    "A":"Ace","2":"Two","3":"Three",
    "4":"Four","5":"Five","6":"Six",
    "7":"Seven","8":"Eight","9":"Nine",
    "T":"Ten","J":"Jack","Q":"Queen","K":"King"
  }
  value = abbrev[0]
  if value not in values:
    print(value, "is an invalid value.")
    return None

  suits = {
    "S":"Spades","D":"Diamonds","C":"Clubs","H":"Hearts"
  }
  suit = abbrev[1]
  if suit not in suits:
    print(suit, "is an invalid suit.")
    return None

  return values[value] + " of " + suits[suit]


def PrintMenu():
  # print("\nEnter an appropriate abbreviation for a solitare card to see its full name,")
  # print("or enter nothing to exit.")
  print("\nEnter an appropriate abbreviation for a solitare card to add it to the list,")
  print("or enter nothing to see the list and exit.")


# Main program
i = "Hello"
cards = []
print("Welcome to the best playing card program in the world.")

while i != "":
  PrintMenu()
  i = input()
  if i != "":
    fullName = CardName(i)
    if fullName != None:
      # print("That is", fullName)
      cards.append(fullName)
      print("Added")

# Bonus 2
print(cards)

print("Come again.")