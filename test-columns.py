import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# graph all of the 
def graph_univariate(df, column):
	columns = df.columns

	for column in columns:
		target_data = df

def bivariate_plot(df, categorical_column, target_column, title):
    pdf_pages = PdfPage(f'bivariate_plots_{title}.pdf')

    plt.figure()
    
    for column in df.columns:
        fig, ax = plt.subplots()
        ax.hist(df[column])
        ax.set_title(f'Graph of {column}')
        pdf_pages.savefig(fig)
        plt.close(fig)
    
    pdf_pages.close()

