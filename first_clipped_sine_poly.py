""" Test the polynomial approximation of a clipped sine on a discrete grid.

The clipped sine is defined by the nested function:

    def clipped_sine(x : float) -> float:
      y = sin(x)
      if y > 0.7071067811865475:
        y = 0.7071067811865475
      elif y < -0.7071067811865475:
        y = -0.7071067811865475
      return y

The approximation is for required for the interval [-pi, pi] using an
polynomial degree of 17. The grid contains 4096 points.

The first algorithm of Remez is used to find the optimal polynomial. The
resulting polynomial is not particularly accurate with a peak error of
2.364630e-02 The algorithm requires 55 iterations to converge to the optimal
polynomial.
"""

from math import sin, pi
from first_algorithm import remez_poly
from utility import plot_residual, plot_polynomial, show

def main() -> None:
  """Polynomial approximation of clipped on a discrete grid"""
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
