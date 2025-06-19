import pandas as pd
import logging

# Configuración básica de logging
def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Configura y retorna un logger.

    Args:
        name: nombre del logger.
        level: nivel de log (default INFO).

    Returns:
        Logger configurado.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(level)
    return logger


def save_dataframe(df: pd.DataFrame, path: str, format: str = 'csv') -> None:
    """
    Guarda un DataFrame en disco en formato CSV o Excel.

    Args:
        df: DataFrame a guardar.
        path: ruta de salida sin extensión.
        format: 'csv' o 'excel'.
    """
    if format == 'csv':
        df.to_csv(f"{path}.csv", index=True)
    elif format == 'excel':
        df.to_excel(f"{path}.xlsx", index=True)
    else:
        raise ValueError(f"Formato no soportado: {format}")


def load_vintage_series(path: str) -> pd.DataFrame:
    """
    Lee un CSV/Excel con columnas ['date','vintage','value'] y pivota.

    Retorna un DataFrame pivotado con fechas reales como índice
    y columnas de vintages.
    """
    df = pd.read_csv(path) if path.endswith('.csv') else pd.read_excel(path)
    df['date'] = pd.to_datetime(df['date'])
    df['vintage'] = pd.to_datetime(df['vintage'])
    return df.pivot(index='date', columns='vintage', values='value').sort_index()
