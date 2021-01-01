class NonTerminal:

    def __init__(self):
        self.value = ""
        self.code = ""
        self.place = ""

    def get_value(self):
        if self.value == "":
            return self.place
        return self.value


class LogicalTerminal(NonTerminal):

    def __init__(self):
        super().__init__()
        self.true_list = []
        self.false_list = []

    def true_list_back_patch(self, label):
        lines = self.code.split('\n')
        for goto in self.true_list:
            for i in range(len(lines)):
                if lines[i].startswith(goto):
                    temp = lines[i]
                    lines[i].replace('-', label)
                    self.code.replace(temp, lines[i])

    def false_list_back_patch(self, label):
        lines = self.code.split('\n')
        for goto in self.false_list:
            for i in range(len(lines)):
                if lines[i].startswith(goto):
                    temp = lines[i]
                    lines[i].replace('-', label)
                    self.code.replace(temp, lines[i])
