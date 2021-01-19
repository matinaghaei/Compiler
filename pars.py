from ply import yacc
from lexer import Lexer
from codeGenerator import CodeGenerator


class Parser:
    tokens = Lexer().tokens

    def __init__(self):
        self.tempCount = 0
        self.quad = 0
        self.codeGenerator = CodeGenerator()
    
    # part 1 ----------------------------------------------------------------------------------------
    def p_program(self, p):
        "program : declist MAIN LRB RRB block"
        self.codeGenerator.generate_main_code(p, self.next_quad(), self.next_quad())

    def p_declist_empty(self, p):
        """
        declist :
        """
        self.codeGenerator.generate_declist_empty_code(p)
    
    def p_declist(self, p):
        """
        declist : declist dec
        """
        self.codeGenerator.generate_declist_code(p, self.next_quad())
        

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
        self.codeGenerator.generate_iddec_assign_code(p, self.next_quad(), self.next_quad(), self.next_quad())

    def p_iddec_array(self, p):
        """
        iddec : ID LSB exp RSB
        """
        self.codeGenerator.generate_iddec_array_code(p, self.new_temp())

    def p_idlist(self, p):
        """
        idlist : iddec
        """
        self.codeGenerator.generate_idlist_code(p)

    def p_idlist_comma(self, p):
        """
        idlist : idlist COMMA iddec
        """
        self.codeGenerator.generate_idlist_comma_code(p, self.next_quad())

    def p_exp_assign(self, p):
        "exp : ID ASSIGN exp"
        self.codeGenerator.generate_exp_assign_code(p, self.next_quad(), self.next_quad(), self.next_quad())

    def p_exp_arithmetic(self, p):
        """
        exp : exp SUM exp
        exp : exp SUB exp
        exp : exp DIV exp
        exp : exp MOD exp
        exp : exp MUL exp
        """
        self.codeGenerator.generate_exp_arithmetic_code(p, self.new_temp(), self.new_temp(), self.new_temp(), self.next_quad(), self.next_quad(), self.next_quad(), self.next_quad(), self.next_quad(), self.next_quad())

    def p_exp_const(self, p):
        "exp : const"
        self.codeGenerator.generate_exp_const_code(p)

    def p_exp_ID(self, p):
        "exp : ID"
        self.codeGenerator.generate_exp_ID_code(p)

    def p_exp_array(self, p):
        "exp : ID LSB exp RSB"
        self.codeGenerator.generate_exp_array_code(p, self.new_temp(), self.new_temp(), self.new_temp())

    def p_lvalue(self, p):
        "exp : ID LSB exp RSB ASSIGN exp"
        self.codeGenerator.generate_lvalue_code(p, self.new_temp(), self.new_temp(), self.new_temp(), self.next_quad(), self.next_quad(), self.next_quad())

    def p_exp_sub(self, p):
        "exp : SUB exp"
        self.codeGenerator.generate_exp_sub_code(p, self.new_temp(), self.new_temp(), self.next_quad(), self.next_quad(), self.next_quad())

    def p_exp_par(self, p):
        "exp : LRB exp RRB"
        self.codeGenerator.generate_exp_par_code(p)

    def p_const_arithmetic(self, p):
        """
        const : FLOATNUMBER
        const : INTEGERNUMBER
        """
        self.codeGenerator.generate_const_arithmetic_code(p)

    def p_block(self, p):
        """
        block : LCB stmtlist RCB
        """
        self.codeGenerator.generate_block_code(p)

    def p_stmtlist(self, p):
        """
        stmtlist : stmtlist stmt
        """
        self.codeGenerator.generate_stmtlist_code(p, self.next_quad())

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

    def p_stmt_if(self, p):
        "stmt : IF LRB exp RRB stmt elseiflist %prec IFREDUCE"
        self.codeGenerator.generate_stmt_if_code(p, self.next_quad(), self.next_quad(), self.next_quad(), self.next_quad(), self.next_quad())

    def p_stmt_while(self, p):
        "stmt : WHILE LRB exp RRB stmt"
        self.codeGenerator.generate_stmt_while_code(p, self.next_quad(), self.next_quad(), self.next_quad(), self.next_quad())

    def p_stmt_if_else(self, p):
        "stmt : IF LRB exp RRB stmt elseiflist ELSE stmt"
        self.codeGenerator.generate_stmt_if_else_code(p, self.next_quad(), self.next_quad(), self.next_quad(), self.next_quad(), self.next_quad(), self.next_quad(), self.next_quad())

    def p_stmt_for(self, p):
        "stmt : FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt"
        self.codeGenerator.generate_stmt_for_code(p, self.next_quad(), self.next_quad(), self.next_quad(), self.next_quad(), self.next_quad())

    def p_stmt_foreach(self, p):
        "stmt : FOR LRB ID IN ID RRB stmt"
        self.codeGenerator.generate_stmt_foreach_code(p, self.next_quad(), self.next_quad(), self.next_quad(), self.next_quad(), self.next_quad(), self.new_temp(), self.new_temp(), self.new_temp(), self.new_temp())

    def p_stmt_case(self, p):
        "stmt : ON LRB exp RRB LCB cases RCB SEMICOLON"
        self.codeGenerator.generate_stmt_case_code(p)

    def p_case(self, p):
        """
        case : WHERE const COLON stmtlist
        """
        self.codeGenerator.generate_case_code(p, self.next_quad(), self.next_quad(), self.next_quad())

    def p_cases(self, p):
        "cases : cases case"
        self.codeGenerator.generate_cases_code(p, self.next_quad(), self.next_quad())

    def p_cases_empty(self, p):
        "cases :"
        self.codeGenerator.generate_cases_empty_code(p)

    def p_elseiflist(self, p):
        """
        elseiflist : elseiflist ELSEIF LRB exp RRB stmt
        """
        self.codeGenerator.generate_elseiflist_code(p, self.next_quad(), self.next_quad(), self.next_quad(), self.next_quad(), self.next_quad())

    def p_elseiflist_empty(self, p):
        "elseiflist :"
        self.codeGenerator.generate_elseiflist_empty_code(p)

    def p_exp_relop(self, p):
        "exp : relopexp %prec EXP"
        self.codeGenerator.generate_exp_relop_code(p)

    def p_relopexp(self, p):
        """
        relopexp : exp GT exp
        relopexp : exp LT exp
        relopexp : exp NE exp
        relopexp : exp EQ exp
        relopexp : exp LE exp
        relopexp : exp GE exp
        """
        self.codeGenerator.generate_relopexp_code(p, self.next_quad(), self.next_quad())

    def p_relopexp_rel(self, p):
        """
        relopexp : relopexp GT exp
        relopexp : relopexp LT exp
        relopexp : relopexp NE exp
        relopexp : relopexp EQ exp
        relopexp : relopexp LE exp
        relopexp : relopexp GE exp
        """
        self.codeGenerator.generate_relopexp_rel_code(p, self.next_quad(), self.next_quad(), self.next_quad())

    def p_exp_and(self, p):
        "exp : exp AND exp"
        self.codeGenerator.generate_exp_and_code(p, self.next_quad(), self.next_quad(), self.next_quad(), self.next_quad(), self.next_quad())

    def p_exp_or(self, p):
        "exp : exp OR exp"
        self.codeGenerator.generate_exp_or_code(p, self.next_quad(), self.next_quad(), self.next_quad(), self.next_quad(), self.next_quad())

    def p_exp_not(self, p):
        "exp : NOT exp"
        self.codeGenerator.generate_exp_not_code(p, self.next_quad(), self.next_quad())

    def p_const(self, p):
        """
        const : TRUE
        const : FALSE
        """
        self.codeGenerator.generate_stmt_const_code(p, self.next_quad())

    # part 3 ----------------------------------------------------------------------------------------

    def p_paramdecs(self, p):
        """
        paramdecs : paramdecslist
        """
        self.codeGenerator.generate_paramdecs_code(p)

    def p_paramdecs_empty(self, p):
        """
        paramdecs :
        """
        self.codeGenerator.generate_paramdecs_empty_code(p)

    def p_paramdecslist(self, p):
        """
        paramdecslist : paramdec
        """
        self.codeGenerator.generate_paramdeclist_code(p)

    def p_paramdecslist_comma(self, p):
        """
        paramdecslist : paramdecslist COMMA paramdec
        """
        self.codeGenerator.generate_paramdeclist_comma_code(p)

    def p_paramdec(self, p):
        """
        paramdec : ID COLON type
        paramdec : ID LSB RSB COLON type
        """
        self.codeGenerator.generate_paramdec_code(p)

    def p_exp_fun(self, p):
        """
        exp : ID LRB RRB
        """
        self.codeGenerator.generate_exp_fun_code(p, self.new_temp(), self.new_temp(), self.next_quad(), self.next_quad())

    def p_exp_fun_explist(self, p):
        "exp : ID LRB explist RRB"
        self.codeGenerator.generate_exp_fun_explist_code(p, self.new_temp(), self.new_temp(), self.next_quad(), self.next_quad(), self.next_quad())

    def p_funcdec(self, p):
        """
        funcdec : FUNCTION ID LRB paramdecs RRB block
        """
        self.codeGenerator.generate_funcdec_code(p, self.next_quad(), self.next_quad(), self.next_quad(), self.new_temp())

    def p_funcdec_return(self, p):
        """
        funcdec : FUNCTION ID LRB paramdecs RRB COLON type block
        """
        self.codeGenerator.generate_funcdec_return_code(p, self.next_quad(), self.next_quad(), self.next_quad(), self.new_temp(), self.new_temp())

    def p_explist(self, p):
        """
        explist : exp
        """
        self.codeGenerator.generate_explist_code(p)

    def p_explist_comma(self, p):
        """
        explist : explist COMMA exp
        """
        self.codeGenerator.generate_explist_comma_code(p, self.next_quad())

    def p_dec_funcdec(self, p):
        """
        dec : funcdec
        """
        self.codeGenerator.generate_dec_fundec_code(p)

    def p_stmt_return(self, p):
        """
        stmt : RETURN exp SEMICOLON
        """
        self.codeGenerator.generate_stmt_return_code(p)

    precedence = (
        ('right', "ASSIGN"),
        ('left', "OR"),
        ('left', "AND"),
        ('left', "NOT"),
        ('left', 'EXP'),
        ('left', "GT", "LT", "NE", "EQ", "LE", "GE"),
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

    def next_quad(self):
        temp = 'L' + str(self.quad)
        self.quad += 1
        return temp

    def p_error (self, p):
        print ('>> Syntax error at', p.value)
        # raise Exception('Syntax error at', p.value)

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser
