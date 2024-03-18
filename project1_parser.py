# Lexer
class Lexer:
    def __init__(self, code):
        self.code = code
        self.position = 0
        self.operators_and_delimiters = ["(", ")", "=", "+", "/", "*", "-", "<", ">", "+", "/", "*", "-"]


    #returns current token at the current position
    def get_token(self):
        # arith = ["+", "/", "*", "-"]
        # comp = "" #for comparison
        # space = " "
        token_str = ""
        while self.position < (len(self.code)):
            if self.code[self.position].isspace(): # takes care of all white spaces, including \t, \n
                self.position += 1 # nothing to do so absorb the space

            elif self.code[self.position].isdigit(): #current char is a number
                while self.position < (len(self.code)) and self.code[self.position].isdigit():
                    token_str += self.code[self.position] # collect number in the token_str
                    self.position += 1
                return int(token_str) # return number token

            elif self.code[self.position].isalnum(): # is alpha numeric
                while self.position < (len(self.code)) and self.code[self.position].isalnum():
                    token_str += self.code[self.position] # collect alphanumeric chars in token_str
                    self.position += 1
                return token_str # return alphanum token

            elif self.code[self.position] in self.operators_and_delimiters: #operators/delimiter
                while self.position < (len(self.code)) and self.code[self.position] in self.operators_and_delimiters:
                    token_str += self.code[self.position] #collect consecutive operators like ">=" as a single token
                    self.position += 1
                return token_str # return operators/delimiter token
            else:
                print("Invalid token") #not a valid token, so can be dealt as ill-formatted


        return None # end of code


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
        self.current_token = lexer.get_token() #set current_token to lexer.get_token() to avoid having to call self.advance() before running program
        self.pass_empty_list = False #default value is False, is True if the program is ill-formatted, and then empty list is passed

    # function to parse the entire program, expected output
    def parse(self):
        ast = self.program()
        if self.pass_empty_list:
            return [] #pass empty list if program is ill-formatted.
        return ast

    # error handler
    def error(self, msg): #handles all improper/ill-formatted code, which sets self.pass_empty_list to True if found. See line 56.
        self.pass_empty_list = True
        print(msg)

    # move to the next token.
    def advance(self):
        self.current_token = self.lexer.get_token()

    # parse the one or multiple statements
    def program(self):
        statements = []
        while self.current_token is not None: #while there are additional tokens to handle, not at end of self.code
            statements.append(self.statement())
        return statements

    # parse if, while, assignment statement.
    def statement(self):
        if self.current_token == "if":
            return self.if_statement() #will handle if-statements
        elif self.current_token == "while":
            return self.while_loop() #will handle while loops
        else:
            return self.assignment()

    # parse assignment statements,expressions
    def assignment(self):
        left_of_assignment = self.current_token #tokens coming left before the operator
        self.advance()

        if self.current_token != '=':
            self.error("Expected '=' for assignment") #no '=' means assignment cannot be done
        assignment_oper = self.current_token
        self.advance()

        exp = self.arithmetic_expression()

        return assignment_oper, left_of_assignment, exp

    # parse arithmetic experssions
    def arithmetic_expression(self): # arithmetic_expression -> term (('+' | '-') term)*
        node = self.term() #call and store result of term
        while self.current_token in ('+', '-'):
            op = self.current_token  #operator stored
            self.advance()
            node = (op, node, self.term()) #call next term, so that the values left of the operator, and right of the operator can be returned
        return node


    def term(self): # term -> factor (('*' | '/') factor)*
        node = self.factor() #call and store result of factor
        while self.current_token in ('*', '/'):
            op = self.current_token
            self.advance()
            node = (op, node, self.factor())
        return node

    def factor(self):
        current_token_str = str(self.current_token)
        if current_token_str.isdigit():
            self.advance()
            return int(current_token_str)
        elif current_token_str.isalnum():  # alpha numeric, ex: variable name
            self.advance()
            return current_token_str
        elif current_token_str == '(': #Return expression in between paranthesis
            self.advance()
            expr = self.arithmetic_expression()
            if self.current_token != ')':
                self.error("Expected closing parenthesis ')'")
            self.advance()
            return expr
        else:
            self.error(f"Unexpected token '{current_token_str}'") #improper token formatting, implies ill-formatted program

    # parse if statement, you can handle then and else part here.
    # you also have to check for condition.
    def if_statement(self):
        if self.current_token != 'if': #sign of ill-formatted program, as "if" is needed here
            self.error("Expected 'if'")
        self.advance()  # absorb the 'if'

        cond = self.condition()  # Parse the condition

        if self.current_token != 'then': #sign of ill-formatted program, as "then" is needed here
            self.error("Expected 'then'")
        self.advance()  # absorb the 'then'

        then_statement = self.statement()
        # as per the grammar, else_statement is optional. so return accordingly
        if self.current_token == 'else':
            self.advance()  # absorb the 'else'
            else_statement = self.statement()
            return ('if', cond, then_statement, else_statement)
        return ('if', cond, then_statement)

    # implement while statment, check for condition
    # possibly make a call to statement?
    def while_loop(self):
        if self.current_token != 'while': #sign of ill-formatted program, as "while" is needed here
            self.error("Expected 'while'")
        self.advance() # absorb while
        while_condition = self.condition()
        while_body_statements = []
        self.advance() # absorb do
        while self.current_token != 'do' and self.current_token != None: #from the "do" token all the way to the end
            statement = self.statement()
            while_body_statements.append(statement)
        self.advance()
        return ('while', while_condition, while_body_statements)

    def condition(self):
        left = self.arithmetic_expression() #expression coming before the comparision operator

        op = self.current_token
        if op not in ('==', '!=', '<', '>', '<=', '>='):
            self.error("Expected a comparison operator")
        self.advance()

        right = self.arithmetic_expression() #expression coming after the comparision operator
        return (op, left, right)
