import pandas as pd
import matplotlib.pyplot as plt
from ydata_profiling import ProfileReport
import numpy as np
import statistics as stat


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

    def generate_report(self, title, name, variables=None):
        profile = ProfileReport(self.df[variables], title=title)
        profile.to_file(f"{name}.html")


if __name__ == "__main__":
    url = 'https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv'
    houses = Df_Stats(url)


    variables = ['crim', 'zn', 'indus', 'chas',  'rm', 'age']
    for var in variables:
        #print(houses.df)
        print(f'Mean of variable {var}: {houses.var_mean(var)}')
        print(f'Median of variable {var}: {houses.var_median(var)}')
        print(f'Standard Deviation of variable {var}: {houses.var_std(var)}')

    print(houses.stats_summary(variables))

    houses.plot_hist_var('crim')
    houses.plot_scatter_two_vars('crim', 'indus')

    houses.generate_report('Houses summary', 'Houses_Report', variables)
