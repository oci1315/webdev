
'''

OCI4 : Développement Web

Génération de HTML, entrainement
url : http://donner-online.ch/oci/webdev/generate/training/exos.html 

'''

from csudoci.html.html import *
from csudoci.html.template import FileTemplate
from utils import write_to_file

class Etudiant(object):

    def __init__(self, prenom, nom):

        self.prenom = prenom
        self.nom = nom

etudiants2 = [
    Etudiant('Guido', 'Van Rossum'),
    Etudiant('Albert', 'Einstein'),
    Etudiant('Berhard', 'Riemann'),
    Etudiant('Leonhard', 'Euler'),
    Etudiant('Allan', 'Turing'),
]

def generate_02(etudiants):
    ul = Ul({'class' : 'etudiants'})
    for etudiant in etudiants:
        ElementList([
            Span({'class' : 'prenom'}).text(etudiant.prenom),
            T(' '),
            Span({'class' : 'nom'}).text(etudiant.nom),
        ]) < Li() < ul

    return ul.html()
    
def full_page():
    title = 'Liste des étudiants'
    
    doc = FileTemplate('base.html')
    html = doc.render({
        'title' : title,
        'content' : generate_02(etudiants2)
    })
    write_to_file('output/liste_etudiants.html', html)

print(generate_02(etudiants2))
full_page()