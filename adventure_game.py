import time
import random


def print_pause(line):
    print(line)
    time.sleep(2)


def intro(enemy):
    print_pause("You find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {enemy} is somewhere around here,"
                " and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.")


def house(enemy):
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door"
                " opens and out steps a {enemy}.")
    print_pause(f"Eep! This is the {enemy}'s house!")
    print_pause(f"The {enemy} attacks you!")


def cave():
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth!")
    print_pause("You discard your silly old dagger "
                "and take the sword with you.")
    print_pause("You walk back out to the field.\n")


def lose(enemy):
    print_pause("You do your best...")
    print_pause(f"but your dagger is no match for the {enemy}.")
    print_pause("You have been defeated!")


def victory(enemy):
    print_pause(f"As the {enemy} moves to attack, "
                "you unsheath your new sword.")
    print_pause("The Sword of Ogoroth shines brightly in your"
                " hand as you brace yourself for the attack.")
    print_pause(f"But the {enemy} takes one look at your"
                " shiny new toy and runs away!")
    print_pause(f"You have rid the town of the {enemy}. You are victorious!")


def house_dilema(enemy, weapon):
    house_response = input("Would you like to(1) fight or (2) run away?\n")
    if house_response == "1" and "Sword of Ogoroth" not in weapon:
        lose(enemy)
    elif house_response == "1" and "Sword of Ogoroth" in weapon:
        victory(enemy)
    elif house_response == "2":
        print_pause("You run back into the field."
                    " Luckily, you don't seem to have been followed.\n")
        story(enemy, weapon)
    else:
        print_pause("Please eneter 1 or 2.")
        house_dilema(enemy, weapon)


def play_again(weapon):
    again = input("Would you like to play again? (y/n)\n").lower()
    if "n" in again:
        print_pause("Thanks for playing! See you next time.")
    elif "y" in again:
        weapon.clear()
        game()
    else:
        print_pause("Please eneter y or n.")
        play_again(weapon)


def story(enemy, weapon):
    response = input("Enter 1 to knock on the door of the house.\n"
                     "Enter 2 to peer into the cave.\n")
    if response == "1" and "Sword of Ogoroth" not in weapon:
        house(enemy)
        print_pause("You feel a bit under-prepared for this,"
                    " what with only having a tiny dagger.")
        house_dilema(enemy, weapon)
    elif response == "1" and "Sword of Ogoroth" in weapon:
        house(enemy)
        house_dilema(enemy, weapon)
    elif response == "2" and "Sword of Ogoroth" not in weapon:
        cave()
        weapon.append("Sword of Ogoroth")
        story(enemy, weapon)
    elif response == "2" and "Sword of Ogoroth" in weapon:
        print_pause("You've been here before, and gotten all the "
                    "good stuff. It's just an empty cave now.\n")
        story(enemy, weapon)
    else:
        print_pause("Please eneter 1 or 2.")
        story(enemy, weapon)


def game():
    weapon = []
    enemy = random.choice(["pirate", "dragon", "knight", "gorgon"])
    intro(enemy)
    story(enemy, weapon)
    play_again(weapon)


game()
