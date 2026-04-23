# Segundo projeto de FP
# Sou a Margarida Nunes (ist1117809), aluna do 1ºano da Licenciatura em Engenharia Informárica e de Computadores (Alameda).
# O meu email institucional é: margarida.isabel.nunes@tecnico.ulisboa.pt
# O meu email pessoal é: mifnunes2007@gmail.com

###
LETRAS=['A','B','C','Ç','D','E','F','G','H','I','J','L','M','N','O','P','Q','R','S','T','U','V','X','Z']
LET_2_INDEX= dict(zip(LETRAS, range(len(LETRAS))))
TAMANHO_TABULEIRO = 15
PASSAR = 'P'
JOGAR = 'J'
TROCAR = 'T'
PONTUACAO_LETRAS={'A':1,'B':3,'C':2,'Ç':3,'D':2,'E':1,'F':4,'G':4,'H':4,'I':1,'J':5,'L':2,'M':1,'N':3,'O':1,'P':2,'Q':6,'R':1,'S':1,'T':1,'U':1,'V':4,'X':8,'Z':8}
saco_jogo={'A':14,'B':3,'C':4,'Ç':2,'D':5,'E':11,'F':2,'G':2,'H':2,'I':10,'J':2,'L':5,'M':6,'N':4,'O':10,'P':4,'Q':1,'R':6,'S':8,'T':5,'U':7,'V':2,'X':1,'Z':1}
###
# Funções auxiliares pessoais:
def lista_letras_ordenada(conj_letras):
    """
    lista_letras_ordenada recebe uma sequência, sobre a qual a função verifica segunda a lista de letras 
    válidas ordenadas inicial, que letras se encontram no conjunto recebido e retorna uma lista ordenada os 
    elementos da mesma pela ordem da lista letras definida inicialmente.
    Args:
    conj_letras --> dict
    Returns:  
    lista_ordenada --> list           
    """
    lista_ordenada= []  # lista vazia na qual se adicionar as letras por ordem ordenada
    for letra in LETRAS:    
        if letra in conj_letras:    # ir letra-a-letra na lista original das letras válidas, ver se alguma se encontra no conjunto recebido
            lista_ordenada += [letra]*conj_letras[letra]    # se houve uma letra comum à lista original e ao conjunto dados, esta integrará a lista_ordenada tantas vezes quantas ela existe no conjunto dado
    return lista_ordenada

def lista_ordenada_espacada (letras_jogador):
    """
    A função recebe as letras do jogador, ordena-a e deixa cada letra separada da letra seguinte 
    por um espaço.
    Args:
    letras_jogador --> dict
    Returns:
    lista_ordenada_espacada --> list
    """
    letras_ordenadas_jogador = lista_letras_ordenada(letras_jogador)  # lista ordenada das letras
    lista_ordenada_espacada = []
    for i in letras_ordenadas_jogador:  # criação de lista com as letras ordenadas intercaladas com espaços
        lista_ordenada_espacada += [i]  # adicionar a letra
        lista_ordenada_espacada += [' ']    # adicionar o espaço
    if len(lista_ordenada_espacada)>0:
        del lista_ordenada_espacada[-1] # retirar o espaço após a última letra
    return lista_ordenada_espacada  

def str_ordenada_espacada(letras_jogador):
    """
    A função recbe as letras do jogador, ordena as letras e deixa-as espaçadas. Por fim, transforma-a
    lista obtida numa string.
    Args:
    letras_jogador --> dict
    Returns:
    str_ordenada_espacada --> str
    """
    str_ordenada_espacada = ''    
    for j in lista_ordenada_espacada(letras_jogador):   # passagem da lista anterior para a forma de string
        str_ordenada_espacada += j  # acrescenta letra,espaço,letra,espaço,... até ao final da lista
    return str_ordenada_espacada  

def valida_palavra(letras_p):
    """
    A função palavra define as palavras válidas através do seu tamanho, obrigatoriamente superior a um; e garante 
    que as letras que a compõe são também elas válidas.
    Args:
    letras_p --> str
    Returns: 
    bool
    """
    if type(letras_p)!=str: # garantir que a palavra é uma string
        return False
    for i in range (len(letras_p)):
        if not letras_p[i] in LETRAS:   # verificar se os elementos introduzidos pertencem à lista letras
            return False   
    if len(letras_p)<=1 or len(letras_p)>TAMANHO_TABULEIRO:    # verificar que a palavra tem no mínimo 2 caracteres
        return False
    else:
        return True

def padrao_tem_pelo_menos_1_letra(padrao):
    """
    A função pretende garantir que o padrão tem pelo menos uma letra.
    Args:
    padrao --> str
    Returns:
    bool
    """        
    for letra in padrao:    # garantir que tem pelo menos uma letra (diferente de ponto)
        if letra != '.':
            return True

def padrao_tem_pelo_menos_1_ponto(padrao):
    """
    A função pretende garantir que o padrão tem pelo menos um ponto.
    Args:
    padrao --> str
    Returns:
    bool
    """        
    for letra in padrao:    # garantir que tem pelo menos 1 ponto
        if letra == '.':
            return True

def padrao_limites_de_espacos(padrao,espacos_limite):
    """
    A função padrao_limites_de_espacos visa ganrantir que o padrao não excede o limite pontos.
    Args:
    padrao --> str
    espacos_limites --> int
    Returns:
    bool
    """ 
    cont = 0    
    for letra in padrao:
        if letra=='.':
            cont += 1
    if cont != 0  and cont <= espacos_limite: # se cont!=0 há pelo menos um espaço; se cont> espacos então tem mais '.' é permitido
        return True
    return False

def lista_ordena_lista(lista):
    """
    A função recebe uma lista e retorna a mesma ordenada consoante a ordem definida em letras.
    Args:
    lista --> list
    Returns:
    lista_ordenada --> list
    """
    lista_ordenada=[]
    for letra in LETRAS:
        vezes=lista.count(letra)    # contar o número de vezes que cada letra aparece
        lista_ordenada += [letra]*vezes    # se houve uma letra comum à lista original e ao conjunto dados, esta integrará a lista_ordenada tantas vezes quantas ela existe no conjunto dado
    return lista_ordenada

def indica_direcao(i,f):
    """
    A função recebe duas casa e, ao comparar as suas linhas e colunas, devolve 'H' ou 'V' consoante
    a direção entre as duas casa.
    Args:
    i (casa inicial) --> tuple 
    f (casa final) --> tuple
    Returns:
    direcao --> str
    """
    direcao=['H','V']   # direções possíveis
    if i[0]==f[0]:  # se a linha da casa inicial e final forem iguais, direção é horizontal
        direcao='H'
    if i[1]==f[1]:  # se a coluna da casa inicial e final forem iguais, a direção é vertical
        direcao='V'
    return direcao

def indices_palavra(palavra):
    """
    A função recebe uma palavra e devolve tuplo em que cada elemento é o índice de cada caracter da palavra
    em LETRAS.
    Args:
    palavra --> str
    Returns:
    tuple
    """
    return tuple(map(lambda x:LET_2_INDEX[x],palavra))  # devolve o índice de cada elemento consoante LETRAS 

def indice_letra_inicial (letra):
    """
    A função recebe uma letra e retorna o seu índice em LETRAS.
    Args:
    letra --> str
    Returns:
    int
    """
    return LET_2_INDEX[letra]

def gera_numero_aleatorio(estado):
    """"
    A função indica um número pseudoaleatório tendo um argumento como estado inicial.
    Args:
    estado --> int
    Returns:
    estado --> int
    """ 
    estado^=(estado<<13) & 0xFFFFFFFF
    estado^=(estado>>17) & 0xFFFFFFFF
    estado^=(estado<<5)  & 0xFFFFFFFF
    return estado

