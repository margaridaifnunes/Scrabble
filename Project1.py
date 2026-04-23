# Primeiro projeto de FP
# Sou a Margarida Nunes (ist1117809), aluna do 1ºano da Licenciatura em Engenharia Informárica e de Computadores (Alameda).
# O meu email institucional é: margarida.isabel.nunes@tecnico.ulisboa.pt
# O meu email pessoal é: mifnunes2007@gmial.com

LETRAS=['A','B','C','Ç','D','E','F','G','H','I','J','L','M','N','O','P','Q','R','S','T','U','V','X','Z']
TAMANHO_TABULEIRO = 15
PASSAR = 'P'
JOGAR = 'J'
TROCAR = 'T'

###
def valida_palavra(letras_p):
    """
    A função palavra define as palavras válidas através do seu tamanho, obrigatoriamente superior a um; e garante 
    que as letras que a compõe são também elas válidas.
    Args:
    letras_p --> string
    Returns: 
    Booleano
    """
    if type(letras_p)!=str:
        return False
    for i in range (len(letras_p)):
        if not letras_p[i] in LETRAS:   # verificar se os elementos introduzidos pertencem à lista letras
            return False   
    if len(letras_p)<=1:    # verificar que a palavra tem no mínimo 2 caracteres
        return False
    else:
        return True
 
###
def tamanhos_iguais(tuplo1, tuplo2):    #compara tamanhos de 2 tuplos
    """
    tamanhos_iguais: recebe 2 tuplos e, retorna True se os tamanhos forem iguais e False se os tamanhos forem diferentes
    Args:
    tuplo1 --> tuplo
    tuplo2 --> tuplo
    Returns: 
    Booleano
    """
    if len(tuplo1)==len(tuplo2):
        return True
    else:
        return False 
   
###
def cria_conjunto(let, occ):
    """
    cria_conjunto: tuplo*tuplo --> conjunto letras
    Recebe dois tuplos de igual tamanho, um com as letras e outro com as ocorrências das mesmas, e retorna 
    um dicionário cujas chaves são as letras e os valores corresponde às ocorrências de cada letra.
    Args:
    let --> tuplo
    occ --> occ
    Returns:
    conjunto_letras --> dicionário
    """
    i=0          
    conjunto_letras={}
###
#Validação de inputs
    if type (let)!= tuple or type(occ)!=tuple:
        raise ValueError('cria_conjunto: argumentos inválidos')
    if not tamanhos_iguais(let,occ):    # garantir que len(let)=len(occ)
        raise ValueError('cria_conjunto: argumentos inválidos') 
    for i in range (len(occ)):  # garantir que occ é um inteiro positivo
        if type(occ[i])!=int  or occ[i]<=0:
            raise ValueError('cria_conjunto: argumentos inválidos')
        if len(let[i])!=1:  #garantir que cada elemento de let tem uma, e uma só letra  
            raise ValueError('cria_conjunto: argumentos inválidos')          
        if let[i] not in LETRAS:    #garantir que só tem letras válidas      
            raise ValueError('cria_conjunto: argumentos inválidos')
        if let[i] in let[i+1:]:   #garantir que não há elementos de let repetidos    
            raise ValueError('cria_conjunto: argumentos inválidos')   
###    
    i=0
    for i in range(len(let)):  #adicionar pares_(chave,valor) ao dicionário conjunto_letras  
        conjunto_letras[let[i]]=occ[i]
    return conjunto_letras

###
def gera_numero_aleatorio(estado):
    """"
    gera_numero_aleatorio: inteiro --> inteiro
    A função indica um número pseudoaleatório tendo um argumento como estado inicial.
    Args:
    estado --> inteiro
    Returns:
    estado --> inteiro
    """ 
    estado^=(estado<<13) & 0xFFFFFFFF
    estado^=(estado>>17) & 0xFFFFFFFF
    estado^=(estado<<5)  & 0xFFFFFFFF
    return estado

