"""Discrete Remez Algorithm for Polynomials

Find the optimal polynomial for approximating a function on a discrete linear
grid using Remez's second algorithm.

Module:
  second_algorithm.py

Typical usage:

  from math import tan, pi
  from second_algorithm import remez_poly

  # define the function to be approximated
  f = tan
  # lower limit on interval
  lower = 0.0
  # upper limit on interval
  upper = 0.25 * pi
  # number of grid points in the interval
  num = 51
  # maximum number of iterations
  mit = 10
  # polynomial order
  order = 5

  # calculate the coefficients of optimal polynomial
  coefficients, error, it = remez_poly(f, lower, upper, num, order, mit)
"""
import numpy as np
# from utility import debug_residual

def remez_poly(
  func,
  start: float,
  stop: float,
  num: int,
  n_deg: int,
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
    n_deg: The degree of the approximation polynomial.
    max_iter: The maximum number of iterations.

  Returns:
    A tuple containing an array of the polynomial coefficients, a float
    which is the error of approximation and an integer which is the number
    of iterations required. The ordering of the coefficients
    in the array is: [a0, a1, ..., an], for an nth order polynomial.
  """

  def alt_col() -> np.ndarray:
    """Generate a column vector with alternating sign integers of magnitude one.

    The column will contain n_deg+2 elements. This column is inserted as
    the rightmost column in the square matrix A. For example:

    column[0] = +1.0
    column[1] = -1.0
    column[2] = +1.0
    ...
    column[n_deg + 1] = (-1.0)**(n_deg + 1)

    Args:
      None.

    Returns:
      An array of floats containing exactly n_deg+2 elements.
    """
    return np.vectorize(lambda i : (-1.0)**(i))(np.arange(n_deg + 2))

  def start_points() -> np.ndarray:
    """Generate an array containing the starting test positions.

    Generate an array containing the starting positions for the first iteration.
    These points are distributed across the grid starting at zero with the last
    point at num - 1 and are the Chebyshev nodes. The values are rounded to
    the nearest integer.

    Args:
      None.

    Returns:
      An array containing the starting integer positions in ascending order.
    """
    return np.vectorize(
      lambda i : round(0.5*(num-1)*(1.0 - np.cos(i*np.pi/(n_deg + 1))))
    )(np.arange(n_deg + 2))

  def match_sign(first: float, second: float) -> bool:
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

  # initial error
  error = 0.0
  # create grid of points
  grid = np.linspace(start, stop, num)
  # function mapped onto grid
  f = np.vectorize(func)(grid)
  # alternate signs column (n_deg+2 elements)
  alt = alt_col()
  # starting array of trial points for the first iteration
  u = start_points()

  for it in range(max_iter):
    # create square matrix for lhs of linear system
    v = np.vander(grid[u], u.size-1, True)
    a = np.insert(v, u.size-1, alt, 1)
    # solve linear system ax = b
    x = np.linalg.solve(a, f[u])
    # retrieve polynomial coefficients and error
    p = x[:-1]
    eiter = abs(x[-1])
    # check this iteration is close to the optimal polynomial
    if eiter < 1.000000000000001 * error:
      return (p, eiter, it+1)
    # save current error for next iteration
    error = eiter
    # calculate the residual error over the grid
    r_grid = f - np.polynomial.polynomial.polyval(grid, p)
    # debug_residual(it + 1, grid, r_grid, u)
    # check if need to use first algorithm to handle zero error
    if eiter == 0:
      # get the position of the extreme residual
      pos = np.argmax(np.fabs(r_grid))
      # update the list of trial points to include a point at the extreme
      if pos < u[0]:
        if not match_sign(r_grid[u[0]], r_grid[pos]):
          u = np.roll(u, 1)
        u[0] = pos
      elif pos > u[-1]:
        if not match_sign(r_grid[pos], r_grid[u[-1]]):
          u = np.roll(u, -1)
        u[-1] = pos
      else:
        for i in range(u.size-1):
          # test if position is in the interval [u[i], u[i+1]]
          if u[i] <= pos <= u[i+1]:
            if match_sign(r_grid[u[i]], r_grid[pos]):
              u[i] = pos
            else:
              u[i+1] = pos
            break
    else:
      # remez second algorithm
      update = np.empty_like(u)
      # first leftmost test point
      if r_grid[u[0]] < 0.0:
        update[0] = np.argmin(r_grid[0 : u[1]])
      else:
        update[0] = np.argmax(r_grid[0 : u[1]])
      #intermediate test points
      for i in range(1, u.size-1):
        lower = update[i-1]+1 if update[i-1] > u[i-1] else u[i-1]+1
        if r_grid[u[i]] < 0.0:
          update[i] = lower + np.argmin(r_grid[lower : u[i+1]])
        else:
          update[i] = lower + np.argmax(r_grid[lower : u[i+1]])
      # last rightmost test point
      lower = update[-2]+1 if update[-2] > u[-2] else u[-2]+1
      if r_grid[u[-1]] < 0.0:
        update[-1] = lower + np.argmin(r_grid[lower : num])
      else:
        update[-1] = lower + np.argmax(r_grid[lower : num])

      # attempt to find an extrema to the left of the first point
      pos_first = update[0] if update[0] < u[0] else u[0]
      extrema_first = 0.0
      if pos_first > 0:
        pos_first = np.argmax(np.fabs(r_grid[0 : pos_first]))
        if not match_sign(r_grid[pos_first], r_grid[update[0]]):
          extrema = np.fabs(r_grid[pos_first])
          if extrema > np.fabs(r_grid[update[-1]]):
            extrema_first = extrema
      # attempt to find an extrema to the right of the last test point
      pos_last = update[-1]+1 if update[-1] > u[-1] else u[-1]+1
      extrema_last = 0.0
      if pos_last < num:
        pos_last += np.argmax(np.fabs(r_grid[pos_last : num]))
        if not match_sign(r_grid[pos_last], r_grid[update[-1]]):
          extrema = np.fabs(r_grid[pos_last])
          if (extrema_first == 0.0 and extrema > np.fabs(r_grid[update[0]])
              ) or (extrema > extrema_first > 0.0):
            extrema_last = extrema
      # if there is an additional extrema insert it into the test points
      if extrema_last > 0.0:
        update = np.roll(update, -1)
        update[-1] = pos_last
      elif extrema_first > 0.0:
        update = np.roll(update, 1)
        update[0] = pos_first
      # save the updated test points for the next iteration
      u = update
    # debug_residual(it + 1, grid, r_grid, u)
  raise RuntimeWarning('Failed to converge!')

