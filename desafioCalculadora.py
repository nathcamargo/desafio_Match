try:
    # Solicita a renda mensal
    renda_mensal = float(input("Informe sua renda mensal (entre R$ 3.500,00 e R$ 8.400,00): R$ "))
    if 3500.00 <= renda_mensal <= 8400.00:
        print(f"Renda mensal permitida: R$ {renda_mensal:,.2f}")
    else:
        print("Valor de renda não permitida para o tipo de produto solicitado.")
        exit()

    # Solicita o valor do empréstimo dentro do novo intervalo
    valor_emprestimo = float(input("Informe o valor desejado do empréstimo (Permitido: entre R$ 5.000,00 e R$ 180.000,00): R$ "))
    if 5000.00 <= valor_emprestimo <= 180000.00:
        print(f"Valor de empréstimo permitido: R$ {valor_emprestimo:,.2f}")
    else:
        print("Valor de empréstimo não permitido para o tipo de produto solicitado.")
        exit()

    # Solicita o prazo de pagamento em anos (até 18 anos)
    prazo_pagamento = int(input("Informe o prazo de pagamento em anos (máximo 18 anos): "))
    if 1 <= prazo_pagamento <= 18:
        print(f"Prazo de pagamento válido: {prazo_pagamento} anos")
    else:
        print("Prazo de pagamento não permitido para o tipo de produto solicitado.")
        exit()

    # Calcula o valor da parcela mensal
    taxa_juros_mensal = 0.012
    num_parcelas = prazo_pagamento * 12
    valor_parcela = (valor_emprestimo * taxa_juros_mensal) / (1 - (1 + taxa_juros_mensal) ** -num_parcelas)

    # Verifica se o valor da parcela é até 60% da renda mensal
    if valor_parcela <= 0.6 * renda_mensal:
       print(f"O valor das prestações mensais será de R$ {valor_parcela:,.2f}")
    else:
        print("Valor da parcela fora dos limites permitidos para o produto solicitado.")
except ValueError:
    print("Valor de renda ou empréstimo inválido. Certifique-se de inserir números válidos.")
except KeyboardInterrupt:
    print("\nOperação interrompida pelo usuário.")
