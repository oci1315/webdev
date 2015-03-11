
'''

html.py : API de génération de HTML en construisant la représentation arborescente

TODO
====

*   Il faudrait encore distinguer entre les éléments qui peuvent contenir des fils
    et les éléments "terminaux" qui ne peuvent contenir aucun élément, comme les 

'''

oneline_elements = [
    'th', 'td', 'li', 'span', 'b', 'i', 'u', 'em', 'strong', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'title', 
]




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
        # indique contenu de l'élément
        self.content_text = None
        
        # cette condition doit être réécrite ... il y a d'autres tags à 
        # écrire que sur une ligne
        if self.tag in oneline_elements:
            self.oneline = True
        
    def __str__(self):
        return 'Element({tag}, {attrs}) > ({childs})'.format(
            tag=self.tag,
            attrs=self.attrs,
            childs=' + '.join([str(c) for c in self.childs]),
        )
        
    def text(self, content_text=None):
        if content_text is None:
            return self.content_text
        else:
            self.content_text = str(content_text)
            # pour permettre le chaînage
            return self
        
    def html_attrs(self, attrs=None):
        attrs = attrs or self.attrs
        #print("attrs : ", attrs, self.attrs, self)
        if len(attrs) == 0:
            return ''
        else:
            return ' ' + ' '.join(['{attr}="{value}"'.format(attr=attr, value=value) for (attr, value) in attrs.items()])
        
    def html(self, indent=0, minify=False):
        
        if self.void:
            template = '{startindent}<{tag}{attrs} />'
        else:
            template = '{startindent}<{tag}{attrs}>{cr}{content}{cr}{endindent}</{tag}>'

        if minify or self.oneline:
            cr = ''
        else:
            cr= '\n'
            
        content = cr.join([child.html(indent=indent+1, minify=minify) for child in self.childs])
        
        char_indent = indent*'   '
            
        if self.content_text:
            if not self.oneline and not minify:
                content += char_indent + '   '
            content += self.content_text
            
                
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
            
    def __add__(self, siblings):
        if isinstance(siblings, list):
            return ElementList([self] + siblings)
        else:
            return ElementList([self] + [siblings])
        
            
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
        self.elements = [e for e in elements if e is not None]
        
    def __lt__(self, parent):
        for e in self.elements:
            e.add_to(parent)
        return parent
        
        
    def html(self, *args, **kwargs):
        return '\n'.join([e.html(*args, **kwargs) for e in self.elements])
        
        
# class L(list):
    

#     def __lshift__(self, parent):
#         for e in self:
#             e.add_to(parent)
#         return parent
        
        
#     def html(self, *args, **kwargs):
#         return '\n'.join([e.html(*args, **kwargs) for e in self.elements])  
        
# import builtins
# builtins.list = L
        
        
html_elements = [
    'a',
    'abbr',
    'acronym',
    'address',
    'applet',
    'area',
    'article',
    'aside',
    'audio',
    'b',
    'base',
    'basefont',
    'bdi',
    'bdo',
    'bgsound',
    'big',
    'blink',
    'blockquote',
    'body',
    'br',
    'button',
    'canvas',
    'caption',
    'center',
    'cite',
    'code',
    'col',
    'colgroup',
    'content',
    'data',
    'datalist',
    'dd',
    'decorator',
    'del',
    'details',
    'dfn',
    'dir',
    'div',
    'dl',
    'dt',
    'element',
    'em',
    'embed',
    'fieldset',
    'figcaption',
    'figure',
    'font',
    'footer',
    'form',
    'frame',
    'frameset',
    'h1',
    'h2',
    'h3',
    'h4',
    'h5',
    'h6',
    'head',
    'header',
    'hgroup',
    'hr',
    'html',
    'i',
    'iframe',
    'img',
    'input',
    'ins',
    'isindex',
    'kbd',
    'keygen',
    'label',
    'legend',
    'li',
    'link',
    'listing',
    'main',
    'map',
    'mark',
    'marquee',
    'menu',
    'menuitem',
    'meta',
    'meter',
    'nav',
    'nobr',
    'noframes',
    'noscript',
    'object',
    'ol',
    'optgroup',
    'option',
    'output',
    'p',
    'param',
    'plaintext',
    'pre',
    'progress',
    'q',
    'rp',
    'rt',
    'ruby',
    's',
    'samp',
    'script',
    'section',
    'select',
    'shadow',
    'small',
    'source',
    'spacer',
    'span',
    'strike',
    'strong',
    'style',
    'sub',
    'summary',
    'sup',
    'table',
    'tbody',
    'td',
    'template',
    'textarea',
    'tfoot',
    'th',
    'thead',
    'time',
    'title',
    'tr',
    'track',
    'tt',
    'u',
    'ul',
    'var',
    'video',
    'wbr',
    'xmp',
]

