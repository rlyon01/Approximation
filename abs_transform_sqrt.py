""" Test the polynomial approximation for the abs function.

The test uses Remez's second algorithm to find a 5th order polynomial
approximation to the sqrt function over the interval [-1.0, +1.0]. A linear grid
of 5000 points is used. The resulting polynomial is converted to the best
approximation polynomial for the abs function by substituting x -> y*y. The
substitution results in a 10th order polynomial.

Module:
  abs_transform_sqrt

Usage:
  >>> from abs_transform_sqrt import main
  >>> main()
  Polynomial approximation of ABS function via sqrt
  Order: 10
  Coefficients: [2.784511295627812e-02, 0.000000000000000e+00,
  4.753651366305149e+00, 0.000000000000000e+00, -2.064625642431383e+01,
  0.000000000000000e+00, 4.777535052265449e+01, 0.000000000000000e+00,
  -4.959210799337704e+01, 0.000000000000000e+00, 1.870936252873123e+01]
  Error: 2.784511295627934e-02
  Iterations: 6
  Duration: 0.0018 sec
  Finished.
"""

from math import sqrt
from time import thread_time_ns
from remes_second_algorithm import remez_poly
from utility import plot_result

def main() -> None:
  """Polynomial approximation of ABS function via sqrt."""
  print('Polynomial approximation of ABS function via sqrt')
  lower = 0.0   # lower limit on interval of approximation
  upper = 1.0   # upper limit on interval of approximation
  num = 5000    # number of grid points in the interval
  mit = 50      # maximum number of iterations
  order = 5     # Polynomial order
  # start the timekeeping
  start_time = thread_time_ns()
  # calculate the best approximation on grid for sqrt
  sqrt_coeffs, error, it = remez_poly(sqrt, lower, upper, num, order, mit)
  # transform coefficients by substitution (x -> x*x)
  abs_coeffs = [0.0]*(2*order+1)
  for (i, coeff) in enumerate(sqrt_coeffs): # type: ignore
    abs_coeffs[2*i] = coeff
  # stop the timekeeping
  end_time = thread_time_ns()
  duration = 1.0e-9 * (end_time - start_time)
  # display the results
  print(f'Order: {2*order}')
  print(f"Coefficients: [{', '.join([f'{c:.15e}' for c in abs_coeffs])}]")
  print(f'Error: {error:.15e}')
  print(f'Iterations: {it}')
  print(f'Duration: {duration:.4f} sec')
  # plot results using matplotlib
  plot_result(abs, abs_coeffs, -upper, upper, 2*num-1, # type: ignore
    'Polynomial Approximation of ABS function')
  print('Finished.')

if __name__ == '__main__':
  main()
