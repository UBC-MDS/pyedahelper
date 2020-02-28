
def fast_outlier_id(data, columns, method):
    """Documentatation for function: fast_outlier_identifier

    Analyzes the values of a given column list in a given dataframe, identifies outliers using either the Z-Score algorithm or interquantile range algorithm.
    The return is a dataframe containing the following columns: column name, list containing the outlier's index position, percentage of total counts considered outliers.

    Arguments:
    data (dataframe): Dataframe to be analyzed.
    columns (list): List containing the columns to be analyzed with the Z-score algorithm.
    method (string) : string indicating which method to be used to identify outliers (methods available are: "Z-score algorithm" or "Interquantile Range")


    Returns:
    dataframe: Results summary as a dataframe containing the following columns: column name, list containing the outlier's index position, percentaje of total counts considered outliers.
    """

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