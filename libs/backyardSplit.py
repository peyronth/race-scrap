import pandas as pd
from libs import excelExport
import tkinter.messagebox

def exportbybistance(df, distancecolumn): 
    # Sort each sub dataset by time in ascending order
    sub_datasets = df.groupby(distancecolumn)

    filesnames = []
    # Export each sorted sub dataset to Excel
    for race, sub_dataset in sub_datasets:
        distance = sub_dataset[distancecolumn].iloc[0]
        filesnames.append(excelExport.excel_export(sub_dataset, "--backyard--" + str(distance) + "--"))

    return filesnames

def exportbylapcount (df, lapcount_column):
    sub_datasets = df.groupby(lapcount_column)

    filesnames = []
    lapcountarray = []
    for race, sub_dataset in sub_datasets:
        lapcount = sub_dataset[lapcount_column].iloc[0]
        filesnames.append(excelExport.excel_export(sub_dataset, "--backyard--" + str(lapcount) + "laps--"))
        lapcountarray.append(lapcount)

    return filesnames
    

def excelsplitdistance(filepath, distancecolumn = "Distance"):
    # Create pandas dataframe from excel file
    df = pd.read_excel(filepath)
    return exportbybistance(df, distancecolumn)

def excelsplitlapcount(filepath, lapcount_column = "Lap count"):
    df = pd.read_excel(filepath)
    return exportbylapcount(df, lapcount_column)

