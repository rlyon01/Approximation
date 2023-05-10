""" Test the polynomial approximation for a clipped sine function.

The test uses Remez's second algorithm to find a 10th order polynomial
approximation to the clipped sine function over the interval [-pi, +pi]. A
linear grid of 9999 points is used.

Module:
  clipped_sine_second_algorithm

Usage:
  >>> from clipped_sine_second_algorithm import main
  >>> main()
  Polynomial approximation of Clipped-Sine function
  Order: 10
  Coefficients: [3.108624468950438e-15, 1.134440169085747e+00,
  -8.975370614993066e-15, -5.246896708630510e-01, 1.367504204994999e-14,
  1.359916020436154e-01, -4.445779667613974e-15, -1.611494182503933e-02,
  5.245307811873813e-16, 6.639910919147184e-04, -2.082229309880595e-17]
  Error: 3.250974e-02
  Iterations: 6
  Duration: 0.0039 sec
  Finished.
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
  num = 9999    # number of grid points in the interval
  mit = 100     # maximum number of iterations
  order = 10    # polynomial order
  # calculate the best approximation on grid
  start_time = process_time()
  coefficients, error, it = remez_poly(clipped_sine, lower, upper, num,
    order, mit)
  end_time = process_time()
  # display the results
  print(f'Order: {order}')
  print(f"Coefficients: [{', '.join([f'{c:.15e}' for c in coefficients])}]")
  print(f'Error: {error:.6e}')
  print(f'Iterations: {it}')
  print(f'Duration: {end_time-start_time:.4f} sec')
  # plot results
  plot_result(clipped_sine, coefficients, lower, upper, num,
    'Polynomial Approximation of Clipped-Sine function')
  print('Finished.')

if __name__ == '__main__':
  main()
