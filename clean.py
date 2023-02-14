import pandas as pd
import numpy as np
import pickle

def clean(input_1,input_2):
    df1 = pd.read_csv(input_1)
    df2 = pd.read_csv(input_2)
    dm = pd.merge(df1, df2, left_on="respondent_id", right_on="id")
    dm = dm.drop(['id'],axis=1)
    dd = dm.dropna()
    #dj = dd.drop(dd[(dd["job"]=="insurance") | (dd["job"]=="Insurance")].index)
    dj = dd[dd["job"].str.contains("insurance|Insurance")==False]
    return dj

if __name__ == '__main__':
    print("clean data")
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("contact_info", help="data file1(CSV)")
    parser.add_argument("other_info", help="data file2(CSV)")
    parser.add_argument("output", help="Clean the data")
    args = parser.parse_args()
   # data_cleaned = clean("respondent_contact.csv","respondent_other.csv")
    data_cleaned = clean(args.contact_info,args.other_info)
    data_cleaned.to_csv(args.output,index=False)

a=1;b=10  # add some new content to update the clean.py
x=a+b