import matplotlib.pyplot as plt

def afficher_motif(sequence, motif):
    """ Affiche un graphique montrant l'emplacement du motif """
    positions = [i for i in range(len(sequence)) if sequence.startswith(motif, i)]
    
    plt.figure(figsize=(10, 2))
    plt.bar(positions, [1]*len(positions), width=0.5, color='red')
    plt.xlabel("Position dans la séquence")
    plt.title(f"Occurrences du motif '{motif}'")
    plt.show()

if _name_ == "_main_":
    afficher_motif("ACGTACGTGCAACGT", "ACGT")
