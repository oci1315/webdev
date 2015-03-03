from template import FileTemplate

def write_to_file(filename, html):
    with open(filename, 'w', encoding='utf-8') as fd:
        fd.write(html)
        
def base_html(title):
    # chargement du template à partir d'un fichier externe
    doc = FileTemplate('base.html')
    return doc.render_to_template(context={'title' : title})