###
def permuta_letras(letras, estado):
    """
    permuta_letras:lista * inteiro --> inteiro --> {}
    A função recebe uma sequência de letras e um estado, retornanando uma ordem aleatória da sequência dada.
    Args:
    letras --> inteiro positivo
    estado --> inteiro positivo
    j: valor aleatório gerado; isto é, ao próximo indice que permuta com o último elemento, que ainda não permutou.
    """
    i=((len(letras))-1)   
    for i in range(i,0,-1):
        estado= gera_numero_aleatorio(estado)
        j = estado % (i+1)     # j é o valor aleatório gerado (índice de um elemento)     
        if j==i:    # se o índice(j) corresponder ao último número que ainda não trocou, continuar                              
            continue
        else:
            letras[j], letras[i]= letras[i], letras[j]  # troca de duas posições  
    return  
          
###
def lista_letras_ordenada(conj_letras):
    """
    lista_letras_ordenada recebe uma sequência, sobre a qual a função verifica segunda a lista de letras 
    válidas ordenadas inicial, que letras se encontram no conjunto recebido e retorna uma lista ordenada os 
    elementos da mesma pela ordem da lista letras definida inicialmente.
    Args:
    conj_letras --> dicionário
    Returns:  
    lista_ordenada --> lista            
    """
    lista_ordenada= []  # lista vazia na qual se adicionar as letras por ordem ordenada
    for letra in LETRAS:    
        if letra in conj_letras:    # ir letra-a-letra na lista original das letras válidas, ver se alguma se encontra no conjunto recebido
            lista_ordenada += [letra]*conj_letras[letra]    # se houve uma letra comum à lista original e ao conjunto dados, esta integrará a lista_ordenada tantas vezes quantas ela existe no conjunto dado
    return lista_ordenada        
      
###    
def baralha_conjunto(conj_letras, estado):  
    """
    baralha_conjunto: conjunto letras * inteiro --> lista
    Esta função recebe um conjunto de letras e um estado inicial do gerador pseudo-aleatório. A partir dos
    argumentos recebidos o conjunto de letras, após ordenado, é baralhado.
    Args:
    conj_letras --> dicionário
    estado -->inteiro positivo
    Returns:
    lista_ordenada --> lista
    """  
    lista_ordenada = lista_letras_ordenada(conj_letras)
    permuta_letras(lista_ordenada,estado)  # permuta os elementos da lista ordenada de letras
    return lista_ordenada

###
def testa_palavra_padrao(palavra, padrao, conj):
    """
    testa_palavra_padrao: cad. caracteres * cad. caracteres * conjunto_letras --> booleano
    A função recebe uma palavra e retorna um booleano (True/False) consoante a possibilidade, ou não, de 
    encaixar nos espaços. 
    Aqui, começamos por verificar se a palavra e o padrao tem, ou não, o mesmo número de caracteres e só é 
    possível avançar se os tamanhos forem idênticos.
    De seguida, é necessário verificar se as letras já colocadas no tabuleiro, que estão no padrão, coincidem
    com o caracter ocupado na palavra.
    Args:
    palavra-->string
    padrao -->string
    conj -->dicionário
    Returns:
    Booleano
    """
    lista_conj = lista_letras_ordenada(conj)

    if not tamanhos_iguais(palavra, padrao):    # verirficar se a palavra e o padrão tem o mesmo número de caracteres
        return False   
    
    for i in range(len(palavra)):
        letra_da_palavra = palavra[i]
        if padrao[i] == '.':    #se for um ponto, pode-se inserir uma letra disponível na lista_conj
            if not letra_da_palavra in lista_conj:  # se for uma letra que não esteja na lista
                return False
            else:   # se a letra estiver na lista é necessário remove-la da mesma
                lista_conj.remove(letra_da_palavra)
        else:
            if letra_da_palavra != padrao[i]:   # se o padrao tiver um letra esta tem de coincidir com a letra da palavra
                return False
    return True            

###  
def cria_tabuleiro():
    """
    cria_tabuleiro é uma função que não recebe nada, sendo iniciado por um conjunto vazio, e que retorna
    um tabuleiro vazio onde cada casa é identificada por '.'.O tabuleiro comtempla tantas linhas e colunas
    quantas o valor correspondente ao TAMANHO_TABULEIRO (15). Ao ser iniciado como uma lista vazia vai ter 15
    sublistas, onda cada uma tem 15 elementos no seu interior. 
    Args:
    Returns:
    tab --> lista
    """
    tab=[]  #tabuleiro vazio                                     
    for i in range(0,TAMANHO_TABULEIRO):   # ciclo que repete o número de vezes do TAMANHO_TABULEIRO
        linha=[]
        for j in range(0, TAMANHO_TABULEIRO): # criação das linhas
            linha.append('.')   # acrescenta '.' a cada iteração
        tab.append(linha)   # acrescentar as linhas ao tabuleiro                    
    return tab

