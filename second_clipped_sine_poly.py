""" Test the polynomial approximation for a clipped sine function.

This test uses Remez's second algorithm as implemented in the module
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

The algorithm is completed after 11 iterations. The resulting approximation
has a maximum error of 2.364630e-02.

Module:
  second_clipped_sine_poly.py

Usage:

  python second_clipped_sine_poly.py

"""

from math import sin, pi
from second_algorithm import remez_poly
from utility import plot_residual, plot_polynomial, show

def main() -> None:
  """Polynomial approximation of clipped sine on a discrete grid"""
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
  plot_residual(clipped_sine, coefficients, lower, upper, num,
    'Residual error for polynomial approximation')
  plot_polynomial(clipped_sine, coefficients, lower, upper, num,
    'Polynomial approximation for clipped-sine function')
  # display results on screen
  show()

if __name__ == '__main__':
  print('Best polynomial approximation for clipped sine function')
  main()
  print('Finished.')
