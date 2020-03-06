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
    median, or mode imputation.
    The function includes error handling to stop plots from being created for inappropriate 
    column types, such as a categorical column being used with the "mean" method. 
    
    Arguments
    -----------------------
    df: pandas dataframe
        The dataframe of interest
    method: str
        The method of imputation from: {remove, mean, median, mode}
    cols: lst 
        The names of columns with missing data to be modified
    
    Returns
    ------------------------
    new_df
        A new dataframe with the missing values imputed
        
    Examples
    ------------------------
    >>> sample = {"col_a": [50, 50, 6, 8, float("nan")],
                  "col_b": ["the", "quick", float("nan"), "quick", "fox"],
                  "col_c": [67.56, float("nan"), 80, 34.39, 76]
                }
    >>> sample_data = pd.DataFrame(sample)
    
    >>> fast_missing_impute(df = sample_data, method = "mean", cols = ["col_a", "col_c"])
    
    >>> fast_missing_impute(df = sample_data, method = "mode", cols = ["col_a", "col_b"])
    
    """
    assert isinstance(df, pd.DataFrame), "Data must be a data frame!"
    
    assert isinstance(method, str), "Method must be a string!" #Will also check for only one method
    
    assert type(cols) == list, "Cols must be a list!"
    
    assert method in ["remove", "mean", "median", "mode"], "Not a valid method!"
    
    for col in cols:
        assert isinstance(col, str), "Columns must be a list of strings"
        assert col in df.columns, "One or more of the column names are not in the data frame!"
        if df[col].dtype != 'int64' and df[col].dtype != 'float64':
            assert method in ["remove", "mode"], "With non-numeric columns, can only use method = 'remove' or 'mode'"
    new_df = df.copy()
    if method == "remove":
        new_df = new_df.dropna(subset = cols)
    
    elif method == "mean":
        for col in cols:
            new_df[col] = new_df[col].fillna(new_df[col].mean(), inplace = False)
    
    elif method == "median":
        for col in cols:
            new_df[col] = new_df[col].fillna(new_df[col].median(), inplace = False)
    
    elif method == "mode":
        for col in cols:
            new_df[col] = new_df[col].fillna(mode(new_df[col]), inplace = False)
            
    return new_df
