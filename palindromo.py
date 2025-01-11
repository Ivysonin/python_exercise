def eh_palindromo(palavra : str):
    if palavra[::-1] == palavra:
        return True
    else:
        return False

palavra = input('Digite uma palavra e veja se é Palíndromo: ')

print(eh_palindromo(palavra))