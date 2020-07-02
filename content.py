import os

path = os.path.abspath(os.path.dirname(__file__))
input_file = os.path.join(path, 'input.md')
output_file = os.path.join(path, 'output.md')

with open(input_file, 'r') as f:
    input_data = f.readlines()

output_data = input_data[0:]
chapter = -1
section = 1

if __name__ == "__main__":
    for line in input_data:
        line_num = input_data.index(line)
        last_line_numer = line_num - 1·
        if line[:3] == '---':
            chapter += 1
        elif last_line_numer >= 0 and input_data[last_line_numer][:3] == '---':
            if line[:3] != '## ':
                output_data[line_num] = '## ' + str(chapter) + '. ' + line
            section = 1
        else:
            if line[:4] != '### ':
                output_data[line_num] = '### ' + str(chapter) + '.' + str(section) + ' ' + line
            section += 1
    
    with open(output_file, 'w') as f:
        f.writelines(output_data)