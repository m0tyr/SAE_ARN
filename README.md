# SAE_ARN
SAE BUT1
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "a023b3ed",
   "metadata": {},
   "source": [
    "# Notebook de présentation de la SAE S01.02"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "47840237",
   "metadata": {},
   "source": [
    "## Binôme \n",
    "\n",
    "* ZHANG Claude\n",
    "* TLEMSANI Sofiane "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "e2dbe7e8",
   "metadata": {},
   "outputs": [],
   "source": [
    "from json import *\n",
    "import copy\n",
    "import biology as b\n",
    "import test_biology as test_b\n",
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f771db82",
   "metadata": {},
   "source": [
    " ### QUESTION 1 : \n",
    " \n",
    " *Définir la fonction est_base prenant en paramètre un caractère et retournant True si ce caractère correspond à une base de l'ADN (est un des caractères A, T, G, C), et False sinon.*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "91e225f6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b.est_base(\"C\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c73939d5",
   "metadata": {},
   "source": [
    "### QUESTION 2 :\n",
    "\n",
    "*Définir la fonction est_adn prenant en paramètre une chaîne de caractères et retournant True si la chaîne correspond à un ADN (est constituée uniquement des caractères A, T, G, C), et False sinon.*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "1ea6f9a8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b.est_adn(\"ATGTCAAA\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3620ed5d",
   "metadata": {},
   "source": [
    "### QUESTION 3 :\n",
    "\n",
    "*Définir la fonction arn prenant en paramètre une séquence d'ADN et retournant la séquence ARN associée.*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "085ce733",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'AUGACCU'"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b.arn(\"ATGACCT\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "425ee1d4",
   "metadata": {},
   "source": [
    "### QUESTION 4 :\n",
    "\n",
    "*Définir la fonction arn_to_codons prenant en paramètre une chaîne de caractères correspondant à de l'ARN et découpant cet ARN en codons. La fonction doit retourner un tableau contenant la liste des codons.\n",
    "Par exemple, l'appel de la fonction arn_to_codons avec l'ARN \"CGUUAGGGG\" doit retourner le tableau [\"CGU\", \"UAG\", \"GGG\"].*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "10758ac8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['CUC']"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b.arn_to_codons(\"CUCGG\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0b7a3991",
   "metadata": {},
   "source": [
    "### QUESTION 5 :\n",
    "\n",
    "##### Remarque : Les chemins de fichier sont les notres vous devenez les changer en fonction de où ce trouve votre répertoire data avec codons_aa.json\n",
    "\n",
    "\n",
    "#### Partie 1 :\n",
    " *Définir la fonction load_dico_codons_aa qui prend en paramètre un fichier au format JSON et retourne la structure de données chargée en mémoire à partir du JSON.*\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "550c43e0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine', 'UUA': 'Leucine', 'UUG': 'Leucine', 'CUU': 'Leucine', 'CUC': 'Leucine', 'CUA': 'Leucine', 'CUG': 'Leucine', 'AUU': 'Isoleucine', 'AUC': 'Isoleucine', 'AUA': 'Methionine', 'AUG': 'Methionine', 'GUU': 'Valine', 'GUC': 'Valine', 'GUA': 'Valine', 'GUG': 'Valine', 'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine', 'CCU': 'Proline', 'CCC': 'Proline', 'CCA': 'Proline', 'CCG': 'Proline', 'ACU': 'Threonine', 'ACC': 'Threonine', 'ACA': 'Threonine', 'ACG': 'Threonine', 'GCU': 'Alanine', 'GCC': 'Alanine', 'GCA': 'Alanine', 'GCG': 'Alanine', 'UAU': 'Tyrosine', 'UAC': 'Tyrosine', 'CAU': 'Histidine', 'CAC': 'Histidine', 'CAA': 'Glutamine', 'CAG': 'Glutamine', 'AAU': 'Asparagine', 'AAC': 'Asparagine', 'AAA': 'Lysine', 'AAG': 'Lysine', 'GAU': 'Aspartic acid', 'GAC': 'Aspartic acid', 'GAA': 'Glutamic acid', 'GAG': 'Glutamic acid', 'UGU': 'Cysteine', 'UGC': 'Cysteine', 'UGA': 'Tryptophan', 'UGG': 'Tryptophan', 'CGU': 'Arginine', 'CGC': 'Arginine', 'CGA': 'Arginine', 'CGG': 'Arginine', 'AGU': 'Serine', 'AGC': 'Serine', 'GGU': 'Glycine', 'GGC': 'Glycine', 'GGA': 'Glycine', 'GGG': 'Glycine'}\n"
     ]
    }
   ],
   "source": [
    "dictionnaire = b.load_dico_codons_aa(r\"C:\\Users\\sofkh\\Documents\\sae_s01.02-main\\data/codons_aa.json\")\n",
    "print(dictionnaire)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4fdd4764",
   "metadata": {},
   "source": [
    "#### Partie 2 :\n",
    "*Définir la fonction codons_stop prenant en paramètre un dictionnaire dont les clés sont les codons et les valeurs les acides aminés correspondants (chaînes de caractères). La fonction retournera un tableau contenant l'ensemble des codons stop, c'est-à-dire l'ensemble des codons possibles avec les caractères AUGC qui ne sont pas des clés du dictionnaire.*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "409f955a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['AGA', 'AGG', 'UAA', 'UAG']"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b.codons_stop(dictionnaire)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f046c527",
   "metadata": {},
   "source": [
    "### QUESTION 6 :\n",
    "\n",
    "*Définir la fonction codons_to_aa prenant en paramètre un tableau de codons (correspondant par exemple à une valeur retournée par la fonction arn_to_codons) et le dictionnaire de correspondance entre codons et acides aminés. La fonction devra retourner un tableau contenant les acides aminés correspondant aux codons.*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "2263bbb1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Arginine', 'Asparagine', 'Tryptophan']"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b.codons_to_aa([\"CGU\", \"AAU\", \"UGA\", \"UAG\", \"CGU\"],dictionnaire)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
