# Para método de verificação automático
import requests
import json
# Insira suas nesse formato: "LINHA": ["01", "02", "03", "04", "05", "06"]
apostas = {
    "LINHA": ["01", "02", "03", "04", "05", "06"]
}
# Isso será usado para contar os acertos, insira a letra das linhas aqui e o número de números sorteados
acertos = {
    "LINHA": 0
}
numeros = ["00", "00", "00", "00", "00", "00"]

# Escolha do método de verificação
escolha = input("Método de verificação (1 - Manual, 2 - Automático): ")
# Metódo de verificação manual
if escolha == "1":
    for x in range(len(numeros)):
        numeros[x] = input("Insira o %s° número: " % ((x + 1)))
# Método de verificação automática
elif escolha == "2":
    url = "https://apiloterias.com.br/app/resultado?loteria=megasena&token=%s&concurso=%s" # URL da API usada, mude o query da loteria para a sua loteria
    token = input("Insira o seu token (https://apiloterias.com.br/): ") # Token para API
    concurso = input("Insira o número do concurso: ") # Número do concurso
    GET = requests.get(url % ((token), (concurso))) # GET
    if GET.status_code == 200:
        # Em caso de sucesso do GET, escrever as dezenas
        i = 0
        for x in json.loads(GET.text)["dezenas"]:
            numeros[i] = x
            i += 1
    else:
        # Caso o contrário, avisar com o código do erro
        input("Houve um erro ao fazer o GET. Aperte ENTER para sair. (%s)" % GET.status_code)
# Método de verificação inválido
else:
    input("Método de verificação inválido. Aperte ENTER para sair.")

# Contando número de acertos
for x in apostas:
    for y in apostas[x]:
        if y in numeros:
            acertos[x] += 1

# Resultado do número de acertos
for x in acertos:
    print("Acertos na linha %s: %s" % ((x), (acertos[x])))
input("Aperte ENTER para sair.")
