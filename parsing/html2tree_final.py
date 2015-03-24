from html.parser import HTMLParser

from csudoci.ds.stack import Stack
from csudoci.html.html import E, T

class HTMLParseError(Exception):

    def __init__(self, msg='Balise manquante, HTML non conforme'):
        Exception.__init__(self, msg)

class HTMLTreeParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.stack = Stack()

    def handle_starttag(self, tag, attrs):
        attr_dict = {}
        for (attr, value) in attrs:
            attr_dict[attr] = value
            
        self.stack.push(E(tag, attr_dict))


    def handle_endtag(self, tag):        
        # Lorsqu'on rencontre une balise fermante, il faut fabriquer
        # un arbre avec tous les éléments qui se trouvent sur la pile
        # jusqu'à ce qu'on rencontre la balise ouvrante qui devra être
        # la racine de cet arbre. On suppose que le code HTML est
        # correctement équilibré en balises

        # la pile tmp_stack est utilisée pour rétablir l'ordre inversé
        # des sous-arbres qui sont remis sur la pile
        tmp_stack = Stack()

        # flag qui indique si la balise ouvrante se trouve au sommet
        # de la pile. Il faut déjà faire la vérification avant
        # d'essayer de dépiler des éléments
        top = self.stack.peek()
        opening_tag_on_top = (top.tag == tag)

        # on dépile tous les éléments jusqu'à ce qu'on rencontre au
        # sommet de la pile la balise ouvrante correspondant à la
        # balise fermante actuellement traitée.
        while not opening_tag_on_top:
            tmp = self.stack.pop()
            tmp_stack.push(tmp)

            # on utilise un bloc try, car il se peut que top soit un
            # objet de type Text (qui ne possède pas d'attribut
            # tagname)
            try:
                top = self.stack.peek()
                opening_tag_on_top = (top.tag == tag)
            except:
                pass
                

        # il faut construire un arbre dont la racine est la balise du
        # sommet de la pile et dont les sous-arbres sont les arbres
        # qui se trouvent sur la pile tmp_stack
        tree = self.stack.pop()

        while not tmp_stack.is_empty():
            tree.add_child(tmp_stack.pop())

        self.stack.push(tree)
        

    def handle_startendtag(self, tag, attrs):
        attr_dict = {}
        for (attr, value) in attrs:
            attr_dict[attr] = value

        self.stack.push(E(tag, attr_dict))

    def handle_data(self, data):
        self.stack.push(T(data))

    def get_tree(self):
        if self.stack.size() == 1:
            return self.stack.pop()
        else:
            raise HTMLParseError("La pile ne pas contient l'arbre à son sommet")

# test
def test(html):
    p = HTMLTreeParser()
    p.feed(html)

    p.get_tree().draw()
    

test('<ul><li>Texte 1</li><li>Texte 2</li></ul>')
test('<ul><li><p class="salut" id="special">Du texte</p></li></ul>')
test('<ul><li><p class="salut">Du texte</p><img src="image.jpeg" /></li></ul>')
    
