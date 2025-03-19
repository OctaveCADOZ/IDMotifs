#  Guide d'utilisation - IDMotifs

Ce guide explique **comment utiliser** les fonctionnalités du projet.

---

##  **1. Exécuter le programme principal**
Pour analyser une séquence ADN et identifier un motif, utilisez :
```sh
python src/motif_identifier.py
```
**Exemple de sortie attendue** :
```
Motif 'ACGT' trouvé : True
```

---

##  **2. Nettoyer une séquence ADN**
Si vous avez une séquence contenant des caractères invalides :
```python
from src.preprocessing import nettoyer_sequence

sequence = "ACGXTGCA123"
sequence_propre = nettoyer_sequence(sequence)
print(sequence_propre)  # "ACGTGCA"
```

---

##  **3. Visualiser les motifs trouvés**
Pour afficher une représentation graphique des motifs :
```python
from src.visualization import afficher_motif

sequence = "ACGTACGTGCAACGT"
motif = "ACGT"
afficher_motif(sequence, motif)
```
Une fenêtre s’ouvrira avec un **graphique** indiquant où le motif apparaît.

---

##  **4. Lancer les tests unitaires**
Avant de faire des modifications, assurez-vous que tout fonctionne :
```sh
python -m unittest discover tests/
```

---

## **5. Exécuter Infer.NET (optionnel)**
Si vous utilisez **Infer.NET** pour analyser la probabilité d'un motif :
```python
from src.infernet_model import detect_motif

sequence = "ACGTACGTGCAA"
prob = detect_motif(sequence)
print(f"Probabilité du motif : {prob}")
```

---

##  **6. Ajouter une nouvelle fonctionnalité**
Si vous voulez contribuer, créez une **nouvelle branche** :
```sh
git checkout -b nouvelle-fonctionnalite
```
Ajoutez votre code, puis envoyez-le sur GitHub avec :
```sh
git add .
git commit -m "Ajout d'une nouvelle fonctionnalité"
git push origin nouvelle-fonctionnalite
```
Puis, ouvrez une **Pull Request** sur GitHub.

---

 **Votre projet est maintenant fonctionnel et prêt à être utilisé !** 
