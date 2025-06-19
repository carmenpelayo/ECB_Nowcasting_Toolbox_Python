import pandas as pd
from dateutil import parser


def load_excel(path: str, sheet_name: str = None) -> pd.DataFrame:
    """
    Carga datos desde un archivo Excel.

    Args:
        path: Ruta al archivo .xlsx o .xls.
        sheet_name: Nombre de la hoja a leer. Si es None, lee la primera hoja.

    Returns:
        DataFrame de pandas con los datos cargados.
    """
    df = pd.read_excel(path, sheet_name=sheet_name)
    return df


def load_csv(path: str, **kwargs) -> pd.DataFrame:
    """
    Carga datos desde un archivo CSV.

    Args:
        path: Ruta al archivo .csv.
        **kwargs: Parámetros adicionales para pd.read_csv.

    Returns:
        DataFrame de pandas con los datos cargados.
    """
    df = pd.read_csv(path, **kwargs)
    return df


def preprocess_transformations(df: pd.DataFrame, transformations: dict) -> pd.DataFrame:
    """
    Aplica transformaciones a las columnas del DataFrame.

    transformations: Diccionario donde la clave es el nombre de la columna y el valor es
                     una función o lista de funciones a aplicar.

    Ejemplo:
        transformations = {
            'gdp': lambda x: x.diff(1).pct_change(),
            'cpi': [np.log, lambda x: x.diff(1)]
        }

    Returns:
        DataFrame transformado.
    """
    df_out = df.copy()
    for col, funcs in transformations.items():
        if col not in df_out.columns:
            continue
        series = df_out[col]
        # Normalizar funciones a lista
        func_list = funcs if isinstance(funcs, (list, tuple)) else [funcs]
        for func in func_list:
            series = func(series)
        df_out[col] = series
    return df_out


def parse_date_column(df: pd.DataFrame, date_col: str, fmt: str = None) -> pd.DataFrame:
    """
    Convierte una columna de fechas a datetime.

    Args:
        df: DataFrame original.
        date_col: Nombre de la columna que contiene fechas.
        fmt: Formato de fecha (opcional) para usar con pd.to_datetime.

    Returns:
        DataFrame con la columna date_col convertida.
    """
    df[date_col] = pd.to_datetime(df[date_col], format=fmt)
    return df


def align_vintages(data: pd.DataFrame, date_col: str, vintage_col: str) -> pd.DataFrame:
    """
    Reordena y pivota un DataFrame de datos tipo vintage para análisis.

    Supone un DataFrame con columnas de fecha real y fecha de publicación (vintage).

    Args:
        data: DataFrame con columnas de fecha y vintage.
        date_col: Nombre de la columna de la fecha real (ej. 'date').
        vintage_col: Nombre de la columna de la fecha de publicación (ej. 'vintage').

    Returns:
        DataFrame pivotado con index en date_col y columnas en vintage_col.
    """
    pivoted = data.pivot(index=date_col, columns=vintage_col, values='value')
    pivoted = pivoted.sort_index().sort_index(axis=1)
    return pivoted
