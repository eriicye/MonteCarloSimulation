# Monte Carlo Simulation

Estimates **π** by generating random points into a square and counting how many land inside a circle.

## How it works

A circle of radius 1 is centered in a 2×2 square. Random `(x, y)` values are generated in that square. A point is inside the circle if its distance from the centre is less than 1.

The area of the square is 4 and the area of the circle is π, so:

```
π ≈ 4 × (points inside the circle / total points)
```

More samples will generally give a closer estimate.

## Requirements

- Python 3.12+ (or another recent 3.x)
- [NumPy](https://numpy.org/)

```bash
pip install numpy
```

## Run

From the `src` directory:

```bash
python main.py
```

Enter how many random points to generate. The program prints the π estimate.

Example:

```text
Enter in the amount of times you would like to run the simulation: 1000000
3.141592
```

## Project layout

```
src/
  MonteCarlo.py   # sampling and π estimate
  main.py         # CLI entry point
```

`MonteCarlo.calculate(amount)` draws `amount` points, classifies them, and returns `4 * (inside / counted)`.
