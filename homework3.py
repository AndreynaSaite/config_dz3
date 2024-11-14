import json
import re
import sys

# Регулярные выражения для различных конструкций языка
COMMENT_PATTERN = re.compile(r'<!--.*?-->', re.DOTALL)
ARRAY_PATTERN = re.compile(r'#\((.*?)\)')
CONST_PATTERN = re.compile(r'([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.+)')
EXPR_PATTERN = re.compile(r'\|\+|\-|\*|mod|')
NUMBER_PATTERN = re.compile(r'\d+')
dict = {}
# Парсер входного файла

def parse_config(content):
    # Удаление комментариев
    content = re.sub(COMMENT_PATTERN,'',content)
    array = []
    for line in content.splitlines():
        if line != '':
            array.append(line)
    return array

def work_with_data(data):
    for line in data:
        constants = CONST_PATTERN.match(line)
        if constants:
            name, value = constants.groups()
            dict[name] = work_with_value(value)            
    return dict



def work_with_value(value):
    value = value.strip()
    if NUMBER_PATTERN.fullmatch(value):
        return int(value)
    if ARRAY_PATTERN.match(value):
        array = []
        for char in value.split():
            try:
                int(char)
                array.append(int(char))
            except:
                continue
        return array
    
    if EXPR_PATTERN.search(value):
        return evaluate_expression(value)
    
    return value



def contains_letters(array):
    return any(re.search(r'[a-zA-Z]', item) for item in array)



def convert_prefix(stack,operations):
    while len(stack) != 1:
        el1 = int(stack.pop())
        el2 = int(stack.pop())
        oper = operations[-1]
        operations = operations[:-1]
        if oper == "+":
            stack.append(el1 + el2)
        if oper == "-":
            stack.append(el1 - el2)
        if oper == "*":
            stack.append(el1 * el2)
        if oper == "/":
            stack.append(el1 / el2)
        if oper == "%":
            stack.append(el1 % el2)

    return stack.pop()

def evaluate_expression(value):
    parts = value.strip('|').split()
    stack = []
    operations = ''
    super_stek = []
    # Вложенные массивы
# Пропускаем массивы, содержащие буквы
    filtered_arrays = [array for array in parts if not contains_letters(value)]
    if filtered_arrays:
        for i in filtered_arrays:
            i = i.replace('|','')
            try:
                int(i)
                stack.append(i)
            except:
                if i == "mod":
                    super_stek.append(i)
                operations += i
        stack = stack[::-1]
        return convert_prefix(stack,operations)
    
    else:
        for elements in range(len(parts)):
            for k in dict:
                if parts[elements] == k:
                    parts[elements] = dict.get(k)
        for i in parts:
            try:
                int(i)
                stack.append(i)
            except:
                if i == "mod":
                    operations += "%"
                else: operations += i
        stack = stack[::-1]
        return convert_prefix(stack,operations)

def write_to_json(data, output_file):
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)


# Основная функция
def main():
    if len(sys.argv) != 3:
        print("Usage: python config_tool.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    #output_file = sys.argv[2]
    
    # Чтение входного файла
    with open(input_file, 'r') as f:
        content = f.read()

    # Парсинг конфигурационного файла
    config_data = parse_config(content)

    # Работа с данными
    dictionry = work_with_data(config_data)
    write_to_json(dictionry, output_file)
    
    # Запись в JSON
    #write_to_json(config_data, output_file)
    #print(f"Configuration converted to JSON and saved to {output_file}")

if __name__ == "__main__":
    main()
