from nonTerminal import NonTerminal


class CodeGenerator:

    def __init__(self):
        pass

    def generate_main_code (self, p):
        p[0] = NonTerminal()
        p[0].code = p[1].code
        p[0].code += "main()" + p[5].code
        print(p[0].code)

    def generate_declist_empty_code (self, p):
        p[0] = NonTerminal()
        p[0].code = ""

    def generate_declist_code (self, p):
        p[0] = NonTerminal()
        p[0].code = p[1].code + p[2].code

    def generate_dec_vardec_code (self, p):
        p[0] = NonTerminal()
        p[0].code = p[1].code

    def generate_vardec_code (self, p):
        p[0] = NonTerminal()
        p[0].code = p[1].code

    def generate_iddec_ID_code (self, p):
        p[0] = NonTerminal()
        p[0].code = 'int ' + p[1] + ';\n'

    def generate_idlist_comma_code(self, p):
        p[0] = NonTerminal()
        p[0].code = p[1].code + p[3].code

    def generate_idlist_code(self, p):
        p[0] = NonTerminal()
        p[0].code = p[1].code

    def generate_iddec_array_code(self, p):
        p[0] = NonTerminal()
        p[0].code = "array[arr_p] =" + p[2].get_value() + ";\n" + "int" + p[1] + "= arr_p;\n" + "arr_p += " + p[2].get_value() + ";\n"

    def generate_iddec_assign_code(self, p):
        p[0] = NonTerminal()
        p[0].code = 'int ' + p[1] + p[2] + p[3].get_value() + ';\n'

    def generate_exp_assign_code(self, p):
        p[0] = NonTerminal()
        p[0].code = p[3].code + p[1] + p[2] + p[3].get_value()

    def generate_exp_arithmetic_code(self, p, temp):
        p[0] = NonTerminal()
        p[0].place = temp
        p[0].code = p[1].code + p[3].code + temp + '=' + str(p[1].get_value()) + p[2] + str(p[3].get_value()) + ";\n"

    def generate_exp_const_code(self, p):
        p[0] = NonTerminal()
        p[0].value = p[1].get_value()

    def generate_exp_ID_code(self, p):
        p[0] = NonTerminal()
        p[0].value = p[1]

    def generate_exp_array_code(self, p, temp):
        p[0] = NonTerminal()
        p[0].place = temp
        p[0].code = p[3].code + '\n' + temp + '=' + "array[" + p[1] + "+" + p[3].get_value() + "]"

    def generate_exp_sub_code(self, p, temp):
        p[0] = NonTerminal()
        p[0].place = temp
        p[0].code = p[2].code + '\n' + temp + '=' + p[1] + p[2].get_value()

    def generate_exp_par_code(self, p):
        p[0] = NonTerminal()
        p[0].code = p[2].code
        p[0].value = p[1] + p[2].get_value() + p[3]

    def generate_const_arithmetic_code(self, p):
        p[0] = NonTerminal()
        p[0].value = int(p[1])

    def generate_explist_code(self, p):
        p[0] = NonTerminal()
        p[0].value = p[1].get_value()

    def generate_explist_comma_code(self, p):
        p[0] = NonTerminal()
        p[0].value = p[1].get_value() + p[2] + p[3].get_value()

    def generate_block_code(self, p):
        p[0] = NonTerminal()
        p[0].code = '{\n' + p[2].code + '}\n'

    def generate_stmtlist_code(self, p):
        p[0] = NonTerminal()
        p[0].code = p[1].code + p[2].code

    def generate_stmtlist_empty_code(self, p):
        p[0] = NonTerminal()
        p[0].code = ""

    def generate_stmt_sem_code(self, p):
        p[0] = NonTerminal()
        p[0].code = p[1].code + p[2] + '\n'

    def generate_stmt_block_code(self, p):
        p[0] = NonTerminal()
        p[0].code = p[1].code

    def generate_stmt_var_code(self, p):
        p[0] = NonTerminal()
        p[0].code = p[1].code

    def generate_stmt_print_code(self, p):
        p[0] = NonTerminal()
        p[0].code = 'printf("%d", ' + p[3] + ');\n'



