import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("startup_funding.csv")
df_list = df.InvestorsName.str.split(",")
df.InvestorsName = df_list
df = df.explode('InvestorsName')
df["InvestorsName"] = df["InvestorsName"].str.strip()
df_test = df[df["InvestorsName"].str.strip() == "Sequoia Capital"]["InvestorsName"]
# c =0
# for ele in df_test:
    # print(ele)
    # c+=1
# df.loc[(df["StartupName"].str.lower() == "ola cabs")|(df["StartupName"].str.lower() == "olacabs"), "StartupName"] = "Ola"
# df.loc[df["StartupName"].str.lower().str.find("flipkart") > -1, "StartupName"] = "Flipkart"
# df.loc[df["StartupName"].str.lower().str.find("paytm") > -1, "StartupName"] = "Paytm"
# df.loc[df["StartupName"].str.lower().str.find("oyo rooms") > -1, "StartupName"] = "Oyo"
# df.loc[df["StartupName"].str.lower().str.find("oyorooms") > -1, "StartupName"] = "Oyo"

#
# df.loc[df["InvestmentType"] == "PrivateEquity", "InvestmentType"] = "Private Equity"
# df.loc[df["InvestmentType"] == "Crowd funding", "InvestmentType"] = "Crowd Funding"
# df.loc[df["InvestmentType"] == "SeedFunding", "InvestmentType"] = "Seed Funding"
#
df_funding_round = df.groupby("InvestorsName")["InvestorsName"].count()
df_funding_round.sort_values(inplace=True, ascending=False)
df_funding_round = df_funding_round[:1]
total = df_funding_round.count()
for ele in df_funding_round.index:
    print("{} {}".format(ele, df_funding_round[ele]))

