import seaborn as sns
import pandas as pd
from pytest import raises
from pyedahelper import pyedahelper
iris = sns.load_dataset('iris')

def test_input():
    """
    This function tests whether the input for pyedahelper.fast_corr is valid
    """
    data = iris.to_numpy()
    col_name = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
    col_name1 = (1,2,3,4)
    col_name2 = [1,2,3, 'sepal_length']
    col_name3 = [1]
    col_name4 = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'abc']
    col_name5 = [1,2,6]
    
    with raises(TypeError):
            pyedahelper.fast_corr(data, col_name)
    with raises(TypeError):
            pyedahelper.fast_corr(iris, col_name1)
    with raises(ValueError):
            pyedahelper.fast_corr(iris, col_name2)
    with raises(ValueError):
            pyedahelper.fast_corr(iris, col_name3)
    with raises(ValueError):
            pyedahelper.fast_corr(iris, col_name4)
    with raises(ValueError):
            pyedahelper.fast_corr(iris, col_name5)

def test_remove_non_numberic():
    """
    This function tests whether the pyedahelper.fast_corr removes the non-numeric columns
    """
    data=iris
    col_name = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
    p=pyedahelper.fast_corr(data,col_name)
    df=data.loc[:,col_name]
    assert str(p.get_xticklabels())[11:12]==str(df._get_numeric_data().shape[1])
            
            
def test_plot():
    """
    This function tests whether the plot object is correct
    """
    data=iris
    col_name = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
    p=pyedahelper.fast_corr(data, col_name)
    assert str(type(p))=="<class 'matplotlib.axes._subplots.AxesSubplot'>"
    assert p.get_title()=='Correlation Matrix'
    assert str(p.get_yticklabels())== '<a list of 4 Text yticklabel objects>'
    assert str(p.get_xticklabels())== '<a list of 4 Text xticklabel objects>'
    assert 'matplotlib.collections.QuadMes' in str(p.get_children()[0])
    assert 'Spine' in str(p.get_children()[1])

