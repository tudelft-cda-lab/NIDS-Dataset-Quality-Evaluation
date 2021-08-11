#Experiment helper functions that are commonly used through most or all notebooks

def abbrv_num(num):
    """Shorten string representation of large numbers by single-letter notation and rounding to 2 decimals
    
    Arguments:
        num (int): (Large) number to be formatted
        
    Return:
        Abbreviated and rounded number with single-letter notation
    """
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    # add more suffixes if you need them
    if magnitude == 0:
        return '%s' % (num)
    else:
        return '%.2f%s' % (num, ['', 'K', 'M', 'B', 'T', 'Q'][magnitude])
    
def objectToFile(obj, path: str):
    """ Small helper function pickle Python objects, primary use to store results and data
    
    Arguments:
        obj (object): Object to be pickled
        path (str): Full path of file to be pickled to.
    """
    with open(path, 'wb') as fp:
        pickle.dump(obj, fp)
        
def objectFromFile(path: str):
    """ Small helper function read pickled Python objects and return as value
    
    Arguments:
        path (str): Full path of file to be read from.
        
    Return:
        object from pickled file.
    """
    with open(path, 'rb') as fp:
        return pickle.load(fp)
    
def add_value_labels(ax, spacing=5):
    """Add labels to the end of each bar in a bar chart.

    Arguments:
        ax (matplotlib.axes.Axes): The matplotlib object containing the axes
            of the plot to annotate.
        spacing (int): The distance between the labels and the bars.
    """

    # For each bar: Place a label
    for rect in ax.patches:
        # Get X and Y placement of label from rect.
        y_value = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2

        # Number of points between bar and label. Change to your liking.
        space = spacing
        # Vertical alignment for positive values
        va = 'bottom'

        # If value of bar is negative: Place label below bar
        if y_value < 0:
            # Invert space to place label below
            space *= -1
            # Vertically align label at top
            va = 'top'

        # Use Y value as label and format number with one decimal place
        label = "{:.3f}".format(y_value)

        # Create annotation
        ax.annotate(
            label,                      # Use `label` as label
            (x_value, y_value),         # Place label at end of the bar
            xytext=(0, space),          # Vertically shift label by `space`
            textcoords="offset points", # Interpret `xytext` as offset in points
            ha='center',                # Horizontally center label
            va=va)                      # Vertically align label differently for
                                        # positive and negative values.