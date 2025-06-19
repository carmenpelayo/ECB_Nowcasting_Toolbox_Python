import pandas as pd
import numpy as np
from nowcasting_toolbox_py.variable_selection.selector import select_by_correlation, select_by_mutual_info, select_by_lasso, rank_variables


def test_select_by_correlation():
    X = pd.DataFrame({
        'a': [1,2,3,4],
        'b': [4,3,2,1]
    })
    y = pd.Series([1,2,3,4])
    idx = select_by_correlation(X, y, k=1)
    # 'a' es perfectamente correlacionada
    assert list(idx) == ['a']


def test_select_by_mutual_info():
    X = pd.DataFrame({
        'a': [1,2,3,4],
        'b': [4,3,2,1]
    })
    y = pd.Series([1,2,3,4])
    idx = select_by_mutual_info(X, y, k=1)
    assert isinstance(idx, pd.Index)
    assert len(idx) == 1


def test_select_by_lasso():
    # X con una variable irrelevante
    X = pd.DataFrame({
        'a': [1,2,3,4],
        'b': [0,0,0,0]
    })
    y = pd.Series([2,4,6,8])
    idx = select_by_lasso(X, y)
    assert 'a' in idx
    assert 'b' not in idx


def test_rank_variables():
    X = pd.DataFrame({
        'a': [1,2,3,4],
        'b': [4,3,2,1],
        'c': [1,1,1,1]
    })
    y = pd.Series([1,2,3,4])
    df_rank = rank_variables(X, y, methods=['corr'], k=2)
    assert set(df_rank['variable']) == {'a', 'b'}
    assert all(df_rank['method'] == 'corr')
