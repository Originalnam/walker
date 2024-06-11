import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def visualize_values(values, position = None):
    cmap = mcolors.ListedColormap(['gray', 'black', 'red', 'green'])
    bounds = [-2.5, -1.5, -0.5, 0.5, 1.5]
    norm = mcolors.BoundaryNorm(bounds, cmap.N)

    plt.imshow(values, cmap=cmap, norm=norm)
    if position:
        x, y = position
        plt.text(y, x, 'o', ha='center', va='center', color='black', fontsize=30)

    plt.axis('off')
    plt.show()

