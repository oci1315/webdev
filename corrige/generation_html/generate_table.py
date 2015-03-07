#!/usr/bin/python3

###
## OCI 4 : Module ?? : applications Web
## Section : Génération de code HTML (tableaux)
## URL : http://donner-online.ch/oci/manuel/exo_02_generation_tableau.html
## année : 2014 - 2015

from template import FileTemplate, StringTemplate
from utils import *
from donnee import TableExo
from html import *

def generate_table_02(headers, products):

    thead = E( [ Text(field) < Th() for field in headers ] ) < Tr() < THead()
    tbody = TBody()
    for product in products:
        E( [ Text(field) < Td() for field in product ] ) < Tr() < tbody

    table = E([thead, tbody]) < Table({
        'id' : "livres",
        'class' : "produits"
    })
    
    return table

def main():        
    headers = TableExo.headers
    products = TableExo.products
    print(generate_table_02(headers, products).html(minify=True))


if __name__ == '__main__':
    main()