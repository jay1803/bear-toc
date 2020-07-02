import os
import urllib.parse

path = os.path.abspath(os.path.dirname(__file__))
input_file = os.path.join(path, 'input.md')
output_file = os.path.join(path, 'output.md')
'''
note_id = '469E7C32-9482-499F-87EE-FA72A87815EF-760-0000807520424871'
'''

def get_title(title):
    if title[:2] == '# ':
        return title[2:-1]
    if title[:3] == '## ':
        return title[3:-1]
    if title[:4] == '### ':
        return title[4:-1]
    if title[:5] == '#### ':
        return title[5:-1]

def encode_title(title):
    return urllib.parse.quote(get_title(title))

def generate_link(id, title):
    url = 'bear://x-callback-url/open-note?id=%s&header=%s' % (id, encode_title(title))
    return '* [%s](%s)\n' % (get_title(title), url)

with open(input_file, 'r') as f:
    input_data = f.readlines()

output_data = input_data[0:]
header = 0
subheader = 0
subtitle = 0


if __name__ == "__main__":
    from sys import argv
    def cmd_value(parameter):
        num_index = argv.index(parameter) + 1
        return argv[num_index]
    try:
        note_id = cmd_value('-n')
    except:
        note_id = input('Please input the note id: ')
    for line in input_data:
        if line[:3] == '## ' or line[:2] == '# ':
            subheader = output_data.index(line) + 2
            output_data.insert(header, generate_link(note_id, line))
            header += 1
        if line[:4] == '### ':
            subtitle = output_data.index(line) + 2
            output_data.insert(subheader, generate_link(note_id, line))
            subheader += 1
        if line[:5] == '#### ':
            output_data.insert(subtitle, generate_link(note_id, line))
            subtitle += 1
    
    with open(output_file, 'w') as f:
        f.writelines(output_data)