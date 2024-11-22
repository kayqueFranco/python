def somaLista(valores=[]):
    """
    A funçaõ somaLista, recebeuma lista de número e
    faz a soma de todos os números da lista e retorna
    o resultado da soma
    Parameters
    -------------------------
    valores: int[]
        Lista de númerp para soma 

    Returns
    -----------------------------
        Retona a soma de uma lista
    """
    resultado =0
    for i in valores:
        resultado+=i

    return resultado

def maiorValor(lista=[]):
    """
    A função maorValor encontra o valor
    em uma lista numérica.


    parameters
    ------------------------
        lista: int[]

    Returns
    ------------------------
        Retorna o maior valor da lista    
    
    """

    m= lista[0]
    for i in lista:
        if i > m:
            m = i

    return m
def inverter(palavra=""):
    # Vamos utilizar o comando 
    # len(length-comprimento)para obter
    # a quantidade de caracteres da palavres 
    qtd = len(palavra)
    invertida =""
    for i in range(qtd-1,-1,-1):
        invertida+=palavra[i]
    return invertida

def palindromo(palavra=""):
    org = inverter(palavra).lower()
    if palavra.lower()==org:
            return"É um palindro"
    else:
        return"Não é um palindromo"
    