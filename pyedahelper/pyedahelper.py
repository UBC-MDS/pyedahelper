def fast_plot(df, x, y, plot_type):
    """
    The function takes in a dataframe, two column names for x and y axis and a plot type and 
    creates the plot using the Altair library.
    The plot types are restricted to either line plot, scatter plot or bar chart.
    The function includes error handling to stop plots from being created for inappropriate 
    column types, such as a scatter plot will not be appropriate if both columns have categorical types.
    
    Arguments:
    df - (pandas dataframe) the data that will be plotted
    x - (str) the column name for the x variable
    y - (str) the column name for the y variable
    plot_type - (str) the type of plot from: {scatter, line, bar}
    """
    
    
    pass