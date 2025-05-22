import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from matplotlib.backends.backend_pdf import PdfPages
from pathlib import Path

dataset_path = Path("./data/2025_LoL_clean_stats.csv")
# /data/2025_LoL_clean_stats.csv
data = pd.read_csv(dataset_path)


num_missing = data.apply(pd.isna).sum()
num_missing = num_missing / data.shape[0] * 100

fig = px.bar(num_missing[num_missing != 0].sort_values(), 
	labels={'index': 'Column name', 'value': '% missing'}
	)
fig.update_layout(
    title={
        'text': 'Data missing from partial rows',
        'font': {'size': 24}
    }
)
fig.show()