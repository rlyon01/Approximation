# Chebyshev Approximation of a Function on a Linear Finite Grid.

The python files in this repository are simple naive implementations of Remes's
first and second algorithms for finding a polynomial of best approximation to
a function on a discrete finite linear grid. The purpose is to investigate the
limitations and issues when implementing Remes's algorithms in the most
straight-forward concise manner. A number of test cases are included.

The algorithms are implemented in python and roughly follow the approach of
Curtis and Frank [\[1\]](#Ref1)[\[2\]](#Ref2). These references contain a number
ambiguities, perhaps reflecting their age. So it required some experimentation
and thought to implement working algorithms.

## Dependencies

The code was written in Python and assumes that version 3.9 or later
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
        <td>Some functions to plot results.</td>
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

### `abs` Function

```
Polynomial approximation of ABS function
Coefficients: [2.791249516087373e-02, -9.840281293753858e-15, 4.751255548115536e+00, 7.426477170369968e-14, -2.062873910856450e+01, 2.232263841190505e-14, 4.772834599399463e+01, -7.052582472977443e-13, -4.953971350946165e+01, 1.124328697465918e-12, 1.868874694996265e+01, -5.058175789900250e-13]
Error: 2.780837e-02
Iterations: 5
```

![Polynomial approximation of abs function][abs_test_first]


## References

1. <a name="Ref1"></a> Philip C. Curtis and Werner L. Frank. 1958. An algorithm
for the determination of the polynomial of best minimax approximation to a
function defined on a finite point set. In Preprints of papers presented at the
13th national meeting of the Association for Computing Machinery (ACM '58).
Association for Computing Machinery, New York, NY, USA, 1–3.
See: <https://doi.org/10.1145/610937.610959>

2. <a name="Ref2"></a> Philip C. Curtis and Werner L. Frank. 1959. An Algorithm
for the Determination of the Polynomial of Best Minimax Approximation to a
Function Defined on a Finite Point Set. J. ACM 6, 3 (July 1959), 395–404.
See: <https://doi.org/10.1145/320986.320994>


[abs_test_first]: ./images/Polynomial_Approximation_of_ABS_function.svg