###
def cria_casa(l,c):
    """
    cria_casa recebe uma linha e uma casa, e devolve a casa do tabuleiro.
    Args:
    l --> int
    c --> int
    Returns:
    casa --> tuplo
    """
#Validação de inputs    
    if (type(l)!=int or type(c)!=int):   # garantir de a linha e a coluna são inteiros
        raise ValueError ('cria_casa: argumentos inválidos')
    if (l<=0 or c<=0):  # garantir que são positivos
        raise ValueError ('cria_casa: argumentos inválidos')
    if (l>TAMANHO_TABULEIRO or c>TAMANHO_TABULEIRO):  # garantir que não supera as medidas do tabuleiro
        raise ValueError ('cria_casa: argumentos inválidos')
    casa=(l,c)
    return casa

###
def obtem_valor(tab,casa):     
    """
    obtem_valor é uma função que recebe um tabuleiro, juntamente com uma casa, e retorna o valor a ela
    correspondente, sob a forma de string.
    Args:
    tab --> lista
    casa --> tuplo
    Returns:
    tab[linha][coluna] --> string
    """
    linha = casa[0] - 1   # retirar um valor nas linhas (porque o índice começa em zero)
    coluna = casa[1] - 1   # retirar um valor nas colunas (porque o índice começa em zero)
    return tab[linha][coluna]
                  
###
def insere_letra(tab, casa, letras):
    """
    insere_letras é uma função que ao receber um tabuleiro, uma casa do tabuleiro e uma letra, insere a letra
    na casa indicada alterando destrutivamente o tabuleiro.
    no fim, delvolve o tabuleiro modificado.
    Args:
    tab --> lista
    casa --> tuplo
    letras --> string
    Returns:
    tab --> lista
    """
    linha = casa[0] - 1 # retirar um valor nas linhas (porque o índice começa em zero)
    coluna = casa[1] -1 # retirar um valor nas colunas (porque o índice começa em zero) 
    tab[linha][coluna]= letras
    return tab

###
def obtem_sequencia(tab,casa,direcao,tamanho):
    """
    obtem_sequencia: tabuleiro*casa*string*inteiro --> string
    A string devolvida tem tantos caracteres quanto o argumento inteiro referente a todos os valores nas casas
    do tabuleiro, a partir da casa e na direção indicadas.
    Args:
    tab --> lista
    casa --> tuplo
    direçao --> string (pode ser 'H'-horizontal ou 'V'-vertical)
    tamanho --> inteiro
    Returns:
    sequencia --> string
    """
    sequencia=''
    if direcao=='H':
        for i in range(tamanho):
            sequencia += obtem_valor(tab, cria_casa(casa[0], casa[1] + i))  # a cada iteração vai ver a coluna da direita
    else:
        for i in range(tamanho):
            sequencia += obtem_valor(tab, cria_casa(casa[0] + i, casa[1]))  # a cada iteração vai ver a linha abaixo
    return sequencia  

###
def insere_palavra (tab, casa, direcao, palavra):
    """
    insere_palavra: tabuleiro*casa*string*string --> tabuleiro
    A função depende preponderantemente da direcão inserida, fazendo variar o modo de inserção das letras
    seguintes, se a direção for 'H' (horizontal- da esquerda para a direita) a próxima letra será inserida 
    uma coluna à direita da letra anterior; se a direção for 'V' (vertical- de cima para baixo) a próxima 
    letra será inserida um linha abaixo comparativamente à posição da letra anterior.
    Args:
    tab --> lista
    casa --> tuplo
    direçao --> string (pode ser 'H'-horizontal ou 'V'-vertical)
    palavra --> string
    Returns:
    tab --> lista
    """
    if direcao == 'H':
        for i in range(len(palavra)):   # vai acrescentar um letra de cada vez, cada uma numa casa à direita da anterior
            insere_letra(tab, cria_casa(casa[0] , casa[1] + i), palavra[i])
    else:
        for i in range(len(palavra)):   # vai acrescentar um letra de cada vez, cada uma numa casa abaixo da anterior
            insere_letra(tab, cria_casa(casa[0] + i, casa[1]), palavra[i])
    return tab        

