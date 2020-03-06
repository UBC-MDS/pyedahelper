
def fast_outlier_id(data,cols="All",method = "z-score",threshold_low_freq = 0.05):
    """Documentatation for function: fast_outlier_identifier

    Analyzes the values of a given column list in a given dataframe, identifies outliers using either the Z-Score algorithm or interquantile range algorithm.
    The return is a dataframe containing the following columns: column name, list containing the outlier's index position, percentage of total counts considered outliers.

    Arguments:
    data (dataframe) -  Dataframe to be analyzed.
    cols (list) -  List containing the columns to be analyzed with the Z-score algorithm.
    method (string) - string indicating which method to be used to identify outliers (methods available are: "Z-score" or "Interquantile")
    threshold_low_freq (float) - threshold indicating value at which a frequency is considered to be an outlier for categorical values.


    Returns:
    dataframe: Results summary as a dataframe containing the following columns: column name, list containing the outlier's index position, percentaje of total counts considered outliers.
    """
    
    if type(cols) == str:
        if cols.lower() == "all":
            cols = list(data.columns)
        
    # ASSERT TESTS
    assert isinstance(data, pd.DataFrame), "Data must be in pandas Data Frame!"
    
    if type(cols) != str:
        assert isinstance(cols, list), "Columns must be inputted in a list"
        for i in cols:
            assert i in list(data.columns),"Columns must exist in the inputted data dataframe"
        

    assert method.lower() in ["z-score","interquantile"], "The only permitted values are z-score or interquantile,thank you"
    
    ##Initialize lists containing summary values
    no_nans_list = list()
    col_type_list = list()
    perc_nans_list = list()
    outlier_values_list = list()
    outlier_count_list = list()
    outlier_perc_list = list()
    method_list = list()
    
    ##Subsetting the data by the columns selected by the user
    subset = data[cols]
    for i in cols:
        ##More lists containing summary values
        no_nans = subset[i].isna().sum()
        no_nans_list.append(no_nans)
        col_type_list.append(subset[i[0]].dtype)
        perc_nans_list.append(round(no_nans/len(subset[i[0]]),2))
        data_no_nans = subset[i][~pd.isna(subset[i])]
        if data_no_nans.dtypes in ['float64']:
            if method.lower() == "z-score":
                score = np.abs(stats.zscore(data_no_nans))
                data_no_nans = data_no_nans.to_numpy()
                outlier_values = data_no_nans[np.where(score>2)]
                outlier_count_list.append(len(outlier_values))
                outlier_perc_list.append(round(len(outlier_values)/len(data_no_nans),2))
                outlier_values_list.append(outlier_values)
                method_list.append("Z-Score")
            elif method.lower() == "interquartile":
                Q1 = np.quantile(data_no_nans,0.25)
                Q3 = np.quantile(data_no_nans,0.75)
                IQR = Q3 - Q1
                score = (data_no_nans < (Q1 - 1.5 * IQR)) | (data_no_nans > (Q3 + 1.5 * IQR))
                outlier_values = data_no_nans[np.where(score>0)]
                outlier_count_list.append(len(outlier_value))
                outlier_perc_list.append(round(len(outlier_value)/len(data_no_nans),2))
                outlier_values_list.append(outlier_values)
                method_list.append("Interquartile")
        elif data_no_nans.dtype in ['object']:
            score = data_no_nans.value_counts()/len(data_no_nans)
            outlier_values = score[score< 0.05].index.tolist()
            outlier_count_list.append(data_no_nans.value_counts()[score< 0.05].sum())
            outlier_perc_list.append(round(sum(score[score< 0.05]),2))
            outlier_values_list.append(outlier_values)
            method_list.append("low-freq")
    summary_dict = {'column_name':cols,'type':col_type_list,'no_nans':no_nans_list,'perc_nans':perc_nans_list,'outlier_method':method_list,"no_outliers":outlier_count_list,"perc_outliers":outlier_perc_list,"outlier_values":outlier_values_list}
    summary = pd.DataFrame(summary_dict)
    return(summary)

    

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