void_elements = [
    'area', 
    'base', 
    'br', 
    'col', 
    'embed', 
    'hr', 
    'img', 
    'input', 
    'keygen', 
    'link', 
    'meta', 
    'param', 
    'source', 
    'track', 
    'wbr', 
]



class A (E):
    
    def __init__(self, attrs=None):
        super().__init__('a', attrs, void=False)

class Abbr (E):
    
    def __init__(self, attrs=None):
        super().__init__('abbr', attrs, void=False)

class Acronym (E):
    
    def __init__(self, attrs=None):
        super().__init__('acronym', attrs, void=False)

class Address (E):
    
    def __init__(self, attrs=None):
        super().__init__('address', attrs, void=False)

class Applet (E):
    
    def __init__(self, attrs=None):
        super().__init__('applet', attrs, void=False)

class Area (E):
    
    def __init__(self, attrs=None):
        super().__init__('area', attrs, void=True)

class Article (E):
    
    def __init__(self, attrs=None):
        super().__init__('article', attrs, void=False)

class Aside (E):
    
    def __init__(self, attrs=None):
        super().__init__('aside', attrs, void=False)

class Audio (E):
    
    def __init__(self, attrs=None):
        super().__init__('audio', attrs, void=False)

class B (E):
    
    def __init__(self, attrs=None):
        super().__init__('b', attrs, void=False)

class Base (E):
    
    def __init__(self, attrs=None):
        super().__init__('base', attrs, void=True)

class Basefont (E):
    
    def __init__(self, attrs=None):
        super().__init__('basefont', attrs, void=False)

class Bdi (E):
    
    def __init__(self, attrs=None):
        super().__init__('bdi', attrs, void=False)

class Bdo (E):
    
    def __init__(self, attrs=None):
        super().__init__('bdo', attrs, void=False)

class Bgsound (E):
    
    def __init__(self, attrs=None):
        super().__init__('bgsound', attrs, void=False)

class Big (E):
    
    def __init__(self, attrs=None):
        super().__init__('big', attrs, void=False)

class Blink (E):
    
    def __init__(self, attrs=None):
        super().__init__('blink', attrs, void=False)

class Blockquote (E):
    
    def __init__(self, attrs=None):
        super().__init__('blockquote', attrs, void=False)

class Body (E):
    
    def __init__(self, attrs=None):
        super().__init__('body', attrs, void=False)

class Br (E):
    
    def __init__(self, attrs=None):
        super().__init__('br', attrs, void=True)

class Button (E):
    
    def __init__(self, attrs=None):
        super().__init__('button', attrs, void=False)

class Canvas (E):
    
    def __init__(self, attrs=None):
        super().__init__('canvas', attrs, void=False)

class Caption (E):
    
    def __init__(self, attrs=None):
        super().__init__('caption', attrs, void=False)

class Center (E):
    
    def __init__(self, attrs=None):
        super().__init__('center', attrs, void=False)

class Cite (E):
    
    def __init__(self, attrs=None):
        super().__init__('cite', attrs, void=False)

class Code (E):
    
    def __init__(self, attrs=None):
        super().__init__('code', attrs, void=False)

class Col (E):
    
    def __init__(self, attrs=None):
        super().__init__('col', attrs, void=True)

