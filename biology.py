from json import *
import copy


def est_base(a):
    if a =="A" or a =="T" or a =="G" or a=="C" :
        return True
    else:
        return False




def est_adn(chaine):
    i=0
    b=0
    while i <len(chaine):
        if chaine[i]=="A" or chaine[i]=="T" or chaine[i]=="G" or chaine[i]=="C":
            b=b+1
            if b== len(chaine):
                return True
        else:
            return False
        i=i+1


def arn(ADN):
    i=0
    a=""

    if est_adn(ADN)== True:

        while i < len(ADN):

            if ADN[i]=="T":
                a=a+"U"
            else:
                a=a+ADN[i]

            i=i+1

        return a


    else:
        return None



def arn_to_codons(ARN):
    i=0
    b=""
    arn_codons=[]
    while i<len(ARN):
        b+=ARN[i]
        if len(b)%3==0:
            arn_codons.append(b)
            b=""
        i+=1
    return arn_codons


def load_dico_codons_aa(file):
    fichier =open(file,"r")
    strjson=fichier.read()
    fichier.close()
    cours = loads(strjson)
    return cours


def codons_stop(dico):

    a=["A","U","G","C"]
    i=0
    smart=0
    tableau=[]
    c=0
    delta=0
    augmenter=0


    while i < len(a):

        if len(tableau)%16==0:

            while smart < len(a):
                tableau.append(a[i]+a[c]+a[augmenter])
                augmenter=augmenter+1
                smart=smart+1

        else :

            while smart < len(a):


                tableau.append(a[i]*2+a[augmenter])
                augmenter=augmenter+1
                smart=smart+1



        while delta < len(a):
            augmenter=1


            tableau.append(a[i]+a[augmenter]+a[c])
            c=c+1
            delta=delta+1
        delta=0

        c=0

        while delta < len(a):
            augmenter=2
            tableau.append(a[i]+a[augmenter]+a[c])
            c=c+1
            delta=delta+1
        c=0
        delta=0

        while delta < len(a):
            augmenter=3
            tableau.append(a[i]+a[augmenter]+a[c])
            delta=delta+1
            c=c+1

        c=0
        delta=0




        i=i+1
        smart=0
        delta=0
        augmenter=0

# Le tableau contient toutes les possibilités

    i=0
    dico_tab=list(dico.keys())
    delta=0
    c=0
    essai=0
    tab=[]

    while i < len(tableau):

        while essai <len(dico_tab):
            if tableau[c]!= dico_tab[delta]:
                delta=delta+1
            if delta == len(dico_tab):
                tab.append(tableau[c])
            essai=essai+1
        delta=0
        essai=0
        c=c+1
        i=i+1

    return tab



def codons_to_aa(tab,dico):
    i=0
    c=0
    indice=0
    tab_cod=[]
    dico_key= list(dico.keys())
    dico_val = list(dico.values())

    while i < len(tab):

        while c  < len(dico_val):

            if tab[i] != dico_key[c]:

                indice=indice+1

            if tab[i]==dico_key[c]:

                tab_cod.append(dico_val[c])

            if indice == len(dico_val):

                c=len(dico_val)
                i=len(tab)

            c=c+1

        indice=0
        c=0
        i=i+1
    return tab_cod








def nextIndice(tab, ind, elements):
    pass


def decoupe_sequence(seq, start, stop):
    pass


def codons_to_seq_codantes(codons, dico):
    pass


def seq_codantes_to_seq_aas(seq_codantes, dico):
    pass


def adn_encode_molecule(adn, dico, molecule):
    pass
