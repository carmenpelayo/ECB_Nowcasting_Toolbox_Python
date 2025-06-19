import pandas as pd


def align_time_index(df: pd.DataFrame, freq: str = 'Q') -> pd.DataFrame:
    """
    Asegura que el DataFrame tenga un índice de tiempo regular.

    Args:
        df: DataFrame con índice de fechas.
        freq: frecuencia deseada (p.ej. 'Q' para trimestral, 'M' mensual).

    Returns:
        DataFrame reindexado con missing filled as NaN.
    """
    idx = pd.date_range(start=df.index.min(), end=df.index.max(), freq=freq)
    return df.reindex(idx)


def vintage_dates(reference_date, periods: int = 4, freq: str = 'Q') -> pd.DatetimeIndex:
    """
    Genera fechas de vintage anteriores al reference_date.

    Args:
        reference_date: fecha límite (datetime o str).
        periods: número de vintages previos a generar.
        freq: frecuencia de las series.

    Returns:
        Índice de fechas de vintage.
    """
    ref = pd.to_datetime(reference_date)
    return pd.date_range(end=ref, periods=periods, freq=freq)
