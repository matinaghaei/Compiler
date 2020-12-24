from lexer import Lexer
from pars import Parser


def main():
    lexer = Lexer().build()
    file = open('./test.txt')
    text_input = file.read()
    file.close()
    lexer.input(text_input)
    parser = Parser()
    parser.build().parse(text_input, lexer, False)


if __name__ == "__main__":
    main()
