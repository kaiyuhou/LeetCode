def get_ruler(kingdom):
  kingdom = kingdom.lower()
  if kingdom.endswith('y'):
      return 'nobody'
  if kingdom[-1] in ['a', 'e', 'i', 'o', 'u']:
      return 'Alice'
  return 'Bob'


def main():
  # Get the number of test cases
  T = int(input())
  for t in range(T):
    # Get the kingdom
    kingdom = input()
    print('Case #%d: %s is ruled by %s.' % (t + 1, kingdom, get_ruler(kingdom)))

if __name__ == '__main__':
  main()