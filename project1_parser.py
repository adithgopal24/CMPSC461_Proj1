# Lexer
class Lexer:
    def __init__(self, code):
        self.code = code.strip().replace("\n", " ").replace("\t", "")
        #self.code += "dummy"
        self.position = 0

    # move the lexer position and identify next possible tokens.
    def get_token(self): #keep adding values until you reach =, or operator and (), then return that
        tokens = list(self.code)
        #print("len of tokens: ", len(tokens))
        #print("tokens list", tokens)
        #print(len(self.code) - 1)
        # tokens = self.code.replace("\n", "")
        string = ""
        non_token = ["(", ")", "=", "+", "/", "*", "-", " ", "<", ">"]
        arith = ["+", "/", "*", "-"]
        #print(tokens[self.position])
        ''''''
        #print(tokens[self.position])
        while self.position < (len(self.code)):
            #print("goes into while loop")
            if tokens[self.position] == " ":
                self.position += 1
                #print("goes in while loop that skips spaces")

            elif tokens[self.position] not in non_token:
                #while (tokens[self.position] not in non_token) and (self.position < (len(self.code)-1)):
                string += tokens[self.position]
                self.position += 1
                    #return string
            else:
                if tokens[self.position] in arith:
                    string += tokens[self.position]
                    self.position += 1
                if tokens[self.position] == "=":
                    if tokens[self.position + 1] == "=":
                        string += tokens[self.position + 1] + tokens[self.position]
                        self.position += 2
                    else:
                        string += tokens[self.position]
                        self.position += 1
                # elif tokens[self.position] == " ":
                #     self.position += 1
                if string == "":
                    self.position += 1

            if string.isdigit():
                string = int(string)
                print("is digit")
            #self.position += 1
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
        self.expression_counter = 0

    # function to parse the entire program, expected output
    def parse(self):
        '''
        ast = []
        ast.append(self.program())
        return ast
        '''
        # while self.lexer.position < len(self.lexer.code):
        return str(self.program())

    # move to the next token.
    def advance(self):
        self.current_token = self.lexer.get_token()
        '''
        if self.lexer.position < len(self.lexer.code):
            self.current_token = self.lexer.get_token()
        else:
            print("Nuh uh")
        print(self.current_token)
        print(len(self.lexer.code))
        #return self.current_token
        #lexer.position += 1
        '''
    # parse the one or multiple statements
    def program(self): #calls other cases based on first token
        #self.advance()
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
        print(self.current_token)
        self.advance()
        token_2 = self.current_token #equals sign
        self.advance()
        token_3 = self.arithmetic_expression()

        return token_2, token_1, token_3

    # parse arithmetic experssions
    def arithmetic_expression(self):
        arith = ["+", "-", "*", "/"]
        all_symbols = ["+", "-", "*", "/", "="]
        val = ""
        token_1 = ""
        token_2 = ""
        token_3 = ""
        arith_token_1 = ""
        arith_token_2 = ""
        token_counter = 0
        while self.lexer.position < (len(self.lexer.code)-1): #run until end of expression, not end of tokens. Curr_token = digit, next_token = letter?
            #check for space, tok_before and after is numOrDigit,
            if self.lexer.code[self.lexer.position] == " ":
                if (self.lexer.code[self.lexer.position - 1]) and (self.lexer.code[self.lexer.position + 1]) not in all_symbols: #this represents a new expression
                    self.expression_counter += 1
            self.lexer.position += 1


        if self.expression_counter <= 1: #only one or less expressions in input
            while token_counter < (len(self.lexer.code)-1):
                if self.current_token not in arith:
                    if self.current_token == " ": #account for "space" tokens
                        self.advance()
                    else:
                        token_1 = self.current_token #arith symbol
                        self.advance()
                        #token_2 = self.current_token #first value in arith exp
                        #self.advance()
                        token_3 = self.current_token #second value in arith exp
                        self.advance()
                else: #if token is arithmetic symbol
                    token_2 = self.current_token
                    self.advance()
                token_counter += 1
            return token_2, token_1, token_3


        else: #multiple arith expressions in input
            if self.lexer.code[self.lexer.position] == " ":
                if (self.lexer.code[self.lexer.position - 1]) and (self.lexer.code[self.lexer.position + 1]) not in all_symbols:
                    arith_token_1 = self.lexer.code[self.lexer.position + 1]





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
#lexer = Lexer('x = 1 y = 2 z = 3 a = x + y + z')

parser = Parser(lexer).parse()
#print(lexer.get_token())
#print(parser)
'''
print(lexer.get_token())
print(lexer.get_token())
print(lexer.get_token())
print(lexer.get_token())
'''
#t = (lexer.get_token(), lexer.get_token(), lexer.get_token(), lexer.get_token(), lexer.get_token(), lexer.get_token(), lexer.get_token())
#print(t)
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