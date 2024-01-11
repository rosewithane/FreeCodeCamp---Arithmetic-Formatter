def arithmetic_arranger(problems, optional="a"):

  f = []
  s = []
  o = []

  for i in problems:
    k = i.split()
    f.append(k[0])
    o.append(k[1])
    s.append(k[2])

  if len(problems) > 5:
    error = "Error: Too many problems."
    return error

  for i in o:
    if i == '+' or i == '-':
      continue
    else:
      error = "Error: Operator must be '+' or '-'."
      return error

  a = 0
  while a < len(f):
    if len(f[a]) > 4 or len(s[a]) > 4:
      error = "Error: Numbers cannot be more than four digits."
      return error
    else:
      a += 1

  a = 0
  while a < len(f):
    if f[a].isdigit() and s[a].isdigit():
      a += 1
      continue
    else:
      error = "Error: Numbers must only contain digits."
      return error

  a = 0
  b = 0

  while a < len(f):
    if len(f[b]) > len(s[b]):
      c = 0
      while c < 2:
        print(' ', end='')
        c += 1

    else:
      c = 0
      while c < len(s[b]) + 2 - len(f[b]):
        print(' ', end='')
        c += 1

    print(f[a] + "    ", end='')
    a += 1
    b += 1

  a = 0
  b = 0

  print()

  while a < len(s):

    print(o[a], end='')

    if len(f[b]) > len(s[b]):
      c = 0
      while c < len(f[b]) + 1 - len(s[b]):
        print(' ', end='')
        c += 1

    else:
      c = 0
      while c < 1:
        print(' ', end='')
        c += 1

    print(s[a] + "    ", end='')
    a += 1
    b += 1

  print()

  a = 0

  while a < len(s):
    if len(f[a]) > len(s[a]):
      b = 0
      while b < len(f[a]) + 2:
        print("-", end='')
        b += 1

    else:
      b = 0
      while b < len(s[a]) + 2:
        print("-", end='')
        b += 1

    print("    ", end='')
    a += 1

  print()

  if optional == True:

    a = 0

    while a < len(f):

      if o[a] == "+":

        if len(f[a]) > len(s[a]):
          b = 0
          while b < len(f[a]) + 2 - len(str(int(f[a]) + int(s[a]))):
            print(" ", end='')
            b += 1

        else:
          b = 0
          while b < len(s[a]) + 2 - len(str(int(f[a]) + int(s[a]))):
            print(" ", end='')
            b += 1
        print(str(int(f[a]) + int(s[a])) + "    ", end='')

      else:

        if int(f[a]) - int(s[a]) > 0:

          b = 0
          while b < len(f[a]) + 2 - len(str(int(f[a]) + int(s[a]))):
            print(" ", end='')
            b += 1

        else:

          b = 0
          while b < len(s[a]) + 2 - len(str(int(f[a]) - int(s[a]))):
            print(" ", end='')
            b += 1

        print(str(int(f[a]) - int(s[a])) + "    ", end='')

      a += 1


k = ["32 + 8", "1 -_ 114", "9999 + 9999", "5 - 49", "1 - 3801"]
arithmetic_arranger(k, True)