###
def tabuleiro_para_str(tab):
    """
    A função recebe um tabuleiro e retorna uma string que apresenta uma representação externa do mesmo.
    Visando estruturar o código, comecei por separar a função nas seguintes partes: cabeçalho, limite superior
    do tabuleiro, parte lateral e o limite lateral esquerdo e o rodapé. No fim, procedi à montagem das 
    diferentes partes do tabuleiro.
    Args:
    tab --> lista
    Returns:
    tab_para_str: tabuleiro --> string
    """
    tab_para_str = []
### Construção da estrutura do tabuleiro    
# parte do cabeçalho
    dezenas = '1 1 1 1 1 1'
    tab_para_str.append('{:>34}'.format(dezenas))    # 34 = TAMANHO_TABULEIRO*2 + 4
    unidades = '1 2 3 4 5 6 7 8 9 0 1 2 3 4 5'
    tab_para_str.append('{:>34}'.format(unidades))

# limite superior do tabuleiro
    barra_limite_horizontal = '+-------------------------------+'
    tab_para_str.append('{:>36}'.format(barra_limite_horizontal)) # 36 = TAMANHO_TABULEIRO*2 + 6

# parte lateral e limite lateral esquerdo
    numero = 1
    barra_limite_vertical= '|'
    for i in range(0,TAMANHO_TABULEIRO):    # 'varrer' todas as linhas do tabuleiro
        valores_linha = ' '
        espaço = ' '
        for j in range (0, TAMANHO_TABULEIRO):  # 'varrer todas as casa da linha movendo uma ocluna para a direita
            casa = (i + 1, j + 1)
            valor_casa = obtem_valor(tab,casa)
            valores_linha += (valor_casa) + espaço
        tab_para_str.append('{:>2}{:>2}{:2}{:>1}'.format(numero, barra_limite_vertical,valores_linha,barra_limite_vertical))
        numero += 1
# parte do rodapé
    barra_limite_horizontal = '+-------------------------------+'
    tab_para_str.append('{:>36}'.format(barra_limite_horizontal))  
# Representação externa  
    return '\n'.join(tab_para_str)    # montagem final linha-a-linha

###
def cria_jogador(ordem, pontos, conj_letras):
    """
    cria_jogador: inteiro*inteiro*conjunto letras --> jogador
    A função recebe dois inteiros, referentes à ordem do jogador e aos pontos iniciais, e um conjunto de letras
    que correspondem às letras do jogador do Scrabble. No fim, a função devolve um jogador do Scrabble.
    Args:
    ordem --> inteiro positivo
    pontos --> inteiro positivo
    conj_letras --> dicionário
    Returns:
    identidade_do_jogador --> dicionário
    """
# Validação dos inputs    
    if type(ordem) != int:  # a ordem tem de ser um número inteiro 
        raise ValueError ('cria_jogador: argumentos inválidos')
    if not (ordem >= 1 and ordem <= 4):    # pode haver 1-4 jogadores
        raise ValueError ('cria_jogador: argumentos inválidos')
    if type(pontos)!= int:
        raise ValueError('cria_jogador: argumentos inválidos')
    if pontos < 0: # os pontos tem de ser positivos ou zero
        raise ValueError ('cria_jogador: argumentos inválidos')
    if type(conj_letras) != dict:   # conjunto de letras corresponde a um dicionário
        raise ValueError ('cria_jogador: argumentos inválidos')
    for letra in conj_letras:
        if letra not in LETRAS: # tem de ter letras válidas
            raise ValueError ('cria_jogador: argumentos inválidos')
        if type(conj_letras[letra]) != int or conj_letras[letra] <= 0:  # as ocorrências tê, de ser inteiros positivos
            raise ValueError ('cria_jogador: argumentos inválidos')
        
    identidade_do_jogador = {'id':ordem, 'pontos':pontos, 'letras':conj_letras} # devolve o BI do jogador
    return identidade_do_jogador

