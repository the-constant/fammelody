'''
Created on Nov 11, 2017

@author:  the-constant
'''
from builtins import str


class MarketPlace(object):
    
    def __init__(self, id_, name, merchants=None):
        super().__init__()
        self.id_ = id_
        self.name = name
        self.merchants = merchants or []
        
        
class Merchant(object):
    
    def __init__(self, id_, name, contact, logo=None, items=None):
        super().__init__()
        self.id_ = id_
        self.name = name
        self.logo = logo
        self.contact = contact
        self.location = contact.address.location
        self.items = items or []
        

class Item(object):
    
    def __init__(self, id_, name, type_, color, price, description=''):
        super().__init__()
        self.id_ = id_ 
        self.name = name
        self.type_ = type_ 
        self.color = color 
        self.price = price 
        self.desc = description
        
    
    
    
        
        
        
        
