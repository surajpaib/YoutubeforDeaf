# Create Final Metadata file with .gif files

import pandas as pd


df=pd.read_csv('metadata.csv',header=0)
mat=df['Filename'].as_matrix()

fname=[]
for row in mat:
    k = str(row).split(".")
    t = str(k[0]).replace("'", "")
    j=str(t)+".gif"
    fname.append(j)


df['Filename']=fname
df.to_csv('metadatafinal.csv',index=0)

