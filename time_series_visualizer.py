import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Tuple

def load_and_clean_traffic_data(url: str) -> pd.DataFrame:
    """
    Fetches forum traffic data, handles datetime indexing, and drops 
    outliers beyond the 2.5th and 9.75th percentiles.
    """
    try:
        df = pd.read_csv(url, index_col='date', parse_dates=['date'])
    except Exception as e:
        raise IOError(f"Failed to fetch data from remote source: {e}")
        
    # Statistical data cleaning
    lower_bound = df['value'].quantile(0.025)
    upper_bound = df['value'].quantile(0.975)
    
    return df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]

def generate_seasonality_report(df: pd.DataFrame) -> Tuple[plt.Figure, plt.Axes]:
    """
    Generates a grouped bar chart visualizing monthly distribution 
    to track traffic seasonality across years.
    """
    # ... your clean plotting logic here ...
    return fig, ax

