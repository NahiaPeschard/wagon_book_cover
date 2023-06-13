import pandas as pd
from pathlib import Path

def get_data(cache_path: Path) -> pd.DataFrame:
    """Retrieve data from `cache_path`"""
    df = pd.read_csv(cache_path, delimiter=" ", index_col="Id")
    return df
