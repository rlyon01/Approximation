""" Test the polynomial approximation for a clipped sine function.

This test uses Remez's first algorithm as implemented in the module
first_algorithm. A discrete grid over the interval [-pi, pi] with 4096 points is
used. The polynomial order is set to 17.

The clipped sine is defined by the nested function:

    def clipped_sine(x : float) -> float:
      y = sin(x)
      if y > 0.7071067811865475:
        y = 0.7071067811865475
      elif y < -0.7071067811865475:
        y = -0.7071067811865475
      return y

The algorithm is completed after 55 iterations. The resulting approximation
has a maximum error of 2.364630e-02.

Module:
  first_clipped_sine_poly

Usage:
  >>> from first_clipped_sine_poly import main
  >>> main()
"""

from math import sin, pi
from first_algorithm import remez_poly
from utility import plot_result

def main() -> None:
  """Polynomial approximation of Clipped-Sine function"""
  print('Polynomial approximation of Clipped-Sine function')
  # The clipped sine function
  def clipped_sine(x : float) -> float:
    y = sin(x)
    if y > 0.7071067811865475:
      y = 0.7071067811865475
    elif y < -0.7071067811865475:
      y = -0.7071067811865475
    return y

  # lower limit on interval of approximation
  lower = -pi
  # upper limit on interval of approximation
  upper = pi
  # number of grid points in the interval
  num = 4096
  # maximum number of iterations
  mit = 100
  # polynomial order
  order = 17
  # calculate the best approximation on grid
  coefficients, error, it = remez_poly(clipped_sine, lower, upper, num,
    order, mit)
  # display the results
  print(f"Coefficients: [{', '.join([f'{c:.15e}' for c in coefficients])}]")
  print(f'Error: {error:.6e}')
  print(f'Iterations: {it}')
  # plot results
  plot_result(clipped_sine, coefficients, lower, upper, num,
    'Polynomial Approximation of Clipped-Sine function')
  print('Finished.')

if __name__ == '__main__':
  main()

