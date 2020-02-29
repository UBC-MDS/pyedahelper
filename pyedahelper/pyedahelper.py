def fast_outlier_id(data, columns, method):
    """
    The function takes in a dataframe and analyzes the values of a given column list, and 
    identifies outliers using either the ZScore algorithm or interquantile range algorithm.
    The return is a dataframe containing the following columns: column name, list 
    containing the outlier's index position, percentage of total counts considered outliers.

    Arguments:
    data (pandas dataframe) - dataframe to be analyzed.
    columns (list) - the columns to be analyzed with the Z-score algorithm.
    method (string) - which method to be used to identify outliers from: 
    {"z-score algorithm", "interquartile range"} 
    
    Returns:
    dataframe: Results summary as a dataframe containing the following columns: 
    column name, list containingthe outlier's index position, percentage of total counts 
    considered outliers.
    """
    pass

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
    plot_type - (str) the type of plot from: {"scatter", "line", "bar"}
    """
    pass


def fast_corr(df, col_name):
    """
    The function takes in a dataframe/tibble and a vector of column names and
    creates correlation matrix.The correlation matrix can only include numeric columns.

    Arguments:
    df - (dataframe) the input data frame
    col_name - (list) the names of the columns selected for correlation analysis
    """
    pass
    
def fast_missing_impute(df, method, cols):
    """
    The function takes in a dataframe, a method of imputation, and a list of column names to modify. 
    The choices of imputation are either remove (removes all rows with missing data), mean, 
    median, mode, or multiple imputation. 
    The function includes error handling to stop plots from being created for inappropriate 
    column types, such as a categorical column being used with the "mean" method. 
    
    Arguments:
    df - (pandas dataframe) the dataframe of interest
    method - (str) the method of imputation from: {remove, mean, median, mode, multiple}
    cols - (lst) the names of columns with missing data to be modified

    Returns: 
    df - the missing data is imputed into the original dataframe  
    """
    pass
