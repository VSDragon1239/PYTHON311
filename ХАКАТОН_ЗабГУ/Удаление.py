line_to_delete = 66288

with open('./Ресурсы/UScomments.csv', 'r', encoding='utf-8') as infile:
    lines = infile.readlines()

with open('./Ресурсы/UScomments.csv', 'w', encoding='utf-8') as outfile:
    for i, line in enumerate(lines):
        if i != line_to_delete:
            outfile.write(line)
