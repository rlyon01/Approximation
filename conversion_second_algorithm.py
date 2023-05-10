"""Test the optimal polynomial approximation for the sensor conversion.

The test uses Remez's second algorithm to find a 5th order polynomial
approximation to the sensor conversion over the interval [21, 181]. A
linear grid of 161 points is used.

Module:
  conversion_second_algorithm

Usage:
  >>> from conversion_second_algorithm import main
  >>> main()
  Polynomial approximation of SENSOR conversion
  Order: 5
  Coefficients: [1.319699436191457e+02, -3.356182779338306e+00,
  4.725400457537449e-02, -3.903774757931707e-04, 1.650017652970575e-06,
  -2.880578609292462e-09]
  Error: 9.770320e-01
  Iterations: 4
  Duration: 0.0009 sec
  Finished.
"""

from time import process_time
from convert import calibrated
from remes_second_algorithm import remez_poly
from utility import plot_result

def main() -> None:
  """Polynomial approximation of SENSOR conversion."""
  def f(x: float) -> int:
    """Convert raw value to temperature."""
    return calibrated(round(x))
  print('Polynomial approximation of SENSOR conversion')
  lower = 21    # lower limit on interval of approximation
  upper = 181   # define the function to be approximated
  num = 161     # number of grid points in the interval
  mit = 5       # maximum number of iterations
  order = 5     # polynomial order
  # calculate the best approximation on grid
  start_time = process_time()
  coefficients, error, it = remez_poly(f, lower, upper, num, order, mit)
  end_time = process_time()
  # display the results
  print(f'Order: {order}')
  print(f"Coefficients: [{', '.join([f'{c:.15e}' for c in coefficients])}]")
  print(f'Error: {error:.6e}')
  print(f'Iterations: {it}')
  print(f'Duration: {end_time-start_time:.4f} sec')
  # plot results
  plot_result(f, coefficients, lower, upper, num,
    'Polynomial Approximation of SENSOR conversion')
  print('Finished.')

if __name__ == '__main__':
  main()
