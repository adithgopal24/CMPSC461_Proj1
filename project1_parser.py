# Lexer
class Lexer:
    def __init__(self, code):
        self.code = code.strip().replace("\n", " ").replace("\t", "")
        self.position = 0

    # move the lexer position and identify next possible tokens.
    def get_token(self): #keep adding values until you reach =, or operator and (), then return that
        tokens = list(self.code)
        #print(tokens)
        string = ""
        non_token = ["(", ")", "=", "+", "/", "*", "-", " ", "<", ">"]
        arith = ["+", "/", "*", "-"]
        comp = "" #for comparison
        space = " "
        while self.position < (len(self.code)):
            #print("goes into while loop")
            if tokens[self.position] == " ":
                self.position += 1

            elif tokens[self.position].isdigit(): #is a number
                while self.position < (len(self.code)) and tokens[self.position].isdigit():
                    string += tokens[self.position]
                    self.position += 1
                return string

            while tokens[self.position].isalpha(): #is a letter
                while self.position < (len(self.code)) and tokens[self.position].isalpha():
                    string += tokens[self.position]
                    self.position += 1
                return string
            while tokens[self.position] in arith:
                operator = tokens[self.position]
                self.position += 1
                return operator
            while tokens[self.position] == "=":
                if tokens[self.position + 1] == "=":
                    comp += tokens[self.position + 1] + tokens[self.position]
                    self.position += 2
                    return comp
                else:
                    string += tokens[self.position]
                    self.position += 1
                    return string


            if string.isdigit():
                string = int(string)

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
        ast = (str(self.program()))
        print(ast)
        return ast

    # move to the next token.
    def advance(self):
        self.current_token = self.lexer.get_token()

    # parse the one or multiple statements
    def program(self): #calls other cases based on first token
        #self.advance()
        return self.statement()

    # parse if, while, assignment statement.
    def statement(self):
        if self.current_token == "if":
            return self.if_statement()
        elif self.current_token == "while":
            return self.while_loop()
        else:
            return self.assignment()

    # parse assignment statements,expressions
    def assignment(self): #('=', 'x', ('+', 5, 3))
        self.advance()
        token_1 = self.current_token #assigned var
        #print(self.current_token)
        self.advance()
        token_2 = self.current_token # "=" sign
        self.advance()
        exp = self.arithmetic_expression() #term

        return token_2, token_1, exp

    # parse arithmetic experssions
    def arithmetic_expression(self):
        arith = ["+", "-", "*", "/"]
        all_symbols = ["+", "-", "*", "/", "="]
        operator = self.current_token #
        return self.term()
        return self.factor()


    def term(self): #('+', 5, 3)
        term_ops = ['+', '-']
        token_1 = ''
        token_2 = ''
        token_3 = ''
        if self.current_token not in term_ops:
            token_1 = self.current_token
            self.advance()
        while self.current_token in term_ops:
            token_2 = self.current_token
            self.advance()
            token_3 = self.current_token
        return token_2, token_1,token_3

    def factor(self):
        self.current_token = str(self.current_token)
        if self.current_token.isalpnum():
            self.advance()
        elif self.current_token == "(":
            self.advance()
            arith_expr = self.arithmetic_expression()
            self.advance()
            return arith_expr



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
#lexer = Lexer('xx = 5 + 3')
lexer = Lexer('x = 1 y = 2 z = 3 a = x + y + z')

#parser = Parser(lexer).parse()
print(lexer.get_token())
print(lexer.get_token())
print(lexer.get_token())
print(lexer.get_token())
print(lexer.get_token())
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