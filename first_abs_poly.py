""" Test the polynomial approximation for the abs function.

This test uses Remez's first algorithm as implemented in the module
first_algorithm. This test is from:

  Ricardo Pachón and Lloyd N. Trefethen, "Barycentric-Remez algorithms for best
  polynomial approximation in the chebfun system", BIT Numer Math (2009) 49,
  page 736.

A grid size of 9600 is used. A total of 22 iterations are required for the
algorithm to complete. The approximation calculated by this test is close to
the results reported by the reference above, but it could be better.

Module:
  first_abs_poly.py

Usage:

  python first_abs_poly.py
"""
from first_algorithm import remez_poly
from utility import plot_residual, plot_polynomial, show

def main() -> None:
  """Polynomial approximation of abs on a discrete grid"""
  # define the function to be approximated
  f = abs
  # lower limit on interval of approximation
  lower = -1.0
  # upper limit on interval of approximation
  upper = 1.0
  # number of grid points in the interval
  num = 9600
  # maximum number of iterations
  mit = 30
  # polynomial order
  order = 11

  # calculate the best approximation on grid
  coefficients, error, it = remez_poly(f, lower, upper, num, order, mit)

  # display the results
  print(f"Coefficients: [{', '.join([f'{c:.15e}' for c in coefficients])}]")
  print(f'Error: {error:.6e}')
  print(f'Iterations: {it}')
  # plot results
  plot_polynomial(f, coefficients, lower, upper, num,
    'Polynomial approximation for abs function')
  plot_residual(f, coefficients, lower, upper, num,
    'Residual error for polynomial approximation')
  show()

if __name__ == '__main__':
  print('Best polynomial approximation for abs function')
  main()
  print('Finished.')
