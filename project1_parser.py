# Lexer
class Lexer:
    def __init__(self, code):
        self.code = code.strip().replace("\n", " ")
        self.position = 0

    # move the lexer position and identify next possible tokens.
    def get_token(self): #keep adding values until you reach =, or operator and (), then return that
        tokens = list(self.code)
        # tokens = self.code.replace("\n", "")
        string = ""
        non_token = ["(", ")", "=", "+", "/", "*", "-", " ", "<", ">"]
        arith = ["+", "/", "*", "-"]
        while self.position < (len(tokens)):
            if tokens[self.position] not in non_token:
                string += tokens[self.position]
                self.position += 1
                #return string
            else:
                if tokens[self.position] in arith:
                    self.position += 1
                    return tokens[self.position - 1]
                if tokens[self.position] == "=":
                    if tokens[self.position + 1] == "=":
                        string += tokens[self.position + 1] + tokens[self.position]
                        self.position += 2
                    else:
                        string += tokens[self.position]
                        self.position += 1
                if string == "":
                    self.position += 1
                else:
                    break
        if string.isdigit():
            string = int(string)
        return string

        #print(tokens)
        #return string
# Parser
# Input : lexer object
# Output: AST program representation.


# First and foremost, to successfully complete this project you have to understand
# the grammar of the language correctly.

# We advise(not forcing you to stick to it) you to complete the following function 
# declarations.

# Basic idea is to walk over the program by each statement and emit a AST representation
# in list. And the test_utility expects parse function to return a AST representation in list.
# Return empty list for ill-formed programs.

# A minimal(basic) working parser must have working implementation for all functions except:
# if_statment, while_loop, condition.

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = None

    # function to parse the entire program, expected output
    def parse(self):
        ast = []
        ast.append(self.program())
        return ast

    # move to the next token.
    def advance(self):
        self.current_token = self.lexer.get_token()
        #return self.current_token
        #lexer.position += 1

    # parse the one or multiple statements
    def program(self): #calls other cases based on first token
        self.advance()
        if self.current_token == "if":
            return self.if_statement()
        elif self.current_token == "while":
            return self.while_loop()
        else:
            return self.assignment()


    # parse if, while, assignment statement.
    def statement(self):
        pass

    # parse assignment statements,expressions
    def assignment(self): #('=', 'x', ('+', 5, 3))
        token_1 = self.current_token
        self.advance()
        token_2 = self.current_token #equals sign
        self.advance()
        token_3 = self.arithmetic_expression()

        return (token_2, token_1, token_3)

    # parse arithmetic experssions
    def arithmetic_expression(self):
        arith = ["+", "-", "*", "/"]
        val = ""
        token_1 = ""
        token_2 = ""
        token_3 = ""
        while lexer.position < len(lexer.code): #run until end of expression, not end of tokens
            if self.current_token not in arith:
                token_1 = self.current_token
                self.advance()
                token_2 = self.current_token
                self.advance()
                token_3 = self.current_token
                self.advance()
        return (token_2, token_1, token_3)

    def term(self):
        pass

    def factor(self):
        pass

    # parse if statement, you can handle then and else part here.
    # you also have to check for condition.
    def if_statement(self):
        pass

    # implement while statment, check for condition
    # possibly make a call to statement?
    def while_loop(self):
        pass

    def condition(self):
        pass


# Testing
lexer = Lexer('x = 5 + 3')

#lexer = Lexer(code_2)
parser = Parser(lexer).parse()
print(lexer.get_token())
print(lexer.get_token())
print(lexer.get_token())
print(lexer.get_token())
print(lexer.get_token())
#t = (lexer.get_token(), lexer.get_token(), lexer.get_token(), lexer.get_token(), lexer.get_token(), lexer.get_token(), lexer.get_token())
#print(t)
print(parser)
#print(code_2.strip())
'''

test2 = lexer.get_token()
test3 = lexer.get_token()
ad = parser.advance()
print(val_test)
print(lexer.position)
print(test2)
print(test3)
print(ad)
print("hello")
'''