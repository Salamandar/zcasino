#!/usr/bin/env python3

# Exercice chapitre 1
# Jeu de la roulette

import os
from random import randrange
from math import ceil

from enum import Enum

class Couleur(Enum):
    noire = 0
    rouge = 1

    def __str__(self):
        return self.name

    @classmethod
    def _missing_(cls, value):
        return cls(value % 2)


def nouveauGain(pari, roulette, mise):
    if pari == roulette:
        gain=2
    elif Couleur(pari) == Couleur(roulette):
        gain=1.5
    else:
        gain=0
    return ceil(mise*gain)

def partieRoulette():
    # Somme misée
    mise=0
    while mise<=0:
        mise = input("""Croupier - Saisissez une mise entière en dollars \n  """)
        try:
            mise = int(mise)
            assert mise>0
        except ValueError:
            print("""Vous devez taper un nombre entier positif""")
            mise = 0
            continue
        except AssertionError:
            print("""Vous devez taper un nombre entier positif""")
            continue

    # Choix de la case de la roulette
    pari=50
    while pari<0 or pari>49:
        pari = input("""Croupier - Saisissez une case pour votre mise \n  """)
        try:
            pari = int(pari)
            assert pari>=0 and pari<=49
            print("Croupier - Votre case est donc", Couleur(pari))
        except ValueError:
            print("""la case pariée doit être un entier compris entre 0 et 49""")
            pari=50
            continue
        except AssertionError:
            print("""la case pariée doit être un entier compris entre 0 et 49""")
            continue


    # jeu de roulette
    result = randrange(49)
    print("Croupier - Le résultat de la roulette est", result, "qui est", Couleur(result))
    mise = nouveauGain(pari, result, mise)
    if mise:
        print("""Vous avez gagné """, mise, """$""")
    else:
        print("""Désolé, vous avez perdu votre mise entière""")


# début main
if __name__ == "__main__":
    encoreJouer = "Y"
    print("""Croupier - Bienvenu à ce jeu de roulette\n""")
    while encoreJouer in "Yy":
        partieRoulette()
        encoreJouer = input("""\nEncore jouer ? Y ou N ? \n  """)
    print("""Croupier - Au revoir\n""")
    os.system("pause")
