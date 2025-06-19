import pandas as pd
import numpy as np
import os
import pytest
from nowcasting_toolbox_py.data.loader import load_csv, load_excel, preprocess_transformations, parse_date_column, align_vintages


def test_load_csv(tmp_path):
    # Crear un DataFrame de ejemplo y escribir a CSV
    df = pd.DataFrame({
        'a': [1, 2, 3],
        'b': [4, 5, 6]
    })
    file = tmp_path / "test.csv"
    df.to_csv(file, index=False)
    # Cargar con la función
    loaded = load_csv(str(file))
    pd.testing.assert_frame_equal(df, loaded)


def test_parse_date_column():
    df = pd.DataFrame({'date': ['2020-01-01', '2020-02-01', '2020-03-01'], 'value': [1, 2, 3]})
    out = parse_date_column(df.copy(), 'date')
    assert pd.api.types.is_datetime64_any_dtype(out['date'])
    assert list(out['date']) == [pd.Timestamp('2020-01-01'), pd.Timestamp('2020-02-01'), pd.Timestamp('2020-03-01')]


def test_preprocess_transformations():
    df = pd.DataFrame({'x': [1, 4, 9]})
    # Aplicar transformación sqrt
    tf = {'x': np.sqrt}
    out = preprocess_transformations(df, tf)
    expected = pd.Series([1.0, 2.0, 3.0], name='x')
    pd.testing.assert_series_equal(out['x'], expected)


def test_align_vintages():
    data = pd.DataFrame({
        'date': ['2021-01-01', '2021-01-01', '2021-04-01'],
        'vintage': ['2021-01-15', '2021-04-15', '2021-04-15'],
        'value': [100, 110, 120]
    })
    data['date'] = pd.to_datetime(data['date'])
    data['vintage'] = pd.to_datetime(data['vintage'])
    pivoted = align_vintages(data, 'date', 'vintage')
    # Verificar índices y columnas
    assert list(pivoted.index) == [pd.Timestamp('2021-01-01'), pd.Timestamp('2021-04-01')]
    assert pd.Timestamp('2021-01-15') in pivoted.columns
    assert pd.Timestamp('2021-04-15') in pivoted.columns
