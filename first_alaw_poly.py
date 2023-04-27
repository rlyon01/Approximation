"""Test the polynomial approximation for the alaw function.

This test uses Remez's first algorithm as implemented in the module
remes_first_algorithm. A discrete grid over the interval [-1, +1] with 2048
points is used. The polynomial order is set to 15.

The algorithm is completed after 52 iterations. The resulting approximation
has a maximum error of 1.349985e-01. This is not a good approximation, but the
example is useful for testing the algorithm implementation.

Module:
  first_alaw_poly

Usage:
  >>> from first_alaw_poly import main
  >>> main()
"""
from time import process_time
from math import log
from remes_first_algorithm import remez_poly
from utility import plot_result

def main() -> None:
  """Polynomial approximation of A-LAW conversion."""
  print('Polynomial approximation of A-LAW conversion')
  def alaw(x: float) -> float:
    """A-LAW conversion function."""
    abs_x = abs(x)
    if abs_x < 0.011415525114155252:
      y = 16.006487384190198 * abs_x
    else:
      y = 0.1827224587236324 * (1.0 + log(87.6*abs_x))
    return y if x >= 0.0 else -y
  lower = -1.0  # lower limit on interval of approximation
  upper = +1.0  # upper limit on interval of approximation
  num = 2048    # number of grid points in the interval
  mit = 100     # number of grid points in the interval
  order = 15    # polynomial order
  # calculate the best approximation on grid
  start_time = process_time()
  coefficients, error, it = remez_poly(alaw, lower, upper, num, order, mit)
  end_time = process_time()
  # display the results
  print(f"Coefficients: [{', '.join([f'{c:.15e}' for c in coefficients])}]")
  print(f'Error: {error:.6e}')
  print(f'Iterations: {it}')
  print(f'Duration: {end_time-start_time:.4f} sec')
  # plot the results
  plot_result(alaw, coefficients, lower, upper, num,
    'Polynomial Approximation of A-LAW conversion')
  print('Finished.')

if __name__ == '__main__':
  main()
