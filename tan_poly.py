""" Test the polynomial approximation for the tan function on a discrete grid.

This test case is taken from 'Tchebycheff approximation on a discrete point set:
algorithms old and new', William Edward McBride, Doctoral Thesis, 1973,
Problem C, Page 52.

The second algorithm of Remez is used to find the optimal polynomial. The
accuracy of the approximation matches that reported by McBride.
"""
import numpy as np
import matplotlib.pyplot as pp
from minmax import remez_poly

def print_coeff(coeff: list[float], prec: int) -> None:
  """Display the polynomial coefficients on the current terminal line.

  Args:
    coeff: The list of polynomial coefficients.
    prec: The required display floating point precision.

  Returns:
    None.
  """
  print('Coefficients: [{0}]'
    .format(', '.join(['{0:.{1}e}'.format(c, prec) for c in coeff])))

def print_err(err: float, prec: int) -> None:
  """Display the error on the current terminal line.

  Args:
    err: The floating-point value of the error.
    prec: The required display floating-point precision.

  Returns:
    None.
    """
  print('Error: {0:.{1}e}'.format(err, prec))

def print_iter(it: int) -> None:
  """Display the number of iterations on the current terminal line.

  Args:
    it: The number of iterations.

  Returns:
    None
  """
  print('Iterations: {0}'.format(it))

def display_residual(
  func,
  coeffs: list[float],
  start: float,
  stop: float,
  num: int,
) -> None:
  """Display the residual error over the grid for given polynomial and function.

  Args:
    func: A function (or lambda) f: X -> R.
    coeffs: List of the polynomial coeffcients.
    start: The starting value of the grid.
    stop: The end value of the grid.
    num: The number of points on the grid.

  Returns:
    None.
  """
  # construct the grid
  s = np.linspace(start, stop, num)
  # function mapped onto grid
  f = [func(i) for i in s]
  residual = f - np.polynomial.polynomial.polyval(s, coeffs)
  # plot the residual error
  pp.figure(2)
  pp.plot(s, residual, color='blue')
  pp.xlabel('x')
  pp.ylabel('Error')
  pp.grid(True)
  pp.title('Residual Error')

def plot_polynomial(
  func,
  coeffs: list[float],
  start: float,
  stop: float,
  num: int,
) -> None:
  """Plot the polynomial and function over the grid

  Args:
    func: A function (or lambda) f: X -> R.
    coeffs: List of the polynomial coeffcients.
    start: The starting value of the grid.
    stop: The end value of the grid.
    num: The number of points on the grid.

  Returns:
    None.
  """
  # construct the absissa grid
  x = np.linspace(start, stop, num)
  # function mapped over grid
  f = [func(i) for i in x]
  # polynomial mapped over grid
  p = np.polynomial.polynomial.polyval(x, coeffs)
  # plot the function and polynomial
  pp.figure(1)
  pp.plot(x, p, color='red', label='Polynomial')
  pp.plot(x, f, 'b.', markersize='3', label='tan(x)')
  pp.xlabel('x')
  pp.ylabel('y')
  pp.grid(True)
  pp.title('Polynomial Approximation of tan(x)')
  pp.legend()

def main() -> None:
  """Polynomial approximation of tan on a discrete grid
  """
  # define the function to be approximated
  f = np.tan
  # lower limit on interval of approximation
  lower = 0.0
  # upper limit on interval of approximation
  upper = 0.25 * np.pi
  # number of grid points in the interval
  num = 51
  # maximum number of iterations
  mit = 10
  # polynomial order
  order = 5
  # calculate the best approximation on grid
  coefficients, error, it = remez_poly(f, lower, upper, num, order, mit)
  # display the results
  print_coeff(coefficients, 16)
  print_err(error, 3)
  print_iter(it)
  plot_polynomial(f, coefficients, lower, upper, num)
  display_residual(f, coefficients, lower, upper, num)
  # display results on screen
  pp.show()
  pp.close()

if __name__ == '__main__':
  print('Polynomial of Best Approximation')
  main()
  print('Finished.')
