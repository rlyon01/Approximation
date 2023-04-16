from convert import calibrated
from minmax import remez_poly
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
  mit = 50
  # polynomial order
  order = 11
  # calculate the best approximation on grid
  coefficients, error, it = remez_poly(f, lower, upper, num, order, mit)
  # display the results
  print('Coefficients: [{0}]'
    .format(', '.join(['{0:.16e}'.format(c) for c in coefficients])))
  print('Error: {0:.6e}'.format(error))
  print('Iterations: {0}'.format(it))
  # generate plots
  plot_polynomial(f, coefficients, lower, upper, num,
    'Polynomial approximation for sensor conversion')
  plot_residual(f, coefficients, lower, upper, num,
    'Residual Error for polynomial approximation')
  # display plots on screen
  show()

if __name__ == '__main__':
  print('Best polynomial approximation of sensor conversion')
  main()
  print('Finished.')
