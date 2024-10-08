def is_prime(number):
  """Determina se um número é primo.
  Args:
    number: O número a ser verificado.
  Returns:
    True se o número for primo, False caso contrário.
  """
  if number <= 1:
    return False
  for i in range(2, int(number**0.5) + 1):
    if number % i == 0:
      return False
  return True
numero = int(input("Digite um número inteiro: "))
if is_prime(numero):
  print(f"{numero} é um número primo.")
else:
  print(f"{numero} não é um número primo.")