import pandas as pd
import matplotlib.pyplot as plt
from ydata_profiling import ProfileReport
import numpy as np
import statistics as stat
from fpdf import FPDF
#import markdown2

class Df_Stats:
    """ Returns principal stats and summary statistics and prints a report """
    def __init__(self, url):
        self.df = pd.read_csv(url)        
    
    def var_mean(self, variable):
        return np.mean(self.df[variable])

    def var_median(self, variable):
        return stat.median(self.df[variable])

    def var_std(self, variable):
        return np.std(self.df[variable])

    def stats_summary(self, variables=None):
        return self.df.describe() if not variables else self.df[variables].describe()

    def plot_hist_var(self, var, filename="plot_var.png"):
        plt.hist(self.df[var], bins=30, color='skyblue', edgecolor='black')  # Create histogram
        plt.title(f'Distribution of {var}')
        plt.xlabel(var)
        plt.ylabel('Frequency')
        plt.tight_layout()  
        plt.savefig(filename)
        plt.close()

    def plot_scatter_two_vars(self, x, y, filename="plot_two_vars.png"):
        plt.scatter(self.df[x], self.df[y], color='green')
        plt.title(f'Scatter Plot of {x} vs {y}')
        plt.xlabel(x)
        plt.ylabel(y)
        plt.savefig(filename)
        plt.close()

    def generate_report(self, title, name, variables=None, report_type="html"):
        profile = ProfileReport(self.df[variables], title=title)
        profile.to_file(f"{name}.html")
        if report_type == "pdf":
            self.generate_pdf_report(title, name, variables)

    def generate_pdf_report(self, title, name, variables):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Add title
        pdf.cell(200, 10, txt=title, ln=True, align="C")

        # Add summary statistics
        _stats = self.stats_summary(variables)
        for _column in _stats.columns:
            pdf.cell(200, 10, txt=f"{_column} statistics", ln=True)
            for _stat in _stats.index:
                pdf.cell(200, 10, txt=f"{stat}: {_stats[_column][_stat]}", ln=True)

        # Add plots
        pdf.image("plot_var.png", x=10, y=100, w=100)
        pdf.image("plot_two_vars.png", x=110, y=100, w=100)

        pdf.output(f"{name}.pdf")



if __name__ == "__main__":
    houses_url = 'https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv'
    houses = Df_Stats(houses_url)


    columns = ['crim', 'zn', 'indus', 'chas',  'rm', 'age']
    for col in columns:
        #print(houses.df)
        print(f'Mean of variable {col}: {houses.var_mean(col)}')
        print(f'Median of variable {col}: {houses.var_median(col)}')
        print(f'Standard Deviation of variable {col}: {houses.var_std(col)}')

    print(houses.stats_summary(columns))

    houses.plot_hist_var('crim')
    houses.plot_scatter_two_vars('crim', 'indus')

    houses.generate_report('Houses summary', 'Houses_Report', columns, report_type="pdf")