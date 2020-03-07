import pytest
import pandas as pd
from pyedahelper import pyedahelper

test_df_1 = {"col_A": [1,2,1,2,3,3,1,2,4,3,1,2,1,2,3,3,1,2,4,3,1,2,1,2,3,3,1,2,4,3,1,2,1,2,3,3,1,2,4,3], 
     "col_B":["A", "A", "A", "A","A","A","A","A","A","A","B", "B", "B", "B","B","B","B","B","B","B","C", "C", "C", "C","C","C","C","C","C","C","D", "D", "D", "D","D","D","D","D","D","D"],
     "col_C":[8.1, 10.6, 8.9,7.9 ,9.9 ,7.9,10.1,9.5,8.7,8.5,8.1, 10.6, 8.9,7.9 ,9.9 ,7.1,10.1,9.5,8.7,8.5,8.1, 10.6, 8.9,7.9 ,9.9 ,7.1,10.1,9.5,8.7,8.5,8.1, 10.6, 8.9,7.9 ,9.9 ,7.1,10.1,9.5,8.7,8.5]
    }

test_df_2 = {"col_A":[1000,1000,float("nan"),2,3,3,1,2,4,5,1,2,1,2,3,3,1,2,4,5,1,2,1,2,3,3,1,2,4,5,1,2,1,2,3,3,1,2,4,5], 
    "col_B":["T",float("nan"), "Y","Y","A","A","A","A","A","A","B", "B", "B", "B","B","B","B","B","B","B","C", "C", "C", "C","C","C","C","C","C","C","D", "D", "D", "D","D","D","D","D","D","D"],
    "col_C":[1008.1, 1010.6, 1010.7,float("nan") ,9.9 ,12.1,10.1,9.5,8.7,8.5,8.1, 10.6, 8.9,7.9 ,9.9 ,12.1,10.1,9.5,8.7,8.5,8.1, 10.6, 8.9,7.9 ,9.9 ,12.1,10.1,9.5,8.7,8.5,8.1, 10.6, 8.9,7.9 ,9.9 ,12.1,10.1,9.5,8.7,8.5]
}

test_df_1 = pd.DataFrame(test_df_1)
test_df_2 = pd.DataFrame(test_df_2)

answer1 = pyedahelper.fast_outlier_id(test_df_1)
answer2 = pyedahelper.fast_outlier_id(test_df_2)

def test_inputs_fast_outliers_id():
    """
    Function tests inputs for fast_outlier_id function.
    """
    # data input isn't data frame
    with pytest.raises(AssertionError):
        pyedahelper.fast_outlier_id(data = [1,2])
        
    with pytest.raises(AssertionError):
        pyedahelper.fast_outlier_id(test_df_1,method ="x-method")

def test_response_fast_outliers_id():
    
    answer1 = pyedahelper.fast_outlier_id(test_df_1)
    answer2 = pyedahelper.fast_outlier_id(test_df_2)
    
    assert answer1.perc_nans.sum() == 0
    assert answer1.no_outliers.sum() == 0
    assert answer2.perc_nans.sum() == 0.06
    assert answer2.no_outliers.sum() == 6



