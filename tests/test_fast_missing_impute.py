import pytest
import pandas as pd
from pyedahelper import pyedahelper
from statistics import mode

# helper data
my_data = {"a": [3, 2, 3, 4, 5, float('nan')],
           "b": ["a", float("nan"), "d", "d", "f", "e"],
           "c": [7, 10, float('nan'), 13, 4, 12],
           "d": [7, 10.6, 13, 4.2, float('nan'), 11.5],
           "e": ["hello", float("nan"), "be", "hello", "who", "she"],
           "f": [float("nan")] * 6
           }
test_data = pd.DataFrame(my_data)
test_list = [23, 24, 67, 910]


def test_df_assert():
    """
    Tests if the function correctly throws an error if df is not a dataframe
    """
    with pytest.raises(AssertionError, match="Data must be a data frame!"):
        pyedahelper.fast_missing_impute(df=test_list, method="mean", cols="a")


def test_method_str():
    """
    Tests if the function correctly throws an error if the method is not a
    string when one method is inputted
    """
    with pytest.raises(AssertionError, match="Method must be a string!"):
        pyedahelper.fast_missing_impute(df=test_data, method=["mean"],
                                        cols="a")


def test_one_method():
    """
    Tests if the function correctly throws an error if the method is not a
    string when more than one method is inputted
    """
    with pytest.raises(AssertionError, match="Method must be a string!"):
        pyedahelper.fast_missing_impute(df=test_data,
                                        method=["mean", "median"], cols="a")


def test_cols_int():
    """
    Tests if the function correctly throws an error if cols is an integer
    """
    with pytest.raises(AssertionError, match="Cols must be a list!"):
        pyedahelper.fast_missing_impute(df=test_data, method="mean", cols=7)


def test_cols_set():
    """
    Tests if the function correctly throws an error if cols is a set
    """
    with pytest.raises(AssertionError, match="Cols must be a list!"):
        pyedahelper.fast_missing_impute(df=test_data, method="mean",
                                        cols={'R', 'Python'})


def test_method_format():
    """
    Tests if the function correctly throws an error if method is not a valid
    method
    """
    with pytest.raises(AssertionError, match="Not a valid method!"):
        pyedahelper.fast_missing_impute(df=test_data, method="avg",
                                        cols=["a", "b"])


def test_mode_fail():
    """
    Tests if the function correctly throws an error if method is mode
    and one or more of the columns don't have a mode
    """
    with pytest.raises(Exception):
        pyedahelper.fast_missing_impute(df=test_data, method="mode",
                                        cols=["c"])


def test_cols_allstr():
    """
    Tests if the function correctly throws an error if cols is a list that
    contains a non-string element
    """
    with pytest.raises(AssertionError,
                       match="Columns must be a list of strings"):
        pyedahelper.fast_missing_impute(df=test_data, method="median",
                                        cols=["a", 3, "c"])


def test_cols_in_df():
    """
    Tests if the function correctly throws an error if an element in cols
    is not part of the data frame
    """
    with pytest.raises(AssertionError,
                       match="One or more of the column names"
                             " are not in the data frame!"):
        pyedahelper.fast_missing_impute(df=test_data, method="mean",
                                        cols=["a", "c", "fake_col"])


def test_non_numeric():
    """
    Tests if the function correctly throws an error if an column in cols is
    non-numeric and the method selected is not 'remove' or 'mode'
    """
    with pytest.raises(AssertionError,
                       match="With non-numeric columns, can only use "
                             "method = 'remove' or 'mode'"):
        pyedahelper.fast_missing_impute(df=test_data, method="mean",
                                        cols=["e"])


def test_remove_method():
    """
    Tests if the function, when method = 'remove', leaves the selected
    column(s) with no NAs and leaves the other columns the same
    """
    sample_drop = pyedahelper.fast_missing_impute(df=test_data,
                                                  method="remove",
                                                  cols=["a", "e"])
    assert sample_drop["a"].isna().sum() == 0
    assert sample_drop["e"].isna().sum() == 0
    assert sample_drop["f"].isna().sum() == 4
    assert sample_drop.shape[0] < test_data.shape[
        0]  # should have fewer rows because NAs are removed
    assert sample_drop.shape[1] == test_data.shape[
        1]  # number of columns should not change


def test_mean():
    """
    Tests if the function, when method = 'mean', leaves the selected columns
    with NAs imputed with the mean of the column, with no NAs left in the
    column, and leaves the other columns the same
    """
    sample_mean = pyedahelper.fast_missing_impute(df=test_data, method="mean",
                                                  cols=["a", "c"])
    assert sample_mean["a"].isna().sum() == 0
    assert sample_mean["c"].isna().sum() == 0
    assert sample_mean["b"].isna().sum() == test_data[
        "b"].isna().sum()  # should remain unchanged
    assert sample_mean["a"][5] == test_data["a"].mean()
    assert sample_mean["c"][2] == test_data["c"].mean()
    assert sample_mean.shape == test_data.shape  # dimensions should not change


def test_median():
    """
    Tests if the function, when method = 'median', leaves the selected columns
    with NAs imputed with the median of the column, with no NAs left in the
    column, and leaves the other columns the same
    """
    sample_median = pyedahelper.fast_missing_impute(df=test_data,
                                                    method="median",
                                                    cols=["a", "d"])
    assert sample_median["a"].isna().sum() == 0
    assert sample_median["d"].isna().sum() == 0
    assert sample_median["b"].isna().sum() == test_data[
        "b"].isna().sum()  # should remain unchanged
    assert sample_median["a"][5] == test_data["a"].median()
    assert sample_median["d"][4] == test_data["d"].median()
    # dimensions shouldn't change
    assert sample_median.shape == test_data.shape


def test_mode():
    """
    Tests if the function, when method = 'mode', leaves the selected columns
    with NAs imputed with the mode of the column, with no NAs left in the
    column, and leaves the other columns the same
    """
    sample_mode = pyedahelper.fast_missing_impute(df=test_data, method="mode",
                                                  cols=["a", "e"])
    assert sample_mode["a"].isna().sum() == 0
    assert sample_mode["e"].isna().sum() == 0
    assert sample_mode["d"].isna().sum() == test_data[
        "d"].isna().sum()  # should remain unchanged
    assert sample_mode["a"][5] == mode(test_data["a"])
    assert sample_mode["e"][1] == mode(test_data["e"])
    assert sample_mode.shape == test_data.shape  # dimensions shouldn't change
