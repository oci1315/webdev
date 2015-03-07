#!/usr/bin/python3

from template import FileTemplate, StringTemplate
from utils import *
from donnee import TableExo



###
## OCI 4 : Module 6 : applications Web
## Section : Génération de code HTML (tableaux)
## URL : http://donner-online.ch/oci/manuel/exo_02_generation_tableau.html
## année : 2012 - 2013

class Element(object):
    
    def __init__(self, attrs=None, void=False):

        self.attrs = attrs or {}
        self.void = void
        self.tag = None
        self.childs = []
        
    def __str__(self):
        return 'Element({tag}, {attrs})'.format(tag=self.tag, attrs=self.attrs)
        
    def html_attrs(self, attrs=None):
        attrs = attrs or self.attrs
        print("attrs : ", attrs, self.attrs, self)
        return ' '.join(['{attr}="{value}"'.format(attr, value) for (attr, value) in attrs.items()])
        
    def html(self):

        if self.void:
            template = '<{tag} {attrs} />'
        else:
            template = '<{tag} {attrs}>{content}</{tag}>'

        content = '\n'.join([child.html() for child in self.childs])
            
        html_string = template.format(
            tag=self.tag,
            attrs=self.html_attrs(),
            content=content
        )
        
        print(html_string)
        
        return html_string

        
    def _add_child(self, child):
        self.childs.append(child)
        
    def _add_childs(self, childs):
        self.childs += childs
        
    def __gt__(self, childs):
        if isinstance(childs, list):
            self._add_childs(childs)
            return childs[-1]
        else:
            self._add_child(childs)
            return childs
            
class Text(object):
    
    def __init__(self, text):
        self.text = text
        
    def html(self):
        return self.text


class Table(Element):
    
    def __init__(self, attrs=None):
        super().__init__(attrs)
        self.tag = 'table'
        
class THead(Element):
    
    def __init__(self, attrs=None):
        super().__init__(attrs)
        self.tag = 'thead'
        
class TBody(Element):
    
    def __init__(self, attrs=None):
        super().__init__(attrs)
        self.tag = 'tbody'
        
class Tr(Element):
    
    def __init__(self, attrs=None):
        super().__init__(attrs)
        self.tag = 'tr'
        
class Th(Element):
    
    def __init__(self, attrs=None):
        super().__init__(attrs)
        self.tag = 'th'
        
class Td(Element):
    
    def __init__(self, attrs=None):
        super().__init__(attrs)
        self.tag = 'td'
        
        
headers = ['Colonne 1', 'Colonne 2']
products = [
    ('Genèse', '1'),
    ('Deutéronome', '2'),
]


thead = THead() > Tr() > [Th() > Text(field) for field in headers]
tbody = TBody() > [Tr() > [Td() > Text(field) for field in product] for product in products]

print(thead)

table = Table({
    'id' : "livres",
    'class' : "produits"
}) > [thead, tbody]

print(table.html())