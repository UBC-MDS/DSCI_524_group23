import pytest
import pandas as pd
from dsci_524_group23.schema_standardizer import standardize_schema

def test_standardize_schema_invalid_input_type():
    with pytest.raises(TypeError, match="Input must be a pandas DataFrame"):
        standardize_schema([1, 2, 3])

def test_standardize_schema_empty_df():
    df_empty = pd.DataFrame()
    out = standardize_schema(df_empty)
    expected_out = pd.DataFrame()
    
    pd.testing.assert_frame_equal(out, expected_out)
