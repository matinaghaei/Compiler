from nonTerminal import NonTerminal, LogicTerminal, StatementTerminal


class CodeGenerator:

    def __init__(self):
        self.variables = ""
        self.function_dict = {}

    # part 1 ----------------------------------------------------------------------------------------

    def generate_main_code(self, p, q1, q2):
        p[0] = NonTerminal()
        p[0].code = """#include <stdio.h>
#include <setjmp.h>

union jmp_buffer_union
{
    jmp_buf env_in_buf;
    struct {
        int env[64];	
    }env_in_int;
}env;

int arr[(int)1e6];
int arr_p = 0;
int stack_p = (int)1e6 - 1;
int val, index;

#define forward_jmp(position)								\\
    val = 0;												\\
    val=setjmp(env.env_in_buf); 							\\
    if(!val)			 									\\
        for(index = 0;index < 64;index++)								\\
            arr[position + index] = env.env_in_int.env[index]

#define back_jmp(position) 									\\
    for(index = 0;index < 64;index++)									\\
        env.env_in_int.env[index] = arr[position + index];		\\
    longjmp(env.env_in_buf, 1)

"""
        if p[5].address:
            q1 = p[5].address
        p[1].next_list_back_patch(q1)
        p[5].next_list_back_patch(q2)
        if p[5].address:
            p[0].code += self.variables + "\nmain()\n{\n" + p[1].code + p[5].code + q2 + ": return 0;\n}"
        else:
            p[0].code += self.variables + "\nmain()\n{\n" + p[1].code + q1 + ": " + p[5].code + q2 + ": return 0;\n}"
        print(p[0].code)

    def generate_declist_empty_code (self, p):
        p[0] = StatementTerminal()

    def generate_declist_code (self, p, q):
        p[0] = StatementTerminal()
        if p[1].code:
            p[0].address = p[1].address
        else:
            p[0].address = p[2].address
        if p[2].address:
            q = p[2].address
        p[1].next_list_back_patch(q)
        if p[2].address:
            p[0].code = p[1].code + p[2].code
        else:
            p[0].code = p[1].code + q + ': ' + p[2].code
        p[0].next_list = p[2].next_list

    def generate_dec_vardec_code (self, p):
        p[0] = p[1]

    def generate_vardec_code (self, p):
        p[0] = p[1]

    def generate_iddec_ID_code (self, p):
        p[0] = StatementTerminal()
        dec = 'int ' + p[1] + ';\n'
        if dec not in self.variables:
            self.variables += dec
        p[0].code = f'arr[stack_p] = {p[1]};\n stack_p = stack_p - 1;\n'
        p[0].stack.append(p[1])

    def generate_idlist_comma_code(self, p, q):
        p[0] = StatementTerminal()
        p[0].stack = p[1].stack + p[3].stack
        p[0].address = p[1].address
        if p[3].address:
            q = p[3].address
        p[1].next_list_back_patch(q)
        if p[3].address:
            p[0].code = p[1].code + p[3].code
        else:
            p[0].code = p[1].code + q + ': ' + p[3].code
        p[0].next_list = p[3].next_list

    def generate_idlist_code(self, p):
        p[0] = p[1]

    def generate_iddec_array_code(self, p, temp):
        p[0] = StatementTerminal()
        dec = "int " + p[1] + ";\n"
        if dec not in self.variables:
            self.variables += dec
        self.variables += "int " + temp + ";\n"
        p[0].code = f"arr[stack_p] = {p[1]};\nstack_p = stack_p - 1;\n"
        p[0].stack.append(p[1])
        p[0].code = p[1] + " = arr_p;\n" + "arr[arr_p] = " + p[3].get_value() + ";\n" + temp + " = " + p[3].get_value() + " + 1;\narr_p  = arr_p + " + temp + ";\n"

    def generate_iddec_assign_code(self, p, q1, q2, q3):
        p[0] = StatementTerminal()
        dec = "int " + p[1] + ";\n"
        if dec not in self.variables:
            self.variables += dec
        p[0].code = f"arr[stack_p] = {p[1]};\nstack_p = stack_p - 1;\n"
        p[0].stack.append(p[1])
        if isinstance(p[3], StatementTerminal):
            p[0].next_list = p[3].next_list
        if isinstance(p[3], LogicTerminal):
            p[3].true_list_back_patch(q1)
            p[3].false_list_back_patch(q2)
            p[0].code += p[3].code + q1 + ': ' + p[1] + ' = ' + '1;\n' + q3 + ': goto -;\n' + q2 + ': ' + p[1] + ' = ' + '0;\n'
            p[0].next_list = [q3]
        else:
            p[0].code += p[3].code + p[1] + ' = ' + p[3].get_value() + ';\n'

    def generate_exp_assign_code(self, p, q1, q2, q3):
        p[0] = StatementTerminal()
        p[0].place = p[1]
        p[0].address = p[3].address
        if isinstance(p[3], StatementTerminal):
            p[0].next_list = p[3].next_list
        if isinstance(p[3], LogicTerminal):
            p[3].true_list_back_patch(q1)
            p[3].false_list_back_patch(q2)
            p[0].code = p[3].code + q1 + ': ' + p[1] + ' = ' + '1;\n' + q3 + ': goto -;\n' + q2 + ': ' + p[1] + ' = ' + '0;\n'
            p[0].next_list = [q3]
        else:
            p[0].code = p[3].code + p[1] + ' = ' + p[3].get_value() + ';\n'

    def generate_lvalue_code(self, p, temp, temp2, temp3, q1, q2, q3):
        p[0] = StatementTerminal()
        p[0].address = p[3].address
        p[0].place = temp
        p[0].code = p[3].code + temp2 + ' = ' + p[3].get_value() + ' + 1;\n' + temp3 + ' = ' + p[1] + ' + ' + temp2 + ';\n'
        self.variables += 'int ' + temp + ';\n'
        self.variables += 'int ' + temp2 + ';\n'
        self.variables += 'int ' + temp3 + ';\n'
        if isinstance(p[6], StatementTerminal):
            p[0].next_list = p[6].next_list
        if isinstance(p[6], LogicTerminal):
            p[6].true_list_back_patch(q1)
            p[6].false_list_back_patch(q2)
            p[0].code += p[6].code + q1 + ": arr[" + temp3 + "] = 1;\n" + q3 + ': goto -;\n' + q2 + ": arr[" + temp3 + "] = 0;\n"
            p[0].next_list = [q3]
        else:
            p[0].code += p[6].code + "arr[" + temp3 + "] = " + p[6].get_value() + ';\n'
        p[0].code += temp + ' = ' + "arr[" + temp3 + "];\n"

    def generate_exp_arithmetic_code(self, p, temp, temp2, temp3, q1, q2, q3, q4, q6, q7):
        p[0] = NonTerminal()
        p[0].place = temp
        self.variables += 'int ' + temp + ';\n'
        self.variables += 'int ' + temp2 + ';\n'
        self.variables += 'int ' + temp3 + ';\n'
        if p[3].address:
            q7 = p[3].address
        if p[1].code:
            p[0].address = p[1].address
        elif p[3].code:
            p[0].address = q7
        else:
            p[0].address = q6
        if isinstance(p[1], StatementTerminal):
            p[0].next_list = p[1].next_list
        if isinstance(p[1], LogicTerminal):
            p[1].true_list_back_patch(q1)
            p[1].false_list_back_patch(q2)
            if p[3].code:
                next_label = q7
            else:
                next_label = q6
            p[0].code = p[1].code + q1 + ": " + temp2 + " = 1;\ngoto " + next_label + ";\n" + q2 + ": " + temp2 + " = 0;\n"
            p[1].place = temp2
        else:
            p[0].code = p[1].code
        if p[3].code and not p[3].address:
            p[0].code += q7 + ": "
        if isinstance(p[3], StatementTerminal):
            p[0].next_list = p[3].next_list
        if isinstance(p[3], LogicTerminal):
            p[3].true_list_back_patch(q3)
            p[3].false_list_back_patch(q4)
            p[0].code += p[3].code + q3 + ": " + temp3 + " = 1;\ngoto " + q6 + ';\n' + q4 + ": " + temp3 + " = 0;\n"
            p[3].place = temp3
        else:
            p[0].code += p[3].code
        p[0].code += q6 + ": " + temp + " = " + p[1].get_value() + " " + p[2] + " " + p[3].get_value() + ";\n"

    def generate_exp_const_code(self, p):
        p[0] = p[1]

    def generate_exp_ID_code(self, p):
        p[0] = NonTerminal()
        p[0].place = p[1]

    def generate_exp_array_code(self, p, temp, temp2, temp3):
        p[0] = NonTerminal()
        p[0].place = temp
        p[0].address = p[3].address
        self.variables += 'int ' + temp + ';\n'
        self.variables += 'int ' + temp2 + ';\n'
        self.variables += 'int ' + temp3 + ';\n'
        p[0].code = p[3].code + temp2 + ' = ' + p[3].get_value() + ' + 1;\n' + temp3 + ' = ' + p[1] + " + " + temp2 + ';\n' + temp + " = arr[" + temp3 + "];\n"

    def generate_exp_sub_code(self, p, temp, temp2, q1, q2, q3):
        p[0] = NonTerminal()
        p[0].place = temp
        if p[2].code:
            p[0].address = p[2].address
        else:
            p[0].address = q3
        self.variables += 'int ' + temp + ';\n'
        self.variables += 'int ' + temp2 + ';\n'
        if isinstance(p[2], StatementTerminal):
            p[0].next_list = p[2].next_list
        if isinstance(p[2], LogicTerminal):
            p[2].true_list_back_patch(q1)
            p[2].false_list_back_patch(q2)
            p[0].code = p[2].code + q1 + ': ' + temp2 + ' = 1;\ngoto ' + q3 + ';\n' + q2 + ': ' + temp2 + ' = 0;\n'
            p[2].place = temp2
        else:
            p[0].code = p[2].code
        p[0].code += q3 + ': ' + temp + ' = ' + p[1] + ' ' + p[2].get_value() + ';\n'

    def generate_exp_par_code(self, p):
        p[0] = p[2]

    def generate_const_arithmetic_code(self, p):
        p[0] = NonTerminal()
        p[0].value = p[1]

    def generate_block_code(self, p):
        p[0] = p[2]

    def generate_stmtlist_code(self, p, q):
        if p[2].code:
            p[0] = StatementTerminal()
            p[0].stack = p[1].stack + p[2].stack
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
        else:
            p[0] = p[1]

    def generate_stmtlist_empty_code(self, p):
        p[0] = StatementTerminal()
        p[0].code = ""

    def generate_stmt_sem_code(self, p):
        if isinstance(p[1], StatementTerminal):
            p[0] = p[1]
        else:
            p[0] = StatementTerminal()
            p[0].code = p[1].code
            p[0].address = p[1].address

    def generate_stmt_block_code(self, p):
        p[0] = p[1]

    def generate_stmt_var_code(self, p):
        p[0] = p[1]

    def generate_stmt_print_code(self, p):
        p[0] = StatementTerminal()
        p[0].code = 'printf("%d", ' + p[3] + ');\n'

    # part 2 ----------------------------------------------------------------------------------------

    def generate_stmt_const_code(self, p, q):
        p[0] = LogicTerminal()
        p[0].address = q
        if p[1] == 'True':
            p[0].true_list = [q]
        else:
            p[0].false_list = [q]
        p[0].code = q + ": goto -;\n"

    def generate_exp_or_code(self, p, q1, q2, q3, q4, q5):
        if not isinstance(p[1], LogicTerminal):
            p[1] = self.arith_to_logic(q1, q2, p[1])
        if not isinstance(p[3], LogicTerminal):
            p[3] = self.arith_to_logic(q3, q4, p[3])

        p[0] = LogicTerminal()
        p[0].address = p[1].address
        if p[3].address:
            q5 = p[3].address
        p[1].false_list_back_patch(q5)
        if p[3].address:
            p[0].code = p[1].code + p[3].code
        else:
            p[0].code = p[1].code + q5 + ": " + p[3].code
        p[0].true_list = p[1].true_list + p[3].true_list
        p[0].false_list = p[3].false_list

    def generate_exp_and_code(self, p, q1, q2, q3, q4, q5):
        if not isinstance(p[1], LogicTerminal):
            p[1] = self.arith_to_logic(q1, q2, p[1])
        if not isinstance(p[3], LogicTerminal):
            p[3] = self.arith_to_logic(q3, q4, p[3])

        p[0] = LogicTerminal()
        p[0].address = p[1].address
        if p[3].address:
            q5 = p[3].address
        p[1].true_list_back_patch(q5)
        if p[3].address:
            p[0].code = p[1].code + p[3].code
        else:
            p[0].code = p[1].code + q5 + ": " + p[3].code
        p[0].false_list = p[1]
        p[0].false_list = p[1].false_list + p[3].false_list
        p[0].true_list = p[3].true_list

    def generate_exp_not_code(self, p, q1, q2):
        if not isinstance(p[2], LogicTerminal):
            p[2] = self.arith_to_logic(q1, q2, p[2])

        p[0] = LogicTerminal()
        p[0].address = p[2].address
        p[0].code = p[2].code
        p[0].true_list = p[2].false_list
        p[0].false_list = p[2].true_list

    def generate_exp_relop_code(self, p):
        p[0] = p[1]

    def generate_relopexp_code(self, p, q1, q2):
        p[0] = LogicTerminal()
        if p[1].code:
            p[0].address = p[1].address
        elif p[3].code:
            p[0].address = p[3].address
        else:
            p[0].address = q1
        p[0].code += p[1].code + p[3].code
        p[0].code += q1 + ": if (" + p[1].get_value() + ' ' + p[2] + ' ' + p[3].get_value() + ") goto -;\n"
        p[0].code += q2 + ": goto -;\n"
        p[0].true_list = [q1]
        p[0].false_list = [q2]
        p[0].right_most_exp = p[3]

    def generate_relopexp_rel_code(self, p, q1, q2, q3):
        temp_terminal = LogicTerminal()
        if p[3].code:
            temp_terminal.address = p[3].address
        else:
            temp_terminal.address = q1
        temp_terminal.code = p[3].code
        temp_terminal.code += q1 + ": if (" + p[1].right_most_exp.get_value() + ' ' + p[2] + ' ' + p[3].get_value() + ") goto -;\n"
        temp_terminal.code += q2 + ": goto -;\n"
        temp_terminal.true_list = [q1]
        temp_terminal.false_list = [q2]

        p[0] = LogicTerminal()
        p[0].address = p[1].address
        if temp_terminal.address:
            q3 = temp_terminal.address
        p[1].true_list_back_patch(q3)
        if temp_terminal.address:
            p[0].code = p[1].code + temp_terminal.code
        else:
            p[0].code = p[1].code + q3 + ': ' + temp_terminal.code
        p[0].false_list = p[1]
        p[0].false_list = p[1].false_list + temp_terminal.false_list
        p[0].true_list = temp_terminal.true_list
        p[0].right_most_exp = p[3]

    def generate_elseiflist_empty_code(self, p):
        p[0] = LogicTerminal()

    def generate_elseiflist_code(self, p, q1, q2, q3, q4, q5):
        if not isinstance(p[4], LogicTerminal):
            p[4] = self.arith_to_logic(q4, q5, p[4])

        p[0] = LogicTerminal()
        if p[4].address:
            q2 = p[4].address
        p[1].false_list_back_patch(q2)
        if p[1].code:
            p[0].address = p[1].address
            p[0].code = p[1].code + q1 + ": goto -;\n"
        else:
            p[0].address = q2
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
        p[0].false_list = p[4].false_list

    def generate_stmt_if_code(self, p, q1, q2, q3, q4, q5):
        if not isinstance(p[3], LogicTerminal):
            p[3] = self.arith_to_logic(q4, q5, p[3])

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

    def generate_stmt_if_else_code(self, p, q1, q2, q3, q4, q5, q6, q7):
        if not isinstance(p[3], LogicTerminal):
            p[3] = self.arith_to_logic(q6, q7, p[3])

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
            p[0].code = p[3].code
            if p[5].address:
                p[0].code += p[5].code + q3 + ": goto -;\n"
            else:
                p[0].code += q1 + ": " + p[5].code + q3 + ": goto -;\n"
            if p[6].address:
                p[0].code += p[6].code
            else:
                p[0].code += q2 + ": " + p[6].code
            p[0].next_list = p[5].next_list + p[6].false_list + p[6].true_list + [q3, q4] + p[8].next_list
        else:
            p[3].false_list_back_patch(q5)
            p[0].code = p[3].code
            p[0].next_list = p[5].next_list + [q4] + p[8].next_list
            if p[5].address:
                p[0].code += p[5].code
            else:
                p[0].code += q1 + ": " + p[5].code
        if p[8].address:
            p[0].code += q4 + ": goto -;\n" + p[8].code
        else:
            p[0].code += q4 + ": goto -;\n" + q5 + ": " + p[8].code

    def generate_stmt_while_code(self, p, q1, q2, q3, q4):
        if not isinstance(p[3], LogicTerminal):
            p[3] = self.arith_to_logic(q3, q4, p[3])

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

    def generate_stmt_for_code(self, p, q1, q2, q3, q4, q5):
        if not isinstance(p[5], LogicTerminal):
            p[5] = self.arith_to_logic(q3, q4, p[5])

        p[0] = StatementTerminal()
        p[0].code = p[3].code
        if p[5].address:
            q1 = p[5].address
        if p[3].code:
            p[0].address = p[3].address
        else:
            p[0].address = q1
        if p[7].address:
            q5 = p[7].address
        if p[9].address:
            q2 = p[9].address
        p[9].next_list_back_patch(q5)
        p[5].true_list_back_patch(q2)
        if p[5].address:
            p[0].code += p[5].code
        else:
            p[0].code += q1 + ": " + p[5].code
        if p[9].address:
            p[0].code += p[9].code
        else:
            p[0].code += q2 + ": " + p[9].code
        if p[7].address:
            p[0].code += p[7].code + "goto " + q1 + ";\n"
        else:
            p[0].code += q5 + ": " + p[7].code + "goto " + q1 + ";\n"
        p[0].next_list = p[5].false_list

    def generate_stmt_foreach_code(self, p, q1, q2, q3, q4, q5, temp, temp2, temp3, temp4):
        dec = 'int ' + p[3] + ';\n'
        if dec not in self.variables:
            self.variables += dec
        self.variables += 'int ' + temp + ';\n'
        self.variables += 'int ' + temp2 + ';\n'
        self.variables += 'int ' + temp3 + ';\n'
        self.variables += 'int ' + temp4 + ';\n'

        iteration_exp = LogicTerminal()
        iteration_exp.address = q3
        iteration_exp.code += q3 + ": if (" + temp2 + ' < ' + temp4 + ") goto -;\n"
        iteration_exp.code += q4 + ": goto -;\n"
        iteration_exp.true_list = [q3]
        iteration_exp.false_list = [q4]

        p[0] = StatementTerminal()
        p[0].code = temp + ' = ' + p[5] + ';\n' + temp3 + ' = arr[' + temp + '];\n' + temp2 + ' = ' + temp + ' + 1;\n' + temp4 + ' = ' + temp2 + ' + ' + temp3 + ';\n'
        if iteration_exp.address:
            q1 = iteration_exp.address
        p[7].next_list_back_patch(q5)
        iteration_exp.true_list_back_patch(q2)
        if iteration_exp.address:
            p[0].code += iteration_exp.code
        else:
            p[0].code += q1 + ": " + iteration_exp.code
        p[0].code += q2 + ": " + p[3] + ' = arr[' + temp2 + '];\n' + p[7].code
        p[0].code += q5 + ": " + temp2 + " = " + temp2 + " + 1;\ngoto " + q1 + ";\n"
        p[0].next_list = iteration_exp.false_list

    def generate_cases_empty_code(self, p):
        p[0] = LogicTerminal()

    def generate_cases_code(self, p, q1, q2):
        p[0] = LogicTerminal()
        if p[2].address:
            q2 = p[2].address
        p[1].false_list_back_patch(q2)
        if p[1].code:
            p[0].address = p[1].address
            p[0].code = p[1].code + q1 + ": goto -;\n"
        else:
            p[0].address = q2
            p[0].code = ""
        if p[2].address:
            p[0].code += p[2].code
        else:
            p[0].code += q2 + ': ' + p[2].code
        p[0].true_list = p[1].true_list + [q1]
        p[0].false_list = p[2].false_list

    def generate_case_code(self, p, q1, q2, q3):
        logical_exp = LogicTerminal()
        logical_exp.address = q1
        logical_exp.code += q1 + ": if (" + p[2].get_value() + " == $) goto -;\n"
        logical_exp.code += q2 + ": goto -;\n"
        logical_exp.true_list = [q1]
        logical_exp.false_list = [q2]

        p[0] = LogicTerminal()
        p[0].address = logical_exp.address
        if p[4].address:
            q3 = p[4].address
        logical_exp.true_list_back_patch(q3)
        p[0].code = logical_exp.code
        if p[4].address:
            p[0].code += p[4].code
        else:
            p[0].code += q3 + ': ' + p[4].code
        p[0].false_list = logical_exp.false_list

    def generate_stmt_case_code(self, p):
        p[0] = StatementTerminal()
        p[0].address = p[3].address
        p[0].code = p[3].code
        p[0].code += p[6].code.replace('$', p[3].get_value())
        p[0].next_list = p[6].true_list + p[6].false_list

    def arith_to_logic(self, q1, q2, p):
        temp_terminal = LogicTerminal()
        if p.code:
            temp_terminal.address = p.address
        else:
            temp_terminal.address = q1
        temp_terminal.code = p.code
        temp_terminal.code += q1 + ": if (" + p.get_value() + " != 0) goto -;\n"
        temp_terminal.code += q2 + ": goto -;\n"
        temp_terminal.true_list = [q1]
        temp_terminal.false_list = [q2]
        return temp_terminal


    # part 3 ----------------------------------------------------------------------------------------

    def generate_paramdec_code (self, p):
        dec = "int " + p[1] + ";\n"
        if dec not in self.variables:
            self.variables += dec
        p[0] = [p[1]]

    def generate_paramdeclist_code (self, p):
        p[0] = p[1]

    def generate_paramdeclist_comma_code (self, p):
        p[0] = p[1] + p[3]

    def generate_paramdecs_code (self, p):
        p[0] = p[1]

    def generate_paramdecs_empty_code (self, p):
        p[0] = []

    def generate_funcdec_code (self, p, q1, q2 ,q3, temp):
        self.variables += "int " + temp + ";\n"
        param_names = p[4]
        number_of_params = len(param_names)
        p[0] = StatementTerminal()
        p[0].address = q1
        p[0].next_list = [q1]
        p[0].code = f'{q1}: goto -;\n'
        if number_of_params > 0 or not p[6].address:
            p[0].code += f'{q2}: '
        else:
            q2 = p[6].address
        self.function_dict[p[2]] = q2
        p[6].code = p[6].code.replace('?', q2)
        for i in range(number_of_params):
            p[0].code += f'stack_p = stack_p + 1;\n' \
                         f'arr[arr_p] = arr[stack_p];\n' \
                         f'arr_p = arr_p + 1;\n'
        for i in range(number_of_params):
            p[0].code += f'arr[stack_p] = {param_names[i]};\n' \
                         f'stack_p = stack_p - 1;\n' \
                         f'arr_p = arr_p - 1;\n' \
                         f'{param_names[i]} = arr[arr_p];\n'
        func_stack = param_names + p[6].stack
        p[6].next_list_back_patch(q3)
        p[0].code += p[6].code + q3 + ": "
        while func_stack:
            p[0].code += f'stack_p = stack_p + 1;\n' \
                         f'{func_stack.pop()} = arr[stack_p];\n'
        p[0].code += f'stack_p = stack_p + 1;\n' \
                     f'{temp} = arr[stack_p];\n' \
                     f'arr[stack_p] = 0;\n' \
                     f'stack_p = stack_p - 1;\n' \
                     f'back_jmp({temp});\n'

    def generate_funcdec_return_code(self, p, q1, q2, q3, temp, temp2):
        self.variables += "int " + temp + ";\n"
        self.variables += "int " + temp2 + ";\n"
        param_names = p[4]
        number_of_params = len(param_names)
        p[0] = StatementTerminal()
        p[0].address = q1
        p[0].next_list = [q1]
        p[0].code = f'{q1}: goto -;\n'
        if number_of_params > 0 or not p[8].address:
            p[0].code += f'{q2}: '
        else:
            q2 = p[8].address
        p[8].code = p[8].code.replace('?', q2)
        self.function_dict[p[2]] = q2
        for i in range(number_of_params):
            p[0].code += f'stack_p = stack_p + 1;\n' \
                         f'arr[arr_p] = arr[stack_p];\n' \
                         f'arr_p = arr_p + 1;\n'
        for i in range(number_of_params):
            p[0].code += f'arr[stack_p] = {param_names[i]};\n' \
                         f'stack_p = stack_p - 1;\n' \
                         f'arr_p = arr_p - 1;\n' \
                         f'{param_names[i]} = arr[arr_p];\n'
        func_stack = param_names + p[8].stack
        p[8].next_list_back_patch(q3)
        p[0].code += p[8].code.replace('#', q3)
        p[0].code += f'{q3}: stack_p = stack_p + 1;\n' \
                     f'{temp2} = arr[stack_p];\n'
        while func_stack:
            p[0].code += f'stack_p = stack_p + 1;\n' \
                         f'{func_stack.pop()} = arr[stack_p];\n'
        p[0].code += f'stack_p = stack_p + 1;\n' \
                     f'{temp} = arr[stack_p];\n' \
                     f'arr[stack_p] = {temp2};\n' \
                     f'stack_p = stack_p - 1;\n' \
                     f'back_jmp({temp});\n'

    def generate_exp_fun_code(self, p, temp, temp2, q1, q2):
        self.variables += "int " + temp + ";\n"
        self.variables += "int " + temp2 + ";\n"
        p[0] = StatementTerminal()
        p[0].code = f'arr[stack_p] = arr_p;\n' \
                    f'stack_p = stack_p - 1;\n' \
                    f'{temp2} = 0;\n' \
                    f'forward_jmp(arr_p);\n' \
                    f'{q1}: if({temp2} == 1) goto -;\n' \
                    f'arr_p = arr_p + 64;\n' \
                    f'{temp2} = 1;\n'
        p[0].next_list = [q1]
        if p[1] in self.function_dict.keys():
            p[0].code += f'goto {self.function_dict[p[1]]};\n'
        else:
            p[0].code += f'goto ?;\n'
        p[0].code += f'{q2}: stack_p = stack_p + 1;\n' \
                     f'{temp} = arr[stack_p];\n'
        p[0].place = temp
        p[0].next_list_back_patch(q2)

    def generate_exp_fun_explist_code(self, p, temp, temp2, q1, q2, q3):
        self.variables += "int " + temp + ";\n"
        self.variables += "int " + temp2 + ";\n"
        p[0] = StatementTerminal()
        p[0].code = f'arr[stack_p] = arr_p;\n' \
                    f'stack_p = stack_p - 1;\n'
        p[3].next_list_back_patch(q3)
        p[0].code += p[3].code
        p[0].code += f'{q3}: {temp2} = 0;\n' \
                     f'forward_jmp(arr_p);\n' \
                     f'{q1}: if({temp2} == 1) goto -;\n' \
                     f'arr_p = arr_p + 64;\n' \
                     f'{temp2} = 1;\n'
        p[0].next_list = [q1]
        if p[1] in self.function_dict.keys():
            p[0].code += f'goto {self.function_dict[p[1]]};\n'
        else:
            p[0].code += f'goto ?;\n'
        p[0].code += f'{q2}: stack_p = stack_p + 1;\n' \
                     f'{temp} = arr[stack_p];\n'
        p[0].place = temp
        p[0].next_list_back_patch(q2)

    def generate_explist_code(self, p):
        p[0] = StatementTerminal()
        p[0].code = p[1].code + f'arr[stack_p] = {p[1].get_value()};\n' \
                                f'stack_p = stack_p - 1;\n'
        if isinstance(p[1], LogicTerminal):
            p[0].next_list = p[1].next_list

    def generate_explist_comma_code(self, p, q):
        p[0] = StatementTerminal()
        if p[3].address:
            q = p[3].address
        p[1].next_list_back_patch(q)
        p[0].code = p[1].code
        if p[3].address:
            p[0].code += p[3].code
        else:
            p[0].code += q + ': ' + p[3].code
        p[0].code += f'arr[stack_p] = {p[3].get_value()};\n' \
                     f'stack_p = stack_p - 1;\n'
        if isinstance(p[3], LogicTerminal):
            p[0].next_list = p[3].next_list

    def generate_dec_fundec_code(self, p):
        p[0] = p[1]

    def generate_stmt_return_code(self, p):
        p[0] = StatementTerminal()
        p[0].code = p[2].code
        p[0].code += f'arr[stack_p] = {p[2].get_value()};\n' \
                     f'stack_p = stack_p - 1;\n' \
                     f'goto #;\n'
