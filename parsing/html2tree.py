from csudoci.ds.stack import Stack
from csudoci.html.html import *

from html.parser import HTMLParser

class HTMLTreeParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.stack = Stack()

    def handle_starttag(self, tag, attrs):
        self.stack.push(E(tag))

    def handle_endtag(self, tag):
        tmp_stack = Stack()

        top = self.stack.peek()
        opening_tag_on_top = (top.tag == tag)

        while not opening_tag_on_top:
            tmp = self.stack.pop()
            tmp_stack.push(tmp)

            top = self.stack.peek()
            if top.tag == tag:
                opening_tag_on_top = True

        tree = self.stack.pop()

        while not tmp_stack.is_empty():
            tree.add_child(tmp_stack.pop())

        self.stack.push(tree)

    def get_tree(self):
        ''' retourne l'arbre HTML correspondant au code
            HTML indiqué par la méthode feed '''

        if self.stack.size() == 1:
            return self.stack.peek()
        else:
            return None
            
def test(html):
    p = HTMLTreeParser()
    p.feed(html)

    p.get_tree().draw()

html_code = '<ul><li>Texte 1</li><li>Texte 2</li></ul>'
test(html_code)