###
def jogador_para_str(jog):
    """
    jogador_para_str: jogador --> string
    A função recebe um dicionário e devolve uma string correspondente à representação externa do jogador.
    É necessário ordenar as letras do jogador numa lista na qual se assegura logo o espaço em branco entre letras.
    Depois, retiramos o espaço após a última letra e trasnsforma-se a lista para uma string.
    Args:
    jog --> dicionário (chaves do dicionário:'id','pontos','letras')
    Returns:
    f-string com os dados do jogador
    """
    id_jogador = jog['id']  # identificação do jogador
    pontos_jogador = jog['pontos']  # pontuação do jogador
    letras_jogador = jog['letras']  # dicionário com as letras, e respetivas ocorrências, do jogador
    letras_ordenadas_jogador = lista_letras_ordenada(letras_jogador)  # lista ordenada das letras
    lista_ordenada_espacada = []
    for i in letras_ordenadas_jogador:  # criação de lista com as letras ordenadas intercaladas com espaços
        lista_ordenada_espacada += [i]
        lista_ordenada_espacada += [' ']
    if len(lista_ordenada_espacada)>0:
        del lista_ordenada_espacada[-1] # retirar o espaço após a última letra
    str_ordenada_espacada = ''    
    for j in lista_ordenada_espacada:   # passagem da lista anterior para a forma de string
        str_ordenada_espacada += j
     
    return ("#{} ({:>3}): {}".format(id_jogador,pontos_jogador,str_ordenada_espacada))

###
def distribui_letra (letras, jogador):
    """
    distribui_letras: lista*jogador --> booleano
    A função recebe uma lista de letras (eventualmente vazia) e um jogador e retorna um booleano consoante 
    modifique, ou não, os argumentos dados. Aqui, é necessário verificar se, no caso em que a lista não se 
    encontra vazia, se a letra já se encontra documentada no dicionário, sendo apenas imperativo a necessidade
    de acrescentar uma ocorrência, ou, por outro lado, se é necessário acrescentar uma nova chave ao dicionário.
    Args:
    letras --> lista
    jogador --> dicionário
    Returns:
    Booleano
    """
    if letras == []:    # se a lista estiver vazia, retorna False
        return False
    else:
        letra_nova = letras [-1]    # a letra a considerar é a última
        del[letras[-1]]
        letras_jogador = jogador['letras'] # dicionário com as letras, e respetivas ocorrências, do jogador
        if letra_nova in letras_jogador:    # caso a letra já esteja catalogada, incrementa-se +1
            letras_jogador[letra_nova] += 1
        else:   # caso a letra ainda não esteja catalogada
            letras_jogador[letra_nova] = 1
        return True  

###
def lista_ordena_lista(lista):
    """
    A função recebe uma lista e retorna a mesma ordenada consoante a ordem definida em letras.
    Args:
    lista --> lista
    Returns:
    lista_ordenada --> lista
    """
    lista_ordenada=[]
    for letra in LETRAS:
        vezes=lista.count(letra)
        lista_ordenada += [letra]*vezes    # se houve uma letra comum à lista original e ao conjunto dados, esta integrará a lista_ordenada tantas vezes quantas ela existe no conjunto dado
    return lista_ordenada

###
def padrao_tem_pelo_menos_1_letra(padrao):
    """
    A função pretende garantir que o padrão tem pelo menos uma letra.
    Args:
    padrao --> string
    Returns:
    Booleano
    """        
    for letra in padrao:
        if letra != '.':
            return True

