# Projet fourmilère

Introduction 
		
 la représentation d'un système dynamique composé d'individus interagissant entre eux avec des mécanismes simples et n’ayant pas connaissance ni contrôle sur les autres individus. Néanmoins, ces interactions individuelles créent un phénomène macroscopique et transforment ainsi la multitude d’individus en groupe.  On retrouve cet aspect chez les fourmis et le fonctionnement d'une fourmilière. 
 
 Résumé

Notre projet a pour but de modéliser numériquement le fonctionnement d’une fourmilière, super-organisme composé de milliers voire millions d’individus simples mais capable d’organisation interne, d’innovation et d’optimisation. 
Ces caractéristiques en font une des structures connues les plus résilientes et complexes, alors que le comportement de chaque individu n'est régi que par des actions simples. 

On a d'abord crée un monde avec une fourmilière au milieu, ainsi qu'un point de nourriture généré en périphérie avec une certaine quantité de nourriture choisi aléatoirement.  Ensuite, nous faisons apparaître des fourmis autour de la fourmilière, qui se mettent à rechercher de la nourriture. Ces fourmis ayant une durée de vie limitée et les déplacements sont reliés aux phéromones placés par les fourmis. Si une fourmi trouve un point de nourriture, elle revient vers la fourmilière. La réserve de nourriture initiale diminue et celle de la fourmilière augmente après le dépôt. Une fois qu'une fourmi trouve un coin de nourriture, les autres suivent ce même chemin, tout en  faisant des mouvements aléatoires parfois pour innover.

