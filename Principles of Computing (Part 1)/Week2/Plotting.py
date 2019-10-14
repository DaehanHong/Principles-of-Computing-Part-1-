"""
Example of creating a plot using simpleplot
    
Input is a list of point lists (one per function)
Each point list is a list of points of the form 
[(x0, y0), (x1, y1, ..., (xn, yn)]
"""

import simpleplot


# create three sample functions

def double(num):
    """
    Example of linear function
    """
    return 2 * num

def square(num):
    """
    Example of quadratic function
    """
    return num ** 2

def exp(num):
    """
    Example of exponential function
    """
    return 2 ** num


def create_plots(begin, end, stride):
    """ 
    Plot the function double, square, and exp
    from beginning to end using the provided stride
    
    The x-coordinates of the plotted points start
    at begin, terminate at end and are spaced by 
    distance stride
    """
    
    # generate x coordinates for plot points
    x_coords = []
    current_x = begin
    while current_x < end:
        x_coords.append(current_x)
        current_x += stride
        
    # compute list of (x, y) coordinates for each function
    double_plot = [(x_val, double(x_val)) for x_val in x_coords]
    square_plot = [(x_val, square(x_val)) for x_val in x_coords]
    exp_plot = [(x_val, exp(x_val)) for x_val in x_coords]
    
    # plot the list of points
    simpleplot.plot_lines("Plots of three functions", 600, 400, "x", "f(x)",
                         [double_plot, square_plot, exp_plot], 
                         True, ["double", "square", "exp"])
    
create_plots(0, 2, .1)
                          
                   
    
    
    
    
    