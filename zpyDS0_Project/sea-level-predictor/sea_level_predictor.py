import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    reg_x = range(1880, 2051)
    reg_x2 = range(2000, 2051)

    # Create scatter plot
    # plt.plot(df["Year"], df["CSIRO Adjusted Sea Level"], 'm.', label='original data')
    # have to use pandas plot below, if use plt then cannot pass test
    df.plot.scatter(x="Year", y="CSIRO Adjusted Sea Level")
    plt.title("Rise in Sea Level")

    # Create first line of best fit
    slope, intercept, rvalue, pvalue, stderr = linregress(
        df["Year"], df["CSIRO Adjusted Sea Level"]
    )
    plt.plot(reg_x, intercept + slope * reg_x, "r", label="fitted line 1")

    # Create second line of best fit
    df2 = df[df["Year"] >= 2000]
    res2 = linregress(df2["Year"], df2["CSIRO Adjusted Sea Level"])
    plt.plot(reg_x2, res2.intercept + res2.slope * reg_x2, "g--", label="fitted line 2")

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.legend()
    # plt.show()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()
