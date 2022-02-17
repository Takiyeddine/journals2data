# BERT models


Bonjour Florian,

Je te joins quelques exemples de modèles pré-entrainés que tu peux utiliser pour classifier les titres d'articles. Tu peux extraire l'archive dans le répertoire **psat-elod_time_interval/PSAT-master/PSAT-master**

[https://drive.google.com/drive/folders/1iXmDzZOblRBiFshow-QzIeB5f6R8hBX1?usp=sharing](https://drive.google.com/drive/folders/1iXmDzZOblRBiFshow-QzIeB5f6R8hBX1?usp=sharing)
Dans la fonction **find_all_links** du module **FetchArticles.py ** que je t'ai montrée, tu as un paramètre **model** ; c'est le path relatif vers le répertoire contenant le modèle (ici par exemple,  'models/BERT_classifier_en' si tu veux utiliser le modèle entrainé sur les journaux anglophones).

Si tu as besoin de ré-entrainer un modèle, tu peux aussi jeter un oeil au notebook commenté des étudiants 5IF, **BERT_french_commented.ipynb

** (À ce sujet, si tu ne connais pas Jupyter Notebook, je peux aussi te recommander d'y jeter un oeil [https://jupyter.org/index.html](https://jupyter.org/index.html), c'est un outil assez sympa qui permet d'associer des blocs de code executable, du markdown, des visualisations de figures, etc ... dans un même fichier via une interface web. C'est assez pratique pour expérimenter et développer des prototypes de pipelines de Machine Learning avant de les industrialiser. Certains IDE supportent aussi le format Notebook, à toi de voir ce que tu préfères :) )

Cdt,
Cédric
