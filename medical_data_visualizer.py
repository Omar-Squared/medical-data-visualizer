import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
bmi = df["weight"]/ np.square(df["height"]/100)
df["overweight"] = ( bmi > 25).astype(int)

# 3

df[["gluc", "cholesterol"]] = df[["gluc", "cholesterol"]].apply(lambda x: (x > 1).astype(int))

# 4
def draw_cat_plot():
    # 5
    df_cat = df.melt(id_vars=["cardio"], value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])
    # print(df_cat)

    # 6
    df_cat = df_cat.groupby(["cardio","variable", "value"]).size().reset_index(name="total")

    # print(df_cat)

    # 7

    # 8
    fig = sns.catplot(
        x="variable",
        y="total",
        hue="value",
        col="cardio",
        kind="bar",
        data=df_cat).fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"]) & 
        (df["height"] >= df["height"].quantile(0.025)) &
        (df["height"] <= df["height"].quantile(0.975)) & 
        (df["weight"] >= df["weight"].quantile(0.025)) &
        (df["weight"] <= df["weight"].quantile(0.975))
        ]

    # print(df_heat)

    # 12
    corr = df_heat.corr()
    print(corr)

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))
    print(mask)


    # 14
    fig, ax = plt.subplots(figsize=(12,8))

    # 15
    sns.heatmap(corr, mask=mask, ax=ax, annot=True, fmt=".1f", center=0, vmax =0.5)
    ax.set_title("Correlation Heat Map", fontsize=16)

    # 16
    fig.savefig('heatmap.png')
    return fig
