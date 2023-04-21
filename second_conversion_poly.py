"""Test the optimal polynomial approximation for the sensor conversion.

This test uses Remez's second algorithm as implemented in the module
first_algorithm. The discrete is over the interval [21, 181] with 161 points.
The polynomial order is 5.

The algorithm complete after 4 iterations and the maximum error is 9.770320e-01.

Module:
  second_conversion_poly

Usage:
  >>> from second_conversion_poly import main
  >>> main()
"""

from convert import calibrated
from second_algorithm import remez_poly
from utility import plot_result

def main() -> None:
  """Polynomial approximation of SENSOR conversion."""
  print('Polynomial approximation of SENSOR conversion')
  # define the function to be approximated
  f = lambda x : calibrated(round(x))
  # lower limit on interval of approximation
  lower = 21
  # upper limit on interval of approximation
  upper = 181
  # number of grid points in the interval
  num = 161
  # maximum number of iterations
  mit = 5
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
    'Polynomial Approximation of SENSOR conversion')
  print('Finished.')

if __name__ == '__main__':
  main()
