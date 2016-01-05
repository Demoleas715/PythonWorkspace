file_name=file_name
text_file=open(file_name, "r")
    
characters=[]

for line in text_file:
    line=line.strip()
    row=line.split(',')
    characters.append(Character(row[0], row[1], row[2], row[3]))