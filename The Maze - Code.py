# Projeto de Fundamentos da Programacao
# Sofia da Silva Morgado, nr ist195675

########################################
# REPRESENTACAO DO LABIRINTO E UNIDADES#
########################################

#### FUNCAO 1

def eh_labirinto(arg_uni):
    if not isinstance(arg_uni, tuple): #verificou se era um tuplo
        return False
    if len(arg_uni) <3: #verifico colunas >=3
        return False
    for i in range(len(arg_uni)):
        if not isinstance(arg_uni[i],tuple): #verifico se so tem subtplos
            return False
        if len(arg_uni[i])<3: #verifico se as linhas >=3
            return False
        if len(arg_uni[0]) != len(arg_uni[i]):
            return False
        for j in range(len(arg_uni[i])): #verificar se e 0 ou 1 
            if not isinstance(arg_uni[i][j], int):
                return False
            if arg_uni[i][j]!=0 and arg_uni[i][j]!=1:
                return False
            for j in arg_uni[0]: #primeiro subtuplo apenas 1
                if j != 1:
                    return False  
            for j in arg_uni[-1]: #ultimo subtuplo apenas 1
                if j != 1:
                    return False
        for t in range(len(arg_uni[1:])):
            if arg_uni[i][0] != 1 or arg_uni[i][-1] != 1:
                return False
            
    else:
        return True
    
    
### FUNCAO 2

def eh_posicao(arg_uni):
    if not isinstance(arg_uni, tuple): #verificou se era um tuplo
        return False
    if len(arg_uni) != 2: #tem apenas 2 valores
        return False
    for i in range(len(arg_uni)):
        if not isinstance(arg_uni[i],int): #valores inteiros
            return False
        if arg_uni[i] <0: #valores positivos
            return False
    else:
        return True
 
 
 ### FUNCAO 3   
 
def eh_conj_posicoes (arg_uni):
    if not isinstance(arg_uni, tuple):
        return False    
    elif arg_uni == ():
        return True  
    else:
        for i in range(1, len(arg_uni)):
            if not eh_posicao(arg_uni[i]): 
                return False   
            elif arg_uni[0] == arg_uni[i]:
                return False
  
        return eh_conj_posicoes(arg_uni[1:])
    
### FUNCAO 4
def tamanho_labirinto (lab):
    tup = ()
    if not eh_labirinto(lab):
        raise ValueError ('tamanho_labirinto: argumento invalido')
    else:
        x = len(lab)
        for i in range(len(lab)):
            y = len(lab[i])
        return tuple((x, y))


### FUNCAO 5
    
def eh_mapa_valido (labirinto, conjuntop):
    if not eh_labirinto(labirinto): #labirinto e valido
        raise ValueError('eh_mapa_valido: algum dos argumentos e invalido')
    
    if not eh_conj_posicoes(conjuntop): #conjunto de posicoes sao validas
        raise ValueError('eh_mapa_valido: algum dos argumentos e invalido')
    
    colunas, linhas = tamanho_labirinto(labirinto)
    
    for unidade in conjuntop:
        x, y = unidade
        if x >= colunas or y >= linhas:
            return False
        elif labirinto[x][y] == 1:
            return False
    
    return True
        
    
### FUNCAO 6
def eh_posicao_livre (labirinto, unidades, posicao):
    colunas = len(labirinto)
    for i in range(len(labirinto)):
        linhas = len(labirinto[i])
        
    if not eh_labirinto(labirinto): #labirinto e valido
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')
    
    if not eh_conj_posicoes(unidades): #conjunto de posicoes sao validas
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')
    
    if not eh_mapa_valido (labirinto, unidades): #labirinto e unidades validas
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')
    
    if not eh_posicao(posicao) : #posicao valida
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')
    
    for i in range(len(unidades)): #posicao != unidades
        if posicao == unidades[i]:
            return False
    for i in range(len(posicao)): #posicao encontra-se dentro do lab 
        x = posicao[0] #coordenada x
        y = posicao[1] #coordenana y
        if x > (colunas-2) or x ==0:
            return False
        if y > (linhas-2) or y==0:
            return False  
        
    for i in range(1, len(labirinto)-1): #posicoes nao sao paredes
        for j in range(1, len(labirinto[i])-1): #acedemos ao subtuplo
            for x in range(len(posicao)):
                if labirinto[i][j] == 1 and i == posicao[0] and j == posicao[1]:
                    return False    
    else:
        return True

### FUNCAO 7
def posicoes_adjacentes (posicao):
    tup = ()
    if not eh_posicao(posicao):
        raise ValueError('posicoes_adjacentes: argumento invalido')
    for i in range(len(posicao)):
        x = posicao[0]
        y = posicao[1]
        acima = (x,y-1)
        direita = (x-1,y)
        esquerda = (x+1,y)
        baixo = (x,y+1)
        if x == 0 and y == 0:
            return tuple (((esquerda),(baixo)))
        elif x == 0:
            return tuple(((acima),(esquerda),(baixo)))
        elif y == 0:
            return tuple(((direita),(esquerda),(baixo)))
        else:
            return tuple(((acima),(direita),(esquerda),(baixo))) 

