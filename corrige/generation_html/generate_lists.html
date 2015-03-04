#!/usr/bin/python3

from template import FileTemplate, StringTemplate
from utils import *
from donnee import *


######################################################################################
## Génération de HTML
######################################################################################

def simple_list(flat_list):
    
    # Création d'un template HTML à partir d'une chaine de caractères
    ul = StringTemplate('<ul>{{items}}</ul>')
    items = ''
    for item in flat_list:
        items += '<li class="shopping-item">{item}</li>\n'.format(item=item)
    
    return ul.render(context={'items' : items})
    
    
def complex_list(data):
    '''
    
    >>> data = ['Fruits', ['Oranges', 'Pommes'], 'Légumes', ['Poireaux', 'Choux']]
    >>> complex_list(data)
    '<ul><li>Fruits</li><ul><li>Oranges</li><li>Pommes</li></ul><li>Légumes</li><ul><li>Poireaux</li><li>Choux</li></ul></ul>'
    
    '''
    
    if data == []:
        return ''
    elif isinstance(data, str):
        return '<li>{item}</li>'.format(item=data)
    else:
        sublists = [complex_list(item) for item in data]
        html = ''.join(sublists)
        return '<ul>{items}</ul>'.format(items=html)
        
        
######################################################################################
## Fonctions de tests
######################################################################################

### Exercice 1 de génération de HTML (liste simple)
def commission_simple():
    doc = base_html('Liste de commission simple')
    return doc.render(context={'content' : simple_list(commissions)})
    
    
### Exercice 2 de génération de HTML (liste hiérarchisée)
def commission_complexe():
    doc = base_html('Liste de commission hiérarchisée')
    return doc.render(context={'content' : complex_list(commissions2)})
    

def longue_liste():
    liste_nombres = [str(n ** 2) for n in range(1000)]
    doc = base_html('Longue liste de nombres')
    return doc.render(context={'content' : simple_list(liste_nombres)})
    
    
def test():
    
    tests = [
        ('commission_simple.html', commission_simple),
        ('longue_liste.html', longue_liste),
        ('commission_complexe.html', commission_complexe)
    ]
    
    for t in tests:
        filename = t[0]
        html = t[1]()
        write_to_file('output/'+filename, html)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    test()