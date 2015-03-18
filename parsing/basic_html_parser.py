from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    # méthode appelée lors de l'occurrence d'une balise ouvrante
    # exemple : <a href="http://www.donner-online.ch/">
    def handle_starttag(self, tag, attrs):
        print("J'ai rencontré la balise ouvrante :", tag,
              "avec les attributs : ", attrs)

    # méthode appelée lors de l'occurrence d'une balise fermante
    # exemple : </a>
    def handle_endtag(self, tag):
        print("J'ai rencontré la balise fermante :", tag)

    # méthode appelée lors de l'occurrence d'une balise ouvrante/fermante
    # exemple : <img src="image.jpeg" />
    # autres exemples : <hr />, <meta />
    def handle_startendtag(self, tag, attrs):
        print("J'ai rencontré une balise ouvrante/fermante", tag,
              "avec les attributs : ", attrs)

    # méthode appelée lors de données autres qu'une balise
    def handle_data(self, data):
        print("J'ai rencontré des données qui ne sont pas une balise  :", data)
        

### test

if __name__ == '__main__':
    parser = MyHTMLParser()
    html_code = '''<html>
<body>
<p class="introduction" id="exemple">
<img src="image.jpeg" />
</body>
</html>
'''
    parser.feed(html_code)
