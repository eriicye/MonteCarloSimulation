from MonteCarlo import MonteCarlo

monteCarlo = MonteCarlo()

user_input = input("Enter in the amount of times you would like to run the simulation: ")

user_input = int(user_input)

print(monteCarlo.calculate(user_input))
