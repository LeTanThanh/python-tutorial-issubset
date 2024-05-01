if __name__ == "__main__":
  # Introduction to the Python issubset() method

  """
  set_a.issubset(set_b)
  """

  numbers = {1, 2, 3, 4, 5}
  scores = {1, 2, 3}
  print(numbers)
  print(scores)
  print(scores.issubset(numbers))

  numbers = {1, 2, 3, 4, 5}
  print(numbers)
  print(numbers.issubset(numbers))

  numbers = {1, 2, 3, 4, 5}
  scores = {1, 2, 3}
  print(numbers)
  print(scores)
  print(numbers.issubset(scores))
