# Programa que verifica se um número é par ou ímpar.
# O usuário pode digitar vários números até digitar 0 para sair.

def verificar_par_ou_impar(numero):
    return "Par" if numero % 2 == 0 else "Ímpar"

while True:
    n = int(input("Digite um número (ou 0 para sair): "))

    if n == 0:
        break
    
    print(f"O número {n} é {verificar_par_ou_impar(n)}")