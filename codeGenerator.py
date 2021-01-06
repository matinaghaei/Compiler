from nonTerminal import NonTerminal, LogicTerminal, StatementTerminal


class CodeGenerator:

    def __init__(self):
        self.variables = []

    # part 1 ----------------------------------------------------------------------------------------

    def generate_main_code (self, p):
        p[0] = NonTerminal()
        p[0].code = "#include <stdio.h>\nint array[10000]; \nint arr_p = 0;\n" + p[1].code + "main()\n{\n" + p[5].code + "}"
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
        p[0].code = p[3].code + p[1] + p[2] + p[3].get_value() + ';\n'

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
        p[0].code = p[2].code + 'int ' + temp + '=' + p[1] + p[2].get_value() + ';\n'

    def generate_exp_par_code(self, p):
        p[0] = LogicTerminal()
        p[0] = p[2]
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
        p[0] = StatementTerminal()
        p[0] = p[2]

    def generate_stmtlist_code(self, p, q):
        p[0] = StatementTerminal()
        if p[2].address:
            q = p[2].address
        if p[1].code:
            p[0].address = p[1].address
        else:
            p[0].address = q
        p[1].next_list_back_patch(q)
        if p[2].address:
            p[0].code = p[1].code + p[2].code
        else:
            p[0].code = p[1].code + q + ": " + p[2].code
        p[0].next_list = p[2].next_list

    def generate_stmtlist_empty_code(self, p):
        p[0] = StatementTerminal()
        p[0].code = ""

    def generate_stmt_sem_code(self, p):
        p[0] = StatementTerminal()
        p[0].code = p[1].code

    def generate_stmt_block_code(self, p):
        p[0] = p[1]

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

    def generate_exp_relop_code(self, p):
        p[0] = p[1]

    def generate_relopexp_code(self, p, q1, q2):
        p[0] = LogicTerminal()
        p[0].address = q1
        p[0].code += p[1].code + p[3].code
        p[0].code += q1 + ": if (" + p[1].get_value() + ' ' + p[2] + ' ' + p[3].get_value() + ") goto -;\n"
        p[0].code += q2 + ": goto -;\n"
        p[0].true_list = [q1]
        p[0].false_list = [q2]
        p[0].right_most_exp = p[3]

    def generate_relopexp_rel_code(self, p, q1, q2):
        temp_terminal = LogicTerminal()
        temp_terminal.address = q1
        temp_terminal.code = p[1].right_most_exp.code + p[3].code
        temp_terminal.code += q1 + ": if (" + p[1].right_most_exp.get_value() + ' ' + p[2] + ' ' + p[3].get_value() + ") goto -;\n"
        temp_terminal.code += q2 + ": goto -;\n"
        temp_terminal.true_list = [q1]
        temp_terminal.false_list = [q2]

        p[0] = LogicTerminal()
        p[0].address = p[1].address
        p[1].true_list_back_patch(temp_terminal.address)
        p[0].code = p[1].code + temp_terminal.code
        p[0].false_list = p[1]
        p[0].false_list = p[1].false_list + temp_terminal.false_list
        p[0].true_list = temp_terminal.true_list
        p[0].right_most_exp = p[3]

    def generate_elseiflist_empty_code(self, p):
        p[0] = LogicTerminal()

    def generate_elseiflist_code(self, p, q1, q2, q3):
        p[0] = LogicTerminal()
        if p[4].address:
            q2 = p[4].address
        p[1].false_list_back_patch(q2)
        if p[1].code:
            p[0].address = p[1].address
            p[0].code = p[1].code + q1 + ": goto -;\n"
        else:
            p[0].address = p[4].address
            p[0].code = ""
        if p[6].address:
            q3 = p[6].address
        p[4].true_list_back_patch(q3)
        if p[4].address:
            p[0].code += p[4].code
        else:
            p[0].code += q2 + ": goto -;\n" + p[4].code
        if p[6].address:
            p[0].code += p[6].code
        else:
            p[0].code += q3 + ": " + p[6].code
        p[0].true_list = p[1].true_list + p[6].next_list + [q1]
        p[0].false_list = p[1].false_list + p[4].false_list

    def generate_stmt_if_code(self, p, q1, q2, q3):
        p[0] = StatementTerminal()
        p[0].address = p[3].address
        if p[5].address:
            q1 = p[5].address
        p[3].true_list_back_patch(q1)
        if p[6].code:
            if p[6].address:
                q2 = p[6].address
            p[3].false_list_back_patch(q2)
            if p[5].address:
                p[0].code += p[3].code + p[5].code + q3 + ": goto -;\n"
            else:
                p[0].code += p[3].code + q1 + ": " + p[5].code + q3 + ": goto -;\n"
            if p[6].address:
                p[0].code += p[6].code
            else:
                p[0].code += q2 + ": " + p[6].code
            p[0].next_list = p[5].next_list + p[6].false_list + p[6].true_list + [q3]
        else:
            p[0].code = p[3].code
            p[0].next_list = p[3].false_list + p[5].next_list
            if p[5].address:
                p[0].code += p[5].code
            else:
                p[0].code += q1 + ": " + p[5].code

    def generate_stmt_if_else_code(self, p, q1, q2, q3, q4, q5):
        p[0] = StatementTerminal()
        p[0].address = p[3].address
        if p[5].address:
            q1 = p[5].address
        p[3].true_list_back_patch(q1)
        if p[8].address:
            q5 = p[8].address
        p[6].false_list_back_patch(q5)
        if p[6].code:
            if p[6].address:
                q2 = p[6].address
            p[3].false_list_back_patch(q2)
            if p[5].address:
                p[0].code += p[3].code + p[5].code + q3 + ": goto -;\n"
            else:
                p[0].code += p[3].code + q1 + ": " + p[5].code + q3 + ": goto -;\n"
            if p[6].address:
                p[0].code += p[6].code
            else:
                p[0].code += q2 + ": " + p[6].code
            p[0].next_list = p[5].next_list + p[6].false_list + p[6].true_list + [q3, q4]
        else:
            p[0].code = p[3].code
            p[0].next_list = p[3].false_list + p[5].next_list + [q4]
            if p[5].address:
                p[0].code += p[5].code
            else:
                p[0].code += q1 + ": " + p[5].code
        if p[8].address:
            p[0].code += q4 + ": goto -;\n" + p[8].code
        else:
            p[0].code += q4 + ": goto -;\n" + q5 + ": " + p[8].code

    def generate_stmt_while_code(self, p, q1, q2):
        p[0] = StatementTerminal()
        if p[3].address:
            q1 = p[3].address
        p[0].address = q1
        if p[5].address:
            q2 = p[5].address
        p[5].next_list_back_patch(q1)
        p[3].true_list_back_patch(q2)
        if p[3].address:
            p[0].code = p[3].code
        else:
            p[0].code = q1 + ": " + p[3].code
        if p[5].address:
            p[0].code += p[5].code
        else:
            p[0].code += q2 + ": " + p[5].code
        p[0].code += "goto " + q1 + ";\n"
        p[0].next_list = p[3].false_list




    # part 3 ----------------------------------------------------------------------------------------
