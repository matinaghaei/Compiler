from nonTerminal import NonTerminal, LogicTerminal, StatementTerminal


class CodeGenerator:

    def __init__(self):
        self.variables = []

    # part 1 ----------------------------------------------------------------------------------------

    def generate_main_code (self, p):
        p[0] = NonTerminal()
        p[0].code = p[1].code
        p[0].code += "main()" + p[5].code
        print(p[0].code)

    def generate_declist_empty_code (self, p):
        p[0] = NonTerminal()

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
        p[0].code = "int " + p[1] + "= arr_p;\n" + "arr_p += " + p[3].get_value() + ";\n"

    def generate_iddec_assign_code(self, p):
        p[0] = NonTerminal()
        p[0].code += p[3].code
        p[0].code += 'int ' + p[1] + p[2] + p[3].get_value() + ';\n'

    def generate_exp_assign_code(self, p, temp):
        p[0] = NonTerminal()
        p[0].place = temp
        p[0].code = p[3].code + p[1] + p[2] + p[3].get_value() + ';\n' + 'int ' + temp + '=' + p[1] + ';\n'

    def generate_lvalue_code(self, p, temp, temp2):
        p[0] = NonTerminal()
        p[0].place = temp
        p[0].code = 'int ' + temp2 + ' = ' + p[1] + " + " + p[3].get_value() + ';\n' + p[3].code + p[6].code + "array[" + temp2 + "] = " + p[6].get_value() + ';\n' + 'int ' + temp + ' = ' + "array[" + temp2 + "];\n"

    def generate_exp_arithmetic_code(self, p, temp):
        p[0] = NonTerminal()
        p[0].place = temp
        p[0].code = p[1].code + p[3].code + 'int ' + temp + '=' + p[1].get_value() + p[2] + p[3].get_value() + ";\n"

    def generate_exp_const_code(self, p):
        p[0] = NonTerminal()
        p[0].value = p[1].get_value()

    def generate_exp_ID_code(self, p):
        p[0] = NonTerminal()
        p[0].value = p[1]

    def generate_exp_array_code(self, p, temp, temp2):
        p[0] = NonTerminal()
        p[0].place = temp
        p[0].code = p[3].code + 'int ' + temp2 + ' = ' + p[1] + "+" + p[3].get_value() + ';\n' + 'int ' + temp + '=' + "array[" + p[1] + "+" + p[3].get_value() + "];\n"

    def generate_exp_sub_code(self, p, temp):
        p[0] = NonTerminal()
        p[0].place = temp
        p[0].code = p[2].code + '\n' + 'int ' + temp + '=' + p[1] + p[2].get_value()

    def generate_exp_par_code(self, p):
        p[0] = NonTerminal()
        p[0].code = p[2].code
        p[0].value = p[1] + p[2].get_value() + p[3]

    def generate_const_arithmetic_code(self, p):
        p[0] = NonTerminal()
        p[0].value = p[1]

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
        p[0] = StatementTerminal()
        p[0].code = p[1].code + p[2].code

    def generate_stmtlist_empty_code(self, p):
        p[0] = StatementTerminal()
        p[0].code = ""

    def generate_stmt_sem_code(self, p):
        p[0] = StatementTerminal()
        p[0].code = p[1].code + '\n'

    def generate_stmt_block_code(self, p):
        p[0] = StatementTerminal()
        p[0].code = p[1].code

    def generate_stmt_var_code(self, p):
        p[0] = StatementTerminal()
        p[0].code = p[1].code

    def generate_stmt_print_code(self, p):
        p[0] = StatementTerminal()
        p[0].code = 'printf("%d\\n", ' + p[3] + ');\n'

    # part 2 ----------------------------------------------------------------------------------------

    def generate_stmt_const_code(self, p, q):
        p[0] = StatementTerminal()
        p[0].address = q
        if p[1] == 'TRUE':
            p[0].value = 1
            p[0].true_list = [q]
        else:
            p[0].value = 0
            p[0].false_list = [q]
        p[0].code = q + ": goto -;\n"

    def generate_exp_or_code(self, p):
        p[0] = LogicTerminal()
        p[0].address = p[1].address
        p[1].false_list_back_patch(p[3].address)
        p[0].code = p[1].code + p[3].code
        p[0].true_list = p[1].true_list + p[3].true_list
        p[0].false_list = p[3].false_list

    def generate_exp_and_code(self, p):
        p[0] = LogicTerminal()
        p[0].address = p[1].address
        p[1].true_list_back_patch(p[3].address)
        p[0].code = p[1].code + p[3].code
        p[0].false_list = p[1]
        p[0].false_list = p[1].false_list + p[3].false_list
        p[0].true_list = p[3].true_list

    def generate_exp_not_code(self, p):
        p[0] = LogicTerminal()
        p[0].address = p[2].address
        p[0].code = p[2].code
        p[0].true_list = p[2].false_list
        p[0].false_list = p[2].true_list

    def generate_exp_code(self, p, q1, q2):
        p[0] = LogicTerminal()
        p[0].address = q1
        p[0].code += p[1].code + p[3].code
        p[0].code += q1 + ": if (" + p[1].get_value() + ' ' + p[2] + ' ' + p[3].get_value() + ") goto -;\n"
        p[0].code += q2 + ": goto -;\n"
        p[0].true_list = [q1]
        p[0].false_list = [q2]

    def generate_elseiflist_empty_code(self, p):
        p[0] = LogicTerminal()

    def generate_elseiflist_code(self, p, q):
        p[0] = LogicTerminal()
        p[4].true_list_back_patch(q)
        p[0].code = p[1].code + p[4].code + q + ": " + p[6].code
        p[0].true_list = p[1].true_list + p[6].next_list
        p[0].false_list = p[1].false_list + p[4].false_list

    def generate_stmt_if_code(self, p, q1, q2):
        p[0] = StatementTerminal()
        p[3].true_list_back_patch(q1)
        p[3].false_list_back_patch(q2)
        p[0].code = p[3].code + q1 + ": " + p[5].code + q2 + ": " + p[6].code
        p[0].next_list = p[5].next_list + p[6].false_list + p[6].true_list


    # part 3 ----------------------------------------------------------------------------------------
