import os


def create_new_file(name_file):
    with open(f'{name_file}', 'w+', encoding='utf-8') as file:
       file.write('')


create_new_file('New File.txt')

path = os.getcwd()
directory = []
for f in os.listdir(path):
    if f.endswith('.txt'):
        directory.append(f)


def get_size_doc(file_name):
    document_size = {}
    for name in file_name:
        lines = []
        with open(f'{name}', encoding='utf-8') as file:
            for line in file:
                if line.strip() != '':
                    lines.append(line.strip())
        document_size[name] = len(lines)
    sorted_document = {}
    sorted_doc = sorted(document_size, key=document_size.get)
    for w in sorted_doc:
        sorted_document[w] = document_size[w]
    return sorted_document



def write_new_file(file):
    dict_ = get_size_doc(directory)
    list_key = []
    list_value = []
    for key, value in dict_.items():
        list_key.append(key)
        list_value.append(value)
    for i in range(len(list_key)-1):
        with open(f'{list_key[0]}', 'a', encoding='utf-8') as f_n:
            with open(f'{list_key[i+1]}', 'r', encoding='utf-8') as f_r:
                data = f_r.read()
                f_n.write(f'{list_key[i+1]}\n')
                f_n.write(f'{list_value[i+1]}\n')
                f_n.write(f'{data}\n')
                f_n.write('\n')

write_new_file('New File.txt')