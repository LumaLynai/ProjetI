import requests
import pandas as pd
from io import StringIO
import numpy as np

def conversor(c):
        return c.to_csv().encode('utf-8')
    
    
def format(valor):
    return "{:,.2f}".format(valor)
    
def cifra(c):
    return "R${:,.2f}".format(c)

def dc(df, ps):
    dx = []
    dy = []

    for i in range(len(df)-ps-1):
        d = df[i:(i+ps), 0]
        dx.append(d)
        dy.append(df[i + ps, 0])
    return np.array(dx), np.array(dy)
