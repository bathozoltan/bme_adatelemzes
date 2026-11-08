import numpy as np
import pandas as pd

# csv_name_set = set()
# while True:
#    i = input("enter csv name to add to merger, or press enter to merge ")
#    if i == "":
#        break
#    else :
#        csv_name_set.add(i)

csv_name_set = {"konzum_elmu_emasz_raba_mbhjb_1.csv",
                "mbhbank_splus_granit_delta_alteo_masterplast_2.csv",
                "akko_4ig_autowallis_bif_waberers_any_appeninn_cigpannonia_gspark_mtelekom_1.csv",
                "akko_4ig_autowallis_bif_waberers_any_appeninn_cigpannonia_gspark_mtelekom_2.csv",
                "mol_opus_otp_pannergy_richter_zwack_1.csv",
                "mol_opus_otp_pannergy_richter_zwack_2.csv"}

df_list = []
for i in csv_name_set:
    df_list.append(pd.read_csv("./raw_data/" + i, 
                               usecols=["Name", "Date", "Last price"],
                               parse_dates = ["Date"]
                               ))
df_merged = pd.concat(df_list, axis=0).set_index(["Name", "Date"])

df_merged.to_csv("merged.csv")