###
def joga_palavra (tab, palavra, casa, direcao, conj_letras, primeira):
    """
    joga_palavra: tabuleiro*palavra*casa*string*conjunto_letras*booleano --> tuplo
    A função joga_palavra ao receber um tabuleiro, uma palavra, uma casa, direção, conjunto de letras e um 
    booleano que indica se é, ou não, a primeira jogada. Esta função retorna um tuplo vazio, se a jogada não
    for válida de acordo com as regras estabelecidas, se tiverem menos de 2 letras (na 1ª jogada) ou se nas
    restantes jogadas não usar nenhuma letra já inserida no tabuleiro, se a palavra exceder os limites do 
    tabuleiro e, se no caso de ser a primeira jogada não passar na casa central (8,8).
    Caso contrário, retorna um tuplo constituído pelas letras ordenadas que serão inseridas no tabuleiro.
    Args:
    tab --> lista
    palavra --> string
    casa --> tuplo
    direção --> string (pode ser 'H'-horizontal ou 'V'-vertical)
    conj_letras --> dicionário
    primeira --> booleano
    Returns:
    tuplo vazio (se a jogada for inválida) --> tuplo
    tuplo com as letras usadas ordenadas 8se a jogada for válida) --> tuplo
    """ 
    i=0
    tamanho = len(palavra)
    padrao = obtem_sequencia (tab, casa, direcao, tamanho)  # padrão é aquilo que já está no tabuleiro nas casas que se pretende ocupar
    letras_usadas=[]       

    if testa_palavra_padrao(palavra,padrao,conj_letras):
        # Primeira jogada: (o jogador tem apenas 7 letras, logo se passar na casa_central(8,8) é impossível sair do tabuleiro)
        if primeira == True:
            if tamanho < 2:
                return()
            if direcao =='H':
                if 8 not in range(casa[1], casa[1] + tamanho) or casa[0] != 8:
                    return ()
            if direcao == 'V':
                if 8 not in range(casa[0], casa[0] + tamanho) or casa[1] != 8:
                    return ()       
            insere_palavra (tab, casa, direcao, palavra)
            for i in range(tamanho):
                letras_usadas += [palavra[i]]
            return (tuple(lista_ordena_lista(letras_usadas)))  
            
        # Restantes jogadas:
        else:       
            if testa_palavra_padrao(palavra, padrao, conj_letras) and padrao_tem_pelo_menos_1_letra(padrao) == True and tamanho > 1:
                insere_palavra (tab, casa, direcao, palavra)
                for i in range(tamanho):
                    if palavra[i] != padrao[i] and padrao[i] == '.':
                        letras_usadas =  letras_usadas + [palavra[i]]
                return (tuple(lista_ordena_lista(letras_usadas)))             
    return()

###
def troca_letras (jog, pilha, seq_letras):
    """
    troca_letras: jog*pilha*seq_letras
    A função descarta letras do jogador e fornece-lhe novas letras da pilha.
    Args:
    jog --> dicionário
    pilha --> lista (cujos elementos são do tipo string)
    seq_letras --> lista (letras a trocar)
    Returns:
    Booleano
    """
    letras_jogador = jog['letras']  # dicionário com as letras, e respetivas ocorrências, do jogador
    if len(pilha) < 7:  # 7 é o número mínimo de letras no saco para poder efetuar trocas de letras
        return False
    if len (seq_letras) > len (pilha): # Ver occorencias das letras e comparar com o que há no saco

        for i in range(len(seq_letras)):
            if  seq_letras[i] not in letras_jogador: # as letras inseridas têm de pertence ao seu conjunto
                return False  

    for i in range(len(seq_letras)):
        letras_jogador[seq_letras[i]] -= 1
        if letras_jogador[seq_letras[i]] == 0:  # apagar a letra do dicionário se a letra for zero
            del letras_jogador[seq_letras[i]]
        distribui_letra(pilha, jog)
    return True
    
