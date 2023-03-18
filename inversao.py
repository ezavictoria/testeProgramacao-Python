# pede ao usuário para inserir uma string
string = input("Insira uma string: ")

# cria uma nova string vazia
string_invertida = ""

# percorre a string original de trás para frente e adiciona cada caractere à nova string
for i in range(len(string)-1, -1, -1):
    string_invertida += string[i]

# imprime a nova string invertida
print("A string invertida é:", string_invertida)