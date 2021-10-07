import math

def derive_binomial(string):
  start = string.index("(") + 1
  end = string.index(")")
  return string[start:end]

def derive_pow(string):
  start = string.index(")^") + 2
  end = start
  while end < len(string) and string[end].isdigit():
    end += 1
  return int(string[start:end])

def derive_coefficient(element):
  if len(element) == 1 and not element[0].isdigit():
    element = "1" + element

  i = 0
  while i < len(element) and (element[i].isdigit() or element[i] == "-"):
    i += 1
  if i >= len(element):
    return int(element), None
  if i == 1 and element[0] == "-":
      return -1, element[1:]
  return int(element[:i]), element[i:]

def exponent_alg(alg, exponent):
  i = alg.index("^")
  
  coefficient = alg[:i]
  pow = alg[i+1:]

  pow = int(pow) ** exponent

  return "^".join([coefficient, exponent])

def filter_string(string, c):
  return "".join(string.split(c))

def format(coefficient, x, exponent):
  res = ""
  if coefficient == 0:
    return "0"
  if exponent == 0:
    return str(coefficient)
  if coefficient != 1:
    if coefficient == -1:
        res += "-"
    else:
        res += str(coefficient)
  
  res += x

  if exponent != 1:
    res += "^" + str(exponent)
  return res

def expand(string):
  binomial = derive_binomial(string)
  binomial = filter_string(binomial, " ")
  binomial = [element for element in binomial.replace("-", "+-").split("+") if len(element) > 0]
  
  pow = derive_pow(string)

  stack = []

  for i in range(pow + 1):
    j = pow - i
    pascal = math.comb(pow, i)

    left, right = binomial[0], binomial[1]
    (lc, lx), (rc, rx) = derive_coefficient(left), derive_coefficient(right)

    nominal = pascal
    c, x = None, None
    exponent = None

    if not lx:
      c, x = rc, rx
      nominal *= lc ** j
      exponent = i
    if not rx:
      c, x = lc, lx
      nominal *= rc ** i
      exponent = j

    formatted = format(nominal * (c ** exponent), x, exponent)
    stack.append(formatted)

  return " + ".join(stack).replace("+-", "-")
