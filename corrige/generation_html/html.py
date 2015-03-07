class Element(object):
    
    def __init__(self, attrs=None, void=False):

        # dictionnaire des attributs de l'élément
        self.attrs = attrs or {}
        # Les "void elements" sont les éléments du type img, hr, br, meta ...
        # qui n'ont pas de balise fermante
        self.void = void
        # balise correspondant à l'élément
        self.tag = None
        # une liste des éléments enfants dans l'arbre DOM
        self.childs = []
        # référence à l'élément parent dans l'arbre DOM
        self.parent = None
        # référence à la racine de l'arbre ... ne fonctionne pas vraiment
        self.root = self
        
    def __str__(self):
        return 'Element({tag}, {attrs}) > ({childs})'.format(
            tag=self.tag,
            attrs=self.attrs,
            childs=' + '.join([str(c) for c in self.childs]),
        )
        
    def html_attrs(self, attrs=None):
        attrs = attrs or self.attrs
        #print("attrs : ", attrs, self.attrs, self)
        if len(attrs) == 0:
            return ''
        else:
            return ' ' + ' '.join(['{attr}="{value}"'.format(attr=attr, value=value) for (attr, value) in attrs.items()])
        
    def html(self, indent=0, minify=False):
        
        # print('html(): tag', self.tag)

        if self.void:
            template = '<{tag}{attrs} />'
        else:
            template = '{indent}<{tag}{attrs}>{cr}{content}{cr}{indent}</{tag}>'

        if minify:
            cr = ''
            char_indent = ''
        else:
            cr= '\n'
            char_indent = indent*'   '
            
        content = cr.join([child.html(indent=indent+1, minify=minify) for child in self.childs])
            
        html_string = template.format(
            tag=self.tag,
            attrs=self.html_attrs(),
            content=content,
            indent=char_indent,
            cr=cr
        )
        
        #print(html_string)
        
        return html_string

        
    def _add_child(self, child):
        child.parent = self
        child.root = self.root 
        self.childs.append(child)
        
    def _add_childs(self, childs):
        # print(childs)
        for c in childs:
            c.parent = self
            c.root = self.root
        self.childs += childs
        
    def _add_to(self, parent):
        parent._add_child(self)
        return parent
        
    def __lt__(self, parent):
        return self._add_to(parent)
        
    def __gt__(self, childs):
        if isinstance(childs, list):
            self._add_childs(childs)
            return self
        else:
            self._add_child(childs)
            return childs
        
            
class Text(Element):
    
    def __init__(self, text):
        super().__init__(self)
        self.text = text

    def html(self, indent=0, minify=False):
        return indent*'   ' + self.text
        
    def __str__(self):
        return 'Text("{text}")'.format(text=self.text)


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
        
        
class E(object):
    
    def __init__(self, elements):
        self.elements = elements
        
    def _from_generator(self, generator):
        try:
            while True:
                self.elements.append(next(generator))
        except:
            pass
        

    def __lt__(self, parent):
        for e in self.elements:
            e._add_to(parent)
        return parent