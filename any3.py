# Verifique se alguma senha tem mais de 6 caracteres

senhas = ["123", "abc", "senha123", "admin"]

resultado = any(len(senha) > 6 for senha in senhas)

print(resultado)