class Colgroup (E):
    
    def __init__(self, attrs=None):
        super().__init__('colgroup', attrs, void=False)

class Content (E):
    
    def __init__(self, attrs=None):
        super().__init__('content', attrs, void=False)

class Data (E):
    
    def __init__(self, attrs=None):
        super().__init__('data', attrs, void=False)

class Datalist (E):
    
    def __init__(self, attrs=None):
        super().__init__('datalist', attrs, void=False)

class Dd (E):
    
    def __init__(self, attrs=None):
        super().__init__('dd', attrs, void=False)

class Decorator (E):
    
    def __init__(self, attrs=None):
        super().__init__('decorator', attrs, void=False)

class Del (E):
    
    def __init__(self, attrs=None):
        super().__init__('del', attrs, void=False)

class Details (E):
    
    def __init__(self, attrs=None):
        super().__init__('details', attrs, void=False)

class Dfn (E):
    
    def __init__(self, attrs=None):
        super().__init__('dfn', attrs, void=False)

class Dir (E):
    
    def __init__(self, attrs=None):
        super().__init__('dir', attrs, void=False)

class Div (E):
    
    def __init__(self, attrs=None):
        super().__init__('div', attrs, void=False)

class Dl (E):
    
    def __init__(self, attrs=None):
        super().__init__('dl', attrs, void=False)

class Dt (E):
    
    def __init__(self, attrs=None):
        super().__init__('dt', attrs, void=False)

class Element (E):
    
    def __init__(self, attrs=None):
        super().__init__('element', attrs, void=False)

class Em (E):
    
    def __init__(self, attrs=None):
        super().__init__('em', attrs, void=False)

class Embed (E):
    
    def __init__(self, attrs=None):
        super().__init__('embed', attrs, void=True)

class Fieldset (E):
    
    def __init__(self, attrs=None):
        super().__init__('fieldset', attrs, void=False)

class Figcaption (E):
    
    def __init__(self, attrs=None):
        super().__init__('figcaption', attrs, void=False)

class Figure (E):
    
    def __init__(self, attrs=None):
        super().__init__('figure', attrs, void=False)

class Font (E):
    
    def __init__(self, attrs=None):
        super().__init__('font', attrs, void=False)

class Footer (E):
    
    def __init__(self, attrs=None):
        super().__init__('footer', attrs, void=False)

class Form (E):
    
    def __init__(self, attrs=None):
        super().__init__('form', attrs, void=False)

class Frame (E):
    
    def __init__(self, attrs=None):
        super().__init__('frame', attrs, void=False)

class Frameset (E):
    
    def __init__(self, attrs=None):
        super().__init__('frameset', attrs, void=False)

class H1 (E):
    
    def __init__(self, attrs=None):
        super().__init__('h1', attrs, void=False)

class H2 (E):
    
    def __init__(self, attrs=None):
        super().__init__('h2', attrs, void=False)

class H3 (E):
    
    def __init__(self, attrs=None):
        super().__init__('h3', attrs, void=False)

class H4 (E):
    
    def __init__(self, attrs=None):
        super().__init__('h4', attrs, void=False)

class H5 (E):
    
    def __init__(self, attrs=None):
        super().__init__('h5', attrs, void=False)

class H6 (E):
    
    def __init__(self, attrs=None):
        super().__init__('h6', attrs, void=False)

class Head (E):
    
    def __init__(self, attrs=None):
        super().__init__('head', attrs, void=False)

class Header (E):
    
    def __init__(self, attrs=None):
        super().__init__('header', attrs, void=False)

class Hgroup (E):
    
    def __init__(self, attrs=None):
        super().__init__('hgroup', attrs, void=False)

class Hr (E):
    
    def __init__(self, attrs=None):
        super().__init__('hr', attrs, void=True)

class Html (E):
    
    def __init__(self, attrs=None):
        super().__init__('html', attrs, void=False)

class I (E):
    
    def __init__(self, attrs=None):
        super().__init__('i', attrs, void=False)

