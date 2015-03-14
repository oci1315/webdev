
'''

OCI4 : Développement Web

Génération de HTML, entrainement
url : http://donner-online.ch/oci/webdev/generate/training/exos.html 

'''

from csudoci.html.html import *

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

print(generate_02(etudiants2))
