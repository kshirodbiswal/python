import sys
from functools import reduce


def read_test_cases(n_remaining):
  if n_remaining <= 0:
    return []

  x_line = sys.stdin.readline()
  if not x_line:
    return []
  x = int(x_line.strip())

  y_line = sys.stdin.readline()
  y_tokens = y_line.strip().split()

  if len(y_tokens) != x:
    current_result = -1
  else:
    y_nums = list(map(int, y_tokens))
    non_positive = list(filter(lambda v: v <= 0, y_nums))
    powered = list(map(lambda v: v ** 4, non_positive))
    current_result = reduce(lambda a, b: a + b, powered, 0)

  return [current_result] + read_test_cases(n_remaining - 1)


def print_results(res_list):
  if not res_list:
    return
  print(res_list[0])
  print_results(res_list[1:])


def main():
  first_line = sys.stdin.readline()
  if not first_line:
    return
  n = int(first_line.strip())
  results = read_test_cases(n)
  print_results(results)


if __name__ == "__main__":
  main()

  