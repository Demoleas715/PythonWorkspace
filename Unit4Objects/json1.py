import json

def main():
    
    d={}
    
    d["Grades"]={}
    
    d["Grades"]["Bryan"]=80
    d["Grades"]["Grace"]=95
    d["Grades"]["Rebecca"]=92
    d["Grades"]["Dan"]=97
    
    d["Teachers"]=[]
    d["Teachers"].append("Ms. Lee")
    d["Teachers"].append("Mr. Isecke")
    d["Teachers"].append("Mr. Nodarse")
    
    s=json.dumps(d, sort_keys=True, indent=4)
    
    print(s)
    
main()