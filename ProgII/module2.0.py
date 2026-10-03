import numpy as np

class Stack:
    def __init__(self):
        self.list1 = []

    def push(self,item):
        self.list1.append(item)
    
    def pop(self):
        return self.list1.pop()
    
    def is_empty(self):
        return True if len(self.list1) == 0 else False
    
    def peek(self):
        return self.list1[-1]

class EvaluationError(Exception):
    pass

class MockTokenizer:
    """Enkel kö som simulerar token-strömmen på tentan."""
    def __init__(self, tokens):
        self._tokens = tokens

    def peek(self):
        return self._tokens[0] if self._tokens else None

    def get(self):
        return self._tokens.pop(0) if self._tokens else None

def factor(wt, variables):
    token = wt.get()
    if token is None:
        raise EvaluationError("Oväntat slut på uttrycket")
    if token.isdigit():
        return float(token)
    elif token in variables:
        return float(variables[token])
    else:
        raise EvaluationError(f"Ogiltig faktor: {token}")

def term(wt, variables):
    # UPPGIFT:
    # 1. Hämta den första faktorn via factor(wt, variables)
    # 2. Så länge nästa token (wt.peek()) är '*' eller '/':
    #    - Hämta operatorn med wt.get()
    #    - Hämta nästa faktor via factor(wt, variables)
    #    - Utför multiplikationen eller divisionen
    #    - Om nämnaren är 0 vid division: kasta EvaluationError("Division by zero")
    # 3. Returnera det ackumulerade resultatet
    pass

# Testfall att verifiera mot:
wt1 = MockTokenizer(["6", "*", "2", "/", "3"])
print(term(wt1, {}))  # Ska ge 4.0

# wt2 = MockTokenizer(["5", "/", "0"])
# term(wt2, {})         # Ska kasta EvaluationError