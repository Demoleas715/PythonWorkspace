'''
Created on Oct 30, 2015

@author: Evan
'''
def read_char_dist(filename):
    text_file = open (filename, "r")
    
    myd={}
    
    for line in text_file:
        
        line=line.lower()
        
        for c in line:
            if c>='a' and c<='z':
                myd[c]=myd.get(c, 0)+1
            
    return myd

    

def main():
    my_d = read_char_dist("story.txt")
    
    letters=list(my_d.keys())
    letters.sort()
    
    for l in letters:
        print(l + ": " + str(my_d[l]))
        
main()