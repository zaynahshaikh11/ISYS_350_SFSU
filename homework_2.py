# This is a program that asks the user what Muni line they surveyed, how many days they rode, and how many rider they counted while riding.
# Print statement for the start of the program.
print("Welcome to the Muni Ridership Calculator.")
# Gets input from the user to see what line they surveyed.
muni_line = input("Which Muni line did you survey?\n")
# Gets input from the user (as a whole number) to see how many days the user surveyed the line.
days_surveyed = int(input("How many days did you survey ridership?\n"))
# Gets input from the user (as a whole number) to see how many riders they counted.
number_of_riders = int(input("How many riders did you count?\n"))
# This is a variable that calculates the average number of riders.
average_riders = number_of_riders/days_surveyed
print("According to your survey, an average of " + format(average_riders, '.3f') + " people rode the " + muni_line + " per day.")