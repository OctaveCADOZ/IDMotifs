import re

def nettoyer_sequence(sequence):
    """ Supprime les caractères non-ADN de la séquence """
    return re.sub(r'[^ACGT]', '', sequence.upper())

if _name_ == "_main_":
    raw_seq = "ACGXTGCA123"
    print("Séquence nettoyée :", nettoyer_sequence(raw_seq))
