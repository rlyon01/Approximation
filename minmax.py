"""Discrete Remez Algorithms for Polynomials

Find optimal polynomial for approximating a function on a discrete grid using
Remez's algorithms.

Typical usage:

  # define the function to be approximated
  f = np.tan
  # lower limit on interval
  lower = 0.0
  # upper limit on interval
  upper = 0.25 * np.pi
  # number of grid points in the interval
  num = 51
  # maximum number of iterations
  mit = 10
  # polynomial order
  order = 5
  # get coefficients of optimal polynomial using the first algorithm
  coefficients, error, it = remez_poly1(f, lower, upper, num, order, mit)
"""
import numpy as np
# from utility import debug_residual

def remez_poly1(
  func,
  start: float,
  stop: float,
  num: int,
  n_deg: int,
  max_iter: int
) -> tuple[np.ndarray, float, int]:
  """ Discrete Remez Algorithm for polynomials

  This is the first Remez algorithm, hence the function name remez_poly1.

  Args:
    func: A function (or lambda) f: X -> R.
    start: The starting value of the grid.
    stop: The end value of the grid.
    num: The number of points on the grid.
    n_deg: The degree of the approximation polynomial.
    max_iter: The maximum number of iterations.

  Returns:
    A tuple containing an array of the polynomial coefficients, a float
    which is the error of approximation and an integer which is the number
    of iterations required. The ordering of the coefficients
    in the array is: [a0, a1, ..., an], for an nth order polynomial.
  """

  def alternates_column() -> np.ndarray:
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
    """Generate an array containing the starting positions for first iteration.

    Generate an array containing the starting positions for the first iteration.
    These points are distributed across the grid starting at zero with the last
    point at num - 1 and are the Chebyshev nodes. The value are rounded to
    the nearest integer.

    Args:
      None.

    Returns
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
      the same matching sign, otherwise False is returned.
    """
    return (first < 0.0 and second < 0.0) or (first >= 0.0 and second >=0.0)

  # initial error
  e = 0.0
  # create grid of points
  s = np.linspace(start, stop, num)
  # function mapped onto grid
  f = np.vectorize(func)(s)
  # alternate signs column (n_deg+2 elements)
  alt = alternates_column()
  # starting array of trial points for the first iteration
  u = start_points()

  for it in range(max_iter):
    # create square matrix for lhs of linear system
    v = np.vander(s[u], n_deg + 1, True)
    a = np.insert(v, n_deg + 1, alt, 1)
    # solve linear system ax = b
    x = np.linalg.solve(a, f[u])
    # retrieve polynomial coefficients and error
    p = x[:-1]
    e_it = abs(x[-1])
    # calculate the residual error over the grid
    r_grid = f - np.polynomial.polynomial.polyval(s, p)
    # get the coordinate of the extreme residual
    pos = np.argmax(np.fabs(r_grid))
    # check if this is the optimal polynomial
    if e_it <= 1.0000000001 * e:
      return (p, e_it, it+1)
    # save current error
    e = e_it
    # update the list of trial points to include the point at the extreme
    if pos < u[0]:
      if not match_sign(r_grid[u[0]], r_grid[pos]):
        u = np.roll(u, 1)
      u[0] = pos
    elif pos > u[n_deg + 1]:
      if not match_sign(r_grid[u[n_deg + 1]], r_grid[pos]):
        u = np.roll(u, -1)
      u[n_deg + 1] = pos
    else:
      for i in range(0, n_deg + 1):
        # test if position is in the interval u[i], ..., u[i+1], inclusive
        test = u[i] <= pos and pos <= u[i+1]
        if test:
          if match_sign(r_grid[u[i]], r_grid[pos]):
            u[i] = pos
          else:
            u[i+1] = pos
          break
    # debug_residual(it + 1, s, r_grid, u)
  raise RuntimeWarning('Failed to converge!')
