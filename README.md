# Analyseur de sentiment

Ce programme utilise la bibliothèque NLTK et d'autres outils pour analyser le sentiment d'une phrase en français ou en anglais. Il peut détecter si le sentiment est positif ou négatif, ou s'il ne comprend pas la phrase.

## Dépendances

Pour exécuter ce programme, vous devez installer les bibliothèques suivantes :

- nltk
- textblob
- googletrans

Vous pouvez les installer avec la commande `pip install -r requirements.txt`, où `requirements.txt` est un fichier contenant les noms des bibliothèques.

## Utilisation

Pour utiliser ce programme, vous devez entrer votre langue (fr/en) et une phrase à analyser. Le programme affichera le résultat du sentiment sous la forme d'un booléen (True/False) ou d'un message d'erreur (None).

Par exemple :

```
Entrez votre langue (fr/en) : fr
Entrez une phrase : J'aime ce programme
Sentiment positif.
```

```
Entrez votre langue (fr/en) : en
Entrez une phrase : This program is awesome
Sentiment positif.
```

```
Entrez votre langue (fr/en) : fr
Entrez une phrase : Je suis confus
None
```

J'espère que ce fichier README vous sera utile. Si vous avez des questions ou des commentaires sur votre code, n'hésitez pas à me les poser. Je suis toujours heureux de discuter avec vous. 😊
