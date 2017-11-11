'''
Created on Nov 11, 2017

@author:  the-constant
'''


class License(object):
    
    def __init__(self, id_, name, agreement=None, terms=None):
        super().__init__()
        self.id_ = id_
        self.name = name
        self.agreement = agreement
        self.terms = terms or []
    

class Agreement(object):
    
    def __init__(self, id_, name, conditions=None, end_clauses=None):
        super().__init__()
        self.id_ = id_ 
        self.name = name 
        self.conditions = conditions or []
        self.end_clauses = end_clauses or []
        

class Term(object):
    
    def __init__(self, start, end=None, principal=0, rate=0.05):
        super().__init__()
        self.start = start
        self.end = end
        self.principal = principal
        self.rate = rate
        


