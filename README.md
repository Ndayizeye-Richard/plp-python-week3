# PLP Python Week 3

- grade_reporter.py: reads a list of scores, assigns grades using if/elif/else, counts passes and fails, and prints the average.
- bug_hunt.py: fixes a broken loop program that is meant to sum the numbers 1 through 5 and print the correct result.

The hardest bug to find in Part B was the loop condition using `< 5` instead of `<= 5`. Because the program still ran without crashing, it looked like it was working, but the total was too low. I knew something was wrong when the output was not 15, even though the logic looked close to correct, so I rechecked the loop condition and tested the program again after each fix.