###
def processa_jogada (tab, jog, pilha, pontos, primeira):
    """
    processa_jogada: tabuleiro*jogador*lista*dicionário*booleano --> booleano
    A função processa_jogada recebe um tabuleiro, um jogador, uma lista de letras, um dicionário com a correspondênica entre as letras e os pontos obtidos e um booleano que indica se é, ou não, a primeira jogada.
    Esta função é responsável por executar os turnos de cada jogador
    Args:
    tab --> lista
    jog --> diconário
    pilha --> lista
    pontos --> dicionário (chaves correspondem às letras e os values são os pontos correspondentes)
    primeira --> booleano
    Returns:
    Booleano
    """
    pontos = { 'A': 1, 'B': 3, 'C': 2, 'Ç': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 4, 'H': 4, 'I': 1, 'J': 5, 'L': 2, 'M': 1, 'N': 3, 'O': 1, 'P': 2, 'Q': 6, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'X': 8, 'Z': 8 }
    id_jogador = jog['id']

    while True:
        opcao_jogada = input(f"Jogada J{id_jogador}: ").strip().split()
        if opcao_jogada[0] == '' or (opcao_jogada[0] != PASSAR and opcao_jogada[0] !=TROCAR and  opcao_jogada[0] !=JOGAR):   # garantir que as únicas opções válidas são: 'P'/'T'/'J'
            continue
    # Passar    
        if opcao_jogada[0] == PASSAR and len(opcao_jogada)==1:
            return False

    # Trocar  
        if opcao_jogada[0]== TROCAR:
            valido = True # Flag de jogada válida
            seq_letras =[]
            if len(opcao_jogada[0]) != 1:   # garantir que o 1º elemento da lista tem tamanho 1
                continue
            for i in range(1,len(opcao_jogada)):
                if len(opcao_jogada[i])==1:   # não pode permitir a existência de palavras começadas por T
                    seq_letras += opcao_jogada[i]
                else:
                    valido = False
                    break      
            if valido == True:
                troca_letras(jog, pilha,seq_letras)
                return True
            else:
                continue
    
    # Jogar    
        if opcao_jogada[0]== JOGAR:
            linha = int(opcao_jogada[1])
            coluna= int(opcao_jogada[2])
            direcao = opcao_jogada[3]
            palavra = opcao_jogada[4]
## linha e coluna (tem de ser inteiro positivo até tamanho_tabuleiro);
           
            if type(linha)!= int or linha<0 or linha>TAMANHO_TABULEIRO: 
                continue
            if type(coluna)!= int or coluna<0 or coluna>TAMANHO_TABULEIRO:    
                continue
            if type(direcao)!=str or (direcao!='V' and direcao!='H'):    
                continue
            if valida_palavra(palavra)==False:   
                continue
            casa = cria_casa(linha,coluna)
            conj_letras= jog['letras']
            letras_usadas_ordenadas = joga_palavra (tab, palavra, casa, direcao, conj_letras, primeira)  
            if letras_usadas_ordenadas==():
                continue
            pontos_jogador = jog['pontos']  # pontuação do jogador  
            for letra in palavra:
                valor = pontos[letra]  # pontuação de cada letra na palavra
                pontos_jogador += valor # pontuação total atual

            # Atualização do dicionário do jogador
            jog['pontos'] = pontos_jogador  

            # 
            letras_jogador = jog['letras']  # dicionário com as letras, e respetivas ocorrências, do jogador
            for letra in letras_usadas_ordenadas:
                ocorrencias = jog['letras'][letra]
                if ocorrencias > 1:
                    ocorrencias -= 1    # atualização das ocorrências no dicionário
                    jog['letras'][letra] = ocorrencias
                else:   #ocorrência=0
                    del jog['letras'][letra]

            # Ir buscar novas letras à pilha  
            for i in range(len(letras_usadas_ordenadas)):   
                novas_letras = distribui_letra(pilha,jog)   # por cada letra descartada, retira uma nova letra da pilha
                if novas_letras == True:
                    continue
                else:
                    break
            return True

###

def cria_jogadores (numero_de_jogadores):
    """
    cria_jogadores é uma função que ao invocar a função cria_jogador pretende inseri-los numa lista, inicialmente vazia.
    Args:
    numero_de_jogadores --> inteiro
    Returns:
    lista_jogadores --> lista
    """
    lista_jogadores = []
    for i in range(numero_de_jogadores):
        jogador = cria_jogador(i+1,0,{})    # no início o jogador tem 0 pontos e ainda não recebeu letras       
        lista_jogadores.append(jogador)
    return lista_jogadores    

###
def distribui_letras_jogadores (lista_jogadores,saco):
    """
    A função recebe uma lista com os jogadores e o saco e distribui as sete letras iniciais pelos memsmo
    Args:
    lista_jogadores --> lista
    saco --> dicionário
    Returns:

    """
    for jogador in lista_jogadores: # para cada jogador, distribui as 7 letras iniciais
        for j in range(7):
            letras_distribuidas = distribui_letra(saco,jogador)