def permuta_letras(letras, estado):
    """
    A função recebe uma sequência de letras e um estado, retornanando uma ordem aleatória da sequência dada.
    Args:
    letras --> int positivo
    estado --> int positivo
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

def troca_letras (jog, pilha, seq_letras):
    """
    A função descarta letras do jogador e fornece-lhe novas letras da pilha.
    Args:
    jog --> dict
    pilha --> list (cujos elementos são do tipo string)
    seq_letras --> list (letras a trocar)
    Returns:
    Booleano
    """
    letras_jogador = jog['letras']  # dicionário com as letras, e respetivas ocorrências, do jogador
    if len(pilha) < 7:  # 7 é o número mínimo de letras no saco para poder efetuar trocas de letras
        return False
    lista_letras_jog_ordenada = lista_letras_ordenada(letras_jogador)
    for letra in (seq_letras):  #verificar se o jogador tem todas as letras que quer trocar
        if  letra not in lista_letras_jog_ordenada: # as letras inseridas têm de pertence ao seu conjunto
            return False  
        lista_letras_jog_ordenada.remove(letra)

    for letra in (seq_letras):
        letras_jogador[letra] -= 1  # retirar 1 das ocorrências
        if letras_jogador[letra] == 0:  # apagar a letra do dicionário se a letra for zero
            del letras_jogador[letra]
    distribui_letras(jog,pilha,len(seq_letras))
    return True  

def dificuldade_agente(jog):
    """
    A função recebe um jogador e, caso seja um jogador agente, retorna o seu nível.
    Args:
    jog --> dict
    Returns:
    nivel --> str
    """
    if eh_agente(jog):
        return jog['nivel']

def apresenta_jogadores (tuplo_jogadores):
    """
    A função trata da representação externa dos jogadores. Aqui, a lista_jogadores tem os jogadores como
    elementos, os quais são dicionários (chaves: id, pontos e letras).
    Args:
    tuplo_jogadores --> tuple
    Returns:
    """  
    for jogador in tuplo_jogadores:  
        print(jogador_para_str(jogador))  

def pontuacao_final(tuplo_jogadores):
    """
    Esta função recebe a tuplo_jogadores e devolve um tuplo com as respetivas pontuações.
    Args:
    lista_jogadores --> tuple
    Returns:
    tuple(lista_pontuacao_final) --> tuplo
    """
    lista_jogadores= list(tuplo_jogadores)
    lista_pontuacao_final=[]
    for jogador in lista_jogadores:
        lista_pontuacao_final.append(jogador['pontos'])  # adiciona à lista um novo elemento, a pontuação do jogador
    return tuple(lista_pontuacao_final)

###
# TAD casa: 
"""
    Este TAD é imutável e visa representar uma casa do tabuleiro do Scrabble.
    As operações básicas a ele associadas são: o construtor (cria_casa), os seletores (obtem_col e
    obtem_lin), o reconhecedor (eh_casa), o teste(casas_iguais) e os transformadores de alto nível
    (casa_para_str e str_para_casa). No final, conta ainda com a função incrementa_casa, uma funçao
    de alto-nível.
"""
# Construtor:
def cria_casa (lin,col):
    """
    Esta função recebe  dois inteiros equivalentes à linha e coluna e retorna a casa correspondente.
    O construtor verifica a validade dos argumentos recebidos.
    Args:
    lin --> int
    col --> int
    Returns:
    casa --> tuple
    """
    # Validação de inputs:    
    if (type(lin)!=int or type(col)!=int):   # garantir de a linha e a coluna são inteiros
        raise ValueError ('cria_casa: argumentos inválidos')
    if (lin<=0 or lin>TAMANHO_TABULEIRO or col<=0 or col>TAMANHO_TABULEIRO):  # garantir que são positivos e que não superam as medidas do tabuleiro
        raise ValueError ('cria_casa: argumentos inválidos')
    casa=(lin,col)
    return casa

# Seletores:
def obtem_col(c):
    """
    A função retorna a coluna da casa inserida.
    Args:
    c (casa) --> tuple
    Returns:
    c[1] --> col (coluna) --> int
    """
    return c[1]

def obtem_lin(c):
    """
    A função retorna a linha da casa inserida.
    Args:
    c (casa) --> tuple
    Returns:
    c[0] --> lin (linha) --> int
    """
    return c[0]

# Reconhecedor
def eh_casa(arg):
    """
    A função recebe um argumento e retorna um booleano consoante o argumento é um TAD, ou não.
    Aqui, verifica-se:
        - o tipo do argumento, o tamanho do argumento, o tipo que cada elemento do argumento e ainda a
        validade desses elementos consoante o tamanho_tabuleiro.
    Args:
    arg --> tuple
    Returns:
    bool
    """
    return type(arg)==tuple and len(arg)==2 and type(arg[0])==int and type(arg[1])==int and TAMANHO_TABULEIRO>=arg[0]>0 and TAMANHO_TABULEIRO>=arg[1]>0

# Teste
def casas_iguais (c1,c2):
    """
    A função devolve um booleano consoante os argumentos forem casas e se forem, ou não, iguais.
    Args:
    c1,c2 --> tuple
    Returns:
    bool
    """
    if eh_casa(c1) and eh_casa(c2):
        return obtem_lin(c1)==obtem_lin(c2) and obtem_col(c1)==obtem_col(c2)    # garantir que as linhas são iguais às colunas
    return False

# Transformador:
def casa_para_str(c):
    """
    A função devolve uma string com a representação do argumento.
    Args:
    c --> tuplo
    Returns:
    str
    """
    return '('+str(obtem_lin(c))+','+str(obtem_col(c))+')'    # tendo a linha e a coluna, apresenta-se a casa no formato solicitado

def str_para_casa(s):
    """
    A função devolve a casa correspondente à string recebida.
    Args:
    s --> str
    Returns:
    casa --> tuple
    """
    s_sem_parenteses=s.strip('()')  # retirar '(' e ')'
    s_linha_coluna= s_sem_parenteses.split(",") # separar ao encontrar uma vírgula
    casa=(int(s_linha_coluna[0]),int(s_linha_coluna[1]))    # daqui resulta um tuplo com linha e coluna
    return casa

# Funções de alto nível:
def incrementa_casa(c,d,s):
    """
    A função devolve a casa de um determinado tabuleiro do jogo Scrabble a seguir de c, na direção d
    e à distância s (inteiro positivo). Se esta não existir, retorna c.
    Args:
    c (casa)
    d --> str
    s --> int (positivo)
    """
    direcao =['H','V']  # direções possíveis
    try:   
        if eh_casa(c) and type(s)==int and s>0 and d in direcao:    # garantir que é casa e s são argumentos válidos
            if d == 'H':    # se a direção for horizontal
                casa_final=cria_casa(obtem_lin(c),(obtem_col(c)+ s))
            else:   # se a direção for vertical
                casa_final = cria_casa((obtem_lin(c)+ s) , obtem_col(c))
            if eh_casa(casa_final): # garantir que está dentro dos limites do tabuleiro após a incrementação
                return casa_final
    except ValueError:
        return c
    return c
###
# TAD Jogador:   
"""
    O TAD jogador visa representar um jogador do jogo Scrabble, a sua pontuação e letras.
    Os jogadores podem ser: agentes ou humanos.
    Esta TAD conta com as seguintes operações básicas: os construtores (cria_humano e cria_agente),
    os seletores (jogador_identidade, jogador_pontos e jogador_letras), os modificadores
    (recebe_letra,usa_letra e soma_pontos), os reconhecedores (eh_jogador,eh_humano e eh_agente),
    o teste (jogadores_iguais) e o transformador (jogador_para_str).
    No final, conta ainda com a função distribui_letras, uma função de alto-nível.
