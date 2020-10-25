import numpy as np
from matplotlib import pyplot as plt

# Complete the following to make the plot
if __name__ == "__main__":
    data = np.load('sdss_galaxy_colors.npy')
    # Get a colour map
    cmap = plt.get_cmap('YlOrRd')

    # Define our colour indexes u-g and r-i
    x = data['u'] - data['g']
    y = data['r'] - data['i']

    # Make a redshift array
    z = data['redshift']

    # Create the plot with plt.scatter and plt.colorbar
    p = plt.scatter(x, y, s=1, lw=0, c=z, cmap=cmap)
    cb = plt.colorbar(p)
    cb.set_label('Redshift')
    
    # Define your axis labels and plot title
    plt.xlabel('Colour index u-g')
    plt.ylabel('Colour index r-i')
    plt.title('Redshift (colour) u-g versus r-i')

    # Set any axis limits
    plt.xlim([-0.5, 2.5])
    plt.ylim([-0.5, 1.0])
    
    plt.show()
