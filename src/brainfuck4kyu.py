import re

def brainfuck_to_c(text):
    text = re.sub('[^+-<>,.\[\]]', '', text)
    
   
    solved_text = ''
    while text != solved_text:
        solved_text = text
        text = re.sub('\+-|-\+|<>|><|\[\]', '', text)
    
   
    braces = re.sub('[^\[\]]', '', text)
    while braces.count('[]'):
        braces = braces.replace('[]', '')
    if braces:
        return 'Error!'
    
   
    brainfuck_text = re.findall('\++|-+|>+|<+|[.,\[\]]', text)
    
   
    res = []
    idx = 0
    for cmd in brainfuck_text:
        if cmd[0] in '+-<>':
            line = ('%sp %s= %s;\n' %
                ('*' if cmd[0] in '+-' else '',
                 '+' if cmd[0] in '+>' else '-',
                 len(cmd)))
        elif cmd == '.':
            line = 'putchar(*p);\n'
        elif cmd == ',':
            line = '*p = getchar();\n'
        elif cmd == '[':
            line = 'if (*p) do {\n'
        elif cmd == ']':
            line = '} while (*p);\n'
            idx -= 1
        res.append('  ' * idx + line)
        if cmd == '[':
            idx += 1
    
    return ''.join(res)