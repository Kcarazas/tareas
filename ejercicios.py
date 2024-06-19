data = [
    (73, 'Federer R.'), (71, 'Roddick A.'), (67, 'Schuettler R.'), (62, 'Ferrero J.C.'),
    (61, 'Coria G.'), (51, 'Moya C.'), (47, 'Agassi A.'), (43, 'Srichaphan P.'),
    (41, 'Novak J.'), (40, 'Kuerten G.'), (70, 'Federer R.'), (66, 'Roddick A.'),
    (64, 'Hewitt L.'), (53, 'Moya C.'), (50, 'Safin M.'), (42, 'Srichaphan P.'),
    (41, 'Henman T.'), (40, 'Hrbaty D.'), (40, 'Canas G.'), (39, 'Spadea V.')
]

jugadores_unicos = []  # Lista para almacenar nombres únicos

for tupla in data:
    nombre = tupla[1]
    if nombre not in jugadores_unicos:
        jugadores_unicos.append(nombre)

cantidad_personas = len(jugadores_unicos)

print(f"Hay {cantidad_personas} personas sin repeticiones en la lista.")