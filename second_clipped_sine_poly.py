""" Test the polynomial approximation for a clipped sine function.

This test uses Remez's second algorithm as implemented in the module
remes_first_algorithm. A discrete grid over the interval [-pi, pi] with 4096
points is used. The polynomial order is set to 17.

The clipped sine is defined by the nested function:

    def clipped_sine(x : float) -> float:
      y = sin(x)
      if y > 0.7071067811865475:
        y = 0.7071067811865475
      elif y < -0.7071067811865475:
        y = -0.7071067811865475
      return y

The algorithm is completed after 11 iterations. The resulting approximation
has a maximum error of 2.364630e-02.

Module:
  second_clipped_sine_poly

Usage:
  >>> from second_clipped_sine_poly import main
  >>> main()
"""

from time import process_time
from math import sin, pi
from remes_second_algorithm import remez_poly
from utility import plot_result

def main() -> None:
  """Polynomial approximation of Clipped-Sine function"""
  print('Polynomial approximation of Clipped-Sine function')
  def clipped_sine(x : float) -> float:
    """The clipped-sine function."""
    y = sin(x)
    if y > 0.7071067811865475:
      y = 0.7071067811865475
    elif y < -0.7071067811865475:
      y = -0.7071067811865475
    return y
  lower = -pi   # lower limit on interval of approximation
  upper = pi    # upper limit on interval of approximation
  num = 4096    # number of grid points in the interval
  mit = 20      # maximum number of iterations
  order = 17    # polynomial order
  # calculate the best approximation on grid
  start_time = process_time()
  coefficients, error, it = remez_poly(clipped_sine, lower, upper, num,
    order, mit)
  end_time = process_time()
  # display the results
  print(f"Coefficients: [{', '.join([f'{c:.15e}' for c in coefficients])}]")
  print(f'Error: {error:.6e}')
  print(f'Iterations: {it}')
  print(f'Duration: {end_time-start_time:.4f}')
  # plot results
  plot_result(clipped_sine, coefficients, lower, upper, num,
    'Polynomial Approximation of Clipped-Sine function')
  print('Finished.')

if __name__ == '__main__':
  main()