(Résumé de quelques lignes présentant l'objectif de votre projet, la méthode que vous avez suivie pour le réaliser et les résultats marquants que vous avez obtenus.)

## English version

Anthill project

Our project aims to model the functioning of an anthill, a super-organism made up of thousands or even millions of simple individuals but capable of internal organization, innovation and optimization.
These characteristics make it one of the most resilient and complex structures known, while the behavior of each individual is governed only by simple actions.

We first created a world with an anthill in the middle, as well as a food point generated on the outskirts with a certain amount of food chosen at random. Then we spawn ants around the anthill, which start looking for food. These ants have a limited lifespan and movements are linked to the pheromones placed by the ants. If an ant finds a food point, it returns to the anthill. The initial food reserve decreases and that of the anthill increases after the deposit. Once an ant finds a corner of food, the others follow that same path, while making random movements sometimes to innovate.
 

## Présentation de l'équipe

|(´・ω・｀)| ( ͡° ͜ʖ ͡°) | ಠ_ಠ | ᕕ( ᐛ )ᕗ |
|-----|--|--|--|
| N. Pons | H. Allemand | A. Leschallier  | T. Drouard  |


## Description synthétique du projet

**Problématique :** 
Quels sont les interactions, mécanismes organisationnels permettant aux fourmis de faire naître un super-organisme résilient ?
-	Ce qui a été fait : étude de l’optimisation des chemins pris par les fourmis et traduction algorithmique, étude informatique des interactions pouvant mener des entités simples à une organisation plus ou moins complexe, étude empirique des comportements de nombreux types de fourmis
-	Les mots clés : stigmergy, self-organisation, ant colony, ant colony optimization algorithm
-	Les +/- des travaux existants : l’optimisation du chemin a trouvé des applications en informatique et set donc très bien documentée, en revanche les autres comportements organisationnels bien qu’expliqués ne sont pas explicitement décrits et leur lien avec le comportement des fourmis n’est pas toujours direct.
-	Pertinence : Trouver les paramètres internes et externes aux fourmilières qui permettent une organisation durable de celles-ci en étudiant plusieurs interactions via la simulation informatique permettra de mieux comprendre le fonctionnement des fourmilières et, à travers l’études des limites de ces mécanismes organisationnels, les limites éventuelles de leur résilience. On pourra également, à l’aide de ces connaissances, connaître les phénomènes à mettre en place ou à caractériser pour recréer une organisation interne dans un groupe d’agents.
-	Faisabilité : La modélisation de certains comportements risque d’être compliqué, en partie parce que ces comportements peuvent rester encore mal compris dans la nature. De plus, le temps de calcul des algorithmes associés peut aussi s’avérer long.

**Hypothèse principale :** Il est possible de d'établir des chemins entre deux points particuliers en utilisant des entités n'ayant aucune mémoire. Cela revient à pouvoir modéliser la stigmergie donc la modification de l'environnement par les individus afin de construire un comportement de groupe non programmé initialement.

**Hypothèses secondaires :** 
- Un fort taux d'exploration des fourmis n'entraine pas de formation de chemin. Un taux d'exploration trop faible ne permet pas d'optimiser le chemin.
- Des phéromones trop persistantes brouillent les éventuels chemins mais des phéromones trop volatiles ne permettent pas de créer un chemin.

**Objectifs :**
 Modéliser numériquement le fonctionnement d’une fourmilière

**Critère(s) d'évaluation :**
Pour s’assurer de la pertinence de la modélisation, nous comparerons le résultat des interactions modélisées au comportement véritable des fourmis dans une fourmilière. (À détailler par des mesures précises)

## Présentation structurée des résultats


Présentation du choix de modélisation, des outils, du code et des résultats (tableaux, courbes, animations...) (**avec une analyse critique**).

## Lien vers page de blog : <a href="https://github.com/are-dynamic-2021-g5/Projet-fourmili-re/blob/main/blog.md"> C'est ici ! </a>

## Bibliographie :

Lenoir, A., et H. Ataya. « Polyéthisme et Répartition Des Niveaux d’Activité Chez La Fourmi Lasius Niger L. » Zeitschrift Für Tierpsychologie 63, no 2‑3 (1983): 213‑32. 

Passera Luc. Les fourmis : comportement, organisation sociale et évolution / Luc Passera,... Serge Aron,... Ottawa (Ont.): les Presses scientifiques du CNRC, 2005.

WSL (FR), Institut fédéral de recherches WSL-. « Les fourmis des bois en Suisse ». https://www.waldwissen.net/fr/habitat-forestier/faune-forestiere/insectes-invertebres/fourmis-des-bois-en-suisse.

Green, D. G., S. Sadedin, et T. G. Leishman. « Self-Organization ». In Encyclopedia of Ecology, édité par Sven Erik Jørgensen et Brian D. Fath, 3195‑3203. Oxford: Academic Press, 2008. https://doi.org/10.1016/B978-008045405-4.00696-0.


« Entropy-Based Goal-Oriented Emergence Management in Self-Organizing Systems through Feedback Control Loop: A Case Study in NASA ANTS Mission ». Reliability Engineering & System Safety 210 (1 juin 2021): 107506. https://doi.org/10.1016/j.ress.2021.107506.

Berthelot, Kévin. « Communication Chimique et Reconnaissance de Castes Chez Les Fourmis Odontomachus Hastatus et Lasius Niger ». Phd, Université de Toulouse, Université Toulouse III - Paul Sabatier, 2016. http://thesesups.ups-tlse.fr/3594/.

Dorigo, Marco, Mauro Birattari, et Thomas Stützle. « Ant Colony Optimization ». Computational Intelligence Magazine, IEEE 1 (1 décembre 2006): 28‑39. https://doi.org/10.1109/MCI.2006.329691.

Moffett, Mark W., Simon Garnier, Kathleen M. Eisenhardt, Nathan R. Furr, Massimo Warglien, Costanza Sartoris, William Ocasio, Thorbjørn Knudsen, Lars A. Bach, et Joachim Offenberg. « Ant Colonies: Building Complex Organizations with Minuscule Brains and No Leaders ». Journal of Organization Design, 2 février 2021, 1‑20. https://doi.org/10.1007/s41469-021-00093-4.


Le Goff, Line. « Formation spontanée de chemins: des fourmis aux marches aléatoires renforcées ». Thèse de doctorat, Université Paris Nanterre, 2014.


**Carte mentale de vos mots-clés, en utilisant** <a href="https://framindmap.org/mindmaps/index.html">Framindmap </a> 

Liste de l'ensemble des ressources bibliographiques utilisées pour vos travaux. **<= Indiquez le canal utilisé pour les trouver (Google Scholar, sources wikipedia, ressources en ligne SU, ...)**
