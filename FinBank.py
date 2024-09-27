def automato_valida_senha(senha):
    estado_atual = 'q0'
    contem_maiuscula = False
    contem_numero = False
    contem_especial = False
    especiais = "!@#$%^&*"

    for char in senha:
        if estado_atual == 'q0':
            if char.isupper():
                contem_maiuscula = True
            elif char.isdigit():
                contem_numero = True
            elif char in especiais:
                contem_especial = True
            
            # Se todos os critérios forem atendidos, mudar o estado
            if contem_maiuscula and contem_numero and contem_especial:
                estado_atual = 'q1'
                break  # Não precisa continuar verificando a senha
        
    return estado_atual == 'q1'

# Teste de validação de senhas
senhas = ["Teste23@", "teste12@3", "CabralMelhorProsS2@", "Secure#Pass1"]
for senha in senhas:
    if automato_valida_senha(senha):
        print(f"Senha '{senha}' é válida.")
    else:
        print(f"Senha '{senha}' é inválida.")
