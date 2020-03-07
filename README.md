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
pip install -i https://test.pypi.org/simple/ pyedahelper
```

### Functions


| Function Name | Input | Output | Description |
|-----------|------------|---------------|------------------|
|fast_outlier_id|3 parameters:   dataframe , a list of columns to be included in analysis,method to be used to identify outliers ("Z-score algorithm" or "Interquantile Range")| dataframe with included columns and outlier values identified, and % of counts considered as outliers for each anlyzed column| Given a dataframe, a list of given columns are analyzed in search for outlier values and return a dataframe summarizing the outliers values found and indicating which % of the counts are affected by this outlier(s)|
|fast_plot|4 parameters:  dataframe, name of X column, name of y column, plot name  | Plot object | Given a dataframe ,the columns to be considered X an Y respectively, and the desired plot; the function computes and returns the specified plot|
|fast_corr| 2 parameters: dataframe, list of columns to be analyzed, |correlation plot object| Calculates the correlation of all specified columns and generates a plot visualizing the correlation coefficients.|
|fast_missing_impute|3 parameters: dataframe, a string specifying the missing data treatment method,list of columns to be treated| new dataframe without missing values in the specified columns|Given a dataframe and a list of columns in that dataframe, missing values are identified and treated as specified in the missing data treatment method |





## Alignment with Python / R Ecosystems

At this time, there are multiple packages that are used during EDA with a similar functionality in both R and Python. Nevertheless most of these existing packages require multiple steps or provide results that could be simplified.

In our PYEDAHELPR package, our focus is to minimize the code an user uses to generate significant conclusions in relation to: outliers, missing data treatment, data visualization, correlation computing and visualization.

In the following table we have summarized existing packages that are related to the procedures that are simplified in our PYEDAHELPR package.


|EDA Procedure related|Language|Existing Packages/Functions|
|---------|--------|---------------------------|
|Outlier identification| Python|[Box Plot Visualization](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.boxplot.html)
|Outlier identification| Python |[Z-Score ](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.zscore.html)
  |Outlier identification| Python |[Interquantile Range](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.iqr.html)
|Missing Value Treatment|Python| [Pandas Droping NaN Values](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html)
|Missing Value Treatment|Python| [Simple Imputer Values](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer)
|Missing Value Treatment|Python| [Iterative Imputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer)
|Correlation Visualization|Python| [Seaborn Heatmap](https://seaborn.pydata.org/generated/seaborn.heatmap.html)
|Data Visualization|Python| [Altair](https://altair-viz.github.io/)


**How will our package compare to the previous existing packages/functions?**

The pyedahelper package aims to provide an user friendly experience by reducing the code needed to conduct an exploratory data analysis, specifically for identifying outliers, imputing missing data, and generating visualizations for relations and correlations

The fast_plot function leverages the Altair library in Python, however it improves on it by giving the user the ease to change plot type by changing an argument, and including error handling to ensure appropriate column types for certain plots. Also the "seaborn" Python package has similar functions in creating the correlation matrix. However, our function for correlation analysis provides a more user-friendly (less coding) experience and makes it easier to select the columns (features) for the analysis. It will filter out of the categorical columns and only perform the analysis on the numeric columns.
On the other hand the Python packages "sklearn.impute" and "autoimpute" have a similar function to imputing missing data. However, our function is likely more convenient for the user as it involves less coding, requiring the user to simply select the method of imputation and the columns with missing data. Finally, in relation to outlier identification our package will create an integral solution by mixing current existing methods into a single function. It will automatize the usage of Z-score and Interquantile methods to identify outliers.

### Dependencies
- python == 3.7
- pandas == 1.0.1
- altair == 4.0.1
- statistics == 1.0.3
- seaborn == 0.10.0
- matplotlib == 3.2.0
- numpy == 1.18.1
- scipy == 1.4.1

### Documentation
The official documentation is hosted on Read the Docs: <https://pyedahelper.readthedocs.io/en/latest/>

### Credits
This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
