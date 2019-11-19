import argparse

def analyser_commande():
    parser = argparse.ArgumentParser(description = 'Jeu Quorridor - Phase 1')
    parser.add_argument("idul", metavar = 'idul', help = "IDUL du joueur")
    parser.add_argument("-l", "--lister", help="Lister les identifiants de vos 20 dernières parties.", action="store_true")
    return parser.parse_args()

def afficher_damier_ascii(forme):
    liste = [' ', ' ', '|', ' ', '1', ' ', ' ', ' ', '2', ' ', ' ', ' ', '3', ' ', ' ', ' ', '4', 
    ' ', ' ', ' ', '5', '   ', '6', ' ', ' ', ' ', '7', ' ', ' ', ' ', '8', ' ', ' ', ' ', '9', '  ']
    liste1 = [' ', ' ', '|', ' ', '.', ' ', ' ', ' ', '.', ' ', ' ', ' ', '.', ' ', ' ', ' ', '.',
    ' ', ' ', ' ', '.', ' ', ' ', ' ', '.', ' ', ' ', ' ', '.', ' ', ' ', ' ', '.', ' ', ' ', ' ', '.', ' |']
    liste2 = ['-', '-', '|', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
    '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '- ']
    liste3 = [' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
    ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' |']
    damier = [[]] * 20
    damier[0] = liste[:] 
    damier[1] = liste2[:]
    joueur = []
    for i in range(2, 20):
        if i % 2 == 0:
            liste1[0] = str(int(i / 2))
            damier[i] = liste1[:]
        elif i != 19 and i % 2 == 1:
            damier[i] = liste3[:]
        else:
            liste2[0] = ' '
            liste2[1] = ' '
            liste2[2] = ' '
            damier[i] = liste2[:]
    
    for i in forme.keys():
        if i == "joueurs":
            for j in [0, 1]:
                joueur.append(((forme[i])[j])["nom"])
                x = (((forme[i])[j])["pos"])[0]
                y = (((forme[i])[j])["pos"])[1]
                (damier[2 * y])[4 * x] = str(int(j + 1))
        if i == "murs":
            for k in forme[i]["horizontaux"]:
                if k[0] > 0 and k[0] < 9 and k[1] > 1 and k[1] <= 9:
                    for u in range(4 * k[0] - 1, 4 * (k[0] + 1) + 2):
                        (damier[2 * k[1] - 1])[u] = '-'
            for k in forme[i]["verticaux"]:
                if k[0] > 1 and k[0] <= 9 and k[1] > 0 and k[1] < 9:
                    (damier[2 * k[1]])[4 * k[0] - 2] = '|'
                    (damier[2 * k[1] + 1])[4 * k[0] - 2] = '|'
                    (damier[2 * k[1] + 2])[4 * k[0] - 2] = '|'
    print('Légende: 1={}, 2={}'.format(joueur[0], joueur[1]))
    print('\n\n'.join(''.join(damier[19 - i]) for i in range(20)))