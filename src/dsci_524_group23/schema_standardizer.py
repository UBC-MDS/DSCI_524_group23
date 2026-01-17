import pandas as pd

def standardize_schema(data):
    
    # Defensive check: Input type
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")

    # Create a copy to avoid mutating original data
    df = data.copy()

    # If empty, return immediately
    if df.empty:
        return df

    return df