###
def saco_vazio (saco, jogador):
    """
    A função verifica se o jogador ficou sem letras e se o saco se encontra vazio.
    Args:
    saco --> dicionário
    jogador --> dicionário
    Returns:
    Booleano
    """
    return (saco == {} and jogador['letras'] == {})

###
def apresenta_jogadores (lista_jogadores):
    """
    A função trata da representação externa dos jogadores. Aqui, a lista_jogadores tem os jogadores como
    elementos, os quais são dicionários (chaves: id, pontos e letras).
    Args:
    lista_jogadores --> lista
    Returns:
    """  
    for jogador in lista_jogadores:
        print(jogador_para_str(jogador))
        
###
def pontuacao_final(lista_jogadores):
    """
    Esta função recebe a lista_jogadores e devolve um tuplo com as respetivas pontuações.
    Args:
    lista_jogadores --> lista
    Returns:
    tuple(lista_pontuacao_final) --> tuplo
    """
    lista_pontuacao_final=[]
    for jogador in lista_jogadores:
        lista_pontuacao_final.append(jogador['pontos'])  # adiciona à lista um novo elemento, a pontuação do jogador
    return tuple(lista_pontuacao_final)

### 
def scrabble(jogadores, saco, pontos, seed):
    """
    scrabble: inteiro*conjunto letras*dicionário*inteiro -->tuplo
    Esta é a função principal que reflete o encadeamento de todo o jogo, para 2-4 jogadores.
    Primeiramente, baralha-se o saco de letras e distribui-se 7 letras por todos os jogadores, pela ordem de jogo.
    No final do jogo, esta devolve um tuplo com a pontuação final dos jogadores. 
    Args:
    jogadores (número de jogadores) --> inteiro
    saco (conjunto de letras) --> dicionário
    pontos --> dicionário
    seed (estado inicial do gerador pseudo-aleatório) --> inteiro positivo
    Returns:
    pontuacao_final(lista_jogadores) --> tuplo
    """
#Validação de inputs:
    if (type(jogadores) != int or jogadores<2 or jogadores>4):  # garantir que o nº de jogadores é inteiro entre 2 e 4
        raise ValueError('scrabble: argumentos inválidos')
    if type(saco) != dict:  # garantir que o saco é um dicionário
        raise ValueError('scrabble: argumentos inválidos')
    if type(pontos) != dict:    # garantir que os pontos são dicionários
        raise ValueError ('scrabble: argumentos inválidos')
    if (type(seed) != int or seed<0):   #garantir que a seed é inteira e positiva
        raise ValueError ('scrabble: argumentos inválidos')
    if len(LETRAS) != len(pontos):  # garantir que o dicionário está completa
        raise ValueError('scrabble: argumentos inválidos')
    for letra in LETRAS:    # garantir que todas as letras pontuadas são válidas 
        if letra not in pontos or pontos[letra]<0:
            raise ValueError('scrabble: argumentos inválidos')
        
# Mensagem Incial:
    print('Bem-vindo ao SCRABBLE.')
# Impressão do tabuleiro antes da jogada,baralhar e distribuir:
    lista_jogadores = cria_jogadores (jogadores)
    saco = baralha_conjunto(saco,seed)
    distribui_letras_jogadores (lista_jogadores,saco)
    tab=cria_tabuleiro()

    primeira = True # flag de primeira jogada
    fim_jogo = False
    contador_passar = 0
    while not fim_jogo:
        for i in range(jogadores):
            print (tabuleiro_para_str(tab))
            apresenta_jogadores(lista_jogadores)
            retorno = processa_jogada(tab,lista_jogadores[i],saco,pontos,primeira)
            if primeira == True:
                primeira = False
            if retorno == False:    # se a jogada for passar
                contador_passar +=1
                if contador_passar == jogadores:    # se todos os jogadores passarem consecutivamente
                    fim_jogo = True
                    break
            else:
                contador_passar = 0 
            if saco_vazio(saco,lista_jogadores[i]): #verificar se o saco está vazio e se o jogador esgotou as letras
                fim_jogo = True
                break
# Impressão das pontuações:
    return((pontuacao_final(lista_jogadores)))
