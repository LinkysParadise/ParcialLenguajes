import sys
import os
def afd(token):
    if token == "+":
        print("SUMA")
    elif token == "++":
        print("INCR")
    elif token.isdigit():
        print("ENTERO")
    elif es_real(token):
        print("REAL")
    else:
        print(f"Token no reconocido: {token}")

def es_real(token):
    partes = token.split('.')
    if len(partes) == 2 and partes[0].isdigit() and partes[1].isdigit():
        return True
    return False

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if os.path.isfile(sys.argv[1]):
            with open(sys.argv[1], 'r') as file:
                for line in file:
                    afd(line.strip())
        else:
            afd(sys.argv[1])
    else:
        raise ValueError("Error: Se debe proporcionar un archivo o un token como argumento .")


