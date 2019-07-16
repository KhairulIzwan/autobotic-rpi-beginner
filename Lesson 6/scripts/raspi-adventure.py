#!/usr/bin/env python3

# Title: The Silly Sentence Generator 3000
# Author: Your Name
# The game is set in medieval days: a time of stone castles,
# knights with swords, and (some say) mythical beasts that breathe fire.
# Your main character is a young boy named Raspi.1 One day Raspi is
# out gathering firewood and gets lost in the forest. He stumbles upon the
# entrance to a cave. # He peers in the entrance and finds that the cave splits
# into a left tunnel and # a right tunnel. He remembers a folk tale his
# grandmother used to tell of a mysterious cave in this very forest that holds
# enormous treasures. It’s said the treasure is guarded by a ferocious fire-
# breathing dragon. Raspi can’t resist the temptation to explore the cave;
# although he knows he should turn back, he walks slowly into the dark cavern

# Display the title and instruction
print("*" * 80)
print("* Raspi's Cave Adventures *")
print("*" * 80)

# 1st Choice: Left or Right Cave?
print("You see the cave split into a left and right tunnel")
print("Do you choose go left or right?")
cave_choice = input("Enter L for left or R for right: ")
if cave_choice == "L":
    # Left cave
    print("You walk into the left cave.")
else:
    # Right cave
    print("You walk into the right cave. The cave starts sloping downward.")
