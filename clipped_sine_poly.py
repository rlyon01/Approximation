""" Test the polynomial approximation of a clipped sine on a discrete grid.

The clipped sine is defined by the nested function:

    def clipped_sine(x : float) -> float:
      return np.clip(np.sin(x), -0.7, +0.7)

The approximation is for required for the interval [-pi, pi] using an
polynomial degree of 17. The grid contains 4096 points.

The first algorithm of Remez is used to find the optimal polynomial. The
resulting polynomial is not particularly accurate with a peak error of
2.40393e-02. The algorithm requires 56 iterations to converge to the optimal
polynomial.
"""
import numpy as np
from matplotlib.pyplot import show, close
from minmax import remez_poly1
from utility import plot_residual, plot_polynomial

def main() -> None:
  """Polynomial approximation of tan on a discrete grid
  """
  # The clipped sine
  def clipped_sine(x : float) -> float:
    return np.clip(np.sin(x), -0.7, 0.7)
  # lower limit on interval of approximation
  lower = -np.pi
  # upper limit on interval of approximation
  upper = np.pi
  # number of grid points in the interval
  num = 4096
  # maximum number of iterations
  mit = 100
  # polynomial order
  order = 17
  # calculate the best approximation on grid
  coefficients, error, it = remez_poly1(clipped_sine, lower, upper, num,
    order, mit)
  # display the results
  print('Coefficients: [{0}]'
    .format(', '.join(['{0:.16e}'.format(c) for c in coefficients])))
  print('Error: {0:.5e}'.format(error))
  print('Iterations: {0}'.format(it))
  plot_polynomial(clipped_sine, coefficients, lower, upper, num,
                  'Polynomial approximation of clipped sine')
  plot_residual(clipped_sine, coefficients, lower, upper, num,
                'Residual Error for polynimial approximation')
  # display results on screen
  show()
  close()

if __name__ == '__main__':
  print('Best approximation for clipped sine function')
  main()
  print('Finished.')
