""" Test the polynomial approximation for the tan function on a discrete grid.

This test case is taken from 'Tchebycheff approximation on a discrete point set:
algorithms old and new', William Edward McBride, Doctoral Thesis, 1973,
Problem C, Page 52.

The first algorithm of Remez is used to find the optimal polynomial. The
accuracy and convergence of the approximation matches that reported by McBride.
"""
from math import tan, pi
from first_algorithm import remez_poly
from utility import plot_residual, plot_polynomial, show

def main() -> None:
  """Polynomial approximation of tan on a discrete grid
  """
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
  plot_residual(f, coefficients, lower, upper, num,
    'Residual error for polynomial approximation')
  plot_polynomial(f, coefficients, lower, upper, num,
    'Polynomial approximation for tan function')
  # display results on screen
  show()

if __name__ == '__main__':
  print('Best polynomial approximation for tan function')
  main()
  print('Finished.')