"""
def cria_humano(nome):
    """
    A função recebe uma string (não vazia) indicativa no nome do jogador e devolve o jogador de 
    Scrabble humano, com 0 pontos e sem letras.
    Args:
    nome --> str
    Returns:
    jogador_humano --> dict (cujas chaves são: 'nome', 'pontos', 'letras')
    """
    if type(nome)!=str or nome == '' or nome==' ':  # se o nome for uma string vazia
        raise ValueError('cria_humano: argumento inválido')
    pontos = 0
    conj_letras ={} # criação de um dicionário vazio para as letras
    jogador_humano = {'nome':nome, 'pontos':pontos, 'letras':conj_letras} 
    return jogador_humano

def cria_agente(nivel):
    """
    A função recebe uma string correspondente ao nível do agente e, quando válida, retorna o
    jogador de Scrabble agente com 0 pontos e 0 letras.
    Args:
    nivel --> str
    Returns:
    jogador_agente --> dict (cujas chaves são: 'nivel', 'pontos', 'letras')
    """
    if type(nivel)!= str:
        raise ValueError('cria_agente: argumento inválido') # garantir que o nível é uma string
    if nivel!='FACIL' and nivel!='MEDIO' and nivel!='DIFICIL':  # garantir que o nível é válido
        raise ValueError('cria_agente: argumento inválido')
    pontos = 0
    conj_letras ={}
    jogador_agente = {'nivel':nivel, 'pontos':pontos, 'letras':conj_letras}
    return jogador_agente

# Seletores:
def jogador_identidade(j):
    """
    A função recbe o jogador e devolve o nome do jogador j em caso de o jogador ser humano. Caso contrário, é um
    jogador agente e devolve o nível a ele associado.
    Args:
    j --> dict
    nome_j --> str
    nivel_j --> str
    Returns:
    nome/nivel --> str
    """
    if 'nome' in j: # se a chave nome existir no dicionário do jogador, então este é humano
        return j['nome']
    else:   # então o jogador é  agente
        return j['nivel']

###
def jogador_pontos(j):
    """
    A função recebe um jogador e retorna os pontos que este tem.
    Args:
    j --> dict
    Returns:
    pontos_j --> int
    """
    pontos_j=j['pontos']    # os pontos do jogador são os valores da chave 'pontos' do dicionário do jogador
    return pontos_j

def jogador_letras(j):
    """
    A função recebe um jogador e retorna uma string ordenada com todas as letras do jogador.
    Args:
    j --> dict
    Returns:
    letras_ordenadas_j --> str
    """
    letras_ordenadas_j = ''
    for letra in lista_letras_ordenada(j['letras']):
        letras_ordenadas_j += letra
    return letras_ordenadas_j

# Modificador:
def recebe_letra(j,l):
    """
    A função recebe uma letra, a qual ao ser adicionada ao jogador j o modifica destrutivamente. 
    No final, devolve o jogador.
    Args:
    j --> dict
    l --> str
    Returns:
    j --> dict
    """
    if l not in j['letras']:  # se a letra ainda não estiver catalogada
        j['letras'][l] = 1
    else:   # se a letra já estiver catalogada
        j['letras'][l] +=1
    return j

def usa_letra(j,l):
    """
    A função recebe um jogador e as suas letras e retira uma letra às suas letras,
    devolvendo o jogador.
    Args:
    j --> dict
    l --> str
    Returns:
    j --> dict
    """
    if j['letras'][l]==1:   # se apenas restar uma letra da que se pretende remover
        del j['letras'][l]  # remover a letra do dicionário
    else:
        j['letras'][l] -=1  # senão, apenas se retira uma ocorrência da letra
    return j

def soma_pontos(j,p):
    """
    A função recebe um jogador e um dado número de pontos a somar aos que já possui.
    Args:
    j --> dict
    p --> int
    Returns:
    j --> dict
    """
    j['pontos'] += p    # somar os pontos recebidos 
    return j

# Reconhecedor:
def eh_jogador(arg):
    """
    A função recebe um argumento e determina se é, ou não, um TAD jogador, retornando um booleano,
    True, se for um jogador, False, caso contrário.
    É necessário garantir que o argumento é um dicionário, que tem 3 chaves e que as chaves são: nivel ou nome(str)/
    pontos(int)/letras(dict). Os pontos tem ainda de ser inteiros positivos ou zero.
    Args:
    arg --> universal
    Returns:
    bool
    """
    return (type(arg)==dict and len(arg)==3 and (('nivel' in arg  and type(arg['nivel'])==str) or ('nome' in arg and type(arg['nome'])==str ))\
        and 'pontos' in arg and type(arg['pontos'])==int and arg['pontos']>=0 and 'letras' in arg and type(arg['letras'])==dict)

def eh_humano(arg):
    """
    A função recebe um argumento e determina se é um TAD jogador humano, retornando um booleano, True,
    se for um jogador humano, False, caso contrário.
    Args:
    arg --> universal
    Returns:
    bool
    """
    return eh_jogador(arg) and 'nome' in arg

def eh_agente (arg):
    """
    A função A função recebe um argumento e determina se é um TAD jogador agente, retornando um booleano, True,
    se for um jogador humano, False, caso contrário.
    Args:
    arg --> universal
    Returns:
    bool
    """
    return eh_jogador(arg) and 'nivel' in arg

# Teste:
def jogadores_iguais (j1,j2):
    """
    A função recebe dois argumentos e retorna True se ambos forem jogadores e, se forem iguais.
    Args:
    j1 --> universal
    j2 --> universal
    Returns:
    bool
    """
    return eh_jogador(j1) and eh_jogador(j2) and j1==j2 # garantir que são jogadores e que são iguais

# Transformador:
def jogador_para_str(t):
    """
    A função recebe um jogador e devolve uma string com os dados do jogador.
    No caso de ser um jogador humano retorna '<nome> (<pontos>): <letras espaçadas>'
    No caso de ser um jogador agente retorna 'BOT(<nível>) (<pontos>): <letras espaçadas>'
    Args:
    t --> dict
    Returns:
    jogador_str --> str
    """
    if eh_humano(t):    # Se for um jogador humano
        if jogador_letras(t)=='':
            return("{} ({:>3}):".format(jogador_identidade(t),jogador_pontos(t)))
        else:
            return("{} ({:>3}): {}".format(jogador_identidade(t),jogador_pontos(t),str_ordenada_espacada(t['letras'])))
    else: 
        if jogador_letras(t)=='':  # Se for um jogador agente
            return("BOT({}) ({:>3}):".format(jogador_identidade(t),jogador_pontos(t)))
        else:
            return("BOT({}) ({:>3}): {}".format(jogador_identidade(t),jogador_pontos(t),str_ordenada_espacada(t['letras']))) 
# Função de alto nível:
def distribui_letras(jog, saco, num):
    """
    A função recebe um jogador, um saco e um número (nº máximo de letras a retirar do final da lista
    saco, eventualmente vazia). Essas letras são acrescentadas ao jogador e retorna-se o jogador.
    Args:
    jog --> dict
    saco --> list
    num --> int
    Returns:
    jog --> dict
    """
    if eh_jogador(jog):
        while saco !=[] and num>0:  # Enquanto o saco tiver letras e não exceder o num máximo 
            recebe_letra(jog,saco[-1])  # Acrescentar a letra ao jogador
            del saco[-1]    # Retirar a última letra
            num -=1
        return jog  
    
###
# TAD Vocabulário:
"""
    O TAD vocabulario visa representar o conjunto de palavras que se podem usar durante o jogo.
    Para tal, regista ainda a pontuação das palavras, por meio da pontuação das letras.
    Este TAD conta com as seguintes operações básicas: o construtor (cria_vocabulario), os
    seletores (obtem_pontos e obtem_palavras), o teste (testa_palavra_padrao), o transformador
    (ficheiro_para_vocabulario e vocabulario_para_str).
    Conta ainda com a função de alto-nível: procura_palavra_padrao.
