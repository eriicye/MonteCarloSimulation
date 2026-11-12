from MonteCarlo import MonteCarlo

monteCarlo = MonteCarlo()

for i in range(10):
    print(monteCarlo.calculate(1_000_000_000))
