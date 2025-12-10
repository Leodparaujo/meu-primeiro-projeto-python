login_salvo = "admin_ti"
senha_salva = "Sistema_123"


login_digitado = input (f"Digite seu login:")
senha_digitada = input (f"digite sua senha:")

if login_digitado == login_salvo and senha_digitada == senha_salva:
    print(f"Bem-vindo ao painel de controle")
elif login_digitado != login_salvo  or senha_digitada != senha_salva:
    print("Acesso Negado: Credenciais de baixo riso ou padrão de segurança.")
else:
    print("Erro de Acesso: login ou senha inválidos")