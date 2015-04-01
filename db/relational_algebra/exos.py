client = [
    {'client.no_client': 1, 'client.prenom': 'Alan', 'client.nom': 'Turing'},
    {'client.no_client': 2, 'client.prenom': 'Arthur', 'client.nom': 'Honegger'},
    {'client.no_client': 3, 'client.prenom': 'Leonhard', 'client.nom': 'Euler'},
    {'client.no_client': 4, 'client.prenom': 'Berhard', 'client.nom': 'Riemann'},
    {'client.no_client': 5, 'client.prenom': 'John', 'client.nom': 'von Neuman'}
]

possession = [
    {'possession.no_compte': 1, 'possession.no_client': 1},
    {'possession.no_compte': 1, 'possession.no_client': 2},
    {'possession.no_compte': 2, 'possession.no_client': 1},
    {'possession.no_compte': 3, 'possession.no_client': 2},
    {'possession.no_compte': 4, 'possession.no_client': 1},
    {'possession.no_compte': 5, 'possession.no_client': 4},
    {'possession.no_compte': 6, 'possession.no_client': 2},
    {'possession.no_compte': 7, 'possession.no_client': 2},
    {'possession.no_compte': 8, 'possession.no_client': 1},
    {'possession.no_compte': 9, 'possession.no_client': 4},
    {'possession.no_compte': 10, 'possession.no_client': 1},
    {'possession.no_compte': 11, 'possession.no_client': 3}
]

def show_table(table):
    try:
        print(tuple(table[0].keys()))
        for r in table:
            print(tuple(r.values()))
    except:
        pass
    
def cartprod(table1, table2):
    result_table = []

    for r1 in table1:
        for r2 in table2:
            r= dict(list(r1.items())+ list(r2.items()))

            result_table.append(r)
            
    return result_table
    
    
def selection(table, condition):
    result_table = []

    for record in table:
        if condition(record):
            result_table.append(record)

    return result_table
    
    
def projection(table, fields):
    result_table = []

    for record in table:

        final_row = {}
        for (key, value) in record.items():
            if key in fields:
                final_row[key] = value

        # on ajoute la ligne à la table résultat une fois que la ligne
        # a été projetée sur les champs désirés
        result_table.append(final_row)

    return result_table
    
##########
## tests
##########
print('-- Question 2 : produit cartésien --')
grossetable = cartprod(client, possession)
show_table(grossetable)

print('-- Question 3 : sélection --')
def condition(record):
    return record['client.no_client'] > 2

resultat = selection(client, condition)
show_table(resultat)

print('-- Question 4 : projection --')
resultat = projection(client, fields=['client.nom', 'client.prenom'])
show_table(resultat)

