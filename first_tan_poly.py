""" Test the optimal polynomial approximation for the tan function.

This test case is taken from 'Tchebycheff approximation on a discrete point set:
algorithms old and new', William Edward McBride, Doctoral Thesis, 1973,
Problem C, Page 52.

The first algorithm of Remez is used to find the optimal polynomial. The
accuracy and convergence of the approximation matches that reported by McBride.

Module:
  first_tan_poly

Usage:
  >>> first_tan_poly import main
  >>> main()
"""

from time import process_time
from math import tan, pi
from remes_first_algorithm import remez_poly
from utility import plot_result

def main() -> None:
  """Polynomial approximation of TAN function"""
  print('Polynomial approximation of TAN function')
  f = tan             # define the function to be approximated
  lower = 0.0         # lower limit on interval of approximation
  upper = 0.25*pi     # upper limit on interval of approximation
  num = 51            # number of grid points in the interval
  mit = 10            # maximum number of iterations
  order = 5           # polynomial order
  # calculate the best approximation on grid
  start_time = process_time()
  coefficients, error, it = remez_poly(f, lower, upper, num, order, mit)
  end_time = process_time()
  # display the results
  print(f"Coefficients: [{', '.join([f'{c:.15e}' for c in coefficients])}]")
  print(f'Error: {error:.6e}')
  print(f'Iterations: {it}')
  print(f'Duration: {end_time-start_time:.4f} sec')
  # plot the results
  plot_result(f, coefficients, lower, upper, num,
    'Polynomial Approximation of TAN function')
  print('Finished.')

if __name__ == '__main__':
  main()
