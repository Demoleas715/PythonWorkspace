'''
Created on Nov 20, 2015

@author: Evan
'''
class point(object):
    def __init__(self, x, y):
        self.x=x
        self.y=y
        
        
    def translate(self, dx, dy):
        self.x+=dx
        self.y+dy