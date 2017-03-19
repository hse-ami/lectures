# -*- coding: utf-8 -*-
# Change coding to UTF-8

# Import section
import os
import subprocess
import re

# Creating temp file with all lectures
with open('temp.tex', 'w', encoding="utf8") as temp:
    # Adding header
    with open('header.tex', 'r', encoding="utf8") as header:
        temp.write(header.read())

    # Adding necessary lines (beginning of document, title and table of contents)
    temp.write('\n\\begin{document}\n\n')
    temp.write('\\maketitle\n\n')
    temp.write('\\tableofcontents\n\n')

    # Collecting text from separate lecture files
    lectures = []

    for elem in os.listdir('./'):
        if elem.startswith('linear-algebra') and elem.endswith('.tex'):
            lectures.append(elem)
    lectures.sort()

    # Adding it to the temp file
    for lecture_name in lectures:
        with open(lecture_name, 'r', encoding='utf8') as lecture:
            temp.write(r'\newpage')
            temp_lines = lecture.readlines()
            for line in temp_lines[3:-1]:
                temp_line = line.replace('section*', 'section')
                temp.write(temp_line)
    # Adding the final line
    temp.write(r'\end{document}')

# In order to create table of contents, I have to compile it twice.
for _ in range(2):
    proc = subprocess.Popen(['pdflatex', 'temp.tex'])
    proc.communicate()

# Saving the file
os.chdir('..')
for file in os.listdir('./'):
    if file == 'linear-algebra_all_lectures.pdf':
        os.remove(os.path.join('./', file))
os.rename('./tex/temp.pdf', 'linear-algebra_all_lectures.pdf')

for elem in os.listdir('./tex/'):
    if elem.startswith('linear-algebra') and elem.endswith('.pdf'):
        if elem in os.listdir('./'):
            os.remove(os.path.join('./', elem))
        os.rename('./tex/'+elem, elem)
os.chdir('tex')

# Removing the litter
for file in os.listdir('./'):
    if not (file.endswith('.tex') or file.endswith('.py')):
        os.remove(os.path.join('./', file))
os.remove('./temp.tex')
