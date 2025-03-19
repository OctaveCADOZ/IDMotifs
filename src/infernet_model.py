import clr  # pythonnet permet d'exécuter du C#
clr.AddReference("InferNet")
from InferNet import Model

def detect_motif(sequence):
    """ Exécute un modèle bayésien d'Infer.NET """
    model = Model()
    return model.infer(sequence)

if _name_ == "_main_":
    seq = "ACGTACGTGCAA"
    print("Résultat d'Infer.Net :", detect_motif(seq))
