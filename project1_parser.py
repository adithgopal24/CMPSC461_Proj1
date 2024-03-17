# Lexer
class Lexer:
    def __init__(self, code):
        self.code = code
        self.position = 0
        self.operators_and_delimiters = ["(", ")", "=", "+", "/", "*", "-", " ", "<", ">", "+", "/", "*", "-"]

    # move the lexer position and identify next possible tokens.
    def get_token(self): #keep adding values until you reach =, or operator and (), then return that
        token_str = ""
        while self.position < (len(self.code)):
            if self.code[self.position].isspace():  # takes care of all white spaces including \t, \n, so no changes of self.code needed in init
                self.position += 1  # nothing to do for space, move to next pos

            elif self.code[self.position].isdigit():  # is a number
                while self.position < (len(self.code)) and self.code[self.position].isdigit():
                    token_str += self.code[self.position]  # collect number in the token_str
                    self.position += 1
                return int(token_str)  # number token

            elif self.code[self.position].isalnum():  # is alpha numeric
                while self.position < (len(self.code)) and self.code[self.position].isalnum():
                    token_str += self.code[self.position]  # collect alphanumeric chars in the token_str
                    self.position += 1
                return token_str  # alphanum token

            elif self.code[self.position] in self.operators_and_delimiters: #non-alphanum symbol
                token_str = self.code[self.position]
                self.position += 1
                return token_str  # operator/delimiter


        return None

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
    def assignment(self):
        self.advance()
        token_1 = self.current_token #assigned var
        #print(self.current_token)
        self.advance()
        token_2 = self.current_token # "=" sign
        self.advance()
        exp = self.arithmetic_expression()

        return token_2, token_1, exp

    # parse arithmetic expressions
    def arithmetic_expression(self):
        arith = ["+", "-"]
        if self.term().isdigit():
            expr = int(self.term())
        else:
            expr = self.term()
        self.advance()
        while self.current_token in arith:
            operator = self.current_token
            self.advance()
            if self.current_token.isdigit():
                val = int(self.current_token)
            else:
                val = self.current_token
            expr = operator, expr, val
        return expr

    def term(self): #('+', 5, 3)
        ops = ['*', '/'] #deal with mult and division
        factor = self.factor()
        while self.current_token in ops:
            operator = self.current_token
            self.advance()
            term = operator, factor, self.factor()
        return factor


    def factor(self):
        self.current_token = str(self.current_token)
        if self.current_token.isalnum(): #is digit or number
            return self.current_token

        elif self.current_token.isdigit():
            self.advance()
            return int(self.current_token)

        elif self.current_token == "(": #start of paranthesis, will likely utilize PEMDAS
            self.advance()
            arith_expr = self.arithmetic_expression()
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
