import re 
import pygments 
from django import template 
from pygments import lexers 
from pygments import formatters 

register = template.Library() 

regex = re.compile(r'&lt;code(.*?)&gt;(.*?)&lt;/code&gt;', re.DOTALL)

def highlighter(value):
    """
    highlighter a programming language
    """
    class_code = ''
    code = ''
    last_end = 0
    final_text = ''
    format_text = ''
    replace_items = {'&nbsp;': ' ', '<div>': '', '\r': '', '\n\n': '\n', '\t': '', '</div>': '',  '</code>': ''}
    
    for inf in regex.finditer(value):
        class_code = re.split(r"&#39;|&quot;", inf.group(1))
        code = inf.group(2)
        
        for k,v in replace_items.items():
            code = code.replace(k, v)

        #Sometimes there are some characters before the first piece of code 
        for char in code:
            if char.isnumeric() or char.isalpha():
                ind = code.find(char)
                code = code[ind:]
                break
        try:
            if class_code:
                class_code = class_code[1]
                lexer = lexers.get_lexer_by_name(class_code)
        except:
            try: 
                lexer = lexers.guess_lexer(str(code)) 
            except ValueError: 
                lexer = lexers.PythonLexer()
                
        format_text = pygments.highlight(code, lexer, formatters.HtmlFormatter())
        final_text = final_text + value[last_end:inf.start(0)] + format_text 
        last_end = inf.end(2)
            
        value = value.replace('&lt;/code&gt;', '')
        final_text += value[last_end:]
    if final_text == '':
        return value
            
    return final_text
    

register.filter('highlighter', highlighter)
