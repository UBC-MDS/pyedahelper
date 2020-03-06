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
    
    Parameters
    ----------
    df: pandas.core.frame.DataFrame
      The data that will be plotted.
    x: str
      The column name for the x variable.
    y: str
      The column name for the y variable.
    plot_type: str
      The type of plot from: {"scatter", "line", "bar"}.
    
    Returns
    -------
    altair.vegalite.v3.api.Chart
      The plot created.
    
    Examples
    --------
    >>> d = {"col_int": [1, 2, 3, 4, 5, 6], 
     "col_chr":["a", "b", "d", "d", "f","e"],
     "col_flt":[7, 10.6, 13, 4.2, 12, float("nan")],
     "col_nan": [float("nan")] * 6,
     "col_date": ["2018-02-04","2018-02-05","2018-02-06","2018-02-07","2018-02-08","2018-02-09"]
     }

    >>> df = pd.DataFrame(d)
    
    >>> fast_plot(df = df, x = "col_int", y = "col_flt", plot_type = "scatter")
    
    """
    
    # ASSERT TESTS
    
    # check that df is pd.DataFrame
    assert isinstance(df, pd.DataFrame), "Data must be in pandas Data Frame!"
    
    # check that x and y are strings, and are valid columns
    assert isinstance(x, str), "x column name must be a string!"
    assert isinstance(y, str), "y column name must be a string!"
    assert x in df.columns, "x column name is not a column in data frame entered!"
    assert y in df.columns, "y column name is not a column in data frame entered!"
    
    # check that plot_type is one of the three allowed
    assert plot_type.lower() in {"scatter", "line", "bar"}, 'plot_type must be either: "scatter", "line",  or "bar"'
    
    # check that column is not all nulls
    assert df[x].isnull().sum() != len(df[x]), "x Column must not be all Null!"
    assert df[y].isnull().sum() != len(df[y]), "y Column must not be all Null!"
    
    # get types of each column
    x_type = df[x].dtype
    y_type = df[y].dtype
    
    # set x to be ordinal if x column is integer or date
    if x_type == 'int64' or all(df[x].map(type) == pd.Timestamp):
        x_arg = x + ":O"
    else:
        x_arg = x
    
    if plot_type.lower() == "scatter":
        # don't allow y to be date
        if all(df[y].map(type) == pd.Timestamp):
            raise Exception("Y column cannot be a date type!")
        chart = alt.Chart(df).mark_point().encode(
            x=alt.X(x_arg),
            y=alt.Y(y))
    
    elif plot_type.lower() == "line":
        # don't allow y to be date
        if all(df[y].map(type) == pd.Timestamp):
            raise Exception("Y column cannot be a date type!")
            
        if y_type not in ["float64", "int64"]:
            if x_type == y_type:
                x_arg = x
                y_arg = y
        else:
            x_arg = x + ":N"
            y_arg = "sum("+y+")"
        
        chart = alt.Chart(df).mark_line().encode(
            x=alt.X(x_arg),
            y=alt.Y(y_arg))
    
    # bar chart takes sum of y column, unless y column is non-numeric (then takes sum of x column)
    else:
        # check if column is non numeric
        if y_type not in ["float64", "int64"]:
            # raise error if both columns are non numeric
            if x_type == y_type or (x_type == "O" and all(df[y].map(type) == pd.Timestamp)) or (y_type == "O" and all(df[x].map(type) == pd.Timestamp)):
                raise Exception("Bar charts should have a numeric column, and both X and Y are non numeric!")
            
            if all(df[y].map(type) == pd.Timestamp):
                x_arg = "sum("+x+")"
                y_arg = y + ":O"
            else:
                x_arg = "sum("+x+")"
                y_arg = y
        else:
            x_arg = x + ":N"
            y_arg = "sum("+y+")"

        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X(x_arg),
            y=alt.Y(y_arg))
        
    return chart.properties(width = 900, height = 600)


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
