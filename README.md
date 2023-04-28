# Chebyshev Approximation of a Function on a Linear Finite Grid.

The Python files in this repository implementations of the first and second
algorithms of Remes. The algorithms may be used for finding a polynomial of best
approximation to a function. The purpose is to investigate the limitations and
issues when implementing the algorithms in the most straight-forward concise
manner. A number of test cases are included.

The algorithms consist of the following steps:

1. Select a starting set of test points
2. Calculate the test polynomial for best approximation
3. Check if the calculation is complete and to stop.
4. Calculate the residual error
5. Update the set of test points and go back to step 2.

For the first algorithm only a single test point is updated at step 5. Whereas
with the second algorithm it is possible for all test points to be updated
at step 5.

The algorithms are applied over a real interval [a, b]. To simplify the
implementation, the real interval is a discrete linear grid of points arranged
in ascending order. The test points are selected from the grid and the residual error is only calculated at the grid points.

A test polynomial is calculated by constructing a linear system, which is
solved using the standard numpy LDU solver.

At each grid point the residual error is the difference between the function
and polynomial evaluations. The numpy polynomial evaluation is used which is
based Horner's rule.

The standard Python float type is used for all calculations.

## Dependencies

The code is written in Python and assumes that version 3.9 or later
is installed on the computer. The code utilises the NumPy 1.19.5 and
Matplotlib 3.3.4 packages. Later package versions should cause no issue.

## Files

<table>
    <tr>
        <th>Filename</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>first_algorithm.py</td>
        <td>Implementation of Remes first algorithm.</td>
    </tr>
    <tr>
        <td>second_algorithm.py</td>
        <td>Implementation of Remes second algorithm.</td>
    </tr>
    <tr>
        <td>utiliy.py</td>
        <td>Some functions to plot results with Matplotlib.</td>
    </tr>
    <tr>
        <td>convert.py</td>
        <td>A simple function to convert a raw sensor reading to a calibrated
        value. This function is used by some of the tests.</td>
    </tr>
    <tr>
        <td>first_abs_poly.py</td>
        <td>Using Remes's first algorithm find a polynomial approximation to
        the <em>abs</em> function on the interval [-1.0, +1.0]</td>
    </tr>
    <tr>
        <td>first_alaw_poly.py</td>
        <td>Using Remes's first algorithm find a polynomial approximation to
        the <em>A-LAW</em> conversion on the interval [-1.0, +1.0].</td>
    </tr>
    <tr>
        <td>first_clipped_sine_poly.py</td>
        <td>Using Remes's first algorithm find a polynomial approximation to
        a <em>Clipped-Sine</em> function on the interval [-pi, +pi].</td>
    </tr>
    <tr>
        <td>first_conversion_poly.py</td>
        <td>Using Remes's first algorithm find a polynomial approximation to a
        sensor <em>Conversion</em> problem.</td>
    </tr>
    <tr>
        <td>first_tan_poly.py</td>
        <td>Using Remes's first algorithm find a polnomial approximation to
        the <em>tan</em> function on the interval [0.0, 0.25*pi]</td>
    </tr>
    <tr>
        <td>second_abs_poly.py</td>
        <td>Using Remes's second algorithm find a polynomial approximation to
        the <em>abs</em> function on the interval [-1.0, +1.0]</td>
    </tr>
    <tr>
        <td>second_alaw_poly.py</td>
        <td>Using Remes's second algorithm find a polynomial approximation to
        the <em>A-LAW</em> conversion on the interval [-1.0, +1.0].</td>
    </tr>
    <tr>
        <td>second_clipped_sine_poly.py</td>
        <td>Using Remes's second algorithm find a polynomial approximation to
        a <em>Clipped-Sine</em> function on the interval [-pi, +pi].</td>
    </tr>
    <tr>
        <td>second_conversion_poly.py</td>
        <td>Using Remes's second algorithm find a polynomial approximation to a
        sensor <em>Conversion</em> problem.</td>
    </tr>
    <tr>
        <td>second_tan_poly.py</td>
        <td>Using Remes's second algorithm find a polnomial approximation to
        the <em>tan</em> function on the interval [0.0, 0.25*pi]</td>
    </tr>
<table>

## Results

