""" Test the polynomial approximation for the abs function on a discrete grid.

This example is from:

  Ricardo Pachón and Lloyd N. Trefethen, "Barycentric-Remez algorithms for best
  polynomial approximation in the chebfun system", BIT Numer Math (2009) 49,
  page 736.

The best approximation polynomial to the abs function may be calculated by
first finding the optimal polynomial p(x) to the sqrt function over the interval
(0, 1). Then using p(x**2) over the interval (-1, +1) yields the best
approximation for the abs function. This technique was orginally used by Remes.

A 5th order polynomial is used to as an approximation to the sqrt function with
a grid size of 48000. A total of 13 iterations are required using the
first Remez algorithm and the maximum error is 2.784512e-02.

The 5th order polynomial is effective translated to a 10th order polynomial for
calculating the abs approximation. The approximation calculated by this test is
close to the results reported by the reference above.
"""
import numpy as np
from matplotlib.pyplot import show, close
from minmax import remez_poly1
from utility import plot_residual, plot_polynomial

def main() -> None:
  """Polynomial approximation of abs on a discrete grid
  """
  # define the function to be approximated
  f = np.sqrt
  # lower limit on interval of approximation
  lower = 0.0
  # upper limit on interval of approximation
  upper = 1.0
  # number of grid points in the interval
  num = 48000
  # maximum number of iterations
  mit = 150
  # polynomial order
  order = 5
  # calculate the best approximation on grid
  coefficients, error, it = remez_poly1(f, lower, upper, num, order, mit)
  # display the results
  print('SQRT Coefficients: [{0}]'
    .format(', '.join(['{0:.16e}'.format(c) for c in coefficients])))
  print('Error: {0:.6e}'.format(error))
  print('Iterations: {0}'.format(it))

  # double the coefficients
  double_coefficients = np.zeros(2*order + 1)

  for i in range(coefficients.size):
    double_coefficients[2*i] = coefficients[i]
  print('ABS coefficients: [{0}]'
    .format(', '.join(['{0:.16e}'.format(c) for c in double_coefficients])))

  f = np.fabs
  lower = -1.0
  num *= 2
  plot_polynomial(f, double_coefficients, lower, upper, num,
                  'Polynomial approximation of abs function')
  plot_residual(f, double_coefficients, lower, upper, num,
                'Residual Error for polynomial approximation')
  # display results on screen
  show()
  close()

if __name__ == '__main__':
  print('Best approximation for abs function')
  main()
  print('Finished.')
