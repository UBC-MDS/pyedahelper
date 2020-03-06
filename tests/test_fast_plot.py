import pytest

d = {"col_int": [1, 2, 3, 4, 5, 6], 
     "col_chr":["a", "b", "d", "d", "f","e"],
     "col_flt":[7, 10.6, 13, 4.2, 12, float("nan")],
     "col_nan": [float("nan")] * 6,
     "col_date": ["2018-02-04","2018-02-05","2018-02-06","2018-02-07","2018-02-08","2018-02-09"]
    }

df = pd.DataFrame(d)
df['col_date'] = pd.to_datetime(df['col_date'])
df

def test_inputs():
    """
    Function tests inputs for fast_plot function.
    """
    # data input isn't data frame
    with pytest.raises(AssertionError, match = "Data must be in pandas Data Frame!"):
        fast_plot(df = [1,2], x = "col_date", y = "col_int", plot_type = "line")
    
    # x input isn't string
    with pytest.raises(AssertionError, match = "x column name must be a string!"):
        fast_plot(df = df, x = ["col_date"], y = "col_int", plot_type = "line")
    
    # y input is not a column in data frame
    with pytest.raises(AssertionError, match = "y column name is not a column in data frame entered!"):
        fast_plot(df = df, x = "col_date", y = "slkfjas", plot_type = "line")
    
    # plot type not bar/line/scatter
    with pytest.raises(AssertionError, match = 'plot_type must be either: "scatter", "line",  or "bar"'):
        fast_plot(df = df, x = "col_date", y = "col_int", plot_type = "slfjalskf")
    # x column should not be all null
    with pytest.raises(AssertionError, match = "x Column must not be all Null!"):
        fast_plot(df = df, x = "col_nan", y = "col_int", plot_type = "line")

def test_scatter():
    """
    Function tests scatter plots created by fast_plot function.
    """
    a = fast_plot(df = df, x = "col_int", y = "col_flt", plot_type = "scatter")
    
    assert a.height == 600
    assert a.width == 900
    assert a.mark == "point"
    assert "col_int" in a.encoding['x']['shorthand']  
    assert "col_flt" in a.encoding['y']['shorthand']
    
    # raise error if y is date
    with pytest.raises(Exception):
        fast_plot(df = df, x = "col_int", y = "col_date", plot_type = "scatter")
        
def test_line():
    """
    Function tests line plots created by fast_plot function.
    """
    a = fast_plot(df = df, x = "col_int", y = "col_flt", plot_type = "line")
    
    assert a.height == 600
    assert a.width == 900
    assert a.mark == "line"
    assert "col_int" in a.encoding['x']['shorthand']  
    assert "col_flt" in a.encoding['y']['shorthand']
    
    # raise error if y is date
    with pytest.raises(Exception):
        fast_plot(df = df, x = "col_int", y = "col_date", plot_type = "line")

def test_bar():
    """
    Function tests bar charts created by fast_plot function.
    """
    a = fast_plot(df = df, x = "col_int", y = "col_flt", plot_type = "bar")
    
    assert a.height == 600
    assert a.width == 900
    assert a.mark == "bar"
    assert "col_int" in a.encoding['x']['shorthand']  
    assert "col_flt" in a.encoding['y']['shorthand']
    
    # ensure Exception gets raised when both columns are non-numeric
    with pytest.raises(Exception):
        fast_plot(df = df, x = "col_date", y = "col_date", plot_type = "bar")
    with pytest.raises(Exception):
        fast_plot(df = df, x = "col_chr", y = "col_chr", plot_type = "bar")
    with pytest.raises(Exception):
        fast_plot(df = df, x = "col_date", y = "col_chr", plot_type = "bar")
    with pytest.raises(Exception):
        fast_plot(df = df, x = "col_chr", y = "col_date", plot_type = "bar")
