""" Test the optimal polynomial approximation for the tan function.

This test case is taken from 'Tchebycheff approximation on a discrete point set:
algorithms old and new', William Edward McBride, Doctoral Thesis, 1973,
Problem C, Page 52.

The second algorithm of Remez is used to find the optimal polynomial. The
accuracy and convergence of the approximation matches that reported by McBride.

Module:
  second_tan_poly

Usage:
  >>> from second_tan_poly import main
  >>> main()
"""

from math import tan, pi
from second_algorithm import remez_poly
from utility import plot_result

def main() -> None:
  """Polynomial approximation of TAN function"""
  print('Polynomial approximation of TAN function')
  # define the function to be approximated
  f = tan
  # lower limit on interval of approximation
  lower = 0.0
  # upper limit on interval of approximation
  upper = 0.25 * pi
  # number of grid points in the interval
  num = 51
  # maximum number of iterations
  mit = 10
  # polynomial order
  order = 5

  # calculate the best approximation on grid
  coefficients, error, it = remez_poly(f, lower, upper, num, order, mit)

  # display the results
  print(f"Coefficients: [{', '.join([f'{c:.15e}' for c in coefficients])}]")
  print(f'Error: {error:.6e}')
  print(f'Iterations: {it}')
  # plot results
  plot_result(f, coefficients, lower, upper, num,
    'Polynomial Approximation of TAN function')
  print('Finished.')

if __name__ == '__main__':
  main()
