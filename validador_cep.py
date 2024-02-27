def validar_cep(cep):
    # Verificar se o CEP está dentro dos parâmetros
    if 100000 <= cep <= 999999:
        # String
        cep_str = str(cep)
        
        # Verificar se não há dígitos repetitivos alternados em pares
        for i in range(1, len(cep_str)-1, 2):
            if cep_str[i] == cep_str[i-1] or cep_str[i] == cep_str[i+1]:
                return False
        
        
        return True
    else:
        
        return False

if __name__ == "__main__":
    # Solicitar que digite o CEP a ser validado
    cep_digitado = input("Digite o CEP a ser validado: ")

    try:
        # Converte a entrada do usuário para um número inteiro
        cep_int = int(cep_digitado)

        # Chama a função de validação e exibe o resultado
        if validar_cep(cep_int):
            print("CEP válido!")
        else:
            print("CEP inválido devido a dígitos repetitivos alternados.")
    except ValueError:
        print("Por favor, insira um número inteiro válido para o CEP.")