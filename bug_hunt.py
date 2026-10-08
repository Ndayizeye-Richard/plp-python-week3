count = 1
total = 0

# BUG: The while loop header was missing a colon, which prevented Python from starting the loop. I added the colon.
while count <= 5:
    # BUG: The loop condition used < 5, so it stopped before adding 5. I changed it to <= 5 to include the final value.
    total = total + count
    count = count + 1

# BUG: The print statement tried to concatenate a string and an integer. I converted total to a string before printing.
print("Sum of 1 to 5 is: " + str(total))
