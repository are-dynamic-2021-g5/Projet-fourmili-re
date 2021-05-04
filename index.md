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

En pratique cela donne ça...

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
