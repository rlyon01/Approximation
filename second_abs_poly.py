""" Test the polynomial approximation for the abs function.

This test uses Remez's second algorithm as implemented in the module
remes_second_algorithm. This test is from:

  Ricardo Pachón and Lloyd N. Trefethen, "Barycentric-Remez algorithms for best
  polynomial approximation in the chebfun system", BIT Numer Math (2009) 49,
  page 736.

A grid size of 9600 is used. A total of 7 iterations are required for the
algorithm to complete. The approximation calculated by this test is close to
the results reported by the reference above, but it could be better.

Module:
  second_abs_poly

Usage:
  >>> from second_abs_poly import main
  >>> main()
"""

from time import process_time
from remes_second_algorithm import remez_poly
from utility import plot_result

def main() -> None:
  """Polynomial approximation of ABS function"""
  print('Polynomial approximation of ABS function')
  f = abs         # define the function to be approximated
  lower = -1.0    # lower limit on interval of approximation
  upper = 1.0     # upper limit on interval of approximation
  num = 9600      # number of grid points in the interval
  mit = 10        # maximum number of iterations
  order = 10      # polynomial order
  # calculate the best approximation on grid
  start_time = process_time()
  coefficients, error, it = remez_poly(f, lower, upper, num, order, mit)
  end_time = process_time()
  # display the results
  print(f"Coefficients: [{', '.join([f'{c:.15e}' for c in coefficients])}]")
  print(f'Error: {error:.6e}')
  print(f'Iterations: {it}')
  print(f'Duration: {end_time-start_time:.4f}')
  # plot results
  plot_result(f, coefficients, lower, upper, num,
    'Polynomial Approximation of ABS function')
  print('Finished.')

if __name__ == '__main__':
  main()

