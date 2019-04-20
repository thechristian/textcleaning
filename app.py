import re # import regex

filename = input("enter filename eg. sample.txt >> ")
file = open(filename, 'rt')
file_content = file.read()
file.close()
placeholder = 'xyz' # placeholder to keep special titles and characters

symbols = ['Dr.', 'Mr.', 'Mrs.', 'Miss.', 'Prof.', 'i.e.', 'etc.'] # special name titles and characters
replacements = [t.replace('.', placeholder) for t in symbols]

for i in range(len(symbols)):
    file_content = file_content.replace(symbols[i], replacements[i])

#spliting by full stop

file_content = re.split(r'(?<=\w\.)\s', file_content)
file_content = [o.replace(placeholder, '.' ) for o in file_content]
for line in file_content:
    newFile = open("new_file.txt", "a+")
    newFile.write(line)
    newFile.write("\n")
newFile.close()