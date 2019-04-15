import sys

latex_f = open(sys.argv[1],"r")
content = latex_f.read()
latex_f.close()
latex_f = open(sys.argv[1],"w")
repl = '\\"'


content = content.replace('ä',repl + "a")
content = content.replace('Ä',repl + "A")
content = content.replace('ü',repl + "u")
content = content.replace('Ü',repl + "U")
content = content.replace('ö',repl + "o")
content = content.replace('Ö',repl + "O")
content = content.replace('ß','"s')

print(content)