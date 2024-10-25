# Dada a lista de nomes ["Ana", "Sabrina", "Douglas", "José"], 
# troque o segundo nome da lista para o nome que usuario escolher e exiba o resultado.

lista_nomes = ["Ana", "Sabrina", "Douglas", "José"]
print (f"===== Lista de nomes {lista_nomes} =====\n")

nome = input ("Digite um nome para adicionar a lista: ")
lista_nomes.remove("Sabrina")
lista_nomes.insert(1, nome)

print (f"\n=== Removendo o segundo nome da lista pelo oque você digitou fica: {lista_nomes}")