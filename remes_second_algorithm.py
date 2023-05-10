"""Discrete Remez Algorithm for Polynomials

Find the optimal polynomial for approximating a function on a discrete linear
grid using Remez's second algorithm.

Module:
  remes_second_algorithm.py

Typical usage:

  from math import tan, pi
  from second_algorithm import remez_poly

  f = tan             # define the function to be approximated
  lower = 0.0         # lower limit on interval
  upper = 0.25 * pi   # upper limit on interval
  num = 51            # number of grid points in the interval
  mit = 10            # maximum number of iterations
  order = 5           # polynomial order

  # calculate the coefficients of optimal polynomial
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

  This is the discrete second Remez algorithm for polynomials. It is used to
  find the optimal polynomial approximation to a function f on a discrete
  linear grid.

  Args:
    func: A function (or lambda) f: X -> Result.
    start: The starting value of the grid.
    stop: The end value of the grid.
    num: The number of equi-distance points on the grid.
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

    These points are distributed across the grid starting at zero with the last
    point at ngrid-1 and are the Chebyshev points of the second kind. The
    values are rounded to the nearest integer.

    Args:
      npts: The number of test points.
      ngrid: The size of the grid

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
    return (first < 0.0 and second < 0.0) or (first >= 0.0 and second >=0.0)

  def exchange(r: np.ndarray, lo: int, mi: int, hi: int) -> int:
    """Identify new test point in an interval.

    Identify point in interval [lo,hi) with same sign as the residual
    error at mi (existing test point) and having an extreme magnitude. This is
    the new test point to replace mi.

    Args:
      lo: The lowest point position in the interval.
      mi: The position of current test point in the interval.
      hi: The next higher point position after the interval.

    Returns:
      The position of the new test point in the interval
    """
    return lo + (np.argmin if r[mi] < 0.0 else np.argmax)(r[lo : hi])

  # error scaling used to check for algorithm termination
  scale =  1.0 + 4.55*np.spacing(1.0)
  # initial level error
  saved_level_error = 0.0
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
    # retrieve magnitude of the residual error at trial points
    level_error = abs(x[-1])
    # calculate the residual error over the grid
    r_grid = f_grid - np.polynomial.polynomial.polyval(grid, p)
    # check this if iteration is close to the optimal polynomial
    if level_error < scale*saved_level_error:
      max_residual = np.amax(np.fabs(r_grid))
      return (p, max_residual, it+1)
    # save residual error for next iteration
    saved_level_error = level_error
    # update trial points using multiple exchange
    trial_update = np.empty_like(trial)
    # exchange first leftmost test point
    trial_update[0] = exchange(r_grid, 0, trial[0], trial[1])
    # exchange intermediate test points
    for i in range(1, trial.size-1):
      trial_update[i] = exchange(r_grid, max(trial_update[i-1], trial[i-1])+1,
        trial[i], trial[i+1])
    # exchange last rightmost test point
    trial_update[-1] = exchange(r_grid, max(trial_update[-2], trial[-2])+1,
      trial[-1], num)

    # attempt to find an extrema residual to the left of the first test point
    first_pos = min(trial_update[0], trial[0])
    first_mag = 0.0
    if first_pos > 0:
      first_pos = np.argmax(np.fabs(r_grid[0 : first_pos]))
      if not is_same_sign(r_grid[first_pos], r_grid[trial_update[0]]):
        mag = np.fabs(r_grid[first_pos])
        if mag > np.fabs(r_grid[trial_update[-1]]):
          first_mag = mag
    # attempt to find an extrema residual to the right of the last test point
    last_pos = max(trial_update[-1], trial[-1]) + 1
    last_mag = 0.0
    if last_pos < num:
      last_pos += np.argmax(np.fabs(r_grid[last_pos : num]))
      if not is_same_sign(r_grid[last_pos], r_grid[trial_update[-1]]):
        mag = np.fabs(r_grid[last_pos])
        if first_mag == 0.0:
          if mag > np.fabs(r_grid[trial_update[0]]):
            last_mag = mag
        elif mag > first_mag:
          last_mag = mag
    # if there is an additional extreme point insert it into the test points
    if last_mag > 0.0:
      # add new point to the right and delete the leftmost point
      trial_update = np.roll(trial_update, -1)
      trial_update[-1] = last_pos
    elif first_mag > 0.0:
      # add new point to the left and delete the rightmost point
      trial_update = np.roll(trial_update, 1)
      trial_update[0] = first_pos
    # save the updated test points for the next iteration
    trial = trial_update
  raise RuntimeWarning('Failed to converge!')

