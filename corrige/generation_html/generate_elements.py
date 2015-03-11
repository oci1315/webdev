from utils import *
from template import *
from html import html_elements, void_elements

python = ''
for e in html_elements:
    py = FileTemplate('element_cls_dfn_template.py')
    class_def = py.render({'class_name' : e.capitalize(), 'tag' : e, 'is_void': e in void_elements})
    python += '\n\n' + class_def
    
print(python)