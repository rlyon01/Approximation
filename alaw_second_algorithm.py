"""Test the polynomial approximation for the alaw function.

The test uses Remez's second algorithm to find a 10th order polynomial
approximation to the ALAW conversion function over the interval [-1.0, +1.0]. A
linear grid of 9999 points is used.

Module:
  alaw_second_algorithm

Usage:
  >>> from alaw_second_algorithm import main
  >>> main()
  Polynomial approximation of A-LAW conversion
  Order: 10
  Coefficients: [1.509903313490213e-14, 5.711621347942959e+00,
  6.223866060379512e-15, -3.814367754230961e+01, -2.353282805501313e-13,
  1.149002804108091e+02, 2.732173246291716e-13, -1.409781429279190e+02,
  3.941328610540449e-13, 5.969949732470351e+01, -4.328626735529707e-13]
  Error: 1.895786e-01
  Iterations: 6
  Duration: 0.0050 sec
  Finished.
"""

from time import process_time
from math import log
from remes_second_algorithm import remez_poly
from utility import plot_result

def main() -> None:
  """Polynomial approximation of A-LAW conversion."""
  print('Polynomial approximation of A-LAW conversion')
  def alaw(x: float) -> float:
    """A-LAW Conversion function"""
    abs_x = abs(x)
    if abs_x < 0.011415525114155252:
      y = 16.006487384190198 * abs_x
    else:
      y = 0.1827224587236324 * (1.0 + log(87.6*abs_x))
    return y if x >= 0.0 else -y
  lower = -1.0    # lower limit on interval of approximation
  upper = +1.0    # upper limit on interval of approximation
  num = 9999      # number of grid points in the interval
  mit = 10        # maximum number of iterations
  order = 10      # polynomial order
  # calculate the best approximation on grid
  start_time = process_time()
  coefficients, error, it = remez_poly(alaw, lower, upper, num, order, mit)
  end_time = process_time()
  # display the results
  print(f'Order: {order}')
  print(f"Coefficients: [{', '.join([f'{c:.15e}' for c in coefficients])}]")
  print(f'Error: {error:.6e}')
  print(f'Iterations: {it}')
  print(f'Duration: {end_time-start_time:.4f} sec')
  # plot results
  plot_result(alaw, coefficients, lower, upper, num,
    'Polynomial Approximation of A-LAW conversion')
  print('Finished.')

if __name__ == '__main__':
  main()
