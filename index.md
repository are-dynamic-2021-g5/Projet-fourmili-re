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
Pour s’assurer de la pertinence de la modélisation, nous comparerons le résultat des interactions modélisées au comportement véritable des fourmis dans une fourmilière : construction d'un chemin entre la nourriture et la fourmilière, distance optimale de recherche de nourriture

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

Les 'p' sont donc des pièges, le 'n' la source de nourriture et les 'h' les cases fourmilières.

![image](https://user-images.githubusercontent.com/80055517/117023153-23a85280-acf9-11eb-8625-e1f8107026eb.png)

Notre modèle utilise un objet assez simple, la matrice, sur lequel on ne peut bien représenter qu'une seule information. C'est pourquoi nous avons séparé chaque degré de lecture en une carte. Il y en a 5 en tout : celle des fourmis, celle des phéromones maison, celle des phéromones nourriture, celle de la nourriture, celle des horloges.

![image](https://user-images.githubusercontent.com/80055517/117024650-78989880-acfa-11eb-802e-da60705d220d.png)


Nous avons ensuite créé la carte des horloges (les durées de vie des fourmis) associées aux fourmis.

![image](https://user-images.githubusercontent.com/80055517/117023672-9b767d00-acf9-11eb-8c7c-ef1bbaad0f41.png)

Nous avons repris la fonction "spatial_neighboorhood" du modèle de Schelling pour en faire deux. La première s'appelle **spatial_ants_neighboorhood** et permet de renvoyer le voisinage d'une certaine case dans la matrice des fourmis dont les constituants sont des caractères. La seconde est **spatial_pher_neighboorhood** et effectue la même chose mais pour des matrices dont les composants sont des entiers.

Après quoi, nous avons fait une fonction qui générait les fourmis à leur place de départ, c'est à dire à côté de la fourmilière. Pour cela, nous avons regarder chaque case vide de la carte fourmis dont le voisinage comportait une case fourmilière et y avont alors ajouté une fourmi 'f'. Si toutes les cases en périphérie de la fourmilière sont déjà occupées, le paramètre de voisinage des cases regardées augmente de un ce qui permet de placer toutes les fourmis en couronne autour de la fourmilière.

![image](https://user-images.githubusercontent.com/80055517/117021886-0a52d680-acf8-11eb-91b9-8467806c2a85.png)

Trois fonctions indicatrices permettent de scanner l'environnement de la fourmi en utilisant les fonctions spatial_neighborhood et en renvoyant False ou True s'il y a présence ou pas des différents éléments (nourriture, phéromones, maison).

![image](https://user-images.githubusercontent.com/80055517/117025904-99152280-acfb-11eb-8eaf-092e1e1948a6.png)

Vient ensuite la fonction qui nous a fait probablement le plus réfléchir, à savoir celle qui permet de suivre les phéromones de manière à remonter vers la source de nourriture si la fourmi est en quête ou vers la maison si elle a de la nourriture.
Après maintes réfléxions et tentatives nous avons séparé la situation en deux cas : 
1) la fourmi n'est pas sur une case avec phéromones mais elle en a dans son voisinage
2) la fourmi est sur une case avec phéromones

Dans le premier cas le but est de trouver le chemin souhaité, elle choisit donc la case avec le 2eme taux de phéromones le plus élevé (pour éviter qu'elle ne fasse des allée-retours entre deux cases) si elle existe. A défaut elle prend celle avec la plus grande valeur puisque c'est le seule chemin possible.

Dans le second cas le but est de suivre le chemin sur lequel elle est. Ainsi elle prend de préférence la direction de la case ayant une valeur de phéromones inférieure de 1 à la sienne. De cette manière elle remonte le chemin de la fourmi qui a laissé ces informations et trouve ce qu'elle cherche (maison ou nourriture). Si aucune case autout d'elle n'est dans ce cas elle reprend la méthode de décision du premier cas (pour éviter encore une fois d'être bloquée entre deux cases).

En pratique ça donne ça...

    def choose_the_way(map_pher, a, b):
    """Renvoie 0, 1, 2 ou 3 pour des déplacements vers le haut, la droite, le bas ou la gauche. Choisit le chemin en faisant la moyenne des phéromones
    d'un type autour de la case et en choisissant la deuxième plus élevée (pour choisir le chemin le plus marqué mais dans le bon sens)"""
    env = spatial_pher_neighborhood(map_pher, a, b, 1)
    up = 0 #valeur des phéromones au dessus
    right = 0 #valeur des phéromones à droite
    down = 0 #valeur des phéromones en dessous
    left = 0 #valeur des phéromones à gauche
    next_move = -1
    pher_value = map_pher[a, b] #valeur de la phéromone de la case où est la fourmi
    
    if 0 < a < n-1 and 0 < b < m-1 : #pas de problème avec les bords
        up = env[0, 1]
        right = env[1, 2]
        down = env[2, 1]
        left = env[1, 0]
    if a == 0 and 0 < b < m-1: # on a atteint le bord haut
        up = 0
        right = env[0, 2]
        down = env[1, 1]
        left = env[0, 0]     
    if a == 0 and b == 0: # on a atteint le bord haut gauche
        up = 0
        right = env[0, 1]
        down = env[1, 0]
        left = 0
    if a == 0 and b == m-1: #on a atteint le bord haut droit
        up = 0
        right = 0
        down = env[1, 0]
        left = env[0, 0]
    if a == n-1 and 0 < b < m-1: # on a atteint le bord bas
        up = env[0, 1]
        right = env[1, 2]
        down = 0
        left = env[1, 0]
    if a == n-1 and b == 0: # on a atteint le bord bas gauche
        up = env[0, 0]
        right = env[1, 1]
        down = 0
        left = 0
    if a == n-1 and b == m-1: #on a atteint le bord bas droit
        up = env[0, 0]
        right = 0
        down = 0
        left = env[1, 0]
    if  0 < a < n-1 and b == 0: #on atteint le bord gauche
        up = env[0, 0]
        right = env[1, 1]
        down = env[2, 0]
        left = 0
    if  0 < a < n-1 and b == m-1: #on atteint le bord droit
        up = env[0, 1]
        right = 0
        down = env[2, 1]
        left = env[1, 0]
    print("up", up)
    print("right", right)
    print("down", down)
    print("left", left)
    
    #on choisit la deuxième direction la plus chargée en phéromones
    list_pher = [up, down, right, left]
    second = sorted(list_pher)[2] #deuxième plus grande valeur de phéromone
    print("second",second)
    if pher_value == 0: #la fourmi est à côté d'une trace de phéromones mais pas dessus car la case où elle est n'a pas de phéromone
        if second == 0: #il n'y a qu'une direction possible pour les phéromones puisque la deuxième valeur la plus grande est nulle
            second = max(list_pher) #on choisit alors la seule case qui a des phéromones
            if second == up:
                next_move = 0
            if second == right:
                next_move = 1
            if second == down:
                next_move = 2
            if second == left:
                next_move = 3
        else : #on prend la deuxième direction la plus forte
            print("re")
            if second == up:
                next_move = 0
            if second == right:
                next_move = 1
            if second == down:
                next_move = 2
            if second == left:
                next_move = 3
    else: #la fourmi est sur une trace de phéromones puisque la case où elle est en possède
        #on veut alors que la fourmi suive un chemin dans le bon sens, ainsi on regarde si une des cases de son voisinage n'a pas une valeur de phéromone inférieure de 1 
        #(pour remonter le chemin d'une fourmi)
        if up == pher_value - 1:
            return 0
        if right == pher_value - 1:
            return 1
        if down == pher_value - 1:
            return 2
        if left == pher_value - 1:
            return 3
        else:
            if second == 0: #il n'y a qu'une direction possible pour les phéromones
                print("po2")
                second = max(list_pher)
                if second == up:
                    next_move = 0
                if second == right:
                    next_move = 1
                if second == down:
                    next_move = 2
                if second == left:
                    next_move = 3
            else : #on prend la deuxième direction la plus forte
                print("re2")
                if second == up:
                    next_move = 0
                if second == right:
                    next_move = 1
                if second == down:
                    next_move = 2
                if second == left:
                    next_move = 3
    print(next_move)
    return next_move

La fonction renvoie donc 0, 1, 2 ou 3  ce qui correspondra dans la fonction de déplacement à une direction : 0 = haut, 1 = droite, 2 = bas et 3 = gauche.

Voici maintenant le coeur de l'ouvrage : la fonction de déplacement. Celle-ci va déplacer une fourmi d'une case [a, b] selon les règles de déplacements.
Ces règles sont :
1) Pour une fourmi exploratrice ('f'), le déplacement se fait aléatoirement si il n'y a pas de phéromones dans son voisinage. Chaque déplacement s'accompagne du déplacement et de la modification (-1) de l'horloge de la fourmi, ainsi que de le dépôt de phéromones maison qui ont une certaine durée de vie. Pour éviter de revenir sans cesse sur les mêmes cases, la fourmi examine si la case où elle est censée aller a un taux de phéromones maison supérieur à un seuil (sa mémoire) et n'y va que si ce taux est inférieur à sa mémoire. Si il y a des phéromones dans le voisinage la fourmi se déplace comme évoqué dans la fonction précédente.
2) Pour une fourmi porteuse de nourriture ('s'), le processus est le même.

Quelques petites subtilités : 
- si deux fourmis se croisent (une veut aller sur une case où est une autre) on effectue le déplacement sur la case suivante (si elle est libre)
- si une fourmi tombe sur un piège, elle meurt (son horloge est remise à 0)
- si une fourmi a une horloge à 0 elle meurt

Autres détails après avoir effectué un déplacement les fourmis changent de nom, les 'f' deviennent 'g' et les 's' deviennent 't'. Cela permet en itérant cette fonction sur toutes les cases de ne pas déplacer deux fois la même fourmi.

    def spatial_relocation (map, map_pher_home, map_pher_food,clock_map, a, b): #map : List[List[int]], a : int(ligne), b : int(colonne)
    """Préconditions : 0 <= a <= n-1  and 0 <= b <= m-1  and 0 <= c <= n-1  and 0 <= d <= m-1 and n >= 2*neigh and m >= 2*neigh and map[c,d] == 0
    Renvoie le monde dans lequel l'individu de coordonnées [a, b] a été déplacé aléatoirement si pas de phéromone, suit les phéromone_food
    si la fourmi est en quête, suit les phéromones_home si la fourmi a de la nourriture. Les matrices sont également modifiées en conséquent."""
    ant = map[a, b] #on enregistre la cellule à déplacer (une fourmi)
    pher_food_map = map_pher_food
    pher_home_map = map_pher_home
    relocation = map
    clock = clock_map
    move_line = a
    move_column = b
    if ant == "f": #déplacement des fourmis en recherche de nourriture
        if pher_home_map[move_line, move_column] == 0: # on ne pose pas de phéromones si il y a déja une trace
            pher_home_map = np.delete(pher_home_map, m*move_line + move_column)
            pher_home_map = np.insert(pher_home_map, m*move_line + move_column, pers_pher) # sur la map de phéromones "maison" la case de même coordonnées que la fourmi prend la valeur de la persistance des phéromones
            pher_home_map = np.array([[pher_home_map[m*j + i] for i in range(0, m)] for j in range(0, n)])
        if no_pheromone(map_pher_food, move_line, move_column): #il n'y a pas de phéromone "nourriture" à coté de la fourmi
            next_move = random.randint(0, 3) #on décide le prochain mouvement au hasard
            if next_move == 0:
                if move_line > 0 and (relocation[move_line - 1, move_column] == " " or relocation[move_line - 1, move_column] == "p") and pher_home_map[move_line - 1, move_column] < pers_pher - memory: #la prochaine case existe et est vide
                    move_line = move_line - 1
                    move_column = move_column
                if move_line > 1 and (relocation[move_line - 2, move_column] == " " or relocation[move_line - 2, move_column] == "p") and (relocation[move_line - 1, move_column] == "f" or relocation[move_line - 1, move_column] == "s") and pher_home_map[move_line - 2, move_column] < pers_pher - memory:
                    move_line = move_line - 2
                    move_column = move_column
            elif next_move == 1:
                if move_column < m - 1 and (relocation[move_line, move_column + 1] == " " or relocation[move_line, move_column + 1] == "p") and pher_home_map[move_line, move_column + 1] < pers_pher - memory:
                    move_line = move_line
                    move_column = move_column + 1
                if move_column < m - 2 and (relocation[move_line, move_column + 2] == " " or relocation[move_line, move_column + 2] == "p") and (relocation[move_line, move_column + 1] == "f" or relocation[move_line, move_column + 1] == "s") and pher_home_map[move_line, move_column + 2] < pers_pher - memory:
                    move_line = move_line
                    move_column = move_column + 2
            elif next_move == 2:
                if move_line < n - 1 and (relocation[move_line + 1, move_column] == " " or relocation[move_line + 1, move_column] == "p") and pher_home_map[move_line + 1, move_column] < pers_pher - memory:
                    move_line = move_line + 1
                    move_column = move_column
                if move_line < n - 2 and (relocation[move_line + 2, move_column] == " " or relocation[move_line + 2, move_column] == "p") and (relocation[move_line + 1, move_column] == "f" or relocation[move_line + 1, move_column] == "s") and pher_home_map[move_line + 2, move_column] < pers_pher - memory:
                    move_line = move_line + 2
                    move_column = move_column
            elif next_move == 3:
                if move_column > 0 and (relocation[move_line, move_column - 1] == " " or relocation[move_line, move_column - 1] == "p") and pher_home_map[move_line, move_column - 1] < pers_pher - memory:
                    move_line = move_line
                    move_column = move_column - 1
                if move_column > 1 and (relocation[move_line, move_column - 2] == " " or relocation[move_line, move_column - 2] == "p") and (relocation[move_line, move_column - 1] == "f" or relocation[move_line, move_column - 1] == "s") and pher_home_map[move_line, move_column - 2] < pers_pher - memory:
                    move_line = move_line
                    move_column = move_column - 2
                    
            #on déplace et modifie l'horloge de la fourmi
            clock1 = np.array(clock)
            clock = np.delete(clock1, m*move_line + move_column)
            clock = np.insert(clock, m*move_line + move_column, int(clock1[a, b] - 1))
            clock = np.array([[clock[m*j + i] for i in range(0, m)] for j in range(0, n)])  
            if a != move_line or b != move_column:
                clock = np.delete(clock, m*a + b)
                clock = np.insert(clock, m*a + b, 0)
                clock = np.array([[clock[m*j + i] for i in range(0, m)] for j in range(0, n)])   
                
             #mort d'une fourmi si déplacement sur piège
            if relocation[move_line, move_column] == "p":
                clock = np.delete(clock, m*move_line + move_column)
                clock = np.insert(clock, m*move_line + move_column, 0)
                clock = np.array([[clock[m*j + i] for i in range(0, m)] for j in range(0, n)])   
                
            # on supprime l'indidu du monde
            relocation = np.delete(relocation, m*a + b) #on copie le monde sans l'individu
            relocation = np.insert(relocation, m*a + b, " ") #on remplace la place de l'individu par une case vide (avec un " ")
            relocation = np.array([[relocation[m*j + i] for i in range(0, m)] for j in range(0, n) ]) #on remet le monde sous forme de tableau
                # on remplace la case vide par l'individu
            relocation = np.delete(relocation, m*(move_line) + move_column) #on copie le monde sans la case vide
            relocation = np.insert(relocation, m*(move_line) + move_column, "g") #on remplace la place de la case vide par l'individu (ant)
            relocation = np.array([[relocation[m*j + i] for i in range(0, m)] for j in range(0, n) ]) #on remet le monde sous forme de tableau


 
        else : #l'individu suit le chemin de phéromones le plus marqué
            relocation = np.delete(relocation, m*move_line + move_column) #on copie le monde sans l'individu
            relocation = np.insert(relocation, m*move_line + move_column, " ") #on remplace la place de l'individu par une case vide (avec un " ")
            relocation = np.array([[relocation[m*j + i] for i in range(0, m)] for j in range(0, n)]) #on remet le monde sous forme de tableau
            way_food = choose_the_way(pher_food_map, move_line, move_column)
            
            if way_food == 0:
                if move_line > 0 and (relocation[move_line - 1, move_column] == " " or relocation[move_line - 1, move_column] == "p"): #la prochaine case existe et est vide
                    move_line = move_line - 1
                    move_column = move_column
                if move_line > 1 and (relocation[move_line - 2, move_column] == " " or relocation[move_line - 2, move_column] == "p") and (relocation[move_line - 1, move_column] == "f" or relocation[move_line - 1, move_column] == "s"): #la prochaine case existe et est vide
                    move_line = move_line - 2
                    move_column = move_column
                    
            if way_food == 1:
                if move_column < m - 1 and (relocation[move_line, move_column + 1] == " " or relocation[move_line + 1, move_column + 1] == "p"):
                    move_line = move_line
                    move_column = move_column + 1
                if move_column < m - 2 and (relocation[move_line, move_column + 2] == " " or relocation[move_line, move_column + 2] == "p") and (relocation[move_line, move_column + 1] == "f" or relocation[move_line, move_column + 1] == "s"):
                    move_line = move_line
                    move_column = move_column + 2
                    
            if way_food == 2:
                if move_line < n - 1 and (relocation[move_line + 1, move_column] == " " or relocation[move_line + 1, move_column] == "p"):
                    move_line = move_line + 1
                    move_column = move_column
                if move_line < n - 2 and (relocation[move_line + 2, move_column] == " " or relocation[move_line + 2, move_column] == "p") and (relocation[move_line + 1, move_column] == "f" or relocation[move_line + 1, move_column] == "s"):
                    move_line = move_line + 2
                    move_column = move_column

            if way_food == 3:
                if move_column > 0 and (relocation[move_line, move_column - 1] == " " or relocation[move_line, move_column - 1] == "p"):
                    move_line = move_line
                    move_column = move_column - 1
                if move_column > 1 and (relocation[move_line, move_column - 2] == " " or relocation[move_line, move_column - 2] == "p") and (relocation[move_line, move_column - 1] == "f" or relocation[move_line, move_column - 1] == "s"):
                    move_line = move_line
                    move_column = move_column - 2
                    

            #on déplace et modifie l'horloge de la fourmi
            clock1 = np.array(clock)
            clock = np.delete(clock1, m*move_line + move_column)
            clock = np.insert(clock, m*move_line + move_column, int(clock1[a, b] - 1))
            clock = np.array([[clock[m*j + i] for i in range(0, m)] for j in range(0, n)])  
            if a != move_line or b != move_column:
                clock = np.delete(clock, m*a + b)
                clock = np.insert(clock, m*a + b, 0)
                clock = np.array([[clock[m*j + i] for i in range(0, m)] for j in range(0, n)]) 
                
             #mort d'une fourmi si déplacement sur piège
            if relocation[move_line, move_column] == "p":
                clock = np.delete(clock, m*move_line + move_column)
                clock = np.insert(clock, m*move_line + move_column, 0)
                clock = np.array([[clock[m*j + i] for i in range(0, m)] for j in range(0, n)])      
                
            # on supprime l'indidu du monde
            relocation = np.delete(relocation, m*a + b) #on copie le monde sans l'individu
            relocation = np.insert(relocation, m*a + b, " ") #on remplace la place de l'individu par une case vide (avec un " ")
            relocation = np.array([[relocation[m*j + i] for i in range(0, m)] for j in range(0, n) ]) #on remet le monde sous forme de tableau
                # on remplace la case vide par l'individu
            relocation = np.delete(relocation, m*(move_line) + move_column) #on copie le monde sans la case vide
            relocation = np.insert(relocation, m*(move_line) + move_column, "g") #on remplace la place de la case vide par l'individu (ant)
            relocation = np.array([[relocation[m*j + i] for i in range(0, m)] for j in range(0, n) ]) #on remet le monde sous forme de tableau


                
        if pher_home_map[move_line, move_column] == 0: # on ne pose pas de phéromones si il y a déja une trace
            pher_home_map = np.delete(pher_home_map, m*move_line + move_column)
            pher_home_map = np.insert(pher_home_map, m*move_line + move_column, pers_pher - 1) # sur la map de phéromones "maison" la case de même coordonnées que la fourmi prend la valeur de la persistance des phéromones
            pher_home_map = np.array([[pher_home_map[m*j + i] for i in range(0, m)] for j in range(0, n)])
            
        #la fourmi est morte
        if clock[move_line, move_column] <= 0:
            relocation = np.delete(relocation, m*move_line + move_column)
            relocation = np.insert(relocation, m*move_line + move_column, " ") #on remplace la place de l'individu par une case vide (avec un " ")
            relocation = np.array([[relocation[m*j + i] for i in range(0, m)] for j in range(0, n) ]) #on remet le monde sous forme de tableau
        
    if ant == "s": #déplacement des fourmis ayant trouvé de la nourriture
        pher_food_map = np.delete(pher_food_map, m*move_line + move_column)
        pher_food_map = np.insert(pher_food_map, m*move_line + move_column, pher_food_map[m*a + b] + pers_pher) # sur la map de phéromones "nourriture" la case de même coordonnées que la fourmi prend la valeur de la persistance des phéromones
        pher_food_map = np.array([[pher_food_map[m*j + i] for i in range(0, m)] for j in range(0, n)])
        if no_pheromone(map_pher_home, move_line, move_column): #il n'y a pas de phéromone "maison" à coté de la fourmi
            next_move = random.randint(0, 3) #on décide le prochain mouvement au hasard
            if next_move == 0:
                if move_line > 0 and (relocation[move_line - 1, move_column] == " " or relocation[move_line - 1, move_column] == "p") and pher_food_map[move_line - 1, move_column] % pers_pher < pers_pher - memory: #la prochaine case existe et est vide
                    move_line = move_line - 1
                    move_column = move_column
                if move_line > 1 and (relocation[move_line - 2, move_column] == " " or relocation[move_line - 2, move_column] == "p") and (relocation[move_line - 1, move_column] == "f" or relocation[move_line - 1, move_column] == "s") and pher_food_map[move_line - 2, move_column] < pers_pher - memory:
                    move_line = move_line - 2
                    move_column = move_column
            elif next_move == 1:
                if move_column < m - 1 and (relocation[move_line, move_column + 1] == " " or relocation[move_line, move_column + 1] == "p") and pher_food_map[move_line, move_column + 1] % pers_pher < pers_pher - memory:
                    move_line = move_line
                    move_column = move_column + 1
                if move_column < m - 2 and (relocation[move_line, move_column + 2] == " " or relocation[move_line, move_column + 2] == "p") and (relocation[move_line, move_column + 1] == "f" or relocation[move_line, move_column + 1] == "s") and pher_food_map[move_line, move_column + 2] < pers_pher - memory:
                    move_line = move_line
                    move_column = move_column + 2
            elif next_move == 2:
                if move_line < n - 1 and (relocation[move_line + 1, move_column] == " " or relocation[move_line + 1, move_column] == "p") and pher_food_map[move_line + 1, move_column] % pers_pher < pers_pher - memory:
                    move_line = move_line + 1
                    move_column = move_column
                if move_line < n - 2 and (relocation[move_line + 2, move_column] == " " or relocation[move_line + 2, move_column] == "p") and (relocation[move_line + 1, move_column] == "f" or relocation[move_line + 1, move_column] == "s") and pher_food_map[move_line + 2, move_column] < pers_pher - memory:
                    move_line = move_line + 2
                    move_column = move_column
            elif next_move == 3:
                if move_column > 0 and (relocation[move_line, move_column - 1] == " " or relocation[move_line, move_column - 1] == "p") and pher_food_map[move_line, move_column - 1] % pers_pher < pers_pher - memory:
                    move_line = move_line
                    move_column = move_column - 1
                if move_column > 1 and (relocation[move_line, move_column - 2] == " " or relocation[move_line, move_column - 2] == "p") and (relocation[move_line, move_column - 1] == "f" or relocation[move_line, move_column - 1] == "s") and pher_food_map[move_line, move_column - 2] < pers_pher - memory:
                    move_line = move_line
                    move_column = move_column - 2
                    
                                        
            #on déplace et modifie l'horloge de la fourmi
            clock1 = np.array(clock)
            clock = np.delete(clock1, m*move_line + move_column)
            clock = np.insert(clock, m*move_line + move_column, int(clock1[a, b] - 1))
            clock = np.array([[clock[m*j + i] for i in range(0, m)] for j in range(0, n)])  
            if a != move_line or b != move_column:
                clock = np.delete(clock, m*a + b)
                clock = np.insert(clock, m*a + b, 0)
                clock = np.array([[clock[m*j + i] for i in range(0, m)] for j in range(0, n)]) 
                
             #mort d'une fourmi si déplacement sur piège
            if relocation[move_line, move_column] == "p":
                clock = np.delete(clock, m*move_line + move_column)
                clock = np.insert(clock, m*move_line + move_column, 0)
                clock = np.array([[clock[m*j + i] for i in range(0, m)] for j in range(0, n)])     
                
            # on supprime l'indidu du monde
            relocation = np.delete(relocation, m*a + b) #on copie le monde sans l'individu
            relocation = np.insert(relocation, m*a + b, " ") #on remplace la place de l'individu par une case vide (avec un " ")
            relocation = np.array([[relocation[m*j + i] for i in range(0, m)] for j in range(0, n) ]) #on remet le monde sous forme de tableau
                # on remplace la case vide par l'individu
            relocation = np.delete(relocation, m*(move_line) + move_column) #on copie le monde sans la case vide
            relocation = np.insert(relocation, m*(move_line) + move_column, "t") #on remplace la place de la case vide par l'individu (ant)
            relocation = np.array([[relocation[m*j + i] for i in range(0, m)] for j in range(0, n) ]) #on remet le monde sous forme de tableau


                    
        else : #l'individu suit le chemin de phéromones le plus marqué
            print("oui")
            relocation = np.delete(relocation, m*move_line + move_column) #on copie le monde sans l'individu
            relocation = np.insert(relocation, m*move_line + move_column, " ") #on remplace la place de l'individu par une case vide (avec un " ")
            relocation = np.array([[relocation[m*j + i] for i in range(0, m)] for j in range(0, n)]) #on remet le monde sous forme de tableau
            way_home = choose_the_way(pher_home_map, move_line, move_column)
            if way_home == 0:
                if move_line > 0 and (relocation[move_line - 1, move_column] == " " or relocation[move_line - 1, move_column] == "p"): #la prochaine case existe et est vide
                    move_line = move_line - 1
                    move_column = move_column
                if move_line > 1 and (relocation[move_line - 2, move_column] == " " or relocation[move_line - 2, move_column] == "p") and (relocation[move_line - 1, move_column] == "f" or relocation[move_line - 1, move_column] == "s"): #la prochaine case existe et est vide
                    move_line = move_line - 2
                    move_column = move_column
                    
            if way_home == 1:
                if move_column < m - 1 and (relocation[move_line, move_column + 1] == " " or relocation[move_line + 1, move_column + 1] == "p"):
                    move_line = move_line
                    move_column = move_column + 1
                if move_column < m - 2 and (relocation[move_line, move_column + 2] == " " or relocation[move_line, move_column + 2] == "p") and (relocation[move_line, move_column + 1] == "f" or relocation[move_line, move_column + 1] == "s"):
                    move_line = move_line
                    move_column = move_column + 2
                    
            if way_home == 2:
                if move_line < n - 1 and (relocation[move_line + 1, move_column] == " " or relocation[move_line + 1, move_column] == "p"):
                    move_line = move_line + 1
                    move_column = move_column
                if move_line < n - 2 and (relocation[move_line + 2, move_column] == " " or relocation[move_line + 2, move_column] == "p") and (relocation[move_line + 1, move_column] == "f" or relocation[move_line + 1, move_column] == "s"):
                    move_line = move_line + 2
                    move_column = move_column

            if way_home == 3:
                if move_column > 0 and (relocation[move_line, move_column - 1] == " " or relocation[move_line, move_column - 1] == "p"):
                    move_line = move_line
                    move_column = move_column - 1
                if move_column > 1 and (relocation[move_line, move_column - 2] == " " or relocation[move_line, move_column - 2] == "p") and (relocation[move_line, move_column - 1] == "f" or relocation[move_line, move_column - 1] == "s"):
                    move_line = move_line
                    move_column = move_column - 2
                    
                    
            #on déplace et modifie l'horloge de la fourmi
            clock1 = np.array(clock)
            clock = np.delete(clock1, m*move_line + move_column)
            clock = np.insert(clock, m*move_line + move_column, int(clock1[a, b] - 1))
            clock = np.array([[clock[m*j + i] for i in range(0, m)] for j in range(0, n)])  
            if a != move_line or b != move_column:
                clock = np.delete(clock, m*a + b)
                clock = np.insert(clock, m*a + b, 0)
                clock = np.array([[clock[m*j + i] for i in range(0, m)] for j in range(0, n)])   
                
             #mort d'une fourmi si déplacement sur piège
            if relocation[move_line, move_column] == "p":
                clock = np.delete(clock, m*move_line + move_column)
                clock = np.insert(clock, m*move_line + move_column, 0)
                clock = np.array([[clock[m*j + i] for i in range(0, m)] for j in range(0, n)]) 
                
            # on supprime l'indidu du monde
            relocation = np.delete(relocation, m*a + b) #on copie le monde sans l'individu
            relocation = np.insert(relocation, m*a + b, " ") #on remplace la place de l'individu par une case vide (avec un " ")
            relocation = np.array([[relocation[m*j + i] for i in range(0, m)] for j in range(0, n) ]) #on remet le monde sous forme de tableau
                # on remplace la case vide par l'individu
            relocation = np.delete(relocation, m*(move_line) + move_column) #on copie le monde sans la case vide
            relocation = np.insert(relocation, m*(move_line) + move_column, "t") #on remplace la place de la case vide par l'individu (ant)
            relocation = np.array([[relocation[m*j + i] for i in range(0, m)] for j in range(0, n) ]) #on remet le monde sous forme de tableau
            
        
        #la fourmi est morte
        if clock[move_line, move_column] <= 0:
            relocation = np.delete(relocation, m*move_line + move_column)
            relocation = np.insert(relocation, m*move_line + move_column, " ") #on remplace la place de l'individu par une case vide (avec un " ")
            relocation = np.array([[relocation[m*j + i] for i in range(0, m)] for j in range(0, n) ]) #on remet le monde sous forme de tableau

    return [relocation, pher_home_map, pher_food_map, clock]
    
   Un petit exemple :
   
   ![image](https://user-images.githubusercontent.com/80055517/117031250-ae408000-ad00-11eb-871e-b81b346de17d.png)

La fonction renvoie (dans l'ordre mais pas sur l'exemple par manque de place) : la carte des fourmis, la carte des phéromones maison, la carte des phéromones nourriture et la carte des horloges.
Un exemple de l'action d'un piège :

![image](https://user-images.githubusercontent.com/80055517/117034024-3162d580-ad03-11eb-95b4-494f70d6e334.png)

![image](https://user-images.githubusercontent.com/80055517/117034085-40e21e80-ad03-11eb-8725-97e2bc4baf7c.png)


Deux autres actions sont effectuables par les fourmis : prendre et déposer la nourriture. On a donc les fonctions **take_food** et **drop_food**.
La première examine le voisinage de la fourmi de coordonées [a, b] et vérifie que celle-ci est bien sans nourriture et s'est déplacée ('g'). Si de la nourriture se trouve dans le voisinage de la fourmi (une case de la carte de la nourriture n'est pas nulle), cette fourmi va se transformer en fourmi avec nourriture ayant bougée ('t'), la valeur de la nourriture va diminuer de un et la fourmi va gagner une récompense (reward) de durée de vie supplémentaire. Si la valeur de la nourriture atteint 0 on enlève la source sur la carte fourmis.

    def take_food(map, food_map, clock_map, a, b):
    """Précondition : 0 >= a >= n, 0 >= b >= m
    Renvoie les mêmes cartes avec une unité de moins sur la nourriture, un bonus de temps de vie sur l'horloge et une fourmi transformée"""
    mapf = map
    food = food_map
    clock = clock_map
    food_value = 0
    life = clock[a, b]
    if map[a, b] == "g": # la cellule sélectionnée est une fourmi sans nourriture ayant bougé
        if 0 < a < n-1 and 0 < b < m-1 : #pas de problème avec les bords
            for i in range(0, 3):
                for j in range(0, 3):
                    if not(no_food(map, a, b)):
                        if spatial_pher_neighborhood(food, a, b, neigh)[i, j] != 0: #la case a de la nourriture
                            food_value = spatial_pher_neighborhood(food, a, b, neigh)[i, j]
                            food = np.delete(food, m*(a - 1 + i) + (b - 1 + j))
                            food = np.insert(food, m*(a - 1 + i) + (b - 1 + j), food_value - 1) #on enlève 1 à la valeur de nourriture
                            food = np.array([[food[m*k + l] for l in range(0, m)] for k in range(0, n)])
                            
                            clock = np.delete(clock, m*a + b)
                            clock = np.insert(clock, m*a + b, int(life + reward))
                            clock = np.array([[clock[m*j + i] for i in range(0, m)] for j in range(0, n)])  
                            mapf = np.delete(mapf, m*a + b) #on copie le monde sans l'individu
                            mapf = np.insert(mapf, m*a + b, "t") #on remplace la place de l'individu par une fourmi avec nourriture mais s'étant déplacée (un "t")
                            mapf = np.array([[mapf[m*j + i] for i in range(0, m)] for j in range(0, n) ]) #on remet le monde sous forme de tableau
                            # on enlève la nourriture si sa valeur est 0
                            if food_value - 1 == 0:
                                mapf = np.delete(mapf, m*(a - 1 + i) + (b - 1 + j))
                                mapf = np.insert(mapf, m*(a - 1 + i) + (b - 1 + j), " ")
                                mapf = np.array([[mapf[m*k + l] for l in range(0, m)] for k in range(0, n)])
        if a == 0 and 0 < b < m-1: # on a atteint le bord haut
            for i in range(0, 2):
                for j in range(0, 3):
                    if not(no_food(map, a, b)):
                        if spatial_pher_neighborhood(food, a, b, neigh)[i, j] != 0: #la case a de la nourriture
                            food_value = spatial_pher_neighborhood(food, a, b, neigh)[i, j]
                            food = np.delete(food, m*(a + i) + (b - 1 + j))
                            food = np.insert(food, m*(a + i) + (b - 1 + j), food_value - 1) #on enlève 1 à la valeur de nourriture
                            food = np.array([[food[m*k + l] for l in range(0, m)] for k in range(0, n)])
                            
                            clock = np.delete(clock, m*a + b)
                            clock = np.insert(clock, m*a + b, int(life + reward))
                            clock = np.array([[clock[m*j + i] for i in range(0, m)] for j in range(0, n)])  
                            mapf = np.delete(mapf, m*a + b) #on copie le monde sans l'individu
                            mapf = np.insert(mapf, m*a + b, "t") #on remplace la place de l'individu par une fourmi avec nourriture mais s'étant déplacée (un "t")
                            mapf = np.array([[mapf[m*j + i] for i in range(0, m)] for j in range(0, n) ]) #on remet le monde sous forme de tableau
                            # on enlève la nourriture si sa valeur est 0
                            if food_value - 1 == 0:
                                mapf = np.delete(mapf, m*(a + i) + (b - 1 + j))
                                mapf = np.insert(mapf, m*(a + i) + (b - 1 + j), " ")
                                mapf = np.array([[mapf[m*k + l] for l in range(0, m)] for k in range(0, n)])
        if a == 0 and b == 0: # on a atteint le bord haut gauche
            for i in range(0, 2):
                for j in range(0, 2):
                    if not(no_food(map, a, b)):
                        if spatial_pher_neighborhood(food, a, b, neigh)[i, j] != 0: #la case a de la nourriture
                            food_value = spatial_pher_neighborhood(food, a, b, neigh)[i, j]
                            food = np.delete(food, m*(a + i) + (b + j))
                            food = np.insert(food, m*(a + i) + (b + j), food_value - 1) #on enlève 1 à la valeur de nourriture
                            food = np.array([[food[m*k + l] for l in range(0, m)] for k in range(0, n)])
                            
                            clock = np.delete(clock, m*a + b)
                            clock = np.insert(clock, m*a + b, int(life + reward))
                            clock = np.array([[clock[m*j + i] for i in range(0, m)] for j in range(0, n)])  
                            mapf = np.delete(mapf, m*a + b) #on copie le monde sans l'individu
                            mapf = np.insert(mapf, m*a + b, "t") #on remplace la place de l'individu par une fourmi avec nourriture mais s'étant déplacée (un "t")
                            mapf = np.array([[mapf[m*j + i] for i in range(0, m)] for j in range(0, n) ]) #on remet le monde sous forme de tableau
                            # on enlève la nourriture si sa valeur est 0
                            if food_value - 1 == 0:
                                mapf = np.delete(mapf, m*(a + i) + (b + j))
                                mapf = np.insert(mapf, m*(a + i) + (b + j), " ")
                                mapf = np.array([[mapf[m*k + l] for l in range(0, m)] for k in range(0, n)])
        if a == 0 and b == m-1: #on a atteint le bord haut droit
            for i in range(0, 2):
                for j in range(0, 2):
                    if not(no_food(map, a, b)):
                        if spatial_pher_neighborhood(food, a, b, neigh)[i, j] != 0: #la case a de la nourriture
                            food_value = spatial_pher_neighborhood(food, a, b, neigh)[i, j]
                            food = np.delete(food, m*(a + i) + (b - 1 + j))
                            food = np.insert(food, m*(a + i) + (b - 1 + j), food_value - 1) #on enlève 1 à la valeur de nourriture
                            food = np.array([[food[m*k + l] for l in range(0, m)] for k in range(0, n)])
                            
                            clock = np.delete(clock, m*a + b)
                            clock = np.insert(clock, m*a + b, int(life + reward))
                            clock = np.array([[clock[m*j + i] for i in range(0, m)] for j in range(0, n)])  
                            mapf = np.delete(mapf, m*a + b) #on copie le monde sans l'individu
                            mapf = np.insert(mapf, m*a + b, "t") #on remplace la place de l'individu par une fourmi avec nourriture mais s'étant déplacée (un "t")
                            mapf = np.array([[mapf[m*j + i] for i in range(0, m)] for j in range(0, n) ]) #on remet le monde sous forme de tableau
                            # on enlève la nourriture si sa valeur est 0
                            if food_value - 1 == 0:
                                mapf = np.delete(mapf, m*(a + i) + (b - 1 + j))
                                mapf = np.insert(mapf, m*(a + i) + (b - 1 + j), " ")
                                mapf = np.array([[mapf[m*k + l] for l in range(0, m)] for k in range(0, n)])
        if a == n-1 and 0 < b < m-1: # on a atteint le bord bas
            for i in range(0, 2):
                for j in range(0, 3):
                    if not(no_food(map, a, b)):
                        if spatial_pher_neighborhood(food, a, b, neigh)[i, j] != 0: #la case a de la nourriture
                            food_value = spatial_pher_neighborhood(food, a, b, neigh)[i, j]
                            food = np.delete(food, m*(a - 1 + i) + (b - 1 + j))
                            food = np.insert(food, m*(a - 1 + i) + (b - 1 + j), food_value - 1) #on enlève 1 à la valeur de nourriture
                            food = np.array([[food[m*k + l] for l in range(0, m)] for k in range(0, n)])
                            
                            clock = np.delete(clock, m*a + b)
                            clock = np.insert(clock, m*a + b, int(life + reward))
                            clock = np.array([[clock[m*j + i] for i in range(0, m)] for j in range(0, n)])  
                            mapf = np.delete(mapf, m*a + b) #on copie le monde sans l'individu
                            mapf = np.insert(mapf, m*a + b, "t") #on remplace la place de l'individu par une fourmi avec nourriture mais s'étant déplacée (un "t")
                            mapf = np.array([[mapf[m*j + i] for i in range(0, m)] for j in range(0, n) ]) #on remet le monde sous forme de tableau
                            # on enlève la nourriture si sa valeur est 0
                            if food_value - 1 == 0:
                                mapf = np.delete(mapf, m*(a - 1 + i) + (b - 1 + j))
                                mapf = np.insert(mapf, m*(a - 1 + i) + (b - 1 + j), " ")
                                mapf = np.array([[mapf[m*k + l] for l in range(0, m)] for k in range(0, n)])
        if a == n-1 and b == 0: # on a atteint le bord bas gauche
            for i in range(0, 2):
                for j in range(0, 2):
                    if not(no_food(map, a, b)):
                        if spatial_pher_neighborhood(food, a, b, neigh)[i, j] != 0: #la case a de la nourriture
                            food_value = spatial_pher_neighborhood(food, a, b, neigh)[i, j]
                            food = np.delete(food, m*(a - 1 + i) + (b + j))
                            food = np.insert(food, m*(a - 1 + i) + (b + j), food_value - 1) #on enlève 1 à la valeur de nourriture
                            food = np.array([[food[m*k + l] for l in range(0, m)] for k in range(0, n)])
                            
                            clock = np.delete(clock, m*a + b)
                            clock = np.insert(clock, m*a + b, int(life + reward))
                            clock = np.array([[clock[m*j + i] for i in range(0, m)] for j in range(0, n)])  
                            mapf = np.delete(mapf, m*a + b) #on copie le monde sans l'individu
                            mapf = np.insert(mapf, m*a + b, "t") #on remplace la place de l'individu par une fourmi avec nourriture mais s'étant déplacée (un "t")
                            mapf = np.array([[mapf[m*j + i] for i in range(0, m)] for j in range(0, n) ]) #on remet le monde sous forme de tableau
                            # on enlève la nourriture si sa valeur est 0
                            if food_value - 1 == 0:
                                mapf = np.delete(mapf, m*(a - 1 + i) + (b + j))
                                mapf = np.insert(mapf, m*(a - 1 + i) + (b + j), " ")
                                mapf = np.array([[mapf[m*k + l] for l in range(0, m)] for k in range(0, n)])
        if a == n-1 and b == m-1: #on a atteint le bord bas droit
            for i in range(0, 2):
                for j in range(0, 2):
                    if not(no_food(map, a, b)):
                        if spatial_pher_neighborhood(food, a, b, neigh)[i, j] != 0: #la case a de la nourriture
                            food_value = spatial_pher_neighborhood(food, a, b, neigh)[i, j]
                            food = np.delete(food, m*(a - 1 + i) + (b - 1 + j))
                            food = np.insert(food, m*(a - 1 + i) + (b - 1 + j), food_value - 1) #on enlève 1 à la valeur de nourriture
                            food = np.array([[food[m*k + l] for l in range(0, m)] for k in range(0, n)])
                            
                            clock = np.delete(clock, m*a + b)
                            clock = np.insert(clock, m*a + b, int(life + reward))
                            clock = np.array([[clock[m*j + i] for i in range(0, m)] for j in range(0, n)])  
                            mapf = np.delete(mapf, m*a + b) #on copie le monde sans l'individu
                            mapf = np.insert(mapf, m*a + b, "t") #on remplace la place de l'individu par une fourmi avec nourriture mais s'étant déplacée (un "t")
                            mapf = np.array([[mapf[m*j + i] for i in range(0, m)] for j in range(0, n) ]) #on remet le monde sous forme de tableau
                            # on enlève la nourriture si sa valeur est 0
                            if food_value - 1 == 0:
                                mapf = np.delete(mapf, m*(a - 1 + i) + (b - 1 + j))
                                mapf = np.insert(mapf, m*(a - 1 + i) + (b - 1 + j), " ")
                                mapf = np.array([[mapf[m*k + l] for l in range(0, m)] for k in range(0, n)])

    return [mapf, food, clock]

La fonction renvoie donc la carte fourmis après la prise de nourriture, celle de la nourriture et celle des horloges.

Avant la prise de nourriture :

![image](https://user-images.githubusercontent.com/80055517/117034306-7424ad80-ad03-11eb-9ae1-8f4d8e6f2b26.png)

![image](https://user-images.githubusercontent.com/80055517/117034358-83a3f680-ad03-11eb-99f1-ae3b5ade15f7.png)

Après la prise de nourriture :

![image](https://user-images.githubusercontent.com/80055517/117034435-97e7f380-ad03-11eb-9221-63806fe989c4.png)

![image](https://user-images.githubusercontent.com/80055517/117034495-a6cea600-ad03-11eb-9241-7cd692118eac.png)

La fonction **drop_food** retransforme une fourmi avec nourriture ayant bougée ('t') en un fourmi exploratrice ayant bougée ('g') si elle est à côté de la fourmilière. De plus le compte de la nourriture de la fourmilière augmente alors de un.

    def drop_food(map, food_count, a, b):
    """Retourne la map où la fourmi avec nourriture en [a, b] dépose sa nourriture dans le nid et redevient chercheuse, ajoute un au compteur de nourriture"""
    ant = map[a, b]
    map1 = map
    count = food_count
    if ant == "t": #la case est bien une fourmi avec nourriture ayant bougé
        if not(no_home(map, a, b)):
            map1 = np.delete(map1, m*a + b)
            map1 = np.insert(map1, m*a + b, "g")
            map1 = np.array([[map1[m*k+l] for l in range(0, m)] for k in range(0, n)])
            count = count + 1
    return [map1, count]
    
   La fonction renvoie la carte fourmis et le compte de nourriture après dépôt.
   
![image](https://user-images.githubusercontent.com/80055517/117035097-3a07db80-ad04-11eb-8c6d-e42a18257fc5.png)

![image](https://user-images.githubusercontent.com/80055517/117035249-61f73f00-ad04-11eb-8536-32004a36f741.png)

![image](https://user-images.githubusercontent.com/80055517/117035304-72a7b500-ad04-11eb-8ad2-e64c5f73985b.png)

Voilà maintenant la fonction qui effectue un tour complet du modèle, c'est à dire le déplacement selon la fonction **relocation**, la prise de nourriture avec **take_food** et le dépôt avec **drop_food** pour chacune des cases de la carte. Elle ajoute également une fonctionnalité : la création de nouvelles fourmis. En effet, si le compte de nourriture déposé à la fourmilière est supérieur à un seuil (creation_rate), une nouvelle fourmi est créée.

    def one_turn(map, map_pher_home, map_pher_food, food_map, clock_map, count):
    """Renvoie la map après avoir effectuer sur toutes les cases une relocation"""
    one_map = map
    one_pher_home_map = map_pher_home
    one_pher_food_map = map_pher_food
    one_food_map = food_map
    one_clock = clock_map
    one_count = count
    for i in range(0, n):
        for j in range(0, m):
            if one_map[i, j] != " ":
                a = spatial_relocation(one_map, one_pher_home_map, one_pher_food_map, one_clock, i, j)
                one_map = a[0]
                one_pher_home_map = a[1]
                one_pher_food_map = a[2]
                one_clock = a[3]
    for i in range(0, n):
        for j in range(0, m):
            if one_map[i, j] == "g" or one_map[i, j] == "t":
                b = take_food(one_map, one_food_map, one_clock, i, j) #si une fourmi est à côté de nourriture on fait la procédure
                one_map = b[0]
                c = drop_food(one_map, one_count, i, j)
                one_map = c[0] #si une fourmi avec nourriture arrive au nid elle dépose la nourriture
                one_food_map = b[1]
                one_clock = b[2]
                one_count = c[1]

    for i in range(0, n):
        for j in range(0, m):
            if one_map[i, j] == "g":
                one_map = np.delete(one_map, m*i + j)
                one_map = np.insert(one_map, m*i + j, "f")
                one_map = np.array([[one_map[m*k + l] for l in range(0, m)] for k in range(0, n)])
            elif one_map[i, j] == "t":
                one_map = np.delete(one_map, m*i + j)
                one_map = np.insert(one_map, m*i + j, "s")
                one_map = np.array([[one_map[m*k + l] for l in range(0, m)] for k in range(0, n)])
                
    #création d'une fourmi si le compte de nourriture atteint creation_rate
    if one_count >= creation_rate:
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                for k in range(0, 3):
                    for l in range(0, 3):
                        if spatial_ants_neighborhood(one_map, i, j, neigh)[k, l] == "h" and one_map[i, j] == " " and one_count >= creation_rate:
                            one_map = np.delete(one_map, m*i + j)
                            one_map = np.insert(one_map, m*i + j, "f")
                            one_map = np.array([[one_map[m*k + l] for l in range(0, m)] for k in range(0, n)])
                            one_clock = np.delete(one_clock, m*i + j)
                            one_clock = np.insert(one_clock, m*i + j, life_time)
                            one_clock = np.array([[one_clock[m*k + l] for l in range(0, m)] for k in range(0, n)])                            
                            one_count = one_count - creation_rate
    one = [one_map, one_pher_home_map, one_pher_food_map, one_food_map, one_clock, one_count]

    return one

![image](https://user-images.githubusercontent.com/80055517/117036973-455c0680-ad06-11eb-9004-02d3b9889ac9.png)


Le dernier élément à ajouter à l'édifice est le facteur d'exploration. Celui-ci entraine un déplacement aléatoire périodique tous les "exploration_rate" tours. Son codage est similaire à la partie aléatoire du déplacement avec **relocation**.

Un mouvement ératique :

    def one_eratic_move(map, map_pher_home, map_pher_food, clock_map, a, b):
    """Retourne les différentes maps après un déplacement aléatoire de la fourmis, y compris si elle suit un chemin de phéromones"""
    ant = map[a, b] #on enregistre la cellule à déplacer (une fourmi)
    pher_food_map = map_pher_food
    pher_home_map = map_pher_home
    relocation = map
    clock = clock_map
    move_line = a
    move_column = b
    if ant == "f": #déplacement des fourmis en recherche de nourriture
        pher_home_map = np.delete(pher_home_map, m*move_line + move_column)
        pher_home_map = np.insert(pher_home_map, m*move_line + move_column, pers_pher) # sur la map de phéromones "maison" la case de même coordonnées que la fourmi prend la valeur de la persistance des phéromones
        pher_home_map = np.array([[pher_home_map[m*j + i] for i in range(0, m)] for j in range(0, n)])
        next_move = random.randint(0, 3) #on décide le prochain mouvement au hasard
        if next_move == 0:
             if move_line > 0 and relocation[move_line - 1, move_column] == " " and pher_home_map[move_line - 1, move_column] < pers_pher - memory: #la prochaine case existe et est vide
                move_line = move_line - 1
                move_column = move_column
                    
        elif next_move == 1:
            if move_column < m - 1 and relocation[move_line, move_column + 1] == " " and pher_home_map[move_line, move_column + 1] < pers_pher - memory:
                move_line = move_line
                move_column = move_column + 1
                    
        elif next_move == 2:
            if move_line < n - 1 and relocation[move_line + 1, move_column] == " " and pher_home_map[move_line + 1, move_column] < pers_pher - memory:
                move_line = move_line + 1
                move_column = move_column
                    
        elif next_move == 3:
            if move_column > 0 and relocation[move_line, move_column - 1] == " " and pher_home_map[move_line, move_column - 1] < pers_pher - memory:
                move_line = move_line
                move_column = move_column - 1
                    
            #on déplace et modifie l'horloge de la fourmi
        clock1 = np.array(clock)
        clock = np.delete(clock1, m*move_line + move_column)
        clock = np.insert(clock, m*move_line + move_column, int(clock1[a, b] - 1))
        clock = np.array([[clock[m*j + i] for i in range(0, m)] for j in range(0, n)])  
        if a != move_line or b != move_column:
            clock = np.delete(clock, m*a + b)
            clock = np.insert(clock, m*a + b, 0)
            clock = np.array([[clock[m*j + i] for i in range(0, m)] for j in range(0, n)])     
                
            # on supprime l'indidu du monde
        relocation = np.delete(relocation, m*a + b) #on copie le monde sans l'individu
        relocation = np.insert(relocation, m*a + b, " ") #on remplace la place de l'individu par une case vide (avec un " ")
        relocation = np.array([[relocation[m*j + i] for i in range(0, m)] for j in range(0, n) ]) #on remet le monde sous forme de tableau
                # on remplace la case vide par l'individu
        relocation = np.delete(relocation, m*(move_line) + move_column) #on copie le monde sans la case vide
        relocation = np.insert(relocation, m*(move_line) + move_column, "g") #on remplace la place de la case vide par l'individu (ant)
        relocation = np.array([[relocation[m*j + i] for i in range(0, m)] for j in range(0, n) ]) #on remet le monde sous forme de tableau
    if ant == "s": #déplacement des fourmis ayant trouvé de la nourriture
        pher_food_map = np.delete(pher_food_map, m*move_line + move_column)
        pher_food_map = np.insert(pher_food_map, m*move_line + move_column, pers_pher) # sur la map de phéromones "nourriture" la case de même coordonnées que la fourmi prend la valeur de la persistance des phéromones
        pher_food_map = np.array([[pher_food_map[m*j + i] for i in range(0, m)] for j in range(0, n)])
        next_move = random.randint(0, 3) #on décide le prochain mouvement au hasard
        if next_move == 0:
            if move_line > 0 and relocation[move_line - 1, move_column] == " " and pher_food_map[move_line, move_column - 1] < pers_pher - 2: #la prochaine case existe et est vide
                move_line = move_line - 1
                move_column = move_column
                    
        elif next_move == 1:
            if move_column < m - 1 and relocation[move_line, move_column + 1] == " " and pher_food_map[move_line, move_column - 1] < pers_pher - 2:
                move_line = move_line
                move_column = move_column + 1
                   
        elif next_move == 2:
            if move_line < n - 1 and relocation[move_line + 1, move_column] == " " and pher_food_map[move_line, move_column - 1] < pers_pher - 2:
                move_line = move_line + 1
                move_column = move_column
                    
        elif next_move == 3:
            if move_column > 0 and relocation[move_line, move_column - 1] == " " and pher_food_map[move_line, move_column - 1] < pers_pher - 2:
                move_line = move_line
                move_column = move_column - 1
                                        
            #on déplace et modifie l'horloge de la fourmi
        clock1 = np.array(clock)
        clock = np.delete(clock1, m*move_line + move_column)
        clock = np.insert(clock, m*move_line + move_column, int(clock1[a, b] - 1))
        clock = np.array([[clock[m*j + i] for i in range(0, m)] for j in range(0, n)])  
        if a != move_line or b != move_column:
            clock = np.delete(clock, m*a + b)
            clock = np.insert(clock, m*a + b, 0)
            clock = np.array([[clock[m*j + i] for i in range(0, m)] for j in range(0, n)])     
                
            # on supprime l'indidu du monde
        relocation = np.delete(relocation, m*a + b) #on copie le monde sans l'individu
        relocation = np.insert(relocation, m*a + b, " ") #on remplace la place de l'individu par une case vide (avec un " ")
        relocation = np.array([[relocation[m*j + i] for i in range(0, m)] for j in range(0, n) ]) #on remet le monde sous forme de tableau
                # on remplace la case vide par l'individu
        relocation = np.delete(relocation, m*(move_line) + move_column) #on copie le monde sans la case vide
        relocation = np.insert(relocation, m*(move_line) + move_column, "t") #on remplace la place de la case vide par l'individu (ant)
        relocation = np.array([[relocation[m*j + i] for i in range(0, m)] for j in range(0, n) ]) #on remet le monde sous forme de tableau
 
    return [relocation, pher_home_map, pher_food_map, clock]
    
 Un tour de mouvement ératique pour toutes les fourmis :

    def one_turn_eratic(map, map_pher_home, map_pher_food, clock_map):
    """Retourne les maps après un déplacement aléatoire de toute les fourmis"""
    one_map1 = map
    one_pher_home_map1 = map_pher_home
    one_pher_food_map1 = map_pher_food
    one_clock1 = clock_map
    one_map2 = map
    one_pher_home_map2 = map_pher_home
    one_pher_food_map2 = map_pher_food
    one_clock2 = clock_map
    one = [one_pher_home_map1, one_pher_food_map1, one_clock1, one_map1]
    for i in range(0, n):
        for j in range(0, m):
            if one_map1[i, j] != " ":
                a = one_eratic_move(one_map1, one_pher_home_map1, one_pher_food_map1, one_clock1, i, j)
                one_map2 = a[0]
                one_pher_home_map2 = a[1]
                one_pher_food_map2 = a[2]
                one_clock2 = a[3]
                one = a
                one_map1 = one_map2
                one_pher_home_map1 = one_pher_home_map2
                one_pher_food_map1 = one_pher_food_map2
                one_clock1 = one_clock2

    for i in range(0, n):
        for j in range(0, m):
            if one_map1[i, j] == "g":
                one_map1 = np.delete(one_map1, m*i + j)
                one_map1 = np.insert(one_map1, m*i + j, "f")
                one_map1 = np.array([[one_map1[m*k + l] for l in range(0, m)] for k in range(0, n)])
            elif one_map1[i, j] == "t":
                one_map1 = np.delete(one_map1, m*i + j)
                one_map1 = np.insert(one_map1, m*i + j, "s")
                one_map1 = np.array([[one_map1[m*k + l] for l in range(0, m)] for k in range(0, n)])
    return one

Le facteur d'exploration permet théoriquement aux fourmis d'innover en sortant un peu des chemins tracés pour éventuellement en trouver un plus efficace qui sera à terme privilégié par une plus forte présence de phéromones.

Il ne reste plus qu'à assembler le tout dans la fonction **simulation**

    def simulation(map, map_pher_home, map_pher_food, food_map, clock_map, food_count, max_turn):
    """Effectue la simulation complète"""
    sim_map = map
    sim_pher_home = map_pher_home
    sim_pher_food = map_pher_food
    sim_food = food_map
    sim_clock = clock_map
    sim_count = food_count
    sim = [sim_map, sim_pher_home, sim_pher_food, sim_food, sim_clock, sim_count]
    for t in range(0, max_turn):
        a = one_turn(sim_map, sim_pher_home, sim_pher_food, sim_food, sim_clock, sim_count)
        sim_map = a[0]
        sim_pher_home = a[1]
        sim_pher_food = a[2]
        sim_food = a[3]
        sim_clock = a[4]
        sim_count = a[5]
        for i in range(0, n):
            for j in range(0, m):
                if sim_pher_home[i, j] > 0 :
                    sim_pher_home[i, j] = sim_pher_home[i, j] - 1
                if int(sim_pher_food[i, j]) > 0 :
                    sim_pher_food[i, j] = sim_pher_food[i, j] - 1
        print("tour :")
        print(t)
        print("sim_map :")
        print(sim_map)

        if t % exploration_rate == 0:
            b = one_turn_eratic(sim_map, sim_pher_home, sim_pher_food, sim_clock)
            sim_map = b[0]
            sim_pher_home = b[1]
            sim_pher_food = b[2]
            sim_clock = b[3]
        sim = [sim_map, sim_pher_home, sim_pher_food, sim_food, sim_clock, sim_count]
    return sim

### Présensentation et analyse des résultats

tour :
55
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' 'f' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[55 50 75 69 65  0  0  0  0  0]
 [56 85 58 65 66  0  0  0  0  0]
 [85 48 46 45  0  0  0  0  0  0]
 [92 95 45 44  0  0  0  0  0  0]
 [ 0 95 96  0  0  0  0  0  0  0]
 [ 0  0 97  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_food :
[[ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [10  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0 144   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
life 143
tour :
56
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' 'f' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[54 49 74 68 64  0  0  0  0  0]
 [55 84 57 64 65  0  0  0  0  0]
 [84 47 45 44  0  0  0  0  0  0]
 [91 94 44 43  0  0  0  0  0  0]
 [ 0 94 95  0  0  0  0  0  0  0]
 [ 0  0 96  0  0  0  0  0  0  0]
 [ 0  0 98  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_food :
[[ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [10  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0 143   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
life 142
tour :
57
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' 's' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[53 48 73 67 63  0  0  0  0  0]
 [54 83 56 63 64  0  0  0  0  0]
 [83 46 44 43  0  0  0  0  0  0]
 [90 93 43 42  0  0  0  0  0  0]
 [ 0 93 94  0  0  0  0  0  0  0]
 [ 0  0 95  0  0  0  0  0  0  0]
 [ 0 98 97  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0 152   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
oui
pher_value : 98
up 0
right 97
down 0
left 0
second 0
life 151
tour :
58
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' 's' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[52 47 72 66 62  0  0  0  0  0]
 [53 82 55 62 63  0  0  0  0  0]
 [82 45 43 42  0  0  0  0  0  0]
 [89 92 42 41  0  0  0  0  0  0]
 [ 0 92 93  0  0  0  0  0  0  0]
 [ 0  0 94  0  0  0  0  0  0  0]
 [ 0 97 96  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0 99  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0 151   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
oui
pher_value : 96
up 94
right 0
down 0
left 97
second 94
re2
0
life 150
tour :
59
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' 's' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[51 46 71 65 61  0  0  0  0  0]
 [52 81 54 61 62  0  0  0  0  0]
 [81 44 42 41  0  0  0  0  0  0]
 [88 91 41 40  0  0  0  0  0  0]
 [ 0 91 92  0  0  0  0  0  0  0]
 [ 0  0 93  0  0  0  0  0  0  0]
 [ 0 96 95  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0 98 99  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0 150   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
oui
pher_value : 93
up 92
right 0
down 95
left 0
second 92
life 149
tour :
60
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' 's' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[50 45 70 64 60  0  0  0  0  0]
 [51 80 53 60 61  0  0  0  0  0]
 [80 43 41 40  0  0  0  0  0  0]
 [87 90 40 39  0  0  0  0  0  0]
 [ 0 90 91  0  0  0  0  0  0  0]
 [ 0  0 92  0  0  0  0  0  0  0]
 [ 0 95 94  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0 99  0  0  0  0  0  0  0]
 [ 0 97 98  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0 149   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
life 148
tour :
61
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' 's' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[49 44 69 63 59  0  0  0  0  0]
 [50 79 52 59 60  0  0  0  0  0]
 [79 42 40 39  0  0  0  0  0  0]
 [86 89 39 38  0  0  0  0  0  0]
 [ 0 89 90  0  0  0  0  0  0  0]
 [ 0  0 91  0  0  0  0  0  0  0]
 [ 0 94 93  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0 99  0  0  0  0  0  0  0]
 [ 0  0 98  0  0  0  0  0  0  0]
 [ 0 96 97  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0 148   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
oui
pher_value : 91
up 90
right 0
down 93
left 0
second 90
life 147
tour :
62
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' 's' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[48 43 68 62 58  0  0  0  0  0]
 [49 78 51 58 59  0  0  0  0  0]
 [78 41 39 38  0  0  0  0  0  0]
 [85 88 38 37  0  0  0  0  0  0]
 [ 0 88 89  0  0  0  0  0  0  0]
 [ 0  0 90  0  0  0  0  0  0  0]
 [ 0 93 92  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0 98  0  0  0  0  0  0  0]
 [ 0  0 99  0  0  0  0  0  0  0]
 [ 0 95 96  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0 147   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
oui
pher_value : 89
up 38
right 0
down 90
left 88
second 88
life 146
tour :
63
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' 's' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[47 42 67 61 57  0  0  0  0  0]
 [48 77 50 57 58  0  0  0  0  0]
 [77 40 38 37  0  0  0  0  0  0]
 [84 87 37 36  0  0  0  0  0  0]
 [ 0 87 88  0  0  0  0  0  0  0]
 [ 0  0 89  0  0  0  0  0  0  0]
 [ 0 92 91  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0 99  0  0  0  0  0  0  0]
 [ 0  0 98  0  0  0  0  0  0  0]
 [ 0 94 95  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0 146   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
oui
pher_value : 87
up 87
right 88
down 0
left 0
second 87
re2
0
life 145
tour :
64
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' 's' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[46 41 66 60 56  0  0  0  0  0]
 [47 76 49 56 57  0  0  0  0  0]
 [76 39 37 36  0  0  0  0  0  0]
 [83 86 36 35  0  0  0  0  0  0]
 [ 0 86 87  0  0  0  0  0  0  0]
 [ 0  0 88  0  0  0  0  0  0  0]
 [ 0 91 90  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0 198  98   0   0   0   0   0   0   0]
 [  0   0  97   0   0   0   0   0   0   0]
 [  0  93  94   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0 145   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
oui
pher_value : 86
up 39
right 36
down 86
left 83
second 83
re2
3
life 144
tour :
65
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['s' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[45 40 65 59 55  0  0  0  0  0]
 [46 75 48 55 56  0  0  0  0  0]
 [75 38 36 35  0  0  0  0  0  0]
 [82 85 35 34  0  0  0  0  0  0]
 [ 0 85 86  0  0  0  0  0  0  0]
 [ 0  0 87  0  0  0  0  0  0  0]
 [ 0 90 89  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0  99   0   0   0   0   0   0   0   0]
 [  0 197  97   0   0   0   0   0   0   0]
 [  0   0  96   0   0   0   0   0   0   0]
 [  0  92  93   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [144   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
oui
pher_value : 82
up 75
right 85
down 0
left 0
second 75
re2
0
life 143
tour :
66
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 ['s' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[44 39 64 58 54  0  0  0  0  0]
 [45 74 47 54 55  0  0  0  0  0]
 [74 37 35 34  0  0  0  0  0  0]
 [81 84 34 33  0  0  0  0  0  0]
 [ 0 84 85  0  0  0  0  0  0  0]
 [ 0  0 86  0  0  0  0  0  0  0]
 [ 0 89 88  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [198  98   0   0   0   0   0   0   0   0]
 [  0 196  96   0   0   0   0   0   0   0]
 [  0   0  95   0   0   0   0   0   0   0]
 [  0  91  92   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [143   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
oui
pher_value : 74
up 45
right 37
down 81
left 0
second 45
re2
0
life 142
tour :
67
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['s' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[43 38 63 57 53  0  0  0  0  0]
 [44 73 46 53 54  0  0  0  0  0]
 [73 36 34 33  0  0  0  0  0  0]
 [80 83 33 32  0  0  0  0  0  0]
 [ 0 83 84  0  0  0  0  0  0  0]
 [ 0  0 85  0  0  0  0  0  0  0]
 [ 0 88 87  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [ 99   0   0   0   0   0   0   0   0   0]
 [197  97   0   0   0   0   0   0   0   0]
 [  0 195  95   0   0   0   0   0   0   0]
 [  0   0  94   0   0   0   0   0   0   0]
 [  0  90  91   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [142   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
oui
pher_value : 44
up 43
right 73
down 73
left 0
second 73
life 141
tour :
68
sim_map :
[['s' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[42 37 62 56 52  0  0  0  0  0]
 [43 72 45 52 53  0  0  0  0  0]
 [72 35 33 32  0  0  0  0  0  0]
 [79 82 32 31  0  0  0  0  0  0]
 [ 0 82 83  0  0  0  0  0  0  0]
 [ 0  0 84  0  0  0  0  0  0  0]
 [ 0 87 86  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[  0   0   0   0   0   0   0   0   0   0]
 [ 99   0   0   0   0   0   0   0   0   0]
 [ 98   0   0   0   0   0   0   0   0   0]
 [196  96   0   0   0   0   0   0   0   0]
 [  0 194  94   0   0   0   0   0   0   0]
 [  0   0  93   0   0   0   0   0   0   0]
 [  0  89  90   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[141   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
oui
pher_value : 42
up 0
right 37
down 43
left 0
second 37
re2
1
life 140
tour :
69
sim_map :
[[' ' 's' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[41 36 61 55 51  0  0  0  0  0]
 [42 71 44 51 52  0  0  0  0  0]
 [71 34 32 31  0  0  0  0  0  0]
 [78 81 31 30  0  0  0  0  0  0]
 [ 0 81 82  0  0  0  0  0  0  0]
 [ 0  0 83  0  0  0  0  0  0  0]
 [ 0 86 85  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 99   0   0   0   0   0   0   0   0   0]
 [ 98   0   0   0   0   0   0   0   0   0]
 [ 97   0   0   0   0   0   0   0   0   0]
 [195  95   0   0   0   0   0   0   0   0]
 [  0 193  93   0   0   0   0   0   0   0]
 [  0   0  92   0   0   0   0   0   0   0]
 [  0  88  89   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0 140   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
oui
pher_value : 36
up 0
right 61
down 71
left 41
second 61
re2
1
life 139
tour :
70
sim_map :
[[' ' ' ' 's' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[40 35 60 54 50  0  0  0  0  0]
 [41 70 43 50 51  0  0  0  0  0]
 [70 33 31 30  0  0  0  0  0  0]
 [77 80 30 29  0  0  0  0  0  0]
 [ 0 80 81  0  0  0  0  0  0  0]
 [ 0  0 82  0  0  0  0  0  0  0]
 [ 0 85 84  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 98  99   0   0   0   0   0   0   0   0]
 [ 97   0   0   0   0   0   0   0   0   0]
 [ 96   0   0   0   0   0   0   0   0   0]
 [194  94   0   0   0   0   0   0   0   0]
 [  0 192  92   0   0   0   0   0   0   0]
 [  0   0  91   0   0   0   0   0   0   0]
 [  0  87  88   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0 139   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
life 138
tour :
71
sim_map :
[[' ' ' ' 's' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[39 34 59 53 49  0  0  0  0  0]
 [40 69 42 49 50  0  0  0  0  0]
 [69 32 30 29  0  0  0  0  0  0]
 [76 79 29 28  0  0  0  0  0  0]
 [ 0 79 80  0  0  0  0  0  0  0]
 [ 0  0 81  0  0  0  0  0  0  0]
 [ 0 84 83  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 97  98  99   0   0   0   0   0   0   0]
 [ 96   0   0   0   0   0   0   0   0   0]
 [ 95   0   0   0   0   0   0   0   0   0]
 [193  93   0   0   0   0   0   0   0   0]
 [  0 191  91   0   0   0   0   0   0   0]
 [  0   0  90   0   0   0   0   0   0   0]
 [  0  86  87   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0 138   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
oui
pher_value : 59
up 0
right 53
down 42
left 34
second 42
re2
2
life 137
tour :
72
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' 's' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[38 33 58 52 48  0  0  0  0  0]
 [39 68 41 48 49  0  0  0  0  0]
 [68 31 29 28  0  0  0  0  0  0]
 [75 78 28 27  0  0  0  0  0  0]
 [ 0 78 79  0  0  0  0  0  0  0]
 [ 0  0 80  0  0  0  0  0  0  0]
 [ 0 83 82  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 96  97  99   0   0   0   0   0   0   0]
 [ 95   0   0   0   0   0   0   0   0   0]
 [ 94   0   0   0   0   0   0   0   0   0]
 [192  92   0   0   0   0   0   0   0   0]
 [  0 190  90   0   0   0   0   0   0   0]
 [  0   0  89   0   0   0   0   0   0   0]
 [  0  85  86   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0 137   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
oui
pher_value : 41
up 58
right 48
down 29
left 68
second 58
re2
0
life 136
tour :
73
sim_map :
[[' ' ' ' 's' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[37 32 57 51 47  0  0  0  0  0]
 [38 67 40 47 48  0  0  0  0  0]
 [67 30 28 27  0  0  0  0  0  0]
 [74 77 27 26  0  0  0  0  0  0]
 [ 0 77 78  0  0  0  0  0  0  0]
 [ 0  0 79  0  0  0  0  0  0  0]
 [ 0 82 81  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 95  96  98   0   0   0   0   0   0   0]
 [ 94   0  99   0   0   0   0   0   0   0]
 [ 93   0   0   0   0   0   0   0   0   0]
 [191  91   0   0   0   0   0   0   0   0]
 [  0 189  89   0   0   0   0   0   0   0]
 [  0   0  88   0   0   0   0   0   0   0]
 [  0  84  85   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0 136   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
oui
pher_value : 57
up 0
right 51
down 40
left 32
second 40
re2
2
life 135
tour :
74
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' 's' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[36 31 56 50 46  0  0  0  0  0]
 [37 66 39 46 47  0  0  0  0  0]
 [66 29 27 26  0  0  0  0  0  0]
 [73 76 26 25  0  0  0  0  0  0]
 [ 0 76 77  0  0  0  0  0  0  0]
 [ 0  0 78  0  0  0  0  0  0  0]
 [ 0 81 80  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 94  95  99   0   0   0   0   0   0   0]
 [ 93   0  98   0   0   0   0   0   0   0]
 [ 92   0   0   0   0   0   0   0   0   0]
 [190  90   0   0   0   0   0   0   0   0]
 [  0 188  88   0   0   0   0   0   0   0]
 [  0   0  87   0   0   0   0   0   0   0]
 [  0  83  84   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0 135   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
oui
pher_value : 39
up 56
right 46
down 27
left 66
second 56
re2
0
life 134
tour :
75
sim_map :
[[' ' ' ' 's' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[35 30 55 49 45  0  0  0  0  0]
 [36 65 38 45 46  0  0  0  0  0]
 [65 28 26 25  0  0  0  0  0  0]
 [72 75 25 24  0  0  0  0  0  0]
 [ 0 75 76  0  0  0  0  0  0  0]
 [ 0  0 77  0  0  0  0  0  0  0]
 [ 0 80 79  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 93  94  98   0   0   0   0   0   0   0]
 [ 92   0  99   0   0   0   0   0   0   0]
 [ 91   0   0   0   0   0   0   0   0   0]
 [189  89   0   0   0   0   0   0   0   0]
 [  0 187  87   0   0   0   0   0   0   0]
 [  0   0  86   0   0   0   0   0   0   0]
 [  0  82  83   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0 134   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
oui
pher_value : 55
up 0
right 49
down 38
left 30
second 38
re2
2
life 133
tour :
76
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' 's' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[34 29 54 48 44  0  0  0  0  0]
 [35 64 37 44 45  0  0  0  0  0]
 [64 27 25 24  0  0  0  0  0  0]
 [71 74 24 23  0  0  0  0  0  0]
 [ 0 74 75  0  0  0  0  0  0  0]
 [ 0  0 76  0  0  0  0  0  0  0]
 [ 0 79 78  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 92  93  99   0   0   0   0   0   0   0]
 [ 91   0  98   0   0   0   0   0   0   0]
 [ 90   0   0   0   0   0   0   0   0   0]
 [188  88   0   0   0   0   0   0   0   0]
 [  0 186  86   0   0   0   0   0   0   0]
 [  0   0  85   0   0   0   0   0   0   0]
 [  0  81  82   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0 133   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
oui
pher_value : 37
up 54
right 44
down 25
left 64
second 54
re2
0
life 132
tour :
77
sim_map :
[[' ' ' ' 's' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[33 28 53 47 43  0  0  0  0  0]
 [34 63 36 43 44  0  0  0  0  0]
 [63 26 24 23  0  0  0  0  0  0]
 [70 73 23 22  0  0  0  0  0  0]
 [ 0 73 74  0  0  0  0  0  0  0]
 [ 0  0 75  0  0  0  0  0  0  0]
 [ 0 78 77  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 91  92  98   0   0   0   0   0   0   0]
 [ 90   0  99   0   0   0   0   0   0   0]
 [ 89   0   0   0   0   0   0   0   0   0]
 [187  87   0   0   0   0   0   0   0   0]
 [  0 185  85   0   0   0   0   0   0   0]
 [  0   0  84   0   0   0   0   0   0   0]
 [  0  80  81   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0 132   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
oui
pher_value : 53
up 0
right 47
down 36
left 28
second 36
re2
2
life 131
tour :
78
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' 's' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[32 27 52 46 42  0  0  0  0  0]
 [33 62 35 42 43  0  0  0  0  0]
 [62 25 23 22  0  0  0  0  0  0]
 [69 72 22 21  0  0  0  0  0  0]
 [ 0 72 73  0  0  0  0  0  0  0]
 [ 0  0 74  0  0  0  0  0  0  0]
 [ 0 77 76  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 90  91  99   0   0   0   0   0   0   0]
 [ 89   0  98   0   0   0   0   0   0   0]
 [ 88   0   0   0   0   0   0   0   0   0]
 [186  86   0   0   0   0   0   0   0   0]
 [  0 184  84   0   0   0   0   0   0   0]
 [  0   0  83   0   0   0   0   0   0   0]
 [  0  79  80   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0 131   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
oui
pher_value : 35
up 52
right 42
down 23
left 62
second 52
re2
0
life 130
tour :
79
sim_map :
[[' ' ' ' 's' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[31 26 51 45 41  0  0  0  0  0]
 [32 61 34 41 42  0  0  0  0  0]
 [61 24 22 21  0  0  0  0  0  0]
 [68 71 21 20  0  0  0  0  0  0]
 [ 0 71 72  0  0  0  0  0  0  0]
 [ 0  0 73  0  0  0  0  0  0  0]
 [ 0 76 75  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 89  90  98   0   0   0   0   0   0   0]
 [ 88   0  99   0   0   0   0   0   0   0]
 [ 87   0   0   0   0   0   0   0   0   0]
 [185  85   0   0   0   0   0   0   0   0]
 [  0 183  83   0   0   0   0   0   0   0]
 [  0   0  82   0   0   0   0   0   0   0]
 [  0  78  79   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0 130   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
oui
pher_value : 51
up 0
right 45
down 34
left 26
second 34
re2
2
life 129
tour :
80
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' 's' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[30 25 50 44 40  0  0  0  0  0]
 [31 60 33 40 41  0  0  0  0  0]
 [60 23 21 20  0  0  0  0  0  0]
 [67 70 20 19  0  0  0  0  0  0]
 [ 0 70 71  0  0  0  0  0  0  0]
 [ 0  0 72  0  0  0  0  0  0  0]
 [ 0 75 74  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 88  89  99   0   0   0   0   0   0   0]
 [ 87   0  98   0   0   0   0   0   0   0]
 [ 86   0   0   0   0   0   0   0   0   0]
 [184  84   0   0   0   0   0   0   0   0]
 [  0 182  82   0   0   0   0   0   0   0]
 [  0   0  81   0   0   0   0   0   0   0]
 [  0  77  78   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0 129   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
life 128
tour :
81
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' 's' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[29 24 49 43 39  0  0  0  0  0]
 [30 59 32 39 40  0  0  0  0  0]
 [59 22 20 19  0  0  0  0  0  0]
 [66 69 19 18  0  0  0  0  0  0]
 [ 0 69 70  0  0  0  0  0  0  0]
 [ 0  0 71  0  0  0  0  0  0  0]
 [ 0 74 73  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 87  88  98   0   0   0   0   0   0   0]
 [ 86   0  99   0   0   0   0   0   0   0]
 [ 85   0   0   0   0   0   0   0   0   0]
 [183  83   0   0   0   0   0   0   0   0]
 [  0 181  81   0   0   0   0   0   0   0]
 [  0   0  80   0   0   0   0   0   0   0]
 [  0  76  77   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0 128   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
oui
pher_value : 39
up 43
right 40
down 19
left 32
second 40
re2
1
life 127
tour :
82
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 's' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[28 23 48 42 38  0  0  0  0  0]
 [29 58 31 38 39  0  0  0  0  0]
 [58 21 19 18  0  0  0  0  0  0]
 [65 68 18 17  0  0  0  0  0  0]
 [ 0 68 69  0  0  0  0  0  0  0]
 [ 0  0 70  0  0  0  0  0  0  0]
 [ 0 73 72  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 86  87  97   0   0   0   0   0   0   0]
 [ 85   0  98  99   0   0   0   0   0   0]
 [ 84   0   0   0   0   0   0   0   0   0]
 [182  82   0   0   0   0   0   0   0   0]
 [  0 180  80   0   0   0   0   0   0   0]
 [  0   0  79   0   0   0   0   0   0   0]
 [  0  75  76   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0 127   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
oui
pher_value : 39
up 38
right 0
down 0
left 38
second 38
life 126
tour :
83
sim_map :
[[' ' ' ' ' ' ' ' 's' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[27 22 47 41 37  0  0  0  0  0]
 [28 57 30 37 38  0  0  0  0  0]
 [57 20 18 17  0  0  0  0  0  0]
 [64 67 17 16  0  0  0  0  0  0]
 [ 0 67 68  0  0  0  0  0  0  0]
 [ 0  0 69  0  0  0  0  0  0  0]
 [ 0 72 71  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 85  86  96   0   0   0   0   0   0   0]
 [ 84   0  97  98  99   0   0   0   0   0]
 [ 83   0   0   0   0   0   0   0   0   0]
 [181  81   0   0   0   0   0   0   0   0]
 [  0 179  79   0   0   0   0   0   0   0]
 [  0   0  78   0   0   0   0   0   0   0]
 [  0  74  75   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0 126   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
oui
pher_value : 37
up 0
right 0
down 38
left 41
second 38
re2
2
life 125
tour :
84
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 's' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[26 21 46 40 36  0  0  0  0  0]
 [27 56 29 36 37  0  0  0  0  0]
 [56 19 17 16  0  0  0  0  0  0]
 [63 66 16 15  0  0  0  0  0  0]
 [ 0 66 67  0  0  0  0  0  0  0]
 [ 0  0 68  0  0  0  0  0  0  0]
 [ 0 71 70  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 84  85  95   0  99   0   0   0   0   0]
 [ 83   0  96  97  98   0   0   0   0   0]
 [ 82   0   0   0   0   0   0   0   0   0]
 [180  80   0   0   0   0   0   0   0   0]
 [  0 178  78   0   0   0   0   0   0   0]
 [  0   0  77   0   0   0   0   0   0   0]
 [  0  73  74   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0 125   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
oui
pher_value : 37
up 36
right 0
down 0
left 36
second 36
life 124
tour :
85
sim_map :
[[' ' ' ' ' ' ' ' 's' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[25 20 45 39 35  0  0  0  0  0]
 [26 55 28 35 36  0  0  0  0  0]
 [55 18 16 15  0  0  0  0  0  0]
 [62 65 15 14  0  0  0  0  0  0]
 [ 0 65 66  0  0  0  0  0  0  0]
 [ 0  0 67  0  0  0  0  0  0  0]
 [ 0 70 69  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 83  84  94   0  98   0   0   0   0   0]
 [ 82   0  95  96  99   0   0   0   0   0]
 [ 81   0   0   0   0   0   0   0   0   0]
 [179  79   0   0   0   0   0   0   0   0]
 [  0 177  77   0   0   0   0   0   0   0]
 [  0   0  76   0   0   0   0   0   0   0]
 [  0  72  73   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0 124   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
oui
pher_value : 35
up 0
right 0
down 36
left 39
second 36
re2
2
life 123
tour :
86
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 's' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[24 19 44 38 34  0  0  0  0  0]
 [25 54 27 34 35  0  0  0  0  0]
 [54 17 15 14  0  0  0  0  0  0]
 [61 64 14 13  0  0  0  0  0  0]
 [ 0 64 65  0  0  0  0  0  0  0]
 [ 0  0 66  0  0  0  0  0  0  0]
 [ 0 69 68  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 82  83  93   0  99   0   0   0   0   0]
 [ 81   0  94  95  98   0   0   0   0   0]
 [ 80   0   0   0   0   0   0   0   0   0]
 [178  78   0   0   0   0   0   0   0   0]
 [  0 176  76   0   0   0   0   0   0   0]
 [  0   0  75   0   0   0   0   0   0   0]
 [  0  71  72   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0 123   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
oui
pher_value : 35
up 34
right 0
down 0
left 34
second 34
life 122
tour :
87
sim_map :
[[' ' ' ' ' ' ' ' 's' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[23 18 43 37 33  0  0  0  0  0]
 [24 53 26 33 34  0  0  0  0  0]
 [53 16 14 13  0  0  0  0  0  0]
 [60 63 13 12  0  0  0  0  0  0]
 [ 0 63 64  0  0  0  0  0  0  0]
 [ 0  0 65  0  0  0  0  0  0  0]
 [ 0 68 67  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 81  82  92   0  98   0   0   0   0   0]
 [ 80   0  93  94  99   0   0   0   0   0]
 [ 79   0   0   0   0   0   0   0   0   0]
 [177  77   0   0   0   0   0   0   0   0]
 [  0 175  75   0   0   0   0   0   0   0]
 [  0   0  74   0   0   0   0   0   0   0]
 [  0  70  71   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0 122   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
oui
pher_value : 33
up 0
right 0
down 34
left 37
second 34
re2
2
life 121
tour :
88
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 's' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[22 17 42 36 32  0  0  0  0  0]
 [23 52 25 32 33  0  0  0  0  0]
 [52 15 13 12  0  0  0  0  0  0]
 [59 62 12 11  0  0  0  0  0  0]
 [ 0 62 63  0  0  0  0  0  0  0]
 [ 0  0 64  0  0  0  0  0  0  0]
 [ 0 67 66  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 80  81  91   0  99   0   0   0   0   0]
 [ 79   0  92  93  98   0   0   0   0   0]
 [ 78   0   0   0   0   0   0   0   0   0]
 [176  76   0   0   0   0   0   0   0   0]
 [  0 174  74   0   0   0   0   0   0   0]
 [  0   0  73   0   0   0   0   0   0   0]
 [  0  69  70   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0 121   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
oui
pher_value : 33
up 32
right 0
down 0
left 32
second 32
life 120
tour :
89
sim_map :
[[' ' ' ' ' ' ' ' 's' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[21 16 41 35 31  0  0  0  0  0]
 [22 51 24 31 32  0  0  0  0  0]
 [51 14 12 11  0  0  0  0  0  0]
 [58 61 11 10  0  0  0  0  0  0]
 [ 0 61 62  0  0  0  0  0  0  0]
 [ 0  0 63  0  0  0  0  0  0  0]
 [ 0 66 65  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 79  80  90   0  98   0   0   0   0   0]
 [ 78   0  91  92  99   0   0   0   0   0]
 [ 77   0   0   0   0   0   0   0   0   0]
 [175  75   0   0   0   0   0   0   0   0]
 [  0 173  73   0   0   0   0   0   0   0]
 [  0   0  72   0   0   0   0   0   0   0]
 [  0  68  69   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0 120   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
oui
pher_value : 31
up 0
right 0
down 32
left 35
second 32
re2
2
life 119
tour :
90
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 's' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[20 15 40 34 30  0  0  0  0  0]
 [21 50 23 30 31  0  0  0  0  0]
 [50 13 11 10  0  0  0  0  0  0]
 [57 60 10  9  0  0  0  0  0  0]
 [ 0 60 61  0  0  0  0  0  0  0]
 [ 0  0 62  0  0  0  0  0  0  0]
 [ 0 65 64  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 78  79  89   0  99   0   0   0   0   0]
 [ 77   0  90  91  98   0   0   0   0   0]
 [ 76   0   0   0   0   0   0   0   0   0]
 [174  74   0   0   0   0   0   0   0   0]
 [  0 172  72   0   0   0   0   0   0   0]
 [  0   0  71   0   0   0   0   0   0   0]
 [  0  67  68   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0 119   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
life 118
tour :
91
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 's' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[19 14 39 33 29  0  0  0  0  0]
 [20 49 22 29 30  0  0  0  0  0]
 [49 12 10  9  0  0  0  0  0  0]
 [56 59  9  8  0  0  0  0  0  0]
 [ 0 59 60  0  0  0  0  0  0  0]
 [ 0  0 61  0  0  0  0  0  0  0]
 [ 0 64 63  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 77  78  88   0  98   0   0   0   0   0]
 [ 76   0  89  90  99   0   0   0   0   0]
 [ 75   0   0   0   0   0   0   0   0   0]
 [173  73   0   0   0   0   0   0   0   0]
 [  0 171  71   0   0   0   0   0   0   0]
 [  0   0  70   0   0   0   0   0   0   0]
 [  0  66  67   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0 118   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
oui
pher_value : 0
up 30
right 0
down 0
left 9
second 9
re
3
life 117
tour :
92
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' 's' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[18 13 38 32 28  0  0  0  0  0]
 [19 48 21 28 29  0  0  0  0  0]
 [48 11  9  8  0  0  0  0  0  0]
 [55 58  8  7  0  0  0  0  0  0]
 [ 0 58 59  0  0  0  0  0  0  0]
 [ 0  0 60  0  0  0  0  0  0  0]
 [ 0 63 62  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 76  77  87   0  97   0   0   0   0   0]
 [ 75   0  88  89  98   0   0   0   0   0]
 [ 74   0   0   0  99   0   0   0   0   0]
 [172  72   0   0   0   0   0   0   0   0]
 [  0 170  70   0   0   0   0   0   0   0]
 [  0   0  69   0   0   0   0   0   0   0]
 [  0  65  66   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0 117   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
0
oui
pher_value : 8
up 28
right 0
down 7
left 9
second 9
life 116
tour :
93
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' 'f' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[17 12 37 31 27  0  0  0  0  0]
 [18 47 20 27 28  0  0  0  0  0]
 [47 10  8  7  0  0  0  0  0  0]
 [54 57  7  6  0  0  0  0  0  0]
 [ 0 57 58  0  0  0  0  0  0  0]
 [ 0  0 59  0  0  0  0  0  0  0]
 [ 0 62 61  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 75  76  86   0  96   0   0   0   0   0]
 [ 74   0  87  88  97   0   0   0   0   0]
 [ 73   0   0 198  98   0   0   0   0   0]
 [171  71   0   0   0   0   0   0   0   0]
 [  0 169  69   0   0   0   0   0   0   0]
 [  0   0  68   0   0   0   0   0   0   0]
 [  0  64  65   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0 116   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
1
pher_value : 0
up 198
right 0
down 0
left 0
second 0
po
0
life 115
tour :
94
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' 'f' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[16 11 36 30 26  0  0  0  0  0]
 [17 46 19 26 27  0  0  0  0  0]
 [46  9  7  6  0  0  0  0  0  0]
 [53 56  6  5  0  0  0  0  0  0]
 [ 0 56 57  0  0  0  0  0  0  0]
 [ 0  0 58  0  0  0  0  0  0  0]
 [ 0 61 60  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 74  75  85   0  95   0   0   0   0   0]
 [ 73   0  86  87  96   0   0   0   0   0]
 [ 72   0   0 197  97   0   0   0   0   0]
 [170  70   0   0   0   0   0   0   0   0]
 [  0 168  68   0   0   0   0   0   0   0]
 [  0   0  67   0   0   0   0   0   0   0]
 [  0  63  64   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0 115   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
1
pher_value : 197
up 87
right 97
down 0
left 0
second 87
re2
0
life 114
tour :
95
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' 'f' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[15 10 35 29 25  0  0  0  0  0]
 [16 45 18 25 26  0  0  0  0  0]
 [45  8  6  5  0  0  0  0  0  0]
 [52 55  5  4  0  0  0  0  0  0]
 [ 0 55 56  0  0  0  0  0  0  0]
 [ 0  0 57  0  0  0  0  0  0  0]
 [ 0 60 59  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 73  74  84   0  94   0   0   0   0   0]
 [ 72   0  85  86  95   0   0   0   0   0]
 [ 71   0   0 196  96   0   0   0   0   0]
 [169  69   0   0   0   0   0   0   0   0]
 [  0 167  67   0   0   0   0   0   0   0]
 [  0   0  66   0   0   0   0   0   0   0]
 [  0  62  63   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0 114   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
1
pher_value : 86
up 0
right 95
down 196
left 85
second 95
life 113
tour :
96
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' 'f' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[14  9 34 28 24  0  0  0  0  0]
 [15 44 17 24 25  0  0  0  0  0]
 [44  7  5  4  0  0  0  0  0  0]
 [51 54  4  3  0  0  0  0  0  0]
 [ 0 54 55  0  0  0  0  0  0  0]
 [ 0  0 56  0  0  0  0  0  0  0]
 [ 0 59 58  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 72  73  83   0  93   0   0   0   0   0]
 [ 71   0  84  85  94   0   0   0   0   0]
 [ 70   0   0 195  95   0   0   0   0   0]
 [168  68   0   0   0   0   0   0   0   0]
 [  0 166  66   0   0   0   0   0   0   0]
 [  0   0  65   0   0   0   0   0   0   0]
 [  0  61  62   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0 113   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
1
pher_value : 84
up 83
right 85
down 0
left 0
second 83
life 112
tour :
97
sim_map :
[[' ' ' ' 'f' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[13  8 33 27 23  0  0  0  0  0]
 [14 43 16 23 24  0  0  0  0  0]
 [43  6  4  3  0  0  0  0  0  0]
 [50 53  3  2  0  0  0  0  0  0]
 [ 0 53 54  0  0  0  0  0  0  0]
 [ 0  0 55  0  0  0  0  0  0  0]
 [ 0 58 57  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 71  72  82   0  92   0   0   0   0   0]
 [ 70   0  83  84  93   0   0   0   0   0]
 [ 69   0   0 194  94   0   0   0   0   0]
 [167  67   0   0   0   0   0   0   0   0]
 [  0 165  65   0   0   0   0   0   0   0]
 [  0   0  64   0   0   0   0   0   0   0]
 [  0  60  61   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0 112   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
1
pher_value : 82
up 0
right 0
down 83
left 72
second 72
re2
3
life 111
tour :
98
sim_map :
[[' ' 'f' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[12  7 32 26 22  0  0  0  0  0]
 [13 42 15 22 23  0  0  0  0  0]
 [42  5  3  2  0  0  0  0  0  0]
 [49 52  2  1  0  0  0  0  0  0]
 [ 0 52 53  0  0  0  0  0  0  0]
 [ 0  0 54  0  0  0  0  0  0  0]
 [ 0 57 56  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 70  71  81   0  91   0   0   0   0   0]
 [ 69   0  82  83  92   0   0   0   0   0]
 [ 68   0   0 193  93   0   0   0   0   0]
 [166  66   0   0   0   0   0   0   0   0]
 [  0 164  64   0   0   0   0   0   0   0]
 [  0   0  63   0   0   0   0   0   0   0]
 [  0  59  60   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0 111   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
1
pher_value : 71
up 0
right 81
down 0
left 70
second 70
life 110
tour :
99
sim_map :
[['f' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[11  6 31 25 21  0  0  0  0  0]
 [12 41 14 21 22  0  0  0  0  0]
 [41  4  2  1  0  0  0  0  0  0]
 [48 51  1  0  0  0  0  0  0  0]
 [ 0 51 52  0  0  0  0  0  0  0]
 [ 0  0 53  0  0  0  0  0  0  0]
 [ 0 56 55  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 69  70  80   0  90   0   0   0   0   0]
 [ 68   0  81  82  91   0   0   0   0   0]
 [ 67   0   0 192  92   0   0   0   0   0]
 [165  65   0   0   0   0   0   0   0   0]
 [  0 163  63   0   0   0   0   0   0   0]
 [  0   0  62   0   0   0   0   0   0   0]
 [  0  58  59   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[110   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
1
pher_value : 69
up 0
right 70
down 68
left 0
second 68
life 109
tour :
100
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['f' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[10  5 30 24 20  0  0  0  0  0]
 [11 40 13 20 21  0  0  0  0  0]
 [40  3  1  0  0  0  0  0  0  0]
 [47 50  0  0  0  0  0  0  0  0]
 [ 0 50 51  0  0  0  0  0  0  0]
 [ 0  0 52  0  0  0  0  0  0  0]
 [ 0 55 54  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 68  69  79   0  89   0   0   0   0   0]
 [ 67   0  80  81  90   0   0   0   0   0]
 [ 66   0   0 191  91   0   0   0   0   0]
 [164  64   0   0   0   0   0   0   0   0]
 [  0 162  62   0   0   0   0   0   0   0]
 [  0   0  61   0   0   0   0   0   0   0]
 [  0  57  58   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [109   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
1
life 108
tour :
101
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['f' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[ 9  4 29 23 19  0  0  0  0  0]
 [99 39 12 19 20  0  0  0  0  0]
 [39  2  0  0  0  0  0  0  0  0]
 [46 49  0  0  0  0  0  0  0  0]
 [ 0 49 50  0  0  0  0  0  0  0]
 [ 0  0 51  0  0  0  0  0  0  0]
 [ 0 54 53  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 67  68  78   0  88   0   0   0   0   0]
 [ 66   0  79  80  89   0   0   0   0   0]
 [ 65   0   0 190  90   0   0   0   0   0]
 [163  63   0   0   0   0   0   0   0   0]
 [  0 161  61   0   0   0   0   0   0   0]
 [  0   0  60   0   0   0   0   0   0   0]
 [  0  56  57   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [108   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
1
pher_value : 66
up 67
right 0
down 65
left 0
second 65
life 107
tour :
102
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 ['f' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[ 8  3 28 22 18  0  0  0  0  0]
 [98 38 11 18 19  0  0  0  0  0]
 [38  1  0  0  0  0  0  0  0  0]
 [45 48  0  0  0  0  0  0  0  0]
 [ 0 48 49  0  0  0  0  0  0  0]
 [ 0  0 50  0  0  0  0  0  0  0]
 [ 0 53 52  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 66  67  77   0  87   0   0   0   0   0]
 [ 65   0  78  79  88   0   0   0   0   0]
 [ 64   0   0 189  89   0   0   0   0   0]
 [162  62   0   0   0   0   0   0   0   0]
 [  0 160  60   0   0   0   0   0   0   0]
 [  0   0  59   0   0   0   0   0   0   0]
 [  0  55  56   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [107   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
1
pher_value : 64
up 65
right 0
down 162
left 0
second 65
re2
0
life 106
tour :
103
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['f' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[ 7  2 27 21 17  0  0  0  0  0]
 [97 37 10 17 18  0  0  0  0  0]
 [37  0  0  0  0  0  0  0  0  0]
 [44 47  0  0  0  0  0  0  0  0]
 [ 0 47 48  0  0  0  0  0  0  0]
 [ 0  0 49  0  0  0  0  0  0  0]
 [ 0 52 51  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 65  66  76   0  86   0   0   0   0   0]
 [ 64   0  77  78  87   0   0   0   0   0]
 [ 63   0   0 188  88   0   0   0   0   0]
 [161  61   0   0   0   0   0   0   0   0]
 [  0 159  59   0   0   0   0   0   0   0]
 [  0   0  58   0   0   0   0   0   0   0]
 [  0  54  55   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [106   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
1
pher_value : 64
up 65
right 0
down 63
left 0
second 63
life 105
tour :
104
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 ['f' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[ 6  1 26 20 16  0  0  0  0  0]
 [96 36  9 16 17  0  0  0  0  0]
 [36  0  0  0  0  0  0  0  0  0]
 [43 46  0  0  0  0  0  0  0  0]
 [ 0 46 47  0  0  0  0  0  0  0]
 [ 0  0 48  0  0  0  0  0  0  0]
 [ 0 51 50  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 64  65  75   0  85   0   0   0   0   0]
 [ 63   0  76  77  86   0   0   0   0   0]
 [ 62   0   0 187  87   0   0   0   0   0]
 [160  60   0   0   0   0   0   0   0   0]
 [  0 158  58   0   0   0   0   0   0   0]
 [  0   0  57   0   0   0   0   0   0   0]
 [  0  53  54   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [105   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
1
pher_value : 62
up 63
right 0
down 160
left 0
second 63
re2
0
life 104
tour :
105
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['f' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[ 5  0 25 19 15  0  0  0  0  0]
 [95 35  8 15 16  0  0  0  0  0]
 [35  0  0  0  0  0  0  0  0  0]
 [42 45  0  0  0  0  0  0  0  0]
 [ 0 45 46  0  0  0  0  0  0  0]
 [ 0  0 47  0  0  0  0  0  0  0]
 [ 0 50 49  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 63  64  74   0  84   0   0   0   0   0]
 [ 62   0  75  76  85   0   0   0   0   0]
 [ 61   0   0 186  86   0   0   0   0   0]
 [159  59   0   0   0   0   0   0   0   0]
 [  0 157  57   0   0   0   0   0   0   0]
 [  0   0  56   0   0   0   0   0   0   0]
 [  0  52  53   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [104   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
1
pher_value : 62
up 63
right 0
down 61
left 0
second 61
life 103
tour :
106
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 ['f' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[ 4  0 24 18 14  0  0  0  0  0]
 [94 34  7 14 15  0  0  0  0  0]
 [34  0  0  0  0  0  0  0  0  0]
 [41 44  0  0  0  0  0  0  0  0]
 [ 0 44 45  0  0  0  0  0  0  0]
 [ 0  0 46  0  0  0  0  0  0  0]
 [ 0 49 48  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 62  63  73   0  83   0   0   0   0   0]
 [ 61   0  74  75  84   0   0   0   0   0]
 [ 60   0   0 185  85   0   0   0   0   0]
 [158  58   0   0   0   0   0   0   0   0]
 [  0 156  56   0   0   0   0   0   0   0]
 [  0   0  55   0   0   0   0   0   0   0]
 [  0  51  52   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [103   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
1
pher_value : 60
up 61
right 0
down 158
left 0
second 61
re2
0
life 102
tour :
107
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['f' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[ 3  0 23 17 13  0  0  0  0  0]
 [93 33  6 13 14  0  0  0  0  0]
 [33  0  0  0  0  0  0  0  0  0]
 [40 43  0  0  0  0  0  0  0  0]
 [ 0 43 44  0  0  0  0  0  0  0]
 [ 0  0 45  0  0  0  0  0  0  0]
 [ 0 48 47  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 61  62  72   0  82   0   0   0   0   0]
 [ 60   0  73  74  83   0   0   0   0   0]
 [ 59   0   0 184  84   0   0   0   0   0]
 [157  57   0   0   0   0   0   0   0   0]
 [  0 155  55   0   0   0   0   0   0   0]
 [  0   0  54   0   0   0   0   0   0   0]
 [  0  50  51   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [102   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
1
pher_value : 60
up 61
right 0
down 59
left 0
second 59
life 101
tour :
108
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 ['f' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[ 2  0 22 16 12  0  0  0  0  0]
 [92 32  5 12 13  0  0  0  0  0]
 [32  0  0  0  0  0  0  0  0  0]
 [39 42  0  0  0  0  0  0  0  0]
 [ 0 42 43  0  0  0  0  0  0  0]
 [ 0  0 44  0  0  0  0  0  0  0]
 [ 0 47 46  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 60  61  71   0  81   0   0   0   0   0]
 [ 59   0  72  73  82   0   0   0   0   0]
 [ 58   0   0 183  83   0   0   0   0   0]
 [156  56   0   0   0   0   0   0   0   0]
 [  0 154  54   0   0   0   0   0   0   0]
 [  0   0  53   0   0   0   0   0   0   0]
 [  0  49  50   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [101   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
1
pher_value : 58
up 59
right 0
down 156
left 0
second 59
re2
0
life 100
tour :
109
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['f' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[ 1  0 21 15 11  0  0  0  0  0]
 [91 31  4 11 12  0  0  0  0  0]
 [31  0  0  0  0  0  0  0  0  0]
 [38 41  0  0  0  0  0  0  0  0]
 [ 0 41 42  0  0  0  0  0  0  0]
 [ 0  0 43  0  0  0  0  0  0  0]
 [ 0 46 45  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 59  60  70   0  80   0   0   0   0   0]
 [ 58   0  71  72  81   0   0   0   0   0]
 [ 57   0   0 182  82   0   0   0   0   0]
 [155  55   0   0   0   0   0   0   0   0]
 [  0 153  53   0   0   0   0   0   0   0]
 [  0   0  52   0   0   0   0   0   0   0]
 [  0  48  49   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [100   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
1
pher_value : 58
up 59
right 0
down 57
left 0
second 57
life 99
tour :
110
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 ['f' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[ 0  0 20 14 10  0  0  0  0  0]
 [90 30  3 10 11  0  0  0  0  0]
 [30  0  0  0  0  0  0  0  0  0]
 [37 40  0  0  0  0  0  0  0  0]
 [ 0 40 41  0  0  0  0  0  0  0]
 [ 0  0 42  0  0  0  0  0  0  0]
 [ 0 45 44  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 58  59  69   0  79   0   0   0   0   0]
 [ 57   0  70  71  80   0   0   0   0   0]
 [ 56   0   0 181  81   0   0   0   0   0]
 [154  54   0   0   0   0   0   0   0   0]
 [  0 152  52   0   0   0   0   0   0   0]
 [  0   0  51   0   0   0   0   0   0   0]
 [  0  47  48   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [99  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_count :
1
life 98
tour :
111
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['f' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[ 0  0 19 13  9  0  0  0  0  0]
 [89 29  2  9 10  0  0  0  0  0]
 [99  0  0  0  0  0  0  0  0  0]
 [36 39  0  0  0  0  0  0  0  0]
 [ 0 39 40  0  0  0  0  0  0  0]
 [ 0  0 41  0  0  0  0  0  0  0]
 [ 0 44 43  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 57  58  68   0  78   0   0   0   0   0]
 [ 56   0  69  70  79   0   0   0   0   0]
 [ 55   0   0 180  80   0   0   0   0   0]
 [153  53   0   0   0   0   0   0   0   0]
 [  0 151  51   0   0   0   0   0   0   0]
 [  0   0  50   0   0   0   0   0   0   0]
 [  0  46  47   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [98  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_count :
1
pher_value : 153
up 55
right 53
down 0
left 0
second 53
re2
1
life 97
tour :
112
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' 'f' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[ 0  0 18 12  8  0  0  0  0  0]
 [88 28  1  8  9  0  0  0  0  0]
 [98  0  0  0  0  0  0  0  0  0]
 [35 38  0  0  0  0  0  0  0  0]
 [ 0 38 39  0  0  0  0  0  0  0]
 [ 0  0 40  0  0  0  0  0  0  0]
 [ 0 43 42  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 56  57  67   0  77   0   0   0   0   0]
 [ 55   0  68  69  78   0   0   0   0   0]
 [ 54   0   0 179  79   0   0   0   0   0]
 [152  52   0   0   0   0   0   0   0   0]
 [  0 150  50   0   0   0   0   0   0   0]
 [  0   0  49   0   0   0   0   0   0   0]
 [  0  45  46   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0 97  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_count :
1
pher_value : 52
up 0
right 0
down 150
left 152
second 150
re2
2
life 96
tour :
113
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' 'f' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[ 0  0 17 11  7  0  0  0  0  0]
 [87 27  0  7  8  0  0  0  0  0]
 [97  0  0  0  0  0  0  0  0  0]
 [34 37  0  0  0  0  0  0  0  0]
 [ 0 37 38  0  0  0  0  0  0  0]
 [ 0  0 39  0  0  0  0  0  0  0]
 [ 0 42 41  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 55  56  66   0  76   0   0   0   0   0]
 [ 54   0  67  68  77   0   0   0   0   0]
 [ 53   0   0 178  78   0   0   0   0   0]
 [151  51   0   0   0   0   0   0   0   0]
 [  0 149  49   0   0   0   0   0   0   0]
 [  0   0  48   0   0   0   0   0   0   0]
 [  0  44  45   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0 96  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_count :
1
pher_value : 149
up 51
right 49
down 0
left 0
second 49
re2
1
life 95
tour :
114
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' 'f' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[ 0  0 16 10  6  0  0  0  0  0]
 [86 26  0  6  7  0  0  0  0  0]
 [96  0  0  0  0  0  0  0  0  0]
 [33 36  0  0  0  0  0  0  0  0]
 [ 0 36 37  0  0  0  0  0  0  0]
 [ 0  0 38  0  0  0  0  0  0  0]
 [ 0 41 40  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 54  55  65   0  75   0   0   0   0   0]
 [ 53   0  66  67  76   0   0   0   0   0]
 [ 52   0   0 177  77   0   0   0   0   0]
 [150  50   0   0   0   0   0   0   0   0]
 [  0 148  48   0   0   0   0   0   0   0]
 [  0   0  47   0   0   0   0   0   0   0]
 [  0  43  44   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0 95  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_count :
1
pher_value : 48
up 0
right 0
down 47
left 148
second 47
life 94
tour :
115
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' 'f' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[ 0  0 15  9  5  0  0  0  0  0]
 [85 25  0  5  6  0  0  0  0  0]
 [95  0  0  0  0  0  0  0  0  0]
 [32 35  0  0  0  0  0  0  0  0]
 [ 0 35 36  0  0  0  0  0  0  0]
 [ 0  0 37  0  0  0  0  0  0  0]
 [ 0 40 39  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 53  54  64   0  74   0   0   0   0   0]
 [ 52   0  65  66  75   0   0   0   0   0]
 [ 51   0   0 176  76   0   0   0   0   0]
 [149  49   0   0   0   0   0   0   0   0]
 [  0 147  47   0   0   0   0   0   0   0]
 [  0   0  46   0   0   0   0   0   0   0]
 [  0  42  43   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0 94  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_count :
1
pher_value : 46
up 47
right 0
down 43
left 0
second 43
re2
2
life 93
tour :
116
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' 'f' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[ 0  0 14  8  4  0  0  0  0  0]
 [84 24  0  4  5  0  0  0  0  0]
 [94  0  0  0  0  0  0  0  0  0]
 [31 34  0  0  0  0  0  0  0  0]
 [ 0 34 35  0  0  0  0  0  0  0]
 [ 0  0 36  0  0  0  0  0  0  0]
 [ 0 39 38  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 52  53  63   0  73   0   0   0   0   0]
 [ 51   0  64  65  74   0   0   0   0   0]
 [ 50   0   0 175  75   0   0   0   0   0]
 [148  48   0   0   0   0   0   0   0   0]
 [  0 146  46   0   0   0   0   0   0   0]
 [  0   0  45   0   0   0   0   0   0   0]
 [  0  41  42   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [9 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0 93  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_count :
1
pher_value : 42
up 45
right 0
down 0
left 41
second 41
life 92
tour :
117
sim_map :
[[' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' 'p' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' 'h' 'h' ' ' ' ' ' ' ' ']
 [' ' 's' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 ['n' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']
 [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ']]
sim_pher_home :
[[ 0  0 13  7  3  0  0  0  0  0]
 [83 23  0  3  4  0  0  0  0  0]
 [93  0  0  0  0  0  0  0  0  0]
 [30 33  0  0  0  0  0  0  0  0]
 [ 0 33 34  0  0  0  0  0  0  0]
 [ 0  0 35  0  0  0  0  0  0  0]
 [ 0 38 37  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]
 [ 0  0  0  0  0  0  0  0  0  0]]
sim_pher_food :
[[ 51  52  62   0  72   0   0   0   0   0]
 [ 50   0  63  64  73   0   0   0   0   0]
 [ 49   0   0 174  74   0   0   0   0   0]
 [147  47   0   0   0   0   0   0   0   0]
 [  0 145  45   0   0   0   0   0   0   0]
 [  0   0  44   0   0   0   0   0   0   0]
 [  0  40  41   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_food :
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [8 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
sim_clock :
[[  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0 102   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]
 [  0   0   0   0   0   0   0   0   0   0]]
sim_count :
1
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
