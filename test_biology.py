# TO DO
import biology

def test_est_base():
    assert biology.est_base("R")==False
    assert biology.est_base("T")==True
    assert biology.est_base("C")==True
    assert biology.est_base("Z")==False
    print("Test de la fonction : OK ")

test_est_base()

def test_est_adn():
    assert biology.est_adn("ATCCCGGGGTAFATGG")==False
    assert biology.est_adn("ATGGGTAACAA")==True
    assert biology.est_adn("ZETUVJD")==False
    assert biology.est_adn("0004832")==False
    print("Test de la fonction : OK ")

test_est_adn()

def test_arn():
    assert biology.arn("AZTGGCCC")== None
    assert biology.arn("ATGGTCC")=="AUGGUCC"
    assert biology.arn("AGGCC")=="AGGCC"
    assert biology.arn("TTTTTT")=="UUUUUU"
    print("Test de la fonction : OK ")

test_arn()

def test_arn_to_codons():
    assert biology.arn_to_codons("CGAGUG")==['CGA', 'GUG']
    assert biology.arn_to_codons("CUCGUG")==['CUC', 'GUG']
    assert biology.arn_to_codons("CUCGUUUG")==['CUC', 'GUU']
    assert biology.arn_to_codons("CUCGG")==['CUC']
    print("Test de la fonction : OK ")

test_arn_to_codons()

def test_load_dico_codons_aa():
    assert biology.load_dico_codons_aa(r"C:\Users\sofkh\Documents\sae_s01.02-main\data/codons_aa.json")=={'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine', 'UUA': 'Leucine', 'UUG': 'Leucine', 'CUU': 'Leucine', 'CUC': 'Leucine', 'CUA': 'Leucine', 'CUG': 'Leucine', 'AUU': 'Isoleucine', 'AUC': 'Isoleucine', 'AUA': 'Methionine', 'AUG': 'Methionine', 'GUU': 'Valine', 'GUC': 'Valine', 'GUA': 'Valine', 'GUG': 'Valine', 'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine', 'CCU': 'Proline', 'CCC': 'Proline', 'CCA': 'Proline', 'CCG': 'Proline', 'ACU': 'Threonine', 'ACC': 'Threonine', 'ACA': 'Threonine', 'ACG': 'Threonine', 'GCU': 'Alanine', 'GCC': 'Alanine', 'GCA': 'Alanine', 'GCG': 'Alanine', 'UAU': 'Tyrosine', 'UAC': 'Tyrosine', 'CAU': 'Histidine', 'CAC': 'Histidine', 'CAA': 'Glutamine', 'CAG': 'Glutamine', 'AAU': 'Asparagine', 'AAC': 'Asparagine', 'AAA': 'Lysine', 'AAG': 'Lysine', 'GAU': 'Aspartic acid', 'GAC': 'Aspartic acid', 'GAA': 'Glutamic acid', 'GAG': 'Glutamic acid', 'UGU': 'Cysteine', 'UGC': 'Cysteine', 'UGA': 'Tryptophan', 'UGG': 'Tryptophan', 'CGU': 'Arginine', 'CGC': 'Arginine', 'CGA': 'Arginine', 'CGG': 'Arginine', 'AGU': 'Serine', 'AGC': 'Serine', 'GGU': 'Glycine', 'GGC': 'Glycine', 'GGA': 'Glycine', 'GGG': 'Glycine'}
    print("Test de la fonction : Ok")

test_load_dico_codons_aa()

def test_codons_stop():
    assert biology.codons_stop(biology.load_dico_codons_aa(r"C:\Users\sofkh\Documents\sae_s01.02-main\data/codons_aa.json"))==['AGA', 'AGG', 'UAA', 'UAG']
    print("Test de la fonction : OK")

test_codons_stop()

def test_codons_to_aa():
    assert biology.codons_to_aa(["CGU", "AAU", "UGA", "UAG", "CGU"],biology.load_dico_codons_aa(r"C:\Users\sofkh\Documents\sae_s01.02-main\data/codons_aa.json"))==['Arginine', 'Asparagine', 'Tryptophan']
    assert biology.codons_to_aa([ "UAA", "UGA", "UAC", "CGU"],biology.load_dico_codons_aa(r"C:\Users\sofkh\Documents\sae_s01.02-main\data/codons_aa.json"))==[]
    assert biology.codons_to_aa([ "GGA", "UGG", "UAAC", "CGU"],biology.load_dico_codons_aa(r"C:\Users\sofkh\Documents\sae_s01.02-main\data/codons_aa.json"))==['Glycine', 'Tryptophan']
    print("Test de la fonction : OK")

test_codons_to_aa()
