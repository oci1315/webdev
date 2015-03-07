commissions = [
    'Salade', 
    'Pain', 
    'Orange', 
    'Poires', 
    'Jus de pomme', 
    'Fromage Gruyère', 
    'Chaussures', 
    'Oignons', 
]
    
commissions2 = [
    'Légumes',
        [
        'Salade',
        'carottes',
        'poireaux',
        ],
    'Fruits',
        [
            'Oranges',
            'Pommes',
            'Poires',
            'Mandarines',
        ],
    'Habits',
        [
        'Hommes',
            [
                'Pantalon',
                'Chaussures',
            ],
        'Dames',
            [
                'Robe',
                'hauts-talons',
                ],
        ],
]


class TableExo(object):
    
    headers = ['Identifiant', 'Titre', 'Type de reliure', 'Prix unitaire (CHF)']
    products = [ ('100', 'Le guide des vins 2005', 'cartonné', '50'),
                 ('200', 'Dieux du stade', 'cartonné', '100'),
                 ('300', 'Rupture de contrat', 'broché', '10'),
                 ('400', 'Pars vite et reviens tard', 'broché', '12'),
                 ('500', 'Panique au collège', 'broché', '7'),
                 ('600', 'Marketing management', 'spirales', '120'),
                 ('700', "L'art de la guerre", 'cartonné', '12'),
                 ('800', 'Excel pour le business et la finance', 'spirales', '75'),
                 ('900', '10 ans de leçon de séduction', 'cartonné', '60'),
                 ('1000', 'Autant en emporte le vent', 'cuir', '150')
                ]
                
