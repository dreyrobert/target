def fibonacci(n):
  n1 = 0
  n2 = 1
  n3 = 0
     
  while n3 < n:
    n3 = n1 + n2
    n1 = n2
    n2 = n3

  return n3 == n

n = int(input("Informe um número: "))
if fibonacci(n):
    print("O número {n} pertence a série de Fibonacci!")
else:
    print("O número {n} não pertence a série de Fibonacci!")