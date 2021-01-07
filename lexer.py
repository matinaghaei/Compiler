from ply import lex


class Lexer:
    reserved = {
        'int' : 'INTEGER', 
        'bool':  'BOOLEAN',
        'float':'FLOAT',
        'fun':'FUNCTION',
        'print':'PRINT',
        'return': 'RETURN',
        'main': 'MAIN',
        'if' : 'IF',   
        'else' : 'ELSE',
        'elseif' : 'ELSEIF',
        'while' : 'WHILE',
        'on':'ON', 
        'where':'WHERE',
        'for':'FOR',
        'and' :'AND', 
        'or':'OR',
        'not':'NOT', 
        'in':'IN'
    }

    tokens = [
        'IF', 'WHILE', 'PRINT','LRB', 'RRB', 'LCB', 'RCB', 'INTEGER', 'SUM', 'SUB', 'MUL', 'DIV',
        'LT', 'GT', 'SEMICOLON', 'FLOAT', 'BOOLEAN', 'FUNCTION', 'TRUE', 'FALSE', 'RETURN', 'MAIN',
        'ELSE', 'ELSEIF', 'ON', 'WHERE', 'FOR', 'AND', 'OR', 'NOT', 'IN', 'ASSIGN', 'MOD', 'GE', 'LE', 
        'NE', 'LSB', 'RSB', 'COLON', 'COMMA', 'ERROR', 'INTEGERNUMBER','ID', 'FLOATNUMBER','EQ'
    ]

    # COLONS
    t_SEMICOLON = r';'
    # BRACKETS
    t_LRB = r'\('
    t_RRB = r'\)'
    t_LCB = r'\{'
    t_RCB = r'\}'
    # OPERATOR
    t_SUM = r'\+'
    t_SUB = r'\-'
    t_MUL = r'\*'
    t_DIV = r'\/'
    t_LT = r'\<'
    t_GT = r'\>'
    t_ASSIGN = r'='
    t_MOD = r'%'
    t_GE = r'\>='
    t_LE = r'\<='
    t_EQ = r'=='
    t_NE = r'!='
    t_LSB = r'\['
    t_RSB = r'\]'
    t_COLON = r':'
    t_COMMA = r','

    def t_ERROR(self, t):
        r"""[%\/\-\*\+]([ ]*[%\/\-\*\+])+
        |[0-9]+[A-Za-z_][A-Za-z0-9_]*
        |[0-9]*\.[0-9]+\.[0-9\.]*
        |For
        |ERROR
        |[0-9]{10}[0-9]*(.[0-9]+)?
        """
        return t



    def t_TRUE(self, t):
        r'True'
        return t

    def t_FALSE(self, t):
        r'False'
        return t

    def t_ID(self, t):
        r'[a-z_][A-Za-z0-9_]*'
        if t.value in self.reserved:
            t.type = self.reserved[ t.value ]
        return t

    def t_FLOATNUMBER(self, t):
        r'[0-9]{1,9}\.[0-9]+'
        real = float(t.value)
        t.value = str(real)
        return t

    def t_INTEGERNUMBER(self, t):
        r'[0-9]{1,9}'
        number = int(t.value)
        t.value = str(number)
        return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)



    t_ignore = '\n \t'

    def t_error(self, t):
        raise Exception('Error at', t.value)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        return self.lexer
