def identifier_motif(sequence, motif):
    """ Vérifie si un motif est présent dans une séquence """
    return motif in sequence

if __name__ == "__main__":
    seq = "ACGTACGTGCAA"
    motif = "ACGT"
    print(f"Motif '{motif}' trouvé : {identifier_motif(seq, motif)}")
