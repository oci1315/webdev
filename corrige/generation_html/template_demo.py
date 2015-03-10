from template import FileTemplate, StringTemplate
from utils import *
from donnee import *
        
def simple_list(flat_list):
    ''' Fabrique le code HTML permettant de générer une liste à puces HTML à
    partir de la liste `flat_list`. Retourne le code HTML généré '''
    
    # Création d'un template HTML à partir d'une chaine de caractères
    ul = StringTemplate('<ul>{{items}}</ul>')
    items = ''
    for item in flat_list:
        items += '<li class="shopping-item">{item}</li>\n'.format(item=item)
    
    return ul.render(context={'items' : items})

### Exercice 1 de génération de HTML (liste simple)
def commission_simple():
    doc = FileTemplate('base.html')
    html = doc.render(context={
        'title' : 'Liste de commission simple',
        'content' : simple_list(commissions)
    })
    return html
    
print(commission_simple())