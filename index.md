# Projet fourmilère

Introduction 
		
 La représentation d'un système dynamique composé d'individus interagissant entre eux avec des mécanismes simples et n’ayant pas connaissance ni contrôle sur les autres individus. Néanmoins, ces interactions individuelles créent un phénomène macroscopique et transforment ainsi la multitude d’individus en groupe.  On retrouve cet aspect chez les fourmis et le fonctionnement d'une fourmilière. 
 
 Résumé

Notre projet a pour but de modéliser numériquement le fonctionnement d’une fourmilière, super-organisme composé de milliers voire millions d’individus simples mais capable d’organisation interne, d’innovation et d’optimisation. 
Ces caractéristiques en font une des structures connues les plus résilientes et complexes, alors que le comportement de chaque individu n'est régi que par des actions simples. 

Tout d'abord nous avons créé un monde avec une fourmilière au milieu, ainsi qu'un point de nourriture généré en périphérie avec une certaine quantité de nourriture choisi aléatoirement.  Ensuite, nous avons fait apparaître des fourmis autour de la fourmilière, qui se mettent à rechercher de la nourriture. Ces fourmis ont une durée de vie limitée et leurs déplacements sont an partie dirigés aux phéromones placées par les fourmis. Si une fourmi trouve un point de nourriture, elle revient vers la fourmilière. La réserve de nourriture initiale diminue et celle de la fourmilière augmente après le dépôt. Une fois qu'une fourmi trouve un coin de nourriture, les autres suivent ce même chemin, tout en  ayant une certaine innovation ce qui permet de trouver des chemins plus efficaces.



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



### Explication du code

Tout d'abord nous avons listé l'ensemble des paramètres que nous allions utilisés et, au besoin, modifié. On a donc regroupé l'ensemble de ceux-ci dans une même case.

![image](https://user-images.githubusercontent.com/80055517/117018918-4173b880-acf5-11eb-980d-8320636e688d.png)



Ensuite nous avons conçu une fonction de base qui permettait de générer un monde avec de la nourriture et des pièges, support de toutes les autres fonctions. Elle crée l'univers en quelque sorte.

def generate_simple_map(n, m, nb_trap): # n : lignes m : colonnes
    """Préconditions : m > 0 et n > 0, initial_size > 0
    Renvoie un monde de taille n*m avec une fourmilière au centre et un point de nourriture en périphérie"""
    map = np.array([[" " for i in range(0, n)] for j in range(0, n)]) # on crée la matrice vide (avec des " " partout)
    # on crée la fourmilière au centre
    for i in range(0, initial_size):
        for k in range(0, initial_size):
            map = np.delete(map, m*(n//2 - initial_size//2 + i) + m//2 - initial_size//2 + k) #on copie le monde en enlevant une à une les cases du carré de taille initial_size situé au centre
            map = np.insert(map, m*(n//2 - initial_size//2 + i) + m//2 - initial_size//2 + k, "h") #on remplace les cases initialement vide (avec un " ") par une case "fourmilière" (avec un "h" pour "home")
            map = np.array([[map[m*j + i] for i in range(0, m)] for j in range(0, n) ])
    
    # on crée un point de nourriture
    food_line = random.randint(0, 2*n//5 - 1) # on définit ainsi la périphérie comme étant les cases du bord de la matrice avec un largeur de n/5
    food_column = random.randint(0, 2*m//5 - 1)
    if food_line > n//5 - 1: # on est sur la périphérie du bas
        food_line = n - 2 - n//5 + food_line
    if food_column > m//5 - 1: # on est sur la périphérie de droite
        food_column = m - 2 - m//5 + food_column
    where = random.sample([food_line, food_column], 1) # on définit une périphérie où se mettre (horizontale ou verticale)
    if where == food_line: # on est sur une périphérie en haut ou en bas
        food_column = random.randint(0, m - 1) # on définit une case au hasard sur cette périphérie
    else : #on est sur une périphérie latérale
        food_line = random.randint(0, n - 1) # on définit une case au hasard sur cette périphérie
    map = np.delete(map, m*food_line + food_column)
    map = np.insert(map, m*food_line + food_column, "n")
    map = np.array([[map[m*j + i] for i in range(0, m)] for j in range(0, n)])
    
    #carte de la nourriture
    food_quantity = random.randint(5, max_food_quantity)
    food_map = np.array([[0 for i in range(0, m)] for j in range(0, n)])
    food_map = np.delete(food_map, m*food_line + food_column)
    food_map = np.insert(food_map, m*food_line + food_column, food_quantity)
    food_map = np.array([[food_map[m*j + i] for i in range(0, m)] for j in range(0, n)])    
        
     #ajout de pièges mortel pour fourmis
    
    for i in range(0,nb_trap):  
        trap_line = random.randint(0, 2*n//3 - 1) 
        trap_column = random.randint(0, 2*m//3 - 1)
        if trap_line > n//3 - 1:
            trap_line = n - 2 - n//3 + trap_line -4
        if trap_column > m//3 - 1: 
            trap_column = m - 2 - m//3 + trap_column -4
        where = random.sample([trap_line, trap_column], 1) 
        if where == trap_line:
            trap_column = random.randint(0, m - 1) 
        else : 
            trap_line = random.randint(0, n - 1) 
        trap = 'p' 
        map = np.delete(map, m*trap_line + trap_column)
        map = np.insert(map, m*trap_line + trap_column, trap)
        map = np.array([[map[m*j + i] for i in range(0, m)] for j in range(0, n) ])
    
    print(map)
    print(food_map)
    return [map, food_map]
    print (generate_simple_map(n, m, nb_trap))

Les 'p' sont deonc des pièges, le 'n' la source de nourriture et les 'h' les cases fourmilières.

[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' 'p' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ']
 [' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' 'p' ' ']
 [' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ']
 [' ' 'n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
[[ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
 [ 0 16  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0]]

Nous avons ensuite créé deux fonctions "neighboorhood" comme dans le modèle de Schelling. La première s'appelle **spatial_ants_neighboorhood** et permet de renvoyer le voisinage d'une certaine case dans la matrice des fourmis dont les constituants sont des caractères. La seconde est **spatial_pher_neighboorhood** et effectue la même chose mais pour des matrices dont les composants sont des entiers.

Après quoi, nous avons fait une fonction qui générait les fourmis à leur place de départ, c'est à dire à côté de la fourmilière. Pour cela, nous avons regarder chaque case vide de la carte fourmis dont le voisinage comportait une case fourmilière et y avont alors ajouté une fourmi 'f'. Si toutes les cases en périphérie de la fourmilière sont déjà occupées, le paramètre de voisinage des cases regardées augmente de un ce qui permet de placer toutes les fourmis en couronne autour de la fourmilière.

![image](https://user-images.githubusercontent.com/80055517/117021886-0a52d680-acf8-11eb-91b9-8467806c2a85.png)

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
