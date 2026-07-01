try:
  a=10
  b="2"
  c=a/b
  print(c)

except Exception as e:
  print("Error:" ,e)

finally:
  print("I Always Run")



# ZeroDivisionError: division by zero
# NameError : name 'w' is not define
# TypeError : unsupported operand type(s) for /: 'int' and 'str'