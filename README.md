# Projet-fourmiliere

def map_color(map):
    if type(map) == list:
        A = np.array([map])
    else:
        A = map
    plt.figure(figsize=(15,12)) # (30,30) = Taille de la figure
    plt.imshow(A,cmap='viridis')
    plt.tick_params(top=False, bottom=False, right=False, left=False, labelleft=False, labelbottom=False)
    plt.show()
