""" Test the polynomial approximation for the abs function.

The test uses Remez's first algorithm to find a 10th order polynomial
approximation to the abs function over the interval [-1.0, +1.0]. A linear grid
of 9999 points is used.

Module:
  abs_first_algorithm

Usage:
  >>> from abs_first_algorithm import main
  >>> main()
  Polynomial approximation of ABS function
  Order: 10
  Coefficients: [2.784511444309240e-02, 7.387882828314054e-15,
  4.753650534277715e+00, -2.198759996752948e-13, -2.064625072315169e+01,
  9.222549488347914e-13, 4.777533702515291e+01, -1.369184236745336e-12,
  -4.959209462628783e+01, 6.694441544223950e-13, 1.870935779000889e+01]
  Error: 2.784511444310045e-02
  Iterations: 32
  Duration: 0.0073 sec
  Finished.
"""

from time import process_time
from remes_first_algorithm import remez_poly
from utility import plot_result

def main() -> None:
  """Polynomial approximation of ABS function"""
  print('Polynomial approximation of ABS function')
  f = abs       # define the function to be approximated
  lower = -1.0  # lower limit on interval of approximation
  upper = 1.0   # upper limit on interval of approximation
  num = 9999    # number of grid points in the interval
  mit = 50      # maximum number of iterations
  order = 10    # Polynomial order
  # calculate the best approximation on grid
  start_time = process_time()
  coefficients, error, it = remez_poly(f, lower, upper, num, order, mit)
  end_time = process_time()
  # display the results
  print(f'Order: {order}')
  print(f"Coefficients: [{', '.join([f'{c:.15e}' for c in coefficients])}]")
  print(f'Error: {error:.15e}')
  print(f'Iterations: {it}')
  print(f'Duration: {end_time-start_time:.4f} sec')
  # plot results using matplotlib
  plot_result(f, coefficients, lower, upper, num,
    'Polynomial Approximation of ABS function')
  print('Finished.')

if __name__ == '__main__':
  main()
