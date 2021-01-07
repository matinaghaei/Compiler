class NonTerminal:

    def __init__(self):
        self.value = ""
        self.code = ""
        self.place = ""
        self.address = ""

    def get_value(self):
        if self.value == "":
            return self.place
        return self.value


class LogicTerminal(NonTerminal):

    def __init__(self):
        super().__init__()
        self.true_list = []
        self.false_list = []
        self.right_most_exp = ""

    def true_list_back_patch(self, label):
        lines = self.code.split('\n')
        for goto_label in self.true_list:
            for i in range(len(lines)):
                if goto_label in lines[i]:
                    temp = lines[i]
                    lines[i] = temp.replace('-', label)
                    self.code = self.code.replace(temp, lines[i])

    def false_list_back_patch(self, label):
        lines = self.code.split('\n')
        for goto_label in self.false_list:
            for i in range(len(lines)):
                if goto_label in lines[i]:
                    temp = lines[i]
                    lines[i] = temp.replace('-', label)
                    self.code = self.code.replace(temp, lines[i])


class StatementTerminal(NonTerminal):

    def __init__(self):
        super().__init__()
        self.next_list = []

    def next_list_back_patch(self, label):
        lines = self.code.split('\n')
        for goto in self.next_list:
            for i in range(len(lines)):
                if lines[i].startswith(goto):
                    temp = lines[i]
                    lines[i] = temp.replace('-', label)
                    self.code = self.code.replace(temp, lines[i])
