def calculadoraIr(salarioInformado):

    tabelaIr = [
       {"Faixa":(0, 1903.98), "Aliquota": 0, "Deducao": 0},
        {"Faixa": (1903.99, 2826.65), "Aliquota": 7.5, "Deducao": 142},
        {"Faixa": (2826.66, 3751.05), "Aliquota": 15, "Deducao": 354.80},
        {"Faixa": (3751.06, 4664.68, 3751.05), "Aliquota": 22.55, "Deducao": 636.130},
        {"Faixa": (4664.69, float("inf")), "Aliquota": 27.5, "Deducao": 869.36}    
    ]
    
    for item in tabelaIr : 
        if salarioInformado > item["Faixa"][0] and salarioInformado <= item["Faixa"][1] :
            imposto = (salarioInformado * item["Aliquota"]) / 100 - item["Deducao"]
            break
        
    return imposto    
        
        
salarioBruto =    float(input("Informe o seu salario bruto:\nR:"))
imposto = calculadoraIr(salarioBruto)
print(f"O imposto de renda devido é de R$ {imposto: .2f}")