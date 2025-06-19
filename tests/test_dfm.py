import pytest
from nowcasting_toolbox_py.models.dfm import DynamicFactorModel
import pandas as pd

def test_nowcast_before_fit_raises():
    # Crear DF de prueba
    df = pd.DataFrame({'x1': [1,2,3], 'x2': [4,5,6]})
    model = DynamicFactorModel(endog=df, k_factors=1)
    with pytest.raises(ValueError):
        model.nowcast()
    with pytest.raises(ValueError):
        model.summarize()
