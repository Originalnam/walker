import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def visualise_values(values):
    cmap = mcolors.ListedColormap(['black', 'red', 'green'])
    bounds = [-1.5, -0.5, 0.5, 1.5]
    norm = mcolors.BoundaryNorm(bounds, cmap.N)

    plt.imshow(values, cmap=cmap, norm=norm)

    # plt.colorbar(ticks=[0, 1], label='Value')
    # plt.title('Zeroes (Red) and Ones (Green) Visualization')
    plt.axis('off')
    plt.show()