"""
# Construtor:
def cria_vocabulario(v):
    """
    A função devolve o vocabulário com todas as palavras contidas no tuplo recebido.
    Args:
    v --> tuple
    Returns:
    vocabulario --> dict (chaves: letras iniciais da palavra; values: lista com as palavras )
    """
    # Validação de inputs:
    if type(v)!= tuple or len(v)<1: # garantir que é um tuplo com pelo menos 1 palavra
        raise ValueError ('cria_vocabulario: argumento inválido')
    if len(v)!= len(set(v)):    # garantir a unicidade das palavras, comparando o tamanho do tuplo ao tamanho do set(tuplo sem repetições)   
        raise ValueError ('cria_vocabulario: argumento inválido')
    for palavra in v:
        if not valida_palavra(palavra): # garantir que a palavra é válida
            raise ValueError ('cria_vocabulario: argumento inválido')

    vocabulario={}
    for palavra in v:  # percorrer todas as palavras na lista ordenada
        letra_inicial=palavra[0]    # ver a letra inicial
        if letra_inicial not in vocabulario:
            vocabulario[letra_inicial]=[]   # se a letra_inicial não for chave, criar uma nova
        vocabulario[letra_inicial].append(palavra)  # chave: letra inicial, valor: palavra
    return vocabulario    

# Seletor:
def obtem_pontos(vocabulario,palavra):
    """
    A função recebe o vocabulario e uma palavra e devolve os pontos da palavra do vocabulário, ou 
    zero, se não a encontrar.
    Args:
    vocabulario --> dict
    palavra --> str
    Returns:
    pontos_palavra --> int
    """
    pontos_palavra = 0
    letra_inicial = palavra[0]

    if letra_inicial not in vocabulario:
        return 0
    if palavra not in vocabulario[letra_inicial]:
        return 0
    for letra in palavra:   # se estiver, ver os pontos de cada letra da palavra
        pontos_palavra += PONTUACAO_LETRAS[letra]   # somar a pontuação da letra à pontuação já obtida das letras analisadas
    return pontos_palavra

def obtem_palavras(vocabulario,comp,letra):
    """
    A função retorna um tuplo cujos elemementos são: palavra e pontuação; consoante um dado comprimento e letra inicial.
    No fim, os pares devem estar ordenados por ordem decrescente de pontuação e, em caso de empate,
    por ordem lexicográfica. Se alguma palavra, não estiver no vocabulário, deve-se retornar um tuplo
    vazio.
    Args:
    vocabulario --> dict
    comp --> int
    letra --> str
    Returns: 
    tuplo_palavra_pontos --> tuple
    """
    palavras_filtradas=filter(lambda x: len(x)==comp,vocabulario)   # filtrar pelo comprimento
    palavras_filtradas = [p for p in vocabulario.get(letra, []) if len(p) == comp]
    
    #palavras_filtradas = [p for p in vocabulario[letra] if len(p) == comp]
    if not palavras_filtradas:
        return ()
    # Dicionácio(chaves:palavras; values: pontos correspondentes às palavras)
    palavra_pontos={}
    for palavra in palavras_filtradas:
        palavra_pontos[palavra]=obtem_pontos(vocabulario,palavra)
    # Ordenação:(pontuação decrescente e, em caso de empate, pela ordem de LETRAS)
    pares_ordenados = []    # Converter dicionário em lista de tuplos
    for palavra in palavra_pontos:
        pares_ordenados.append((palavra, palavra_pontos[palavra]))
    lista_palavra_pontos = sorted(pares_ordenados, key=lambda x: (-x[1], indices_palavra(x[0])))    # ordenar pela ordem dos índices de forma decrescente
    # Converter lista para tuplo:
    return tuple(lista_palavra_pontos)

# Teste:
def testa_palavra_padrao(vocabulario,palavra,padrao,letras):
    """
    A função recebe o vocabulário, uma palavra, um padrão e letras. A função devolve o booleano True
    se a palavra estiver inserida no vocabulario e se for possível substituir os caracteres '.' do
    padrao dado por letras de letras. Se não for possível verificar tais condições, retorna False.
    Args:
    vocabulario --> dict
    palavra --> str
    padrao --> str
    letras (elementos de LETRAS) --> str
    """
    letra_inicial = palavra[0]
    if letra_inicial not in vocabulario:    # ver se a chave existe
        return False
    if palavra not in vocabulario[letra_inicial]:  # garantir que a palavra é válida, de acordo com o vocabulário
        return False
    if len(palavra) != len(padrao): # garantir que a palavra e o padrão têm o mesmo tamanho
            return False

    lista_letras = list(letras) # lista em que cada elemento é uma letra
    for i in range(len(palavra)):
        letra_da_palavra = palavra[i]
        if padrao[i] == '.':    #se for um ponto, pode-se inserir uma letra disponível na lista_conj
            if letra_da_palavra not in lista_letras:  # se for uma letra que não esteja na lista
                return False
            else:   # se a letra estiver na lista é necessário remove-la da mesma
                lista_letras.remove(letra_da_palavra)   # remove a primeira vez que aparece a letra_da_palavra
        else:
            if letra_da_palavra != padrao[i] :   # se o padrao tiver um letra esta tem de coincidir com a letra da palavra
                return False
    return True                              

# Transformador:
def ficheiro_para_vocabulario(nome_fich):
    """
    A função recebe o nome de um ficheiro que deverá conter uma palavra por linha, podendo ter 
    linha vazias (que devem ser ignoradas). As palavras do ficheiro são sequências de caracteres 
    únicas de cumprimento não-definido, podendo conter qualquer caracter.
    A função deverá retornar o vocabulário proveniente das palavras contidas no ficheiro, que tem
    entre 2 a 15 letras convertidas para maiúsculas.
    Args:
    nome_fich --> file
    Returns:
    vocabulario --> dict
    """
    lista_vocabulario=[]
    with open (nome_fich,'r',encoding="UTF-8") as file:  # abrir o ficheiro em modo de leitura
        lista_linhas = file.readlines() # lista em que cada elemento é palavra\n ou só \n (linha vazia)
        
        for i in lista_linhas:
            palavra = i.strip().upper() # remove \n, linhas vazias e converte para letras maiúsculas
            if 2<= len(palavra)<= TAMANHO_TABULEIRO and valida_palavra(palavra):
                lista_vocabulario.append (palavra)    
        tuplo_vocabulario_fich = tuple(set(lista_vocabulario))  # garantindo por fim a unicidade dos elementos
        return cria_vocabulario(tuplo_vocabulario_fich)   

def vocabulario_para_str(vocabulario):
    """
    A função recebe o vocabulário e devolve uma string que concatena todas as palavras guardadas no 
    vocabulário, separadas por um caracter de mudança de linha ('\n'). As palavras devem estar 
    ordenadas por comprimento e, para o mesmo comprimento, por ordem lexicográfica do 1º caracter.
    Se, mesmo assim, houver um empate devem estar ordenadas consoante a ordem  do seletor 
    otem_palavras.
    Args:
    vocabulario --> dict
    Returns:
    str_para_vocabulario --> str
    """
    str_para_vocabulario=''
    lista_palavras_pontos=[]   # criação de lista vazia
    for letra_inicial in vocabulario.keys():
        for palavra in vocabulario[letra_inicial]:
            lista_palavras_pontos.append((palavra, obtem_pontos(vocabulario,palavra)))  # no final do loop, tem-se uma uma lista com todas as palavras do dicionário, ordenada pelas letras_iniciais

    # ordenar consoante o comprimento; em caso de empate, pela letra inicial; em caso de empate pelos pontos das palavras e, em caso de empate, pela lexicografia da palavra
    lista_palavras_ordenada = sorted((lista_palavras_pontos), key=lambda x: (len(x[0]), indice_letra_inicial(x[0][0]),-x[1], indices_palavra(x[0]))) 
    # string que concatena palavra\npalavra\n,...
    lista_palavras=[palavra[0] for palavra in lista_palavras_ordenada]  # lista com as palavras ordenadas
    for palavra in lista_palavras:
            str_para_vocabulario += palavra + '\n'
    return str_para_vocabulario.rstrip()    # retirar o \n após a última palavra

def procura_palavra_padrao (vocabulario,padrao,letras,min_pontos):
    """
    A função recebe o vocabulario, um padrao, letras e min_pontos. e retorna uma palavra do 
    vocabulario para a qual as letras encaixam num padrao tendo pelo menos min_pontos. Se tal não for
    possível, deve retornar-se um tuplo ('',0).
    Args:
    vocabulario --> dict
    padrao --> str
    letras --> str
    min_pontos --> int
    Returns:
    (palavra,pontos) --> tuple
    """
    # se o padrão começar por uma letra
    palavra_max_pontos=''
    numero_max_pontos = 0
    if padrao[0]!='.':

        palavras_possiveis= obtem_palavras((vocabulario),len(padrao),padrao[0])
        if palavras_possiveis==():
                return ('', 0)
        for informacao_palavra in palavras_possiveis:
            palavra = informacao_palavra[0]  # a palavra
            pontos = informacao_palavra[1]   # os pontos
            if testa_palavra_padrao(vocabulario,palavra,padrao,letras) and pontos>=min_pontos:   # não é menor ou igual pois procura-se padrões melhores que os
                return (tuple((palavra, pontos)))
        return ('', 0)    
    # se o padrão não começa por uma letra
    else:
        encontrou = False
        for letra in LETRAS:
            if letra not in vocabulario:
                continue
            palavras_possiveis= obtem_palavras(vocabulario,len(padrao),letra)            
            # por ordem lexicográfica ir comparando os pontos da palavra atual e da seguinte, 
            # se a palavra encaixar e tiver mais pontos, substituir; senão, passar à próxima iteração.
            for informacao_palavra in palavras_possiveis:
                palavra = informacao_palavra[0]  # a palavra
                pontos = informacao_palavra[1]   # os pontos

                if testa_palavra_padrao(vocabulario,palavra,padrao,letras) and pontos>=min_pontos and pontos > numero_max_pontos:   
                    encontrou = True
                    palavra_max_pontos = palavra
                    numero_max_pontos=pontos 
        if encontrou:
            return tuple((palavra_max_pontos, numero_max_pontos))                           
        return('',0)
# TAD Tabuleiro:
"""
    O TAD tabuleiro visa representar visualmente os tabuleiro do jogo Scrabble bem como as letras nele colocadas.
    O TAD tem as seguintes operações básicas associadas: o construtor(cria_tabuleiro), o seletor (obtem_letra),
    o modificador (insere_letra), os reconhecedores (eh_tabuleiro e eh_tabuleiro_vazio), o teste (tabuleiros_iguais).
    O TAD tem ainda associada as funções de alto-nível associadas (obtem_padrao, insere_palavra, obtem_subpadroes e
    gera_todos_padroes).