class Iframe (E):
    
    def __init__(self, attrs=None):
        super().__init__('iframe', attrs, void=False)

class Img (E):
    
    def __init__(self, attrs=None):
        super().__init__('img', attrs, void=True)

class Input (E):
    
    def __init__(self, attrs=None):
        super().__init__('input', attrs, void=True)

class Ins (E):
    
    def __init__(self, attrs=None):
        super().__init__('ins', attrs, void=False)

class Isindex (E):
    
    def __init__(self, attrs=None):
        super().__init__('isindex', attrs, void=False)

class Kbd (E):
    
    def __init__(self, attrs=None):
        super().__init__('kbd', attrs, void=False)

class Keygen (E):
    
    def __init__(self, attrs=None):
        super().__init__('keygen', attrs, void=True)

class Label (E):
    
    def __init__(self, attrs=None):
        super().__init__('label', attrs, void=False)

class Legend (E):
    
    def __init__(self, attrs=None):
        super().__init__('legend', attrs, void=False)

class Li (E):
    
    def __init__(self, attrs=None):
        super().__init__('li', attrs, void=False)

class Link (E):
    
    def __init__(self, attrs=None):
        super().__init__('link', attrs, void=True)

class Listing (E):
    
    def __init__(self, attrs=None):
        super().__init__('listing', attrs, void=False)

class Main (E):
    
    def __init__(self, attrs=None):
        super().__init__('main', attrs, void=False)

class Map (E):
    
    def __init__(self, attrs=None):
        super().__init__('map', attrs, void=False)

class Mark (E):
    
    def __init__(self, attrs=None):
        super().__init__('mark', attrs, void=False)

class Marquee (E):
    
    def __init__(self, attrs=None):
        super().__init__('marquee', attrs, void=False)

class Menu (E):
    
    def __init__(self, attrs=None):
        super().__init__('menu', attrs, void=False)

class Menuitem (E):
    
    def __init__(self, attrs=None):
        super().__init__('menuitem', attrs, void=False)

class Meta (E):
    
    def __init__(self, attrs=None):
        super().__init__('meta', attrs, void=True)

class Meter (E):
    
    def __init__(self, attrs=None):
        super().__init__('meter', attrs, void=False)

class Nav (E):
    
    def __init__(self, attrs=None):
        super().__init__('nav', attrs, void=False)

class Nobr (E):
    
    def __init__(self, attrs=None):
        super().__init__('nobr', attrs, void=False)

class Noframes (E):
    
    def __init__(self, attrs=None):
        super().__init__('noframes', attrs, void=False)

class Noscript (E):
    
    def __init__(self, attrs=None):
        super().__init__('noscript', attrs, void=False)

class Object (E):
    
    def __init__(self, attrs=None):
        super().__init__('object', attrs, void=False)

class Ol (E):
    
    def __init__(self, attrs=None):
        super().__init__('ol', attrs, void=False)

class Optgroup (E):
    
    def __init__(self, attrs=None):
        super().__init__('optgroup', attrs, void=False)

class Option (E):
    
    def __init__(self, attrs=None):
        super().__init__('option', attrs, void=False)

class Output (E):
    
    def __init__(self, attrs=None):
        super().__init__('output', attrs, void=False)

class P (E):
    
    def __init__(self, attrs=None):
        super().__init__('p', attrs, void=False)

class Param (E):
    
    def __init__(self, attrs=None):
        super().__init__('param', attrs, void=True)

class Plaintext (E):
    
    def __init__(self, attrs=None):
        super().__init__('plaintext', attrs, void=False)

class Pre (E):
    
    def __init__(self, attrs=None):
        super().__init__('pre', attrs, void=False)

class Progress (E):
    
    def __init__(self, attrs=None):
        super().__init__('progress', attrs, void=False)

class Q (E):
    
    def __init__(self, attrs=None):
        super().__init__('q', attrs, void=False)

class Rp (E):
    
    def __init__(self, attrs=None):
        super().__init__('rp', attrs, void=False)

