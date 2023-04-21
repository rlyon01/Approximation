"""Some plotting utilities to assist with the development of the minmax module

Module:
  utility.py

This modules contains the following helper functions:

  debug_residual: Plot the residual error on the grid as well as the test
  points. This function is intended to be called directly from within one
  of the minmax function. This function calls the matplotlib show and close
  functions.

  plot_residual: Given the approximation polynomial and the target function
  calculate and plot the residual error. This function does not display the
  plot. The caller is expected to call matplotlib show and close.

  plot_polynomial: Plot the function and approximation polynomial. This
  function does not display the plot. The caller is expected to call matplotlib
  show and close.
"""
import numpy as np
from platform import system
import matplotlib.pyplot as pp

def debug_residual(
  iteration: int,
  grid: np.ndarray,
  residual: np.ndarray,
  u: np.ndarray
) -> None:
  """Plot the residual error on the grid and display test points.

  This plot is intended for debugging purposes. It displays the residual error
  with the test points highlighted. This function will wait for the user to
  close the plot window before exiting.

  Args:
    iteration: The current iteration.
    grid: An array containing the grid points position in ascending order.
    residual: An array containing the residual error at each grid position.
    u: An array containing the test point positions

  Returns:
    None.
  """
  pp.figure('Iteration {0}'.format(iteration))
  # plot the residual error with line graph
  pp.plot(grid, residual, color='blue')
  # highlight the test points with buttons
  pp.plot(grid[u], residual[u], 'ro')
  pp.xlabel('x')
  pp.ylabel('Error')
  pp.grid(True)
  pp.title('Residual Error')
  # display the plot
  pp.show(block=True)

def plot_residual(
  func,
  coeffs: np.array,
  start: float,
  stop: float,
  num: int,
  title: str = None,
) -> None:
  """Plot the residual error on the grid for a given polynomial and function.

  This function create the plot of the residual error. However the caller
  must show the plot and ultimately close it. This may be achieved by
  calling matplotlib.show and matplotlib.close.

  Args:
    func: A function (or lambda) f: X -> R.
    coeffs: Array of the polynomial coeffcients.
    start: The starting value of the grid.
    stop: The end value of the grid.
    num: The number of points on the grid.
    title: Optional title string to appear in plot area.

  Returns:
    None.
  """
  # construct the grid
  s = np.linspace(start, stop, num)
  # function mapped onto grid
  f = np.vectorize(func)(s)
  residual = f - np.polynomial.polynomial.polyval(s, coeffs)
  # plot the residual error
  pp.figure('Residual error')
  pp.plot(s, residual, color='blue')
  pp.xlabel('x')
  pp.ylabel('Error')
  pp.grid(True)
  if title is not None:
    pp.title(title)

def plot_polynomial(
  func,
  coeffs: np.ndarray,
  start: float,
  stop: float,
  num: int,
  title: str = None,
) -> None:
  """Plot the polynomial and function on the grid

  This function create the plot of the function and approximation polynomial.
  The caller must show the plot and ultimately close it. This may be achieved by
  calling matplotlib.show and matplotlib.close.

  Args:
    func: A function (or lambda) f: X -> R.
    coeffs: Array of the polynomial coeffcients.
    start: The starting value of the grid.
    stop: The end value of the grid.
    num: The number of points on the grid.
    title: Optional title string to appear in plot area.

  Returns:
    None.
  """
  # construct the absissa grid
  x = np.linspace(start, stop, num)
  # function mapped onto grid
  f = np.vectorize(func)(x)
  # polynomial mapped over grid
  p = np.polynomial.polynomial.polyval(x, coeffs)
  # plot the function and polynomial
  pp.figure('Polynomial Approximation')
  pp.plot(x, f, 'r-', label='Function')
  pp.plot(x, p, 'b-', label='Polynomial')
  pp.xlabel('x')
  pp.ylabel('y')
  pp.grid(True)
  if title is not None:
    pp.title(title)
  pp.legend()

def show() -> None:
  """ Display plots and block until the user has closed all figures."""
  pp.show(block=True)

def plot_maximize() -> None:
  """Maximize the plot window on the display"""
  backend = pp.get_backend()
  cfm = pp.get_current_fig_manager()
  if backend == 'wxAgg':
    cfm.frame.Maximize(True)
  elif backend == 'TkAgg':
    if system() == 'Windows':
      cfm.window.state('zoomed')
    else:
      cfm.resize(*cfm.window.maxsize())
  elif backend == 'QT4Agg':
    cfm.window.showMaximized()
  elif callable(getattr(cfm, 'full_screen_toggle', None)):
    if not getattr(cfm, 'flag_is_max', None):
      cfm.full_screen_toggle()
      cfm.flag_is_max = True
  else:
    raise RuntimeError('plt_maximize() is not implemented for current backend:',
      backend)

def plot_result(
  func,
  coeffs: np.ndarray,
  start: float,
  stop: float,
  num: int,
  title: str = None,
) -> None:
  """Plot and display the polynomial approximation results

  This function generates a window containing two vertically stacked graphs.
  The top graph contains plots of the polynomial approximation and the
  function. The bottom graph is a plot of the residual error. This function will
  block until the user closes the window.

  Arg:
    func: A function (or lambda) f: X -> Result.
    coeffs: Array of the polynomial coeffcients.
    start: The starting value of the grid.
    stop: The end value of the grid.
    num: The number of points on the grid.
    title: Optional title string to appear on the window titlebar.

  Returns:
    none
  """
  # construct the grid
  grid = np.linspace(start, stop, num)
  # function mapped onto grid
  f_grid = np.vectorize(func)(grid)
  # polynomial mapped over grid
  p_grid = np.polynomial.polynomial.polyval(grid, coeffs)
  # residual error mapped over grid
  r_grid = f_grid - np.polynomial.polynomial.polyval(grid, coeffs)
  # create a window with two plots, (polynomial and residual error)
  _, (ax1, ax2) = pp.subplots(2, 1, constrained_layout=True)
  # plot polynomial and function on top graph
  ax1.set_title('Polynomial Approximation')
  ax1.plot(grid, f_grid, color='red', label='Function')
  ax1.plot(grid, p_grid, color='blue', label='Polynomial')
  ax1.set_xlabel('x')
  ax1.set_ylabel('y')
  ax1.grid(True)
  ax1.legend()
  # plot the residual error on bottom graph
  ax2.set_title('Residual Error')
  ax2.plot(grid, r_grid, color='green')
  ax2.set_xlabel('x')
  ax2.set_ylabel('Error')
  ax2.grid(True)
  # display optional window title
  if title is not None:
    pp.get_current_fig_manager().set_window_title(title)
  # window maximized
  # plot_maximize()
  # display plots
  pp.show()
  pp.close()
