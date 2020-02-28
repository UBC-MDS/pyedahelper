## pyedahelper 

A Python package that simplifies up the main EDA procedures such as: outlier identification, data visualization, correlation, missing data imputation.

### Authors

| [Ofer Mansour](https://github.com/ofer-m) | [Suvarna Moharir](https://github.com/suvarna-m) | [Subing Cao ](https://github.com/scao1)| [Manuel Maldonado](https://github.com/manu2856)|
|:------------:|:--------------:|:--------------:|:--------------:|

### Project Overview

We are aware that data understanding and cleaning represents 60% of data scientist's time in any given project. 
Our goal with this package is to simplify this process , and make a more efficient use of time while working on some of the main procedures done in EDA (outlier identification, data visualization, correlation, missing data imputation).


### Installation:

```
Work in progress. 
```

### Functions


| Function Name | Input | Output | Description |
|-------------|-----|------|-----------|
|fast_outliers|2 parameters:  A dataframe , a list of columns to be included in analysis| dataframe with included columns and outlier values identified| Given a dataframe, a list of given columns are analyzed in search for outlier values and return a dataframe summarizing the outliers values found and indicating which % of the counts are affected by this outlier(s)|
|fast_plot|4 parameters:  dataframe, name of X column, name of y column, plot name  | Plot object | Given a dataframe ,the columns to be considered X an Y respectively, and the desired plot; the function computes and returns the specified plot|
|fast_corr| 2 parameters: dataframe, list of columns to be analyzed, |correlation plot object| Calculates the correlation of all specified columns and generates a plot visualizing the correlation coefficients.|
|fast_missing_impute|3 parameters: dataframe, a string specifying the missing data treatment method,list of columns to be treated| new dataframe without missing values in the specified columns|Given a dataframe and a list of columns in that dataframe, missing values are identified and treated as specified in the missing data treatment method |


## Alignment with Python / R Ecosystems

At this time, there are multiple packages that are used during EDA with a similar functionality in both R and Python. Nevertheless most of these existing packages require multiple steps or provide results that could be simplified.

In our PYEDAHELPR package, our focus is to minimize the code an user uses to generate significant conclusions in relation to: outliers, missing data treatment, data visualization, correlation computing and visualization.

|EDA Procedure related|Language|Existing Packages/Functions|
|---------|--------|---------------------------|
|Outlier identification| Python|[Box Plot Visualization](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.boxplot.html)
|Outlier identification| Python |[Z-Score ](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.zscore.html)
|Outlier identification| Python |[Interquantile Range](scipy.stats.iqr)
|Missing Value Treatment|Python| [Pandas Droping NaN Values](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html)


### Documentation
The official documentation is hosted on Read the Docs: <https://pyedahelper.readthedocs.io/en/latest/>

### Credits
This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
