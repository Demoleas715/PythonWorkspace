class Item (object):
    def __init__(self, name, quantity, cost):
        self.name=name
        self.quantity=quantity
        self.cost=cost
        
    def getTotalCost(self):
        return self.cost * self.quantity
    
class Invoice (object):
    def __init__(self):
        self.items=[]
        
    def addItem(self, item):
        self.items.append(item)
        
    def getItems(self):
        return self.items
    
    def getTotalCost(self):
        totalCost=0
        
        for item in self.items:
            
            totalCost+=item.getTotalCost()
            
        return totalCost