# 📚 Référence API - IDMotifs

Ce document détaille les fonctions et classes principales du projet.

---

## `src/motif_identifier.py`
### `identifier_motif(sequence: str, motif: str) -> bool`
**Description** : Vérifie si un motif est présent dans une séquence.  
**Paramètres** :  
- `sequence` (str) : Séquence de caractères analysée.  
- `motif` (str) : Motif à rechercher.  
**Retourne** : `True` si le motif est trouvé, `False` sinon.  

**Exemple** :
```python
identifier_motif("ACGTACGT", "ACGT")  # True
```

## `src/preprocessing.py`
### `nettoyer_sequence(sequence: str) -> str
**Description** : Supprime les caractères non-ADM d'une séquence. 
**Paramètres** :  
- `sequence` (str) : Séquence brute (peut contenir des caractères invalides).  
**Retourne** : Une séquence propre ne contenant que `A`,`C`,`G`,`T`.

**Exemple** :
```python
nettoyer_sequence("ACGXTGCA123")  # "ACGTGCA"
```

## `src/visualization.py`
### `afficher_motif(sequence: str, motif : str) -> None
**Description** : Génère une visualisation graphique des occurences d'un motif.
**Paramètres** :  
- `sequence` (str) : Séquence ADN analysée.
- `motif` (str) : Motif recherché.

**Exemple** :
```python
afficher_motif("ACGTACGTGCAACGT", "ACGT")
```

## `src/infernet_model.py`
### detect_motif(sequence: str) -> float
**Description** : Utilise Infer.NET pour analyser la probabilité d'un motif.
**Paramètres** :  
- `sequence` (str) : Séquence ADN analysée.
**Retourne** : Probabilité que le motif soit présent.


**Exemple** :
```python
detect_motif("ACGTACGTGCAA")  # Ex : 0.87
```

