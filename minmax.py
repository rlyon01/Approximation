"""Discrete Remez Algorithm for Polynomials

Find optimal polynomial for approximating a function on a discrete grid using
Remez's second algorithm.

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
  # get coefficients of optimal polynomial
  coefficients, error, it = remez_poly(f, lower, upper, num, order, mit)
"""
import numpy as np

def remez_poly(
  func,
  start: float,
  stop: float,
  num: int,
  n_deg: int,
  max_iter: int
) -> tuple[list[float], float, int]:
  """ Discrete Remez Algorithm for polynomials

  Args:
    func: A function (or lambda) f: X -> R.
    start: The starting value of the grid.
    stop: The end value of the grid.
    num: The number of points on the grid.
    n_deg: The degree of the approximation polynomial.
    max_iter: The maximum number of iterations.

  Returns:
    A tuple containing a list of the polynomial coefficients, a float
    which is the error of approximation and an integer which is the number
    of iterations required. The ordering of the coefficients
    in list is: [a0, a1, ..., an], for an nth order polynomial.
  """
  # find index of the minimum or maximum value in a list
  def arg_minmax(l: list[float], m: float ) -> int:
    return np.argmin(l) if m < 0.0 else np.argmax(l)
  # inialise return tupple with default values
  p = np.empty(n_deg + 1)
  e = 0.0
  it = 0
  # create grid of points
  s = np.linspace(start, stop, num)
  # function mapped over grid
  f = [func(i) for i in s]
  # alternate signs column
  alt = [(-1)**(index) for index in range(n_deg + 2)]
  # starting list of trial points on the grid (Chebyshev nodes)
  u = [round(0.5*(num-1)*(1.0 - np.cos(index*np.pi/(n_deg + 1))))
    for index in range(n_deg + 2)]
  for it in range(max_iter):
    # create square matrix for linear system
    v = np.vander([s[i] for i in u], n_deg + 1, True)
    a = np.insert(v, n_deg + 1, alt, 1)
    # create column vector for linear system
    b = [f[i] for i in u]
    # solve linear system ax = b
    x = np.linalg.solve(a, b)
    # retrieve polynomial coefficients and error
    p = x[:-1]
    e_iter = float(np.fabs(x[-1]))
    # if optimal polynomial then exit
    if e == e_iter:
      break
    # save error for next iteration
    e = e_iter
    # calculate the residual error over the grid
    r = f - np.polynomial.polynomial.polyval(s, p)
    # update the list of trial points to match extrema in residual error
    u[0] = arg_minmax(r[:u[1]], r[u[0]])
    for i in range(1, n_deg + 1):
      u[i] = u[i-1] + arg_minmax(r[u[i-1] : u[i+1]], r[u[i]])
    u[n_deg + 1] = u[n_deg] + arg_minmax(r[u[n_deg] : num], r[u[n_deg+1]])
  return (p.tolist(), e, it)