class Rt (E):
    
    def __init__(self, attrs=None):
        super().__init__('rt', attrs, void=False)

class Ruby (E):
    
    def __init__(self, attrs=None):
        super().__init__('ruby', attrs, void=False)

class S (E):
    
    def __init__(self, attrs=None):
        super().__init__('s', attrs, void=False)

class Samp (E):
    
    def __init__(self, attrs=None):
        super().__init__('samp', attrs, void=False)

class Script (E):
    
    def __init__(self, attrs=None):
        super().__init__('script', attrs, void=False)

class Section (E):
    
    def __init__(self, attrs=None):
        super().__init__('section', attrs, void=False)

class Select (E):
    
    def __init__(self, attrs=None):
        super().__init__('select', attrs, void=False)

class Shadow (E):
    
    def __init__(self, attrs=None):
        super().__init__('shadow', attrs, void=False)

class Small (E):
    
    def __init__(self, attrs=None):
        super().__init__('small', attrs, void=False)

class Source (E):
    
    def __init__(self, attrs=None):
        super().__init__('source', attrs, void=True)

class Spacer (E):
    
    def __init__(self, attrs=None):
        super().__init__('spacer', attrs, void=False)

class Span (E):
    
    def __init__(self, attrs=None):
        super().__init__('span', attrs, void=False)

class Strike (E):
    
    def __init__(self, attrs=None):
        super().__init__('strike', attrs, void=False)

class Strong (E):
    
    def __init__(self, attrs=None):
        super().__init__('strong', attrs, void=False)

class Style (E):
    
    def __init__(self, attrs=None):
        super().__init__('style', attrs, void=False)

class Sub (E):
    
    def __init__(self, attrs=None):
        super().__init__('sub', attrs, void=False)

class Summary (E):
    
    def __init__(self, attrs=None):
        super().__init__('summary', attrs, void=False)

class Sup (E):
    
    def __init__(self, attrs=None):
        super().__init__('sup', attrs, void=False)

class Table (E):
    
    def __init__(self, attrs=None):
        super().__init__('table', attrs, void=False)

class Tbody (E):
    
    def __init__(self, attrs=None):
        super().__init__('tbody', attrs, void=False)

class Td (E):
    
    def __init__(self, attrs=None):
        super().__init__('td', attrs, void=False)

class Template (E):
    
    def __init__(self, attrs=None):
        super().__init__('template', attrs, void=False)

class Textarea (E):
    
    def __init__(self, attrs=None):
        super().__init__('textarea', attrs, void=False)

class Tfoot (E):
    
    def __init__(self, attrs=None):
        super().__init__('tfoot', attrs, void=False)

class Th (E):
    
    def __init__(self, attrs=None):
        super().__init__('th', attrs, void=False)

class Thead (E):
    
    def __init__(self, attrs=None):
        super().__init__('thead', attrs, void=False)

class Time (E):
    
    def __init__(self, attrs=None):
        super().__init__('time', attrs, void=False)

class Title (E):
    
    def __init__(self, attrs=None):
        super().__init__('title', attrs, void=False)

class Tr (E):
    
    def __init__(self, attrs=None):
        super().__init__('tr', attrs, void=False)

class Track (E):
    
    def __init__(self, attrs=None):
        super().__init__('track', attrs, void=True)

class Tt (E):
    
    def __init__(self, attrs=None):
        super().__init__('tt', attrs, void=False)

class U (E):
    
    def __init__(self, attrs=None):
        super().__init__('u', attrs, void=False)

class Ul (E):
    
    def __init__(self, attrs=None):
        super().__init__('ul', attrs, void=False)

class Var (E):
    
    def __init__(self, attrs=None):
        super().__init__('var', attrs, void=False)

class Video (E):
    
    def __init__(self, attrs=None):
        super().__init__('video', attrs, void=False)

class Wbr (E):
    
    def __init__(self, attrs=None):
        super().__init__('wbr', attrs, void=True)

class Xmp (E):
    
    def __init__(self, attrs=None):
        super().__init__('xmp', attrs, void=False)
