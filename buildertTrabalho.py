import csv
laptops = []

def carrega_dados():
    with open('laptopPrice.csv', mode='r', encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for linha in csv_reader:
            laptops.append(linha)

def titulo(texto, sublinhado="-"):
    print()
    print(texto)
    print(sublinhado*60)
#1 funcionando
def agrupar_marca():
    titulo("Nº de Laptops por marca")

    dicionario = {}
    for laptop in laptops:
        # busca a palavra (chave). Se não existir: None
        num = dicionario.get(laptop["brand"], None)
        if num == None:
            # não existe, adiciona com o valor 1
            dicionario[laptop["brand"]] = 1
        else:
            # se existe, adiciona mais 1 ao valor
            dicionario[laptop["brand"]] = num + 1

    # classifica os dados do dicionário em uma lista
    lista = sorted(dicionario.items(), key=lambda dic : dic[1], reverse=True)
    # print(lista)
        
    for (marca, num) in lista:
        print(f"{marca:30} {num}")
#2  funcionando
def pesq_processador():
    titulo("Pesquisa por Processador")
    pesq = input("Marca do Processador: ").upper()
    contador = 0
  
    print("Marca.......: Processador.....: RAM: SSD...: Preco:")
    for laptop in laptops:
        if pesq == laptop["processor_brand"].upper():
            print(f"{laptop['brand']:15} {laptop['processor_name']:15} {laptop['ram_gb']:5} {laptop['ssd']:5} {float(laptop['Price']):9.2f}")
            contador = contador + 1

    if contador == 0:
        print(f"Obs.: Não encontrado")
#3  funcionando
def pesq_marca():
    titulo("média de preço por Marca")
    marca = input("Marca: ").upper()
    numPreco = 0
    numMarca = 0
    for laptop in laptops:
        if marca == laptop["brand"].upper():
            numPreco += float(laptop["Price"]) 
            numMarca += 1
            preco_medio = numPreco / numMarca

    print(f"O preço médio dos laptops da marca {marca} é: {preco_medio:9.2f}.")
#4  funcionando
def Listar():
    titulo("Lista dos 10 Laptops mais caros")
    maisCaros = sorted(laptops, key=lambda laptop: float(laptop['Price']), reverse=True)
    print("Marca...........: Processador.....: Preco:")
    for laptop in maisCaros[:10]:
        print(f"{laptop['brand']:15} {laptop['processor_name']:15}  {float(laptop['Price']):9.2f}")
#5  funcionando
def compara():
    titulo("Comparação de quantidade de laptops com")
    dicionario = {}
    pesq1 = input("processador1: ").upper()
    dicionario = {}
    for laptop in laptops:
        if pesq1 == laptop["processor_name"].upper():
            # busca a palavra (chave). Se não existir: None
            num = dicionario.get(laptop["processor_name"], None)
            if num == None:
                # não existe, adiciona com o valor 1
                dicionario[laptop["processor_name"]] = 1
            else:
                # se existe, adiciona mais 1 ao valor
                dicionario[laptop["processor_name"]] = num + 1

    # classifica os dados do dicionário em uma lista
    lista = sorted(dicionario.items(), key=lambda dic : dic[1], reverse=True)
    # print(lista)
        
    for (pesq1, num) in lista:
        print(f"{pesq1} - {num}")

    pesq2 = input("processador2: ").upper()
    dicionario = {}
    for laptop in laptops:
        if pesq2 == laptop["processor_name"].upper():
            # busca a palavra (chave). Se não existir: None
            num = dicionario.get(laptop["processor_name"], None)
            if num == None:
                # não existe, adiciona com o valor 1
                dicionario[laptop["processor_name"]] = 1
            else:
                # se existe, adiciona mais 1 ao valor
                dicionario[laptop["processor_name"]] = num + 1

    # classifica os dados do dicionário em uma lista
    lista = sorted(dicionario.items(), key=lambda dic : dic[1], reverse=True)
    # print(lista)
        
    for (pesq2, num) in lista:
        print(f"{pesq2} - {num}")

#6  funcionando
def ler():
    titulo("Ler marca e preco")
    pesq1 = input("Marca: ").upper()
    pesq2 = input("Preco: ")
    print("Processador.......: Preco:")
    marca = 0

    print("Marca.......: Processador.....: RAM: SSD...: Preco:")
    for laptop in laptops:
        if pesq1 == laptop["brand"].upper() and pesq2 < laptop["Price"]:
            print(f"{laptop['brand']:15} {laptop['processor_name']:15} {laptop['ram_gb']:5} {laptop['ssd']:5} {float(laptop['Price']):9.2f}")
            marca = marca + 1 
    if marca == 0:
        print(f"Obs.: Não encontrado")   
    
carrega_dados()

while True:
    titulo("Estatísticas: Laptops")    
    print("1. Agrupar por Marca")
    print("2. Pesquisar e listar por marca do processador")
    print("3. Calcular o preço médio dos notebooks de uma marca")
    print("4. Listar marca, nome do processador e preço dos 10 mais caros")
    print("5. Comparar 2 processadores")
    print("6. Ler marca e preço")
    print("7. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        agrupar_marca()
    elif opcao == 2:
        pesq_processador()
    elif opcao == 3:
        pesq_marca()
    elif opcao == 4:
        Listar()
    elif opcao == 5:
        compara()
    elif opcao == 6:
        ler()
    else:
        break
