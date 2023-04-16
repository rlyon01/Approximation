""" Test the polynomial approximation for the tan function on a discrete grid.

This test case is taken from 'Tchebycheff approximation on a discrete point set:
algorithms old and new', William Edward McBride, Doctoral Thesis, 1973,
Problem C, Page 52.

The first algorithm of Remez is used to find the optimal polynomial. The
accuracy and convergence of the approximation matches that reported by McBride.
"""
from math import tan, pi
from minmax import remez_poly
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
  mit = 20
  # polynomial order
  order = 5
  # calculate the best approximation on grid
  coefficients, error, it = remez_poly(f, lower, upper, num, order, mit)
  # display the results
  print('Coefficients: [{0}]'
    .format(', '.join(['{0:.16e}'.format(c) for c in coefficients])))
  print('Error: {0:.3e}'.format(error))
  print('Iterations: {0}'.format(it))
  plot_polynomial(f, coefficients, lower, upper, num,
    'Polynomial approximation for tan function')
  plot_residual(f, coefficients, lower, upper, num,
    'Residual error for polynomial approximation')
  # display results on screen
  show()

if __name__ == '__main__':
  print('Best polynomial approximation for tan function')
  main()
  print('Finished.')
