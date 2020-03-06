import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def fast_corr(df, col_name):
    """
    The function takes in a dataframe/tibble and a vector of column names and
    creates correlation matrix.The correlation matrix can only include numeric columns.
    Arguments:
    df - (dataframe) the input data frame
    col_name - (list) the names of the columns selected for correlation analysis
    """
       
    if not isinstance(df, pd.DataFrame):
        raise TypeError("The type of the input data must be dataframe.")
    
    if not isinstance(col_name, list):
        raise TypeError("The col_name must be list.")
               
    if all(isinstance(item, str) for item in col_name)==False and all(isinstance(item, int) for item in col_name)==False:
        raise ValueError("The col_name must be a list of strings or a list of integers.")
    
    if len(col_name) < 2:
        raise ValueError("At least two columns must be selected for correlation analysis.")
    
    if all(isinstance(item, str) for item in col_name)==True and all(elem in df.columns.to_list() for elem in col_name)==False:
        raise ValueError("The column names were not found.")
    
    if all(isinstance(item, int) for item in col_name)==True and max(col_name) > (df.shape[1]-1):
        raise ValueError("The column indexes were out of range.")
    
    
    if all(isinstance(item, str) for item in col_name):
        data=df.loc[:,col_name]
    else:
        data=df.iloc[:,col_name]
    
    data2 = data._get_numeric_data()
    rm_n = data.shape[1] - data2.shape[1]
    print("Removed", rm_n, "non-numberical columns from your selected columns")
    
    sns.set(style="white")
    corr = data2.corr()
    mask = np.triu(np.ones_like(corr, dtype=np.bool))
    f, ax = plt.subplots(figsize=(9, 11))
    ax.set_title('Correlation Matrix', size=20)
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=15)
    
    cmap = sns.diverging_palette(220, 20, as_cmap=True)
    p=sns.heatmap(corr, mask=mask, cmap=cmap,vmin=-1, vmax=1,center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
    p.set_yticklabels(p.get_yticklabels(),rotation=360)
    return p
