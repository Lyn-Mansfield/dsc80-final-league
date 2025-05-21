import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from matplotlib.backends.backend_pdf import PdfPages
from pathlib import Path

dataset_path = Path("./data/2025_LoL_esports_match_data_from_OraclesElixir.csv")
# /data/2025_LoL_esports_match_data_from_OraclesElixir.csv
data_csv = open(dataset_path).read()
rows = data_csv.split('\n')
columnss = rows[0].split(',')
rowss = [x.split(',') for x in rows[1:]]
data = pd.DataFrame(columns = columnss, data = rowss)


complete_samples = data.query("datacompleteness == 'complete'")
partial_samples = data.query("datacompleteness == 'partial'")

team_rows = partial_samples.query("playername == ''")
team_rows['firstblood'] = team_rows['firstblood'].astype(str)
team_rows['result'] = team_rows['result'].astype(str)


#w_first_blood = team_rows.query("firstblood == '1'")
#wo_first_blood = team_rows.query("firstblood == '0'")


#fig = px.histogram(w_first_blood, x='result')
#fig.show()

print(float('11'))