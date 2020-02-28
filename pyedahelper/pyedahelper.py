# author: Manuel Maldonado
# date: 2020-02-28

def fast_outlier_id(data, columns, method):
    """Documentatation for function: fast_outlier_identifier

    Analyzes the values of a given column list in a given dataframe, identifies outliers using either the Z-Score algorithm or interquantile range algorithm.
    The return is a dataframe containing the following columns: column name, list containing the outlier's index position, percentage of total counts considered outliers.

    Args:
        data (dataframe): Dataframe to be analyzed.
        columns (list): List containing the columns to be analyzed with the Z-score algorithm.
        method (string) : string indicating which method to be used to identify outliers (methods available are: "Z-score algorithm" or "Interquantile Range")


    Returns:
        dataframe: Results summary as a dataframe containing the following columns: column name, list containing the outlier's index position, percentaje of total counts considered outliers.
    """
    pass