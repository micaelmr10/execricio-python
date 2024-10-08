texto = input("Digite uma sequência de caracteres: ")

texto_limpo = ''.join(c for c in texto if c.isalnum()).lower()

eh_palindromo = texto_limpo == texto_limpo[::-1]
print(f"A sequência de caracteres '{texto}' {'' if eh_palindromo else 'não '}é um palíndromo.")