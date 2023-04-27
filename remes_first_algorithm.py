"""Discrete Remez Algorithm for Polynomials

Find the optimal polynomial for approximating a function on a discrete linear
grid using Remez's first algorithm.

Module:
  first_algorithm.py

Typical usage:

  from math import tan, pi
  from remes_first_algorithm import remez_poly
  
  f = tan           # define the function
  lower = 0.0       # lower limit on interval
  upper = 0.25*pi   # upper limit on interval
  num = 51          # number of grid points in the interval
  mit = 10          # maximum number of iterations
  order = 5         # polynomial order

  # calculate the coefficients of optimal polynomial and maximum error
  coefficients, error, it = remez_poly(f, lower, upper, num, order, mit)
"""
import numpy as np

def remez_poly(
  func,
  start: float,
  stop: float,
  num: int,
  ndeg: int,
  max_iter: int
) -> tuple[np.ndarray, float, int]:
  """ Discrete Remez Algorithm for polynomials

  This is the first Remez algorithm for polynomials. It is used to find the
  optimal polynomial approximation to a function f on a discrete linear grid.

  Args:
    func: A function (or lambda) f: x -> Result.
    start: The starting value of the grid.
    stop: The end value of the grid.
    num: The number of points on the grid.
    ndeg: The degree of the approximation polynomial.
    max_iter: The maximum number of iterations.

  Returns:
    A tuple containing an array of the polynomial coefficients, a float
    which is the error of approximation and an integer which is the number
    of iterations required. The ordering of the coefficients
    in the array is: [a0, a1, ..., an], for an nth order polynomial.
  """

  # nested functions

  def chebpts(npts: int, ngrid: int) -> np.ndarray:
    """Generate an array containing the starting test points.

    These points are distributed across the grid starting at zero, with the last
    point at ngrid-1 and are the Chebyshev points of the second kind. The
    values are rounded to the nearest integer.

    Args:
      npts:   The number of test points.
      ngrid:  The number of grid points

    Returns:
      An array containing the starting test points in ascending order.
    """
    pts = np.round(0.5*(ngrid-1)*(1.0+np.polynomial.chebyshev.chebpts2(npts)))
    return pts.astype(int)

  def is_same_sign(first: float, second: float) -> bool:
    """ Check two floating point numbers for matching signs.

    A floating point number is considered positive if it is equal to or greater
    than zero.

    Args:
      first: The first floating point number.
      second: The second floating point number.

    Returns:
      A boolean value which is True if the two floating pointer numbers have
      the same sign, otherwise False is returned.
    """
    return (first<0.0 and second<0.0) or (first >= 0.0 and second >=0.0)
  
  # error scaling used to check for algorithm termination
  scale = 1.0 + 10.0*np.spacing(1.0)
  # initial error
  err = 0.0
  # create grid of points
  grid = np.linspace(start, stop, num)
  # function mapped onto grid
  f_grid = np.vectorize(func)(grid)
  # alternate signs array
  sigma = np.power(-1.0, range(ndeg+2))
  # initial array of trial points
  trial = chebpts(ndeg+2, num)

  for it in range(max_iter):
    # solve trial polynomial for given trial points
    v = np.vander(grid[trial], trial.size-1, True)
    a = np.insert(v, trial.size-1, sigma, 1)
    x = np.linalg.solve(a, f_grid[trial])
    # retrieve polynomial coefficients
    p = x[:-1]
    # retrieve residual error at trial points
    eiter = abs(x[-1])
    # check this if iteration is close to the optimal polynomial
    if eiter < scale * err:
      return (p, eiter, it+1)
    # save residual error for next iteration
    err = eiter
    # calculate the residual error over the grid
    r_grid = f_grid - np.polynomial.polynomial.polyval(grid, p)
    point = np.argmax(np.fabs(r_grid))
    # update the array of trial points to include the extreme point
    if point < trial[0]:
      if not is_same_sign(r_grid[trial[0]], r_grid[point]):
        trial = np.roll(trial, 1)
      trial[0] = point
    elif point > trial[-1]:
      if not is_same_sign(r_grid[point], r_grid[trial[-1]]):
        trial = np.roll(trial, -1)
      trial[-1] = point
    else:
      for i in range(trial.size-1):
        # test if point is in the interval [u[i], u[i+1]]
        if trial[i]<=point<=trial[i+1]:
          if is_same_sign(r_grid[trial[i]], r_grid[point]):
            trial[i] = point
          else:
            trial[i+1] = point
          break
  raise RuntimeWarning('Failed to converge!')
