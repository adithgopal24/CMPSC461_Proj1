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
        self.current_token = lexer.get_token() #change from None to not need an advance() call later
        self.expression_counter = 0
        self.pass_empty_list = False

    # function to parse the entire program, expected output
    def parse(self):
        ast = self.program()
        if self.pass_empty_list:
            return [] #empty list returned if ill-formed program (no code) passed
        return ast

    # move to the next token.
    def advance(self):
        self.current_token = self.lexer.get_token()

    # parse the one or multiple statements
    def program(self): #calls other cases based on first token
        statements = []
        while self.current_token is not None:
            statements.append(self.statement()) #append statements until end of self.code
        return statements

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
        left_of_assignment = self.current_token
        self.advance()

        assignment_oper = self.current_token #operator stored
        self.advance()
        exp = self.arithmetic_expression()

        return assignment_oper, left_of_assignment, exp

    # parse arithmetic expressions
    def arithmetic_expression(self):
        node = self.term()
        while self.current_token in ('+', '-'):
            op = self.current_token
            self.advance()
            node = (op, node, self.term())
        return node

    def term(self): #('+', 5, 3)
        node = self.factor()
        while self.current_token in ('*', '/'):
            op = self.current_token
            self.advance()
            node = (op, node, self.factor())
        return node


    def factor(self):
        current_token_str = str(self.current_token)
        if current_token_str.isdigit():
            self.advance()
            return int(self.current_token)

        elif current_token_str == "(": #start of paranthesis, will likely utilize PEMDAS
            self.advance()
            expr = self.arithmetic_expression()
            return expr



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
