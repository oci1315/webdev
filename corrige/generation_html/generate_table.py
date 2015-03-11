#!/usr/bin/python3

###
## OCI 4 : Module ?? : applications Web
## Section : Génération de code HTML (tableaux)
## URL : http://donner-online.ch/oci/webdev/...
## année : 2014 - 2015

from donnee import TableExo
from html import *

def generate_table_02_moche(headers, products):

    thead = ElementList( [ T(field) < E('th') for field in headers ] ) < E('tr') < E('thead')
    tbody = E('tbody')
    for product in products:
        ElementList( [ T(field) < E('td') for field in product ] ) < E('tr') < tbody

    table = ElementList([thead, tbody]) < E('table', {
        'id' : "livres",
        'class' : "produits"
    })
    
    return table
    
    
def generate_table_02(headers, products):

    thead = ElementList( [ Th().text(field) for field in headers ] ) < Tr() < Thead()
    tbody = Tbody()
    for product in products:
        ElementList( [ Td().text(field) for field in product ] ) < Tr() < tbody


    table = ElementList([thead, tbody]) < Table({
        'id' : "livres",
        'class' : "produits"
    })
    

    # content = H1().text('Titre de la page')
    # content += table + Img({'src' : 'http://image.com/1234'}) < Div({'class': 'inventaire'})
    
    # doc = ElementList([
    #     Meta({'charset': 'utf-8'}) + Title().text('Inventaire') < Head(),
    #     content < Body()
    # ]) < Html()

    # return doc
    
    return table

def main():        
    headers = TableExo.headers
    
    products = TableExo.products
    print(generate_table_02(headers, products).html(minify=False))


if __name__ == '__main__':
    main()