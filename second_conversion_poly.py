"""Find the optimal polynomial approximation of the sensor conversion.

The polynomial approximation is calculated using second algorithm of Remez
on a discrete grid. A 5th order polynomial is found after 4 iterations. The
maximum error introduced by the approximation is 9.770320e-01.
"""

from convert import calibrated
from second_algorithm import remez_poly
from utility import plot_residual, plot_polynomial, show

def main() -> None:
  """Polynomial approximation of sensor conversion."""
  # define the function to be approximated
  f = lambda x : calibrated(round(x))
  # lower limit on interval of approximation
  lower = 21
  # upper limit on interval of approximation
  upper = 181
  # number of grid points in the interval
  num = 161
  # maximum number of iterations
  mit = 5
  # polynomial order
  order = 5
  # calculate the best approximation on grid
  coefficients, error, it = remez_poly(f, lower, upper, num, order, mit)
  # display the results
  print(f"Coefficients: [{', '.join([f'{c:.15e}' for c in coefficients])}]")
  print(f'Error: {error:.6e}')
  print(f'Iterations: {it}')
  plot_residual(f, coefficients, lower, upper, num,
    'Residual error for polynomial approximation')
  plot_polynomial(f, coefficients, lower, upper, num,
    'Polynomial approximation for sensor function')
  # display results on screen
  show()

if __name__ == '__main__':
  print('Best polynomial approximation of sensor conversion')
  main()
  print('Finished.')
