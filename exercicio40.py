while True:
    nota = float(input("Informe a nota (entre 0 e 10): "))
    if 0 <= nota <= 10:
        break
    else:
        print("Nota inválida. Digite um valor entre 0 e 10.")