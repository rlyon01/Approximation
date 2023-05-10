""" Convert raw sensor reading to calibrated value.

Module:
    convert.py

Typical usage:
    >>> from convert import calibrated
    >>> reading = 21
    >>> actual = convert.calibrated(reading)
    >>> print(f'Actual = {actual}')
"""

# Lookup table to convert sensor reading to calibrated value
CONVERSION_TABLE: list[int] = [
   80,  78,  76,  74,  72,  71,  69,  67,  66,  65,
   63,  61,  60,  59,  57,  56,  55,  54,  53,  52,
   51,  50,  49,  48,  47,  46,  45,  44,  44,  43,
   42,  41,  41,  40,  39,  38,  38,  37,  36,  36,
   35,  35,  34,  33,  33,  32,  32,  31,  31,  30,
   29,  29,  28,  27,  27,  26,  26,  25,  25,  24,
   24,  23,  23,  22,  22,  21,  21,  20,  20,  19,
   19,  18,  18,  17,  17,  16,  16,  15,  15,  14,
   14,  13,  13,  12,  12,  11,  11,  11,  10,  10,
    9,   9,   8,   8,   8,   7,   7,   6,   6,   6,
    5,   5,   4,   4,   3,   3,   2,   2,   1,   1,
    1,   0,   0,  -1,  -1,  -2,  -2,  -3,  -3,  -4,
   -4,  -4,  -5,  -6,  -6,  -7,  -7,  -8,  -8,  -9,
   -9, -10, -11, -11, -12, -13, -13, -14, -14, -15,
  -16, -17, -17, -18, -19, -19, -20, -21, -22, -22,
  -23, -24, -24, -25, -26, -27, -27, -28, -29, -29,
  -30
]

def calibrated(raw: int) -> int:
  """Convert raw sensor reading to a calibrated value

  Args:
    raw: The raw value read from the sensor. This must have a integer
    value in the range of 21 to 181, inclusive.

  Returns:
    The calibrate value, represented as an integer.

  Raises:
    ValueError: The raw argument does not lie in the range of 21 to 181,
    inclusive.
  """
  if raw < 21 or raw > 181: raise ValueError('Invalid raw argument')
  return CONVERSION_TABLE[raw - 21]

