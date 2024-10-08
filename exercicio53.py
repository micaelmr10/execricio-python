def is_prime(number, count_divisions=0):
  """Determina se um número é primo e conta as divisões realizadas.
  Args:
    number: O número a ser verificado.
    count_divisions: Contador de divisões (opcional, padrão 0).
  Returns:
    Uma tupla com (True/False se o número é primo, número de divisões).
  """
  if number <= 1:
    return False, count_divisions
  for i in range(2, int(number**0.5) + 1):
    count_divisions += 1
    if number % i == 0:
      return False, count_divisions
  return True, count_divisions
n = int(input("Digite um número inteiro: "))
total_divisions = 0
print("Números primos entre 1 e", n, ":")
for num in range(2, n + 1):
  is_prime_result, divisions = is_prime(num)
  total_divisions += divisions
  if is_prime_result:
    print(num)
print("\nNúmero total de divisões:", total_divisions)