import pandas as pd
import plotly.express as px
from IPython.display import display, HTML

# Data
data = {
    "Country": [
        "United States", "China", "India", "Germany", "Russia",
        "Canada", "Italy", "Hong Kong", "Brazil", "United Kingdom"
    ],
    "Billionaires": [902, 450, 205, 171, 140, 76, 74, 66, 56, 55],
    "Wealth_Billion_USD": [6800, 1700, 941, 793, 580, 359, 339, 335, 212, 238],
    "Population_Millions": [331, 1440, 1393, 83, 146, 38, 60, 7.5, 213, 68],
    "Country_Total_Wealth_Billion_USD": [145000, 85000, 15000, 18000, 9500, 11000, 10000, 1700, 4000, 17000],
    "Top10Pct_Wealth_Share": [70, 60, 65, 68, 70, 72, 68, 75, 60, 69],
    "Poverty_Pct": [11.6, 25, 21.9, 15.8, 12.3, 9.4, 13.5, 19.9, 23.5, 18.6]
}

df = pd.DataFrame(data)

# Derived metrics
df["Billionaires_per_Million"] = df["Billionaires"] / df["Population_Millions"]
df["Billionaire_Wealth_Share_Pct"] = (df["Wealth_Billion_USD"] / df["Country_Total_Wealth_Billion_USD"]) * 100
df["Billionaire_Wealth_vs_Top10Pct"] = (df["Billionaire_Wealth_Share_Pct"] / df["Top10Pct_Wealth_Share"]) * 100

# Function to show map and table
def show_map_and_table(df, column, title, scale):
    fig = px.choropleth(df, locations="Country", locationmode="country names",
                        color=column, color_continuous_scale=scale, title=title)
    fig.show()
    
    display(HTML(f"<h3>Data Table: {title}</h3>"))
    display(df[["Country", column]].sort_values(by=column, ascending=False).style.format(precision=2))

# Heatmap + Table 1: Number of Billionaires
show_map_and_table(df, "Billionaires", "Number of Billionaires (2025)", "Reds")

# Heatmap + Table 2: Billionaires per Million People
show_map_and_table(df, "Billionaires_per_Million", "Billionaires per Million People (2025)", "Blues")

# Heatmap + Table 3: % of Country's Wealth Held by Billionaires
show_map_and_table(df, "Billionaire_Wealth_Share_Pct", "% of Country’s Wealth Held by Billionaires", "Oranges")

# Heatmap + Table 4: % of Top 10% Wealth Represented by Billionaires
show_map_and_table(df, "Billionaire_Wealth_vs_Top10Pct", "Billionaire Share of Top 10% Wealth (2025)", "Purples")

# Heatmap + Table 5: % of Population Living in Poverty
show_map_and_table(df, "Poverty_Pct", "% of Population Living in Poverty", "Greens")
