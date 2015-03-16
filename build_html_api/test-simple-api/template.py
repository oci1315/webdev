#!/usr/bin/python3

class BaseTemplate(object):
    
    def __init__(self):
        # définition des variables d'instance
        self.html = ''
        self.rendered_html = ''

        
    def render(self, context):
        rendered_html = self.html
        
        for (var, value) in context.items():
            rendered_html = rendered_html.replace('{{%s}}' % str(var), str(value))
            
        self.rendered_html = rendered_html
        return self.rendered_html
        
    def render_to_template(self, context):
        ''' Au lieu de retourner une chaine, cette méthode retourne un template partiellement formaté '''
        return StringTemplate(html=self.render(context))
        
        
class StringTemplate(BaseTemplate):
    
    def __init__(self, html):
        super().__init__()
        self.html = html
        
        
class FileTemplate(BaseTemplate):
    
    def __init__(self, filepath):
        super().__init__()
        self.html = self.load_template(filepath)
        
    def load_template(self, file):
        html = ''
        
        with open(file, 'r', encoding='utf-8') as fd:
            html = fd.read()
            
        return html
        
        
def test():
    doc = StringTemplate('<p>{{content}}</p>')
    print(doc.render({'content' : 'contenu non vide'}))
    print(doc.render({}))

def main():
    test()
        
        
if __name__ == '__main__':
    main()