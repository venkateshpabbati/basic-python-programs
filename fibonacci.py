def fibonacci(n):
  """Calculates the nth fibonacci number.

  Args:
    n: The index of the fibonacci number to calculate.

  Returns:
    The nth fibonacci number.
  """

  if n < 0:
    raise ValueError("n must be non-negative")

  if n < 2:
    return n

  # Initialize the first two fibonacci numbers.
  a, b = 0, 1

  # Calculate the remaining fibonacci numbers.
  for _ in range(2, n):
    a, b = b, a + b

  return b