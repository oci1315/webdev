from html.parser import HTMLParser

from stack import Stack
from tree import Tree
from html_elements import Tag, SimpleTag, Text

class HTMLTreeParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.stack = Stack()

    def handle_starttag(self, tag, attrs):
        '''

        attrs : [(attr, valeur), (attr2, valeur)]

        ==> { 'attr' : 'valeur', attr2 : valeur }

        '''
        if len(attrs) > 0:
            attr_dict = {}
            for (attr, value) in attrs:
                attr_dict[attr] = value
        else:
            attr_dict = None
                
        
        self.stack.push(Tree(Tag(tag, attrs)))

    def handle_startendtag(self, tag, attrs):
        if len(attrs) > 0:
            attr_dict = {}
            for (attr, value) in attrs:
                attr_dict[attr] = value
        else:
            attr_dict = None

        self.stack.push(Tree(SimpleTag(tag, attrs)))
        

    def handle_endtag(self, tag):
        tmp_stack = Stack()

        top = self.stack.peek()
        opening_tag_on_top = (top.getRootVal().tagname == tag)

        while not opening_tag_on_top:
            tmp = self.stack.pop()
            tmp_stack.push(tmp)

            top = self.stack.peek()
            if top.getRootVal().tagname == tag:
                opening_tag_on_top = True
                
        tree = self.stack.pop()

        while not tmp_stack.is_empty():
            tree.insertSubTree(tmp_stack.pop())

        self.stack.push(tree)

    def handle_data(self, data):
        self.stack.push(Tree(Text(data)))

    def get_tree(self):    
        ''' retourne l'arbre HTML correspondant au code
            HTML indiqué par la méthode feed '''

        if self.stack.size() == 1:
            return self.stack.peek()
        else:
            return None

html_code = '<ul><li>Texte 1</li><li>Texte 2</li></ul>'
p = HTMLTreeParser()
p.feed(html_code)
html_tree = p.get_tree()
html_tree.draw()
