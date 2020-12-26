from ply import yacc
from lexer import Lexer
from codeGenerator import CodeGenerator


class Parser:
    tokens = Lexer().tokens

    def __init__(self):
        self.tempCount = 0
        self.codeGenerator = CodeGenerator()
    
    # part 1 ----------------------------------------------------------------------------------------
    def p_program(self, p):
        "program : declist MAIN LRB RRB block"
        self.codeGenerator.generate_main_code(p)
    

    def p_declist_empty(self, p):
        """
        declist :
        """
        self.codeGenerator.generate_declist_empty_code(p)
    
    def p_declist(self, p):
        """
        declist : declist dec
        """
        self.codeGenerator.generate_declist_code(p)
        

    def p_dec_vardec(self, p):
        """
        dec : vardec
        """
        self.codeGenerator.generate_dec_vardec_code(p)

    def p_vardec(self, p):
        """
        vardec : idlist COLON type SEMICOLON
        """
        self.codeGenerator.generate_vardec_code(p)

    def p_type(self, p):
        """
        type : INTEGER
        type : FLOAT
        type : BOOLEAN
        """
        pass

    def p_iddec_ID(self, p):
        """
        iddec : ID
        """
        self.codeGenerator.generate_iddec_ID_code(p)


    def p_iddec_assign(self, p):
        """
        iddec : ID ASSIGN exp
        """
        self.codeGenerator.generate_iddec_assign_code(p)

    def p_iddec_array(self, p):
        """
        iddec : ID LSB exp RSB
        """
        self.codeGenerator.generate_iddec_array_code(p)

    def p_idlist(self, p):
        """
        idlist : iddec
        """
        self.codeGenerator.generate_idlist_code(p)

    def p_idlist_comma(self, p):
        """
        idlist : idlist COMMA iddec
        """
        self.codeGenerator.generate_idlist_comma_code(p)

    def p_exp_assign(self, p):
        "exp : ID ASSIGN exp"
        self.codeGenerator.generate_exp_assign_code(p, self.new_temp())

    def p_exp_arithmetic(self, p):
        """
        exp : exp SUM exp
        exp : exp SUB exp
        exp : exp DIV exp
        exp : exp MOD exp
        exp : exp MUL exp
        """
        self.codeGenerator.generate_exp_arithmetic_code(p, self.new_temp())

    def p_exp_const(self, p):
        "exp : const"
        self.codeGenerator.generate_exp_const_code(p)

    def p_exp_ID(self, p):
        "exp : ID"
        self.codeGenerator.generate_exp_ID_code(p)

    def p_exp_array(self, p):
        "exp : ID LSB exp RSB"
        self.codeGenerator.generate_exp_array_code(p, self.new_temp())

    def p_lvalue(self, p):
        "exp : ID LSB exp RSB ASSIGN exp"
        self.codeGenerator.generate_lvalue_code(p, self.new_temp())

    def p_exp_sub(self, p):
        "exp : SUB exp"
        self.codeGenerator.generate_exp_sub_code(p, self.new_temp())

    def p_exp_par(self, p):
        "exp : LRB exp RRB"
        self.codeGenerator.generate_exp_par_code(p)

    def p_const_arithmetic(self, p):
        """
        const : FLOATNUMBER
        const : INTEGERNUMBER
        """
        self.codeGenerator.generate_const_arithmetic_code(p)


    def p_explist(self, p):
        """
        explist : exp
        """
        self.codeGenerator.generate_explist_code(p)

    def p_explist_comma(self, p):
        """
        explist : explist COMMA exp
        """
        self.codeGenerator.generate_explist_comma_code(p)

    def p_block(self, p):
        """
        block : LCB stmtlist RCB
        """
        self.codeGenerator.generate_block_code(p)

    def p_stmtlist(self, p):
        """
        stmtlist : stmtlist stmt
        """
        self.codeGenerator.generate_stmtlist_code(p)

    def p_stmtlist_empty(self, p):
        "stmtlist :"
        self.codeGenerator.generate_stmtlist_empty_code(p)

    def p_stmt_sem(self, p):
        """
        stmt : exp SEMICOLON
        """
        self.codeGenerator.generate_stmt_sem_code(p)

    def p_stmt_block(self, p):
        """
        stmt : block
        """
        self.codeGenerator.generate_stmt_block_code(p)

    def p_stmt_var(self, p):
        """
        stmt : vardec
        """
        self.codeGenerator.generate_stmt_var_code(p)

    def p_stmt_print(self, p):
        """
        stmt : PRINT LRB ID RRB SEMICOLON
        """
        self.codeGenerator.generate_stmt_print_code(p)

    # part 2 ----------------------------------------------------------------------------------------


    def p_dec_funcdec(self, p):
        """
        dec : funcdec
        """
        print("dec : vardec | funcdec")
    def p_funcdec(self, p):
        """
        funcdec : FUNCTION ID LRB paramdecs RRB COLON type block
        funcdec : FUNCTION ID LRB paramdecs RRB block
        """
        if len(p) == 9:
            print('FUNCTION ID LRB paramdecs RRB COLON type block')
        else:
            print('funcdec : FUNCTION ID LRB paramdecs RRB block')

    def p_paramdecs(self, p):
        """
        paramdecs : paramdecslist
        paramdecs :
        """
        if len(p) == 2:
            print('paramdecs : paramdecslist')
        else:
            print('paramdecs :')

    def p_paramdecslist(self, p):
        """
        paramdecslist : paramdec
        paramdecslist : paramdecslist COMMA paramdec
        """
        if len(p) == 2:
            print('paramdecslist : paramdec')
        else:
            print('paramdecslist : paramdecslist COMMA paramdec')

    def p_paramdec(self, p):
        """
        paramdec : ID COLON type
        paramdec : ID LSB RSB COLON type
        """
        if len(p) == 4:
            print('paramdec : ID COLON type')
        else:
            print('paramdec : ID LSB RSB COLON type')


    def p_case(self, p):
        """
        case : WHERE const COLON stmtlist
        """
        print("case : WHERE const COLON stmtlist")

    def p_cases(self, p):
        """
        cases : cases case
        cases :
        """
        if len(p) == 3:
            print('cases : cases case')
        else:
            print('cases :')

    def p_stmt(self, p):
        """
        stmt : RETURN exp SEMICOLON
        stmt : WHILE LRB exp RRB stmt
        stmt : ON LRB exp RRB LCB cases RCB SEMICOLON
        stmt : FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt
        stmt : FOR LRB ID IN ID RRB stmt
        stmt : IF LRB exp RRB stmt elseiflist %prec IFREDUCE
        stmt : IF LRB exp RRB stmt elseiflist ELSE stmt
        """
        print("stmt, len:",len(p))

    def p_elseiflist(self, p):
        """
        elseiflist : elseiflist ELSEIF LRB exp RRB stmt
        elseiflist :
        """
        if len(p) == 1:
            print('elseiflist :')
        else:
            print('elseiflist : elseiflist ELSEIF LRB exp RRB stmt')

    def p_exp(self, p):

        """
        exp : exp AND exp
        exp : exp OR exp
        exp : exp GT exp
        exp : exp LT exp
        exp : exp NE exp
        exp : exp EQ exp
        exp : exp LE exp
        exp : exp GE exp
        exp : ID LRB explist RRB
        exp : ID LRB RRB
        exp : NOT exp
        """
        print("exp , len:", len(p))

    def p_const(self, p):
        """
        const : TRUE
        const : FALSE
        """
        print("const : intnumber | floatnumber | True | False ")

    precedence = (

        ('left', "OR"),
        ('left', "AND"),
        ('left', "NOT"),
        ('left', "GT", "LT", "NE", "EQ", "LE", "GE"),
        ('right', "ASSIGN"),
        ('left', "MOD"),
        ('left', "SUM", "SUB"),
        ('left', "MUL", "DIV"),
        ('left', "IFREDUCE"),
        ('left', "ELSE", "ELSEIF"),
    )

    def new_temp(self):
        temp = "T" + str(self.tempCount)
        self.tempCount += 1
        return temp

    def p_error (self, p):
        print ('>> Syntax error at', p.value)
        # raise Exception('Syntax error at', p.value)

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser
