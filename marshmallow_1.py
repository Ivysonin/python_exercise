from marshmallow import Schema, fields, validates, ValidationError


# Simular tabela de banco de dados
class User():
    def __init__(self, nome:str, idade:int, telefone:str):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone

    def JsonAll(self) -> dict:
        return {
            "nome":self.nome,
            "idade":self.idade,
            "telefone":self.telefone,
        }


class UserSchema(Schema):
    nome = fields.Str(required=True) # Campo obrigatório
    idade = fields.Int()
    telefone = fields.Str()

    # Validação para o telefone
    @validates("telefone")
    def validacao_telefone(self, value):
        if len(value) < 8: # verifica se o número é grande o suficiente
            raise ValidationError("O telefone deve ter pelo menos 9 dígitos.")


schema = UserSchema()

# Serializando em formato JSON
usuario1 = User('Lucas', 16, '819 1234-5678')
transforma_json = schema.dump(usuario1)
print(f"Serialize:\n{transforma_json}\n")

print()

# Deserialize de JSON para objeto python
usuario2 = User('Felipe', 17, '819 5678-9101')
transforma_objeto = schema.load(usuario2.JsonAll()) # transformo em dict
print(f'Deserialize:\n{transforma_objeto}\n')

print()

# Capturando erro
usuario3 = User('Matheus', 18, '1234567')
try:
    usuario3 = schema.load(usuario3.JsonAll())
    print(usuario3)
except ValidationError as e:
    print("Erro:")
    print(e.messages)