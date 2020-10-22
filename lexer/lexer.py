from lexer.type import Type
from lexer.token import Token
import re


class LexicalError(Exception):

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
    


def lex_source_file(fd):
    with open(fd, 'r') as file:
        data = file.read()
    return lex_source_string(data)


def lex_source_string(string):
    tokens = list()
    index = 0
    while index < len(string):
        token = separate_token(string, index)
        if token is None:
            break
        index = token.end
        tokens.append(token)
    #if index != len(string):
         #raise LexicalError('Lexical error at position ' + str(index))
    return tokens



def separate_token(string, begin):
    if begin < 0 or begin >= len(string):
        raise IndexError(string, 'Index out of bounds: ' + begin)
    for type in Type:
        #print(str(begin))
        pattern = r'.{' + str(begin) + '}' + type.value
        #print(pattern)
        match = re.match(pattern, string, re.DOTALL)
        if match:
            end = match.end(1)
            #print(end)
            return Token(begin, end, string[begin:end], type)
    else:
        return Token(begin, begin+1, string[begin:begin+1], Type.LEXICO_INCORRECTO)
    return None