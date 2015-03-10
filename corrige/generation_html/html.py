class E(object):
    
    def __init__(self, tag, attrs=None, void=False):

        # dictionnaire des attributs de l'élément
        self.attrs = attrs or {}
        # Les "void elements" sont les éléments du type img, hr, br, meta ...
        # qui n'ont pas de balise fermante
        self.void = void
        # balise correspondant à l'élément
        self.tag = tag
        # une liste des éléments enfants dans l'arbre DOM
        self.childs = []
        # référence à l'élément parent dans l'arbre DOM
        self.parent = None
        # référence à la racine de l'arbre ... ne fonctionne pas vraiment
        self.root = self
        # indique si le tag doit être affiché sur une seule ligne (th, td, li, ...)
        self.oneline = False
        
        if self.tag in ['th', 'td', 'li', 'span', 'b', 'i', 'u', 'em', 'strong']:
            self.oneline = True
        
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
            template = '{startindent}<{tag}{attrs}>{cr}{content}{cr}{endindent}</{tag}>'

        if minify or self.oneline:
            cr = ''
        else:
            cr= '\n'
        char_indent = indent*'   '
            
        content = cr.join([child.html(indent=indent+1, minify=minify) for child in self.childs])
            
        html_string = template.format(
            tag=self.tag,
            attrs=self.html_attrs(),
            content=content,
            startindent=char_indent * int(not minify),
            endindent=char_indent * int(not minify and not self.oneline),
            cr=cr
        )
        
        return html_string

        
    def add_child(self, child):
        child.parent = self
        child.root = self.root 
        self.childs.append(child)
        
    def add_childs(self, childs):
        # print(childs)
        for c in childs:
            c.parent = self
            c.root = self.root
        self.childs += childs
        
    def add_to(self, parent):
        parent.add_child(self)
        return parent
        
    def __lt__(self, parent):
        return self.add_to(parent)
        
    def __gt__(self, childs):
        if isinstance(childs, list):
            self.add_childs(childs)
            return self
        else:
            self.add_child(childs)
            return childs
        
            
class T(E):
    
    def __init__(self, text):
        super().__init__(self)
        self.text = str(text)

    def html(self, indent=0, minify=False):
        if minify or self.parent.oneline:
            char_indent = ''
        else:
            char_indent = indent*'   '
        return char_indent + self.text
        
    def __str__(self):
        return 'Text("{text}")'.format(text=self.text)

        
        
class ElementList(object):
    
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
            e.add_to(parent)
        return parent