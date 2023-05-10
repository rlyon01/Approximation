""" Test the optimal polynomial approximation for the tan function.

The test uses Remez's second algorithm to find a 5th order polynomial
approximation to the tan function over the interval [0, pi/4]. A
linear grid of 51 points is used.

Module:
  tan_second_algorithm

Usage:
  >>> tan_second_algorithm import main
  >>> main()
  Polynomial approximation of TAN function
  Order: 5
  Coefficients: [-4.610770518016552e-05, 1.003821087881176e+00,
  -5.068986304743081e-02, 5.725135256792672e-01, -4.770291791360212e-01,
  4.919336458324009e-01]
  Error: 4.610771e-05
  Iterations: 4
  Duration: 0.0008 sec
  Finished.  
"""

from time import process_time
from math import tan, pi
from remes_second_algorithm import remez_poly
from utility import plot_result

def main() -> None:
  """Polynomial approximation of TAN function"""
  print('Polynomial approximation of TAN function')
  f = tan           # define the function to be approximated
  lower = 0.0       # lower limit on interval of approximation
  upper = 0.25*pi   # upper limit on interval of approximation
  num = 51          # number of grid points in the interval
  mit = 10          # maximum number of iterations
  order = 5         # polynomial order
  # calculate the best approximation on grid
  start_time = process_time()
  coefficients, error, it = remez_poly(f, lower, upper, num, order, mit)
  end_time = process_time()
  # display the results
  print(f'Order: {order}')
  print(f"Coefficients: [{', '.join([f'{c:.15e}' for c in coefficients])}]")
  print(f'Error: {error:.6e}')
  print(f'Iterations: {it}')
  print(f'Duration: {end_time-start_time:.4f} sec')
  # plot results
  plot_result(f, coefficients, lower, upper, num,
    'Polynomial Approximation of TAN function')
  print('Finished.')

if __name__ == '__main__':
  main()
