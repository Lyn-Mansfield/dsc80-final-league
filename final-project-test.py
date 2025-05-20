import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

df = pd.DataFrame({
	'A': np.random.uniform(0, 10, 100), 
	'B': np.random.uniform(0, 10, 100), 
	'C': np.random.uniform(0, 10, 100)
	})


pdf_pages = PdfPages('multipage_plots.pdf')

for column in df.columns:
    fig, ax = plt.subplots()
    ax.hist(df[column])
    ax.set_title(f'Graph of {column}')
    pdf_pages.savefig(fig)
    plt.close(fig)

pdf_pages.close()