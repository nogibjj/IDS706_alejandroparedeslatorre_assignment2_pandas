from main import Df_Stats
import os

def test_mean():
    """Testing mean"""
    assert (
        houses.var_mean('crim')
        == 3.613523557312254
    )
    print("Success")

def test_median():
    """Testing median"""
    assert (
        houses.var_median('crim')
        == 0.25651
    )
    print("Success")

def test_std():
    """Testing standard deviation"""
    assert (
        houses.var_std('crim')
        == 8.59304135129577
    )
    print("Success")


def test_plot_hist_var():
    """Testing histogram plot creation"""
    filename = "test_histogram.png"
    houses.plot_hist_var('crim', filename)
    
    assert os.path.exists(filename), "Histogram plot was not created."
    print("Histogram plot creation test passed")
    
    # Clean up the file after the test
    os.remove(filename)

def test_plot_scatter_two_vars():
    """Testing scatter plot creation"""
    filename = "test_scatter.png"
    houses.plot_scatter_two_vars('crim', 'indus', filename)
    
    assert os.path.exists(filename), "Scatter plot was not created."
    print("Scatter plot creation test passed")
    
    # Clean up the file after the test
    os.remove(filename)

if __name__ == "__main__":
    houses_url = 'https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv'
    houses = Df_Stats(houses_url)
    test_mean()
    test_median()
    test_std()
    # Test plot functions
    test_plot_hist_var()
    test_plot_scatter_two_vars()