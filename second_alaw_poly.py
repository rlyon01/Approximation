"""Find the optimal polynomial approximation of the sensor conversion.

The polynomial approximation is calculated using second algorithm of Remez
on a discrete grid over the interval [-1, +1] with 2048 points. The polynomial
order is set to 15.

The algorithm was completed after 7 iterations. The resulting approximation
has a maximum error of 1.349985e-01. Clearly this is not a good approximation,
but the example is useful for testing the algorithm implementation.
"""
from math import log
from second_algorithm import remez_poly
from utility import plot_residual, plot_polynomial, show

def main() -> None:
  """Polynomial approximation of A-LAW conversion."""
  def alaw(x: float) -> float:
    abs_x = abs(x)
    if abs_x < 0.011415525114155252:
      y = 16.006487384190198 * abs_x
    else:
      y = 0.1827224587236324 * (1.0 + log(87.6*abs_x))
    return y if x >= 0.0 else -y
  # lower limit on interval of approximation
  lower = -1.0
  # upper limit on interval of approximation
  upper = +1.0
  # number of grid points in the interval
  num = 2048
  # maximum number of iterations
  mit = 10
  # polynomial order
  order = 15
  # calculate the best approximation on grid
  coefficients, error, it = remez_poly(alaw, lower, upper, num, order, mit)
  # display the results
  print(f"Coefficients: [{', '.join([f'{c:.15e}' for c in coefficients])}]")
  print(f'Error: {error:.6e}')
  print(f'Iterations: {it}')
  plot_residual(alaw, coefficients, lower, upper, num,
    'Residual error for polynomial approximation')
  plot_polynomial(alaw, coefficients, lower, upper, num,
    'Polynomial approximation for alaw function')
  # display results on screen
  show()

if __name__ == '__main__':
  print('Best polynomial approximation of alaw conversion')
  main()
  print('Finished.')