### FUNCAO 8
def mapa_str(labirinto, unidades):
    mapa = ' '
    if not eh_labirinto(labirinto): #labirinto e valido
        raise ValueError('mapa_str: algum dos argumentos e invalido')
    if not eh_conj_posicoes(unidades): #conjunto de posicoes sao validas
        raise ValueError('mapa_str: algum dos argumentos e invalido')
    if not eh_mapa_valido (labirinto, unidades): #labirinto e unidades validas
        raise ValueError ('mapa_str: algum dos argumentos e invalido')
    else:
        nr = len(unidades)
        
        mapa = []
        labirinto1 = list(labirinto)
        f = False
        for i in range(len(labirinto1[0])):
            for j in range(len(labirinto1)):
                for c in range(len(unidades)):
                    if (unidades[c][0] == j) and (unidades[c][1]) == i:
                        f = True
                        mapa += 'O'                
                if labirinto1[j][i] == 0 and f == False:
                    mapa += ['.']
                if labirinto1[j][i] == 1 and f == False:
                    mapa += ['#']
                f = False
            mapa += ['\n']
        mapa = ''.join(mapa)
        
        return mapa[:-1]
        
########################################
#        FUNCOES DO MOVIMENTO          #
########################################

### FUNCAO M1
def obter_objetivos(labirinto, unidades, uniuser):
    unialvo= ()
    tupadj = ()
    tupadj3 = ()
    
    if not eh_labirinto(labirinto): #labirinto e valido
        raise ValueError('obter_objetivos: algum dos argumentos e invalido')
    if not eh_conj_posicoes(unidades): #conjunto de posicoes sao validas
        raise ValueError('obter_objetivos: algum dos argumentos e invalido')
    if not eh_mapa_valido (labirinto, unidades): #lab e unidades validas
        raise ValueError ('obter_objetivos: algum dos argumentos e invalido')
    if not eh_posicao(uniuser):#unidadeuser validas
        raise ValueError ('obter_objetivos: algum dos argumentos e invalido')
    if uniuser not in unidades:#unidadeuser e uma das unidades
        raise ValueError ('obter_objetivos: algum dos argumentos e invalido')
    
    else:
        for i in range(len(unidades)):
            if unidades[i] != uniuser:
                unialvo = unialvo + (unidades[i],)
                for el in range(len(unialvo)):
                    tupadj = tupadj+ (posicoes_adjacentes (unialvo[el],))
        tupadj2 = tuple(dict.fromkeys(tupadj))
        for i in range(len(tupadj2)):
            if eh_posicao_livre (labirinto, unidades, tupadj2[i]):
                tupadj3 = tupadj3 + (tupadj2[i],)            
        return tupadj3

### FUNCAO M2

def obter_caminho(labirinto, unidades, uniuser):
    if not eh_labirinto(labirinto): #labirinto e valido
        raise ValueError('obter_caminho: algum dos argumentos e invalido')
    if not eh_conj_posicoes(unidades): #conjunto de posicoes sao validas
        raise ValueError('obter_caminho: algum dos argumentos e invalido')
    if not eh_mapa_valido (labirinto, unidades): #lab e unidades validas
        raise ValueError ('obter_caminho: algum dos argumentos e invalido')
    if not eh_posicao(uniuser) : #unidadeuser validas
        raise ValueError ('obter_caminho: algum dos argumentos e invalido')
    if uniuser not in unidades:#unidadeuser e uma das unidades
        raise ValueError ('obter_caminho: algum dos argumentos e invalido')
       
    tupalvos = obter_objetivos(labirinto, unidades, uniuser)
    posi_atual = uniuser
    posi_visitadas = ()
    caminho = ()
    lista_exp = ((posi_atual, caminho),)
    res = () 
    
    while lista_exp != ():
        posi_atual = lista_exp[0][0]
        caminho_atual = lista_exp[0][1]
        lista_exp = lista_exp[1:]
        if posi_atual not in posi_visitadas:
            posi_visitadas += (posi_atual, )
            caminho_atual += (posi_atual, )
            if posi_atual in tupalvos:
                res = caminho_atual
                break
            else:
                for pos_adj in posicoes_adjacentes(posi_atual):
                    if eh_posicao_livre(labirinto, unidades, pos_adj):
                        lista_exp += ((pos_adj, caminho_atual), )   
    return res

### FUNCAO M3
def mover_unidade (labirinto, unidades, uniuser):
    if not eh_labirinto(labirinto): #labirinto e valido
        raise ValueError('mover_unidade: algum dos argumentos e invalido')
    if not eh_conj_posicoes(unidades): #conjunto de posicoes sao validas
        raise ValueError('mover_unidade: algum dos argumentos e invalido')
    if not eh_mapa_valido (labirinto, unidades): #lab e unidades validas
        raise ValueError ('mover_unidade: algum dos argumentos e invalido')
    if not eh_posicao(uniuser):#unidadeuser validas
        raise ValueError ('mover_unidade: algum dos argumentos e invalido')
    if uniuser not in unidades: #unidadeuser e uma das unidades
        raise ValueError ('mover_unidade: algum dos argumentos e invalido')
    
    for adjacente in posicoes_adjacentes(uniuser):
        if adjacente in unidades:
            return unidades
    
    caminho = obter_caminho(labirinto, unidades, uniuser)
    tupalvos = obter_objetivos(labirinto, unidades, uniuser)
     
    unidades = list(unidades)
    passo = caminho[1]
    for i in range(len(unidades)):
        if uniuser == unidades[i]:
            unidades[i] = passo
    return tuple(unidades)