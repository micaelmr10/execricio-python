def metros_para_centimetros(metros):
    """coverte metros para centimetros"""
    return metros * 100

metros = float(input("Digite o valor em metros: "))
centimetros = metros_para_centimetros(metros)
print(f"{metros} metros equivalem a {centimetros} centímetros.")
  
