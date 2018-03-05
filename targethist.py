#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Feb 27 18:46:16 2018

@author: kazuyuki
"""

import pandas as pd

def targethist(df, target, save=False, kind='hist', **kwards):
    
    columns = df.columns[df.columns != target]
    pdf = df.pivot_table(index=df.index, columns=target)
    
    for column in columns:
        
        ax = pdf.loc[:, column].plot(kind=kind, title=column, **kwards)
        
        if save==True:
            ax.get_figure().savefig(column+".png")    

if __name__ == "__main__":
    
    df = pd.read_csv("iris.csv")
    
    target="Name"
    bins=20
    save=False
    
    targethist(df, target, save)
