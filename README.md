# Fakus

\[!\[License](https://img.shields.io/badge/license-MIT-blue.svg)\](LICENSE)
\[!\[GitHub Stars](https://img.shields.io/github/stars/votreutilisateur/votreprojet.svg?style=flat&logo=github)\](https://github.com/votreutilisateur/votprojet/stargazers)

## 🛠 Installation

Pour lancer ce projet avec Docker, suivez ces étapes :

1. Clonez ce dépôt :

```bash
git clone https://github.com/Sl00x/fakus.git
cd fakus
```

2. Créez un fichier `env.ini` pour configurer les variables d'environnement nécessaires.

```ini
# Exemple de fichier env.ini
name=nom du projet
db.url=postgres://utilisateur:mdp@postgres:5432/nomdelabdd
```

3. Utilisez Docker Compose pour construire et lancer les conteneurs :

```bash
docker compose build && docker compose up -d
```

4. L'application sera accessible à l'adresse [http://localhost:8000](http://localhost:8000).

## 🤝 Contribution

Toute contribution est la bienvenue ! Avant de contribuer, veuillez consulter [notre guide de contribution](CONTRIBUTING.md).

## 📝 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## ✉️ Contact

Pour toute question ou suggestion, contactez-nous à [quennehen.alexis@icloud.com](mailto:quennehen.alexis@icloud.com).
