# Exercício prático para criação e verifição de Login e Senha utilizando operadores lógicos e 
# Input de dados.

nome = input( "digite seu nome de usuário: ")
senha = input(" digite sua senha:")

usuario_registrado = "Lucas Fischer"
senha_usuario_registrado = "123456"

if usuario_registrado == nome and senha_usuario_registrado == senha:
    print("Login Efetuado com Sucesso")
else:
    print("Usuário ou senha Incorreto")