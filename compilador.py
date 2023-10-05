#pip install tabulate
from collections import defaultdict
from tabulate import tabulate

class Lexema:
    #variáveis globais da classe
    ALFABETO = 'abcdefghijklmnopqrstuvwxyz'
    NUMERO = '0123456789'
    HEXDEC = '0123456789ABCDEF'
    RESERVADAS = ['programa', 'fim_programa', 'imprima', 'leia', 'se', 'senao', 'entao', 'enquanto']
    
     #construtor da classe lexema   
    def __init__(self, arquivo):
        self.estado = 0
        self.pos = -1
        with open(arquivo, 'r') as arq:
            self.texto = arq.read()
        self.char = None
        self.tabela_tokens = []
        self.proximo()
    #função para trocar o caractere atual pelo próximo       
    def proximo(self):
        self.pos += 1
        if self.pos < len(self.texto):
            self.char = self.texto[self.pos]
        else:
            self.char = None
    #função para criar a tabela de tokens
    def add_tokens(self):
            while self.pos < len(self.texto):
                self.get_token()
                self.proximo()
            return self.tabela_tokens
    #função para atribuir lexemas aos tokens
    def token (self):
        tokens = []
        if self.estado == 1:
            tokens.append('TK_SOMA')
        elif self.estado == 2:
            tokens.append('TK_SUB')
        elif self.estado == 3:
            tokens.append('TK_MULT')
        elif self.estado == 4:
            tokens.append('TK_DIV')
        elif self.estado == 5:
            tokens.append('TK_ABRE_PAR')
        elif self.estado == 6:
            tokens.append('TK_FECHA_PAR')
        elif self.estado == 7:
            tokens.append('TK_OU')
        elif self.estado == 8:
            tokens.append('TK_NAO')
        elif self.estado == 9:
            tokens.append('TK_E')
        elif self.estado == 12:
            tokens.append('TK_IGUAL')
        elif self.estado == 14:
            tokens.append('TK_ATRIB')
        elif self.estado == 15:
            tokens.append('TK_DIF')
        elif self.estado == 18:
            tokens.append('TK_MAIOR_IGUAL')
        elif self.estado == 19:
            tokens.append('TK_MAIOR')
        elif self.estado == 25:
            tokens.append('TK_MENOR')
        elif self.estado == 26:
            tokens.append('TK_MENOR_IGUAL')
        elif self.estado == 28 or self.estado == 30:
            tokens.append(('TK_VAR', self.lexema))
        elif self.estado == 39: 
            tokens.append(('TK_MOEDA', self.lexema))
        elif self.estado == 16 or self.estado == 40 or self.estado == 46 or self.estado == 52 or self.estado == 58 or self.estado == 59:
            tokens.append(('TK_NUMERO', self.lexema))
        elif self.estado == 51:
            tokens.append(('TK_CADEIA', self.lexema))
        elif self.estado == 53:
            tokens.append('TK_VIRGULA')
        elif self.estado == 61:
            if self.lexema == 'programa':
                tokens.append('TK_PROGRAMA')
            elif self.lexema == 'fim_programa':
                tokens.append('TK_FIM_PROGRAMA')
            elif self.lexema == 'imprima':
                tokens.append('TK_IMPRIMA')
            elif self.lexema == 'leia':
                tokens.append('TK_LEIA')
            elif self.lexema == 'se':
                tokens.append('TK_SE')
            elif self.lexema == 'entao':
                tokens.append('TK_ENTAO')
            elif self.lexema == 'senao':
                tokens.append('TK_SENAO')
            elif self.lexema == 'enquanto':
                tokens.append('TK_ENQUANTO')
        return str(tokens)
    #função principal para identificar os tokens    
    def get_token(self):
        self.lexema = ''
        while self.char != None:
            if self.estado == 0:
                if self.char == '+':
                    self.estado = 1
                    self.proximo()            
                elif self.char == '-':
                    self.estado = 2
                    self.proximo()
                elif self.char == '*':
                    self.estado = 3
                    self.proximo()
                elif self.char == '/':
                    self.estado = 4
                    self.proximo()
                elif self.char == '(':
                    self.estado = 5
                    self.proximo()
                elif self.char == ')':
                    self.estado = 6
                    self.proximo()
                elif self.char == '|':
                    self.estado = 7
                    self.proximo()
                elif self.char == '~':
                    self.estado = 8
                    self.proximo()
                elif self.char == '&':
                    self.estado = 9
                    self.proximo()
                elif self.char == ':':
                    self.estado = 10   
                    self.proximo()
                elif self.char == '!':
                    self.estado = 11
                    self.proximo()
                elif self.char == '=':
                    self.estado = 12
                    self.proximo()
                elif self.char == '>':
                    self.estado = 13
                    self.proximo()
                elif self.char == "'":
                    self.estado = 20
                    self.proximo()
                elif self.char == '#':
                    self.estado = 22
                    self.proximo()
                elif self.char == '<':
                    self.estado = 24
                    self.lexema += self.char
                    self.proximo()
                elif self.char in 'GHIJKLMNOPQRSTUVWXYZ':
                    self.estado = 31
                    self.lexema += self.char
                    self.proximo()
                elif self.char in 'ABCDEF':
                    self.estado = 32
                    self.lexema += self.char
                    self.proximo()
                elif self.char in Lexema.NUMERO:
                    self.estado = 33
                    self.lexema += self.char
                    self.proximo()
                elif self.char == '"':
                    self.estado = 50
                    self.proximo()
                elif self.char == ',':
                    self.estado = 53
                    self.proximo()
                elif self.char.islower():
                    self.estado = 60
                    self.lexema += self.char
                    self.proximo()  
                else:
                    self.proximo()

            #codição para '+'
            elif self.estado == 1:
                self.tabela_tokens.append(self.token())
                self.estado = 0
                self.lexema = ''

            #codição para '-'
            elif self.estado == 2:
                self.tabela_tokens.append(self.token())
                self.estado = 0
                self.lexema = ''
            #codição para '*'
            elif self.estado == 3:
                self.tabela_tokens.append(self.token())
                self.estado = 0
                self.lexema = ''
            #codição para '/'
            elif self.estado == 4:
                self.tabela_tokens.append(self.token())
                self.estado = 0
                self.lexema = ''
            #codição para '('
            elif self.estado == 5:
                self.tabela_tokens.append(self.token())
                self.estado = 0
                self.lexema = ''
            #codição para ')'
            elif self.estado == 6:
                self.tabela_tokens.append(self.token())
                self.estado = 0
                self.lexema = ''
            #codição para '|'
            elif self.estado == 7:
                self.tabela_tokens.append(self.token())
                self.estado = 0
                self.lexema = ''
            #codição para '~'
            elif self.estado == 8:
                self.tabela_tokens.append(self.token())
                self.estado = 0
                self.lexema = ''
            #codição para '&'
            elif self.estado == 9:
                self.tabela_tokens.append(self.token())
                self.estado = 0
                self.lexema = ''
            #codição para ':'
            elif self.estado == 10:
                if self.char == '=':
                    self.estado = 14
                    self.proximo()
                else:
                    self.estado = 0
            #codição para '!'     
            elif self.estado == 11:
                if self.char == '=':
                    self.estado = 15
                    self.proximo()
                else:
                    self.estado = 0
            #codição para '='
            elif self.estado == 12:
                self.tabela_tokens.append(self.token())
                self.estado = 0
                self.lexema = ''
            #codição para '>'    
            elif self.estado == 13:
                if self.char == '=':
                    self.estado = 18
                    self.proximo()
                else:
                    self.estado = 19
                    self.proximo()
            #codição para ':='    
            elif self.estado == 14:
                self.tabela_tokens.append(self.token())
                self.estado = 0
                self.lexema = ''
            #codição para '!='
            elif self.estado == 15:
                self.lexema += self.char
                self.tabela_tokens.append(self.token())
                self.estado = 0
                self.lexema = ''
            #codição para numero de até 1 dígito
            elif self.estado == 16:
                self.tabela_tokens.append(self.token())
                self.estado = 0
                self.lexema = ''
            #codição para '>='
            elif self.estado == 18:
                self.tabela_tokens.append(self.token())
                self.estado = 0
                self.lexema = ''
            #codição para '> outros'
            elif self.estado == 19:
                self.tabela_tokens.append(self.token())
                self.estado = 0
                self.lexema = ''

            #codições para comentário em bloco
            elif self.estado == 20:
                if self.char == "'":
                    self.estado = 54
                self.proximo()
            
            elif self.estado == 54:
                if self.char == "'":
                    self.estado = 21
                self.proximo()
            
            elif self.estado == 21:
                if self.char == "'":
                    self.estado = 55
                else:
                    self.estado = 0
                self.proximo()

            elif self.estado == 55:
                if self.char == "'":
                    self.estado = 56
                self.proximo()

            elif self.estado == 56:
                if self.char == "'":
                    self.estado = 57
                self.proximo()    
            #condições para comentário em linha
            elif self.estado == 22:
                if self.char == '\n':
                    self.estado = 0
                else:
                    self.estado = 22
                self.proximo()
            
            elif self.estado == 24:
                if self.char in Lexema.ALFABETO:
                    self.estado = 27
                    self.lexema += self.char
                elif self.char == '=':
                    self.estado = 26              
                else:
                    self.estado = 25
                self.proximo()
            #codição para '<
            elif self.estado == 25:
                self.tabela_tokens.append(self.token())
                self.estado = 0
                self.lexema = ''
            #codição para '<='
            elif self.estado == 26:
                self.tabela_tokens.append(self.token())
                self.estado = 0
                self.lexema = ''
            #codições para variaveis
            elif self.estado == 27:
                if self.char == '>':
                    self.estado = 28
                elif self.char in Lexema.ALFABETO or self.char in Lexema.NUMERO:
                    self.estado = 29
                self.lexema += self.char
                self.proximo()
            
            elif self.estado == 28:
                self.tabela_tokens.append(self.token())
                self.estado = 0
                self.lexema = ''
            
            elif self.estado == 29:
                if self.char == '>':
                    self.estado = 30
                elif self.char in Lexema.ALFABETO or self.char in Lexema.NUMERO:
                    self.estado = 29
                self.lexema += self.char
                self.proximo()

            elif self.estado == 30:
                self.tabela_tokens.append(self.token())
                self.estado = 0
                self.lexema = ''
            #comdições para moedas    
            elif self.estado == 31:
                if self.char == '$':
                    self.estado = 34
                else:
                    self.estado = 0
                self.lexema += self.char
                self.proximo()
            #condição para moedas ou hexadecimal
            elif self.estado == 32:
                if self.char == '$':
                    self.estado = 34
                elif self.char in Lexema.HEXDEC:
                    self.estado = 35
                elif self.char.islower():
                    self.estado = 0
                else:
                    self.estado = 16
                self.lexema += self.char
                self.proximo()

            elif self.estado == 33:
                if self.char in Lexema.HEXDEC:
                    self.estado = 35
                    self.lexema += self.char    
                else:
                    self.estado = 52
                self.proximo()     

            elif self.estado == 34:
                if self.char in Lexema.NUMERO:
                    self.estado = 36
                    self.lexema += self.char
                else:
                    self.estado = 0
                self.proximo()

            elif self.estado == 35:         
                if self.char in Lexema.HEXDEC:
                    self.estado = 35
                    self.lexema += self.char 
                elif self.char == '.':
                    self.lexema += self.char
                    self.estado = 41
                elif self.char == 'e':
                    self.estado = 42
                self.proximo()

            elif self.estado == 36:
                if self.char in Lexema.NUMERO:
                    self.estado = 36
                elif self.char == '.':
                    self.estado = 37
                self.lexema += self.char
                self.proximo()
            
            elif self.estado == 37:
                if self.char in Lexema.NUMERO:
                    self.estado = 38
                self.lexema += self.char
                self.proximo()
            
            elif self.estado == 38:
                if self.char in Lexema.NUMERO:
                    self.estado = 39
                    self.lexema += self.char
                    self.proximo()
                else:
                    self.lexema = ''
                    self.estado = 0
                
            elif self.estado == 39:
                self.tabela_tokens.append(self.token())
                self.estado = 0
                self.lexema = ''

            elif self.estado == 40:
                self.lexema += self.char
                self.tabela_tokens.append(self.token())
                self.estado = 0
                self.lexema = ''
                
            elif self.estado == 41:
                if self.char in Lexema.HEXDEC:
                    self.estado = 43
                else:
                    self.estado = 46
                self.lexema += self.char
                self.proximo()
            
            elif self.estado == 43:
                if self.char in Lexema.HEXDEC:
                    self.estado = 43
                    self.lexema += self.char
                elif self.char == 'e':
                    self.estado = 44
                    self.lexema += self.char
                else:
                    self.estado = 46
                self.proximo()

            elif self.estado == 44:
                if self.char in Lexema.HEXDEC:
                    self.estado = 47
                elif self.char == '-':
                    self.estado = 45
                self.lexema += self.char
                self.proximo()
            
            elif self.estado == 45:
                if self.char in Lexema.HEXDEC:
                    self.estado = 47
                self.lexema += self.char
                self.proximo()
            
            elif self.estado == 46:
                self.tabela_tokens.append(self.token())
                self.estado = 0
                self.lexema = ''

            elif self.estado == 47:
                if self.char in Lexema.HEXDEC:
                    self.estado = 47
                    self.proximo()
                else:
                    self.estado = 58
                self.lexema += self.char
                
            elif self.estado == 42:
                if self.char in Lexema.HEXDEC:
                    self.estado = 49
                elif self.char == '-':
                    self.estado = 48
                self.lexema += self.char
                self.proximo()
            
            elif self.estado == 48:
                if self.char in Lexema.HEXDEC:
                    self.estado = 49
                self.lexema += self.char
                self.proximo()
            
            elif self.estado == 49:
                if self.char in Lexema.HEXDEC:
                    self.estado = 49
                else:
                    self.estado = 59
                self.lexema += self.char
                self.proximo()
            #condições para cadeias
            elif self.estado == 50:
                if self.char == '"':
                    self.estado = 51
                elif self.char == '\n':
                    self.estado = 0
                    self.lexema = ''
                else:
                    self.estado = 50
                    self.lexema += self.char
                self.proximo()

            elif self.estado == 51:
                self.tabela_tokens.append(self.token())
                self.estado = 0
                self.lexema = ''
            #condições para numeros
            elif self.estado == 52:
                if self.char in Lexema.HEXDEC:
                    self.tabela_tokens.append(self.token())
                    self.estado = 0
                    self.lexema = ''
                elif self.char in Lexema.ALFABETO:
                    self.estado = 0   
            
            elif self.estado == 58:
                self.tabela_tokens.append(self.token())
                self.estado = 0
                self.lexema = ''

            elif self.estado == 59:   
                self.tabela_tokens.append(self.token())
                self.estado = 0
                self.lexema = '' 

            #condições especiais para alguns casos de letras e palavras reservadas
            elif self.estado == 60:
                if self.char in self.ALFABETO or self.char == '_':
                    self.estado = 60
                    self.lexema += self.char
                    self.proximo()
                else:
                    self.estado = 61

            elif self.estado == 61:
                if self.lexema in Lexema.RESERVADAS:
                    self.tabela_tokens.append(self.token())
                    self.estado = 0
                    self.lexema = ''
                else:
                    self.estado = 0
                    self.lexema = ''

            #caso caracter seja espaço, tabulação ou quebra de linha
            else:
                self.proximo()

        #condições para caso haja um último caractere = none 

        #condição para '+'
        if self.estado == 1:
            self.tabela_tokens.append(self.token())
            self.lexema = ''
        #condição para '-'
        elif self.estado == 2:
            self.tabela_tokens.append(self.token())
            self.lexema = ''
        #condição para '*'
        elif self.estado == 3:
            self.tabela_tokens.append(self.token())
            self.lexema = ''
        #condição para '/'
        elif self.estado == 4:
            self.tabela_tokens.append(self.token())
            self.lexema = ''
        #condição para '('
        elif self.estado == 5:
            self.tabela_tokens.append(self.token())
            self.lexema = ''
        #condição para ')'
        elif self.estado == 6:
            self.tabela_tokens.append(self.token())
            self.lexema = ''
        #condição para '|'        
        elif self.estado == 7:
            self.tabela_tokens.append(self.token())
            self.lexema = ''
        #condição para '~'
        elif self.estado == 8:
            self.tabela_tokens.append(self.token())
            self.lexema = ''
        #condição para '&'
        elif self.estado == 9:
            self.tabela_tokens.append(self.token())
            self.lexema = ''
        #condição para '>'
        elif self.estado == 13:
            self.estado = 19
            self.tabela_tokens.append(self.token())
        #condição para ':='
        elif self.estado == 14:
            self.tabela_tokens.append(self.token())
            self.lexema = ''
        #condição para '!='
        elif self.estado == 15:
            self.tabela_tokens.append(self.token())
            self.lexema = ''
        #codição para '>='
        elif self.estado == 18:
            self.tabela_tokens.append(self.token())
            self.lexema = ''
        #codição para numeros
        elif self.estado == 35:
            self.estado = 40
            self.tabela_tokens.append(self.token())
            self.lexema = ''
        #codição para numeros    
        elif self.estado == 43:
            self.estado = 46
            self.tabela_tokens.append(self.token())
            self.lexema = ''
            self.estado = 0
        #codição para outros
        elif self.estado == 60:
            self.estado = 61
            self.tabela_tokens.append(self.token())
            self.lexema = '' 

    #função para somar a ocorrência de cada token e o total de tokens presentes e imprimi-los de forma formatada
    def somatorio_tokens(self):
        cont = defaultdict(int)

        for item in self.tabela_tokens:
            token = item.split("'")[1]
            cont[token] += 1
            
        conta_tokens = dict(cont)

        saida_formatada = [["TOKEN", "USOS"]]

        for token, usos in sorted(conta_tokens.items(), key=lambda x: x[1], reverse=True):
            saida_formatada.append([token.strip("[]'"), usos])

        soma_total = sum(usos for token, usos in conta_tokens.items())

        linha_horizontal = ["-" * 13, "-" * 6]
        saida_formatada.append(linha_horizontal)
        saida_formatada.append(["TOTAL", soma_total])

        print(tabulate(saida_formatada, headers="firstrow", tablefmt="pretty"))
    #função para imprimir as linhas e colunas em que cada token aparece e seus respectivos lexemas, caso tenham
    def tokens_reconhecidos(self):
        saida_formatada = [["LINHA", "COLUNA", "TOKEN", "LEXEMA"]]

        linha_atual = 1
        coluna_atual = 1

        for item in self.tabela_tokens:
            if item == "'\\n'":
                linha_atual += 1
                coluna_atual = 1
                continue  # Pule a impressão do caractere '\n'

            token = item.split("'")[1] if "'" in item else item  # Extrai o token entre as aspas simples (se existirem)
            lexema = item.split(", ")[-1].rstrip("']").lstrip("('") if "('" in item else ""

            saida_formatada.append([linha_atual, coluna_atual, token, lexema])

            coluna_atual += len(item) + 1  # +1 para contar o espaço entre os tokens
        print(tabulate(saida_formatada, headers="firstrow", tablefmt="grid"))

#teste do funcionamento de cada arquivo
caminho = 'arquivos/ex1.cic'
teste = Lexema(caminho)
teste.add_tokens()
print('_________________________________________________________________________________________________________________________\n')
print('EXEMPLO 1')
print('Somatório de tokens reconhecimentos:')   
teste.somatorio_tokens()
print('\nLista de tokens reconhecidos:')
teste.tokens_reconhecidos()

caminho = 'arquivos/ex2.cic'
teste = Lexema(caminho)
teste.add_tokens()
print('________________________________________________________________________________________________________________________\n')
print('EXEMPLO 2')
print('Somatório de tokens reconhecimentos:')
teste.somatorio_tokens()
print('\nLista de tokens reconhecidos:')
teste.tokens_reconhecidos()

caminho = 'arquivos/ex4.cic'
teste = Lexema(caminho)
teste.add_tokens()
print('_______________________________________________________________________________________________________________________\n')
print('EXEMPLO 3')
print('Somatório de tokens reconhecimentos:')
teste.somatorio_tokens()
print('\nLista de tokens reconhecidos:')
teste.tokens_reconhecidos()