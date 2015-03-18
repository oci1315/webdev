## fichier utilisé pour montré la vérification de l'équilibre en
## balises du code HTML.

## va avec la section
## http://www.donner-online.ch/oci/manuel/html/html_parsing/html_parsing.html

from html.parser import HTMLParser
from stack import Stack

class CheckBalancedHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)

        self.stack = Stack()
        self.balanced = True


    def handle_starttag(self, tag, attrs):
        self.stack.push(tag)


    def handle_endtag(self, tag):
        if not self.stack.is_empty() and self.stack.peek() == tag:
            self.stack.pop()
        else:
            self.balanced = False


    def handle_startendtag(self, tag, attrs):
        pass


    def handle_data(self, data):
        pass


    def is_balanced(self):
        if not self.stack.is_empty():
            self.balanced = False

        return self.balanced

def test_balanced(html):

    p = CheckBalancedHTMLParser()
    p.feed(html)

    return p.is_balanced()

print(test_balanced(html='''<ul><li>du texte</li><li></li></ul>'''))
test_balanced(html='''<ul><li></li><li></ul>''')
test_balanced(html='''<ul><li></li></li></ul>''')
