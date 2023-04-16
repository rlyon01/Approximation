""" Test the polynomial approximation for the abs function on a discrete grid.

This example is from:

  Ricardo Pachón and Lloyd N. Trefethen, "Barycentric-Remez algorithms for best
  polynomial approximation in the chebfun system", BIT Numer Math (2009) 49,
  page 736.

A grid size of 48000 was used. A total of 24 iterations were required using the
first Remez algorithm. The approximation calculated by this test is close to
the results reported by the reference above, but it could be better.
"""
from matplotlib.pyplot import show, close
from minmax import remez_poly
from utility import plot_residual, plot_polynomial, show

def main() -> None:
  """Polynomial approximation of tan on a discrete grid
  """
  # define the function to be approximated
  f = abs
  # lower limit on interval of approximation
  lower = -1.0
  # upper limit on interval of approximation
  upper = 1.0
  # number of grid points in the interval
  num = 96000
  # maximum number of iterations
  mit = 150
  # polynomial order
  order = 11
  # calculate the best approximation on grid
  coefficients, error, it = remez_poly(f, lower, upper, num, order, mit)
  # display the results
  print('Coefficients: [{0}]'
    .format(', '.join(['{0:.16e}'.format(c) for c in coefficients])))
  print('Error: {0:.6e}'.format(error))
  print('Iterations: {0}'.format(it))
  plot_polynomial(f, coefficients, lower, upper, num,
                  'Polynomial approximation of abs function')
  plot_residual(f, coefficients, lower, upper, num,
                'Residual Error for polynomial approximation')
  show()
  
if __name__ == '__main__':
  print('Best polynomial approximation for abs function')
  main()
  print('Finished.')