"""
# Construtor:
def cria_tabuleiro ():
    """
    cria_tabuleiro é uma função que não recebe nada, sendo iniciado por um conjunto vazio, e que retorna
    um tabuleiro vazio onde cada casa é identificada por '.'.O tabuleiro comtempla tantas linhas e colunas
    quantas o valor correspondente ao TAMANHO_TABULEIRO (15). Ao ser iniciado como uma lista vazia vai ter 15
    sublistas, onda cada uma tem 15 elementos no seu interior. 
    Args:
    Returns:
    tab --> list
    """
    tab=[]  #tabuleiro vazio                                     
    for i in range(0,TAMANHO_TABULEIRO):   # ciclo que repete o número de vezes do TAMANHO_TABULEIRO
        linha=[]
        for j in range(0, TAMANHO_TABULEIRO): # criação das linhas
            linha.append('.')   # acrescenta '.' a cada iteração
        tab.append(linha)   # acrescentar as linhas ao tabuleiro                    
    return tab  

# Seletores:
def obtem_letra(t,c):    
    """
    obtem_letra é uma função que recebe um tabuleiro, juntamente com uma casa, e retorna o valor a ela
    correspondente, sob a forma de string.
    Args:
    t --> list
    c --> tuple
    Returns:
    t[linha][coluna] --> str 
    """
    linha = obtem_lin(c) - 1  # retirar um valor nas linhas (porque o índice começa em zero)
    coluna = obtem_col(c) - 1   # retirar um valor nas colunas (porque o índice começa em zero)
    return t[linha][coluna] 

# Modificadores:
def insere_letra(t,c,l):
    """
    insere_letra é uma função que ao receber um tabuleiro, uma casa do tabuleiro e uma letra, insere a letra
    na casa indicada alterando destrutivamente o tabuleiro.
    no fim, delvolve o tabuleiro modificado.
    Args:
    t --> list
    c --> tuple
    l --> str
    Returns:
    tab --> list
    """
    linha = obtem_lin(c) - 1 # retirar um valor nas linhas (porque o índice começa em zero)
    coluna = obtem_col(c) -1 # retirar um valor nas colunas (porque o índice começa em zero) 
    t[linha][coluna]= l
    return t

# Reconhecedor:
def eh_tabuleiro(arg):
    """
    A função recebe um argumento e verifica se é um tabuleiro. Para tal efetua as seguintes verificações:
    que o argumento é uma lista com TAMANHO_TABULEIRO listas. Neste caso, o tabuleiro deverá ser uma 
    lista com 15 sublistas em que cada lista deverá ter 15 elementos. Por sua vez, cada elemento deverá
    ser uma string; ou um pontos ou uma letra válida.
    Args:
    arg --> universal
    Returns:
    bool
    """
    if type(arg)==list and len(arg)==TAMANHO_TABULEIRO:
        for i in range(TAMANHO_TABULEIRO): # cada i é o índice de uma lista com 15 elementos
            for j in range(TAMANHO_TABULEIRO):   # j é o índice dos elementos de cada sublista
                if len(arg[i]) != TAMANHO_TABULEIRO or type(arg[i]) != list:
                    return False
                if type(arg[i][j])!= str or (arg[i][j]!='.' and arg[i][j] not in LETRAS):
                    return False
        return True 
    return False       

def eh_tabuleiro_vazio (arg):
    """
    A função recebe um argumento e determina se é um tabuleiro vazio, retornando True; ou não, 
    retornando False.
    Args:
    arg --> universal
    Returns:
    bool
    """
    if not eh_tabuleiro(arg):
        return False
    for i in range(TAMANHO_TABULEIRO):  # i --> índice de cada sublista
        for j in range(TAMANHO_TABULEIRO):  # j --> índice dos elementos de cada sublista
            if arg[i][j]!='.':
                return False
    return True        

# Teste:
def tabuleiros_iguais (t1,t2):
    """
    A função verifica se os argumentos são tabuleiro e verifica se são, ou não, idênticos.
    Args:
    t1 --> universal
    t2 --> universal
    Returns:
    bool
    """
    return eh_tabuleiro(t1) and eh_tabuleiro(t2) and t1==t2 # verificar se ambos são tabuleiro válidos e se são iguais
               
# Transformador:
def tabuleiro_para_str(t):
    """
    A função recebe um tabuleiro e retorna uma string que apresenta uma representação externa do mesmo.
    Visando estruturar o código, comecei por separar a função nas seguintes partes: cabeçalho, limite superior
    do tabuleiro, parte lateral e o limite lateral esquerdo e o rodapé. No fim, procedi à montagem das 
    diferentes partes do tabuleiro.
    Args:
    tab --> list
    Returns:
    tab_para_str: tabuleiro --> str
    """
    tab_para_str = []
    ### Construção da estrutura do tabuleiro    
    # Parte do cabeçalho
    dezenas = '1 1 1 1 1 1'
    tab_para_str.append('{:>34}'.format(dezenas))    # 34 = TAMANHO_TABULEIRO*2 + 4
    unidades = '1 2 3 4 5 6 7 8 9 0 1 2 3 4 5'
    tab_para_str.append('{:>34}'.format(unidades))

    # Limite superior do tabuleiro
    barra_limite_horizontal = '+-------------------------------+'
    tab_para_str.append('{:>36}'.format(barra_limite_horizontal)) # 36 = TAMANHO_TABULEIRO*2 + 6

    # Parte lateral e limite lateral esquerdo
    numero = 1
    barra_limite_vertical= '|'
    for i in range(0,TAMANHO_TABULEIRO):    # 'varrer' todas as linhas do tabuleiro
        valores_linha = ' '
        espaço = ' '
        for j in range (0, TAMANHO_TABULEIRO):  # 'varrer todas as casa da linha movendo uma ocluna para a direita
            casa = (i + 1, j + 1)
            valor_casa = obtem_letra(t,casa)
            valores_linha += (valor_casa) + espaço
        tab_para_str.append('{:>2}{:>2}{:2}{:>1}'.format(numero, barra_limite_vertical,valores_linha,barra_limite_vertical))
        numero += 1
    # Parte do rodapé
    barra_limite_horizontal = '+-------------------------------+'
    tab_para_str.append('{:>36}'.format(barra_limite_horizontal))  
    # Representação externa  
    return '\n'.join(tab_para_str)    # montagem final linha-a-linha             

# Funções de alto-nível:
def obtem_padrao(t,i,f):
    """
    A função recebe o tabuleiro e duas casas e devera devolver a sequência de letras entre as mesmas.
    Args:
    t --> list
    i --> tuple
    f --> tuple
    Returns:
    padrao --> str
    """
    padrao = ''
    linha_i=obtem_lin(i)
    linha_f=obtem_lin(f)
    coluna_i=obtem_col(i)
    coluna_f=obtem_col(f)

    if linha_i==linha_f:      # se a direção for horizontal, então i e f tem a mesma linha
        tamanho = abs(coluna_f-coluna_i) + 1
        if coluna_i< coluna_f:  # determinar qual está mais à esqueda, isto é, qual é ,de facto, a casa inicial
            for j in range(tamanho):
                padrao += obtem_letra(t, cria_casa(linha_i, coluna_i+j))
        else:
            for j in range(tamanho):
                padrao += obtem_letra(t,cria_casa(linha_f, coluna_f +j))

    elif coluna_i==coluna_f:    # se a direção for vertical, então i e f tem a mesma coluna
        tamanho = abs(linha_f -linha_i) + 1
        if linha_i<linha_f:   # determinar qual está mais à acima, isto é, qual é ,de facto, a casa inicial
            for j in range(tamanho):
                padrao += obtem_letra(t,cria_casa(linha_i+j,coluna_i))
        else:
            for j in range(tamanho):
                padrao += obtem_letra(t,cria_casa(linha_f+j,coluna_f))  
    return padrao                

def insere_palavra(t,c,d,p):
    """
    insere_palavra: tabuleiro*casa*string*string --> tabuleiro
    A função depende preponderantemente da direcão inserida, fazendo variar o modo de inserção das letras
    seguintes, se a direção for 'H' (horizontal- da esquerda para a direita) a próxima letra será inserida 
    uma coluna à direita da letra anterior; se a direção for 'V' (vertical- de cima para baixo) a próxima 
    letra será inserida um linha abaixo comparativamente à posição da letra anterior.
    Args:
    t --> list
    c --> tuple
    d --> str (pode ser 'H'-horizontal ou 'V'-vertical)
    p --> str
    Returns:
    t --> list
    """
    if d == 'H':
        for i in range(len(p)):   # vai acrescentar um letra de cada vez, cada uma numa casa à direita da anterior
            insere_letra(t, cria_casa(c[0] , c[1] + i), p[i])
    else:
        for i in range(len(p)):   # vai acrescentar um letra de cada vez, cada uma numa casa abaixo da anterior
            insere_letra(t, cria_casa(c[0] + i, c[1]), p[i])
    return t

def obtem_subpadroes(t,i,f,l):
    """
    A função recebe um tabuleiro, a casa inicial, a casa final e a letra inicial e retorna dois
    tuplos de tamanhos iguais.
    O 1º tuplo contem: todos os subpadrões viáveis ordenados a partir do padrão original, 
    pertencentes ao taubleiro entre as casas i e f, inculsive; com o máximo de l espaços livres.~
    O 2º tuplo inclui as casa iniciais de cada um dos subpadrões no tuplo 1.
    Args:
    t --> list
    i --> tuple
    f --> tuple
    l --> int
    """
    padrao = obtem_padrao(t,i,f)
    lista_subpadroes=[]
    lista_casa_iniciais=[]
    direcao= indica_direcao(i,f)
    tamanho= len(padrao)
    # condição do algoritmo 0<=h<tamanho e h<j<=tamanho
    for h in range(tamanho):     # h --> indice da casa inicial do subpadrão
        for j in range(tamanho, h, -1): # j --> indice da casa final do subpadrão
            subpadrao=padrao[h:j]
            # Validações dos subpadrões:                            
            if padrao_tem_pelo_menos_1_letra(subpadrao) and padrao_tem_pelo_menos_1_ponto(subpadrao) and padrao_limites_de_espacos(subpadrao,l):
                existe_letra_atras = (h>0 and not padrao[h-1]=='.')
                existe_letra_frente=( j < tamanho and not padrao[j]=='.')
                if not existe_letra_atras and not existe_letra_frente:    # se o subpadrão verificar as condições atrás, é valido
                    lista_subpadroes.append(subpadrao)
                    casa_inicial= incrementa_casa(i, direcao, h)
                    lista_casa_iniciais.append(casa_inicial)

    tuplo_subpadroes= tuple(lista_subpadroes)
    tuplo_casa_iniciais= tuple (lista_casa_iniciais)     
    return (tuplo_subpadroes, tuplo_casa_iniciais)  

def gera_todos_padroes(t,l):
    """
    A função recebe o tabuleiro e o um l-máximo de espaços livres e retorna 3 tuplos de igual tamanho.
    O 1º tuplo: inclui todos os subpadrões que tem no máximo l espaços livres. Estes devem encontrar-se 
    ordenados obtidos de cada uma das linhas do tabuleiro.
    O 2º tuplo: contém a casa inicial
    o 3º tuplo: contém a direção ('V' ou 'H')
    Args:
    t --> list
    l --> int
    Returns:
    (tuplo_todos_subpadroes,tuplo_casa_iniciais,tuplo_direcoes) --> tuple
    """
    lista_todos_subpadroes= []
    lista_casa_iniciais= []
    lista_direcoes= []
    for linha in range(1, TAMANHO_TABULEIRO+1): # para cada sublista (linha)
        palavras, casas = obtem_subpadroes(t,cria_casa(linha,1),cria_casa(linha,TAMANHO_TABULEIRO), l)
        for i in range(len(palavras)):
            lista_todos_subpadroes.append(palavras[i])
            lista_casa_iniciais.append(casas[i])
            lista_direcoes.append("H")

    for coluna in range(1, TAMANHO_TABULEIRO+1): # para cada sublista (linha)
        palavras, casas = obtem_subpadroes(t,cria_casa(1,coluna),cria_casa(TAMANHO_TABULEIRO,coluna),l)
        for i in range(len(palavras)):
            lista_todos_subpadroes.append(palavras[i])
            lista_casa_iniciais.append(casas[i])
            lista_direcoes.append("V")

    return (tuple(lista_todos_subpadroes),tuple(lista_casa_iniciais),tuple(lista_direcoes)) 

# Funções adicionais:
def baralha_saco(seed):
    """
    A função recebe uma seed, um inteiro positivo, que corresponde ao estado
    inicial do gerador pseudo-aleatório. É esperado que a função retorne
    uma lista baralhada com todas as letras no saco Scrabble.
    Args:
    seed --> int (positivo)
    Returns:
    lista_ordenada (é na verdade retornada como saco já baralhado) --> list                 
    """
    lista_ordenada = lista_letras_ordenada (saco_jogo)
    permuta_letras(lista_ordenada,seed)
    return lista_ordenada

def jogada_humano (tab,jog,vocab,pilha):
    """
    A função visa efetuar o turno completo de um jogador humano. Para tal, recebe o tabuleiro, 
    o jogador, o vocabulário e a pilha.Como tal tem de receber o input do jogador acerca da jogada 
    que pretende efetuar. O jogador pode passar, trocar ou jogar.
    Passar: retornar Falso;
    Trocar: se for válido, retornar True e modificar o jogador, retirando novas letras da pilha.
            Recebe 'T<seq. letras>', na qual a sequência tem 1 ou mais letras espaçadas entre si.
    Jogar: se for válido, ao receber 'J <linha> <coluna> <dir> <palavra>', retorna-se True e
            modifica-se o tabuleiro, atualiza-se o jogador (pontuação, letras novas retiradas da pilha).
            Se for a primeira jogada, a palavra a inserir deverá passar na casa central. Nas jogadas seguintes
            as casas a ocupar tem de ser padrões válidos e as palavras tem de estar no vocabulário.
    Args:
    tab --> list
    jog --> dict
    vocab --> dict
    pilha --> list
    Returns:
    Bool
    """
    nome_jogador = jogador_identidade(jog)

    while True:        
        opcao_jogada = input(f"Jogada {nome_jogador}: ").strip().split()
        if len(opcao_jogada)==0 or (opcao_jogada[0] != PASSAR and opcao_jogada[0] !=TROCAR and  opcao_jogada[0] !=JOGAR):   # garantir que as únicas opções válidas são: 'P'/'T'/'J'
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
                    if opcao_jogada[i] not in LETRAS:
                        valido = False
                        break
                    seq_letras += opcao_jogada[i]
                else:
                    valido = False
                    break      
            if valido == True:
                troca_resultado_final = troca_letras(jog, pilha,seq_letras)
                if troca_resultado_final:
                    return True
                else:
                    continue
            else:
                continue
    # Jogar    
        if opcao_jogada[0]== JOGAR:

            try:    #tentar convertê-lo para inteiro, se não for possível voltar a pedir um input
                linha = int(opcao_jogada[1])
                coluna= int(opcao_jogada[2])
            except ValueError:
                continue    
            direcao = opcao_jogada[3]
            palavra = opcao_jogada[4]
            # Validações dos inputs:
            if type(linha)!= int or linha<=0 or linha>TAMANHO_TABULEIRO: # garantir que a linha está nos limites do tabuleiro
                continue
            if type(coluna)!= int or coluna<=0 or coluna>TAMANHO_TABULEIRO:  # garantir que a coluna está nos limites do tabuleiro    
                continue
            letra_inicial = palavra[0]
            if letra_inicial not in vocab or palavra not in vocab[letra_inicial]:   # a letra inicial tem de ser uma chave
                continue
            if type(direcao)!=str or (direcao!='V' and direcao!='H'):    
                continue
            if valida_palavra(palavra)==False:   
                continue

            casa = cria_casa(linha,coluna)
            tamanho = len(palavra)
            if direcao=='H':
                if not casa[1]+(tamanho-1)<=TAMANHO_TABULEIRO:
                    continue    # se for inválido, passa à proxima iteração (pedindo novo input)
                padrao = obtem_padrao(tab,casa,(casa[0],casa[1]+tamanho-1))
            if direcao=='V':
                if not casa[0]+(tamanho-1)<=TAMANHO_TABULEIRO:
                    continue
                   # return jogada_humano (tab,jog,vocab,pilha)  # aqui não é válido
                padrao = obtem_padrao (tab,casa,(casa[0]+tamanho-1,casa[1]))

        # Implementação direta da joga_palavra:
            primeira_jogada = eh_tabuleiro_vazio(tab)
            tamanho = len(palavra)
            
            if not primeira_jogada and not padrao_tem_pelo_menos_1_letra(padrao):
                continue
            letras_disponíveis = jogador_letras(jog)
            letras_usadas = []
            if testa_palavra_padrao(vocab,palavra,padrao,letras_disponíveis):
                # Primeira jogada: (o jogador tem apenas 7 letras, logo se passar na casa_central(8,8) é impossível sair do tabuleiro)
                if primeira_jogada:
                    if tamanho < 2:
                        continue
                    if direcao =='H':
                        if 8 not in range(casa[1], casa[1] + tamanho) and casa[0] != 8:
                            continue
                    if direcao == 'V':
                        if 8 not in range(casa[0], casa[0] + tamanho) and casa[1] != 8:
                            continue
                    for i in range(tamanho):
                        letras_usadas += [palavra[i]]

                insere_palavra(tab,casa,direcao,palavra)
                pontos_palavra = obtem_pontos(vocab,palavra)
                soma_pontos(jog,pontos_palavra)
                
                num_letras_trocadas=0
                for i in range(len(palavra)):
                    if padrao[i]=='.':
                        usa_letra(jog,palavra[i])
                        num_letras_trocadas += 1

                # Ir buscar novas letras à pilha 
                for i in range(num_letras_trocadas):   
                    novas_letras = distribui_letras(jog,pilha,num_letras_trocadas)   # por cada letra descartada, retira uma nova letra da pilha
                    if novas_letras == True:
                        continue
                    else:
                        break
                return True  

def jogada_agente(tab,jog,vocab,pilha):
    """
    A função recebe o tabuleiro, o jogador, o vocabulário e a pilha (lista de letras) e pode:
     - Jogar: devolve True que a jogada for válida. Começa-se por gerar todos os padrões
     possíveis para o estado atual do tabuleiro e depois, seleciona-se 1 em cada N padrões ([::N]),
     consoante o nível do agente. De seguida, invoca-se a função procura_palavra_padrao
     para selecionar a melhor palavra, isto é, a 1ª palavra obtida com a maior pontuação.
     Por fim, tem de ser modificar o tabuleiro e atualizar o jogador, ao atualizar a sua 
     pontuação bem como retirar novas letras do final da pilha.
     - Trocar: se não puder jogar, tentará trocar. Para tal, é necessário haver pelo menos 7 
     letras no saco (pilha). Aí, retorna True, modifica o jogador ao retirar novas letras do fim
     da pilha, esta que também é modificada.
     - Passar: caso seja a 1ª jogada, ou haja a impossibilidade de jogar e trocar, o jogador passa.
     Args:
     tab --> list
     jog --> dict
     vocab --> dict
     pilha --> list
     Returns:
     bool
    """
    nome_jogador= jogador_identidade(jog)
    # verificar se é a primeira jogada:
    if  eh_tabuleiro_vazio(tab):
        print(f"Jogada {nome_jogador}: P")
        return False
    # Jogar:       
    # Escolha da palavra:
    # gerar todos os padrões possíveis:
    todos_padroes, todas_casas, todas_direcoes=gera_todos_padroes(tab,(len(jogador_letras(jog))))
    # seleção de padrões conforme o nível:
    if dificuldade_agente(jog)=='FACIL':
        N=100
    elif dificuldade_agente(jog)=='MEDIO':
        N=50
    elif dificuldade_agente(jog)=='DIFICIL': 
        N=10
    padroes_a_considerar = list(zip(todos_padroes[::N], todas_casas[::N], todas_direcoes[::N]))
    # procura da melhor palavra (inicialização de variáveis):
    min_pontos=0
    casa_inicial_palavra=None
    direcao_palavra=''
    palavra_a_inserir=''
    melhor_padrao=''

    for padrao,casa,direcao in padroes_a_considerar:
        tuplo_palavra_pontos=procura_palavra_padrao(vocab,padrao,jogador_letras(jog),min_pontos)
        if tuplo_palavra_pontos!= ('',0) and tuplo_palavra_pontos[1] > min_pontos:
            min_pontos= tuplo_palavra_pontos[1]
            palavra_a_inserir = tuplo_palavra_pontos[0]
            casa_inicial_palavra= casa
            direcao_palavra = direcao
            melhor_padrao = padrao
    if palavra_a_inserir!='':
        print(f"Jogada {nome_jogador}: J {obtem_lin(casa_inicial_palavra)} {obtem_col(casa_inicial_palavra)} {direcao_palavra} {palavra_a_inserir}")
        insere_palavra(tab,casa_inicial_palavra, direcao_palavra,palavra_a_inserir)

    # atualizar pontuação:
        soma_pontos(jog,min_pontos)
        # atualização das letras do jogador:
        for i in range(len(palavra_a_inserir)):
            if melhor_padrao[i]=='.':
                usa_letra(jog, palavra_a_inserir[i])
        # tirar novas letras da pilha para repor as letras usadas:
        num_letras_usadas=0
        for j in melhor_padrao:
            if j=='.':
                num_letras_usadas+=1
        distribui_letras(jog,pilha,num_letras_usadas)  
        return True      
    
    # Trocar (se não jogou, então pode trocar):
    if len(pilha)>= 7:
        seq_letras = jogador_letras(jog)

        letras= jogador_letras(jog)
        letras_ordenadas_jogador = lista_ordena_lista(list(letras))
        letras_ordenadas_espacadas=list(map(lambda x: x+' ',letras_ordenadas_jogador))
        res=''
        for i in range(len(letras_ordenadas_espacadas)):
            res += letras_ordenadas_espacadas[i]
        str_ordenada_espacada=res.rstrip()   
        print(f"Jogada {nome_jogador}: T {str_ordenada_espacada}")

        troca_resultado_final = troca_letras(jog, pilha,seq_letras)
        if troca_resultado_final:
            return True 
        
    # Passar:   (se o tabuleiro estiver vazio ou se não puder jogar ou trocar):
    print(f"Jogada {nome_jogador}: P")
    return False

def scrabble2 (jogadores, nome_fich, seed):
    """
    É a função principal que permite jogar o Scrabble, no seu todo. Este é um jogo de 
    2 a 4 jogadores.
    A função recebe um tuplo com o nome dos jogadores humanos (não-vazia), o nível dos jogadores
    agentes(começando por @, seguidos do nível) na ordem em que jogam, o nome do ficheiro com
    o vocabulário e um inteiro positivo(seed do gerador pseudo-aleatório).
    No final devolve um tuplo com a pontuação final obtida pelos jogadores. Ao início, baralha-se o 
    saco de letras e, distribui-se 7 letras pelos jogadores, na respetiva ordem.
    O jogo termina quando todos os jogadores passam consecutivamente ou quando um jogador ficar sem
    letras e o saco  se encontrar vazio.
    Args:
    jogadores --> tuple
    nome_fich --> file
    seed --> int (positivo)
    """
    #Validação de inputs:
    if (type(jogadores) != tuple or len(jogadores)<2 or len(jogadores)>4):  # garantir que o recebe os jogadores como um tuplo entre 2 e 4
        raise ValueError('scrabble2: argumentos inválidos')
    for jogador in jogadores:
        if type(jogador)!=str or jogador.strip()=='':   # o jogador é representado por uma string, não vazia, que contem o seu nome
            raise ValueError('scrabble2: argumentos inválidos')
    if type(nome_fich)!= str or nome_fich.strip()=='':  # garantir que o nome do ficheir é uma str (não vazia)
            raise ValueError('scrabble2: argumentos inválidos')    
    if (type(seed) != int or seed<=0):   # garantir que a seed é inteira e positiva
        raise ValueError ('scrabble2: argumentos inválidos')    
        
# Mensagem Incial:
    print('Bem-vindo ao SCRABBLE2.')
# Impressão do tabuleiro antes da jogada,baralhar e distribuir:
    saco_jogo = baralha_saco(seed)   # baralhar o saco
    tab = cria_tabuleiro()    # criar o tabuleiro
    # criar jogadores
    lista_jogadores=[]
    for jogador in jogadores:
        if jogador[0]=='@':
            jog = cria_agente(jogador[1:])
        else:
            jog = cria_humano(jogador) 
        lista_jogadores.append(jog)       
        distribui_letras(jog,saco_jogo,7)    # distribuir as 7 letras iniciais
    
    numero_jogadores= len(jogadores)
    fim_jogo = False    # flag de fim de jogo
    contador_passar = 0
    vocab = ficheiro_para_vocabulario(nome_fich)

    while not fim_jogo:
        for i in range(numero_jogadores):
            print (tabuleiro_para_str(tab))
            jog=lista_jogadores[i]
                # Apresentação dos jogadores:
            apresenta_jogadores(tuple(lista_jogadores))
            # jogada:
            if eh_humano(jog):
                retorno = jogada_humano(tab,jog,vocab,saco_jogo)
            else:
                retorno = jogada_agente(tab,jog,vocab,saco_jogo)    
            if retorno == False:    # se a jogada for passar
                contador_passar +=1
                if contador_passar == numero_jogadores:  # se todos os jogadores passarem consecutivamente
                    fim_jogo = True
                    break  
            else:
                contador_passar = 0        
            if len(jogador_letras(lista_jogadores[i]))==0 and saco_jogo=={}:  
                fim_jogo=True
                break   
# Impressão das pontuações:
    return((pontuacao_final(lista_jogadores)))
