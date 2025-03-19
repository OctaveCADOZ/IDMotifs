#  Installation du projet IDMotifs

Ce guide explique comment installer et configurer **IDMotifs**.

---

##  **1. Prérequis**
Avant d’installer le projet, assurez-vous d’avoir :
- **Python 3.x** installé (`python --version` pour vérifier).
- **Git** installé (`git --version` pour vérifier).
- **pip** mis à jour (`pip install --upgrade pip`).

---

##  **2. Installation du projet**
###  1️ Cloner le dépôt GitHub
```sh
git clone https://github.com/OctaveCADOZ/IDMotifs.git
cd IDMotifs
```

###  2️ Installer les dépendances
```sh
pip install -r requirements.txt
```

Si vous utilisez un environnement virtuel, créez et activez-le avant :
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

---

##  **3. Lancer un test rapide**
Une fois installé, testez avec :
```sh
python src/motif_identifier.py
```
Vous devriez voir un message indiquant si un motif est trouvé.

---

##  **4. Résolution des problèmes**
### ❌ Problème : "pip command not found"
Essayez :
```sh
python -m ensurepip --default-pip
```

### ❌ Problème : "ModuleNotFoundError"
Si une dépendance ne s’installe pas correctement, réessayez :
```sh
pip install --upgrade pip
pip install -r requirements.txt
```

Si le problème persiste, ouvrez une **Issue** sur GitHub ou contactez un mainteneur.

---

##  **5. Prochaine étape**
Après l’installation, vous pouvez consulter :
- **[Guide d’utilisation](usage.md)** pour exécuter le projet.
- **[Référence API](api_reference.md)** pour voir les fonctions disponibles.
- **Exécuter les tests** pour vérifier que tout fonctionne :
  ```sh
  python -m unittest discover tests/
  ```

**Félicitations ! Vous avez installé IDMotifs avec succès.**
