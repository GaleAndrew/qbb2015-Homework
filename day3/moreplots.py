#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

metadata = pd.read_csv('~/qbb2015/rawdata/samples.csv')
metadatar = pd.read_csv('~/qbb2015/rawdata/replicates.csv')
sxlf = []
for samplef in metadata[metadata['sex'] == "female"]['sample']:  ######pulls out the rows that have female sex and assigns it to a new metadata than pulls the sample name of those files
    dff = pd.read_table('~/qbb2015/stringtie/'+samplef+'/t_data.ctab')                   #####makes dataframe or the t_data.ctab files baed on the sample name
    roif = dff['t_name'].str.contains('FBtr0331261')
    sxlf.append(dff[roif]['FPKM'].values)  ###makes new df for those that are one of the files we want with the string and pulls FPKM values and adds it to the list sxl
    
sxlm = []  
for samplem in metadata[metadata['sex'] == "male"]['sample']:  ######pulls out the rows that have female sex and assigns it to a new metadata than pulls the sample name of those files
    dfm = pd.read_table('~/qbb2015/stringtie/'+samplem+'/t_data.ctab')                   #####makes dataframe or the t_data.ctab files baed on the sample name
    roim = dfm['t_name'].str.contains('FBtr0331261')
    sxlm.append(dfm[roim]['FPKM'].values)  ###makes new df for those that are one of the files we want with the string and pulls FPKM values and adds it to the list sxl
sxlr=[]
for sampler in metadatar[metadatar['sex'] == "male"]['sample']:  ######pulls out the rows that have female sex and assigns it to a new metadata than pulls the sample name of those files
    dfr = pd.read_table('~/qbb2015/stringtie/'+sampler+'/t_data.ctab')                   #####makes dataframe or the t_data.ctab files baed on the sample name
    roir = dfr['t_name'].str.contains('FBtr0331261')
    sxlr.append(dfr[roir]['FPKM'].values)  ###makes new df for those that are one of the files we want with the string and pulls FPKM values and adds it to the list sxl
    
    
    
    
sxlg=[]
for sampleg in metadatar[metadatar['sex']=='female']['sample']:  ######pulls out the rows that have female sex and assigns it to a new metadata than pulls the sample name of those files
     dfg = pd.read_table('~/qbb2015/stringtie/'+sampleg+'/t_data.ctab')                   #####makes dataframe or the t_data.ctab files baed on the sample name
     roig = dfg['t_name'].str.contains('FBtr0331261')
     sxlg.append(dfg[roig]['FPKM'].values)  ###makes new df for those that are one of the files we want with the string and pulls FPKM values and adds it to the list sxl   
 
#print sxlg, "\n", sxlr
plt.figure()
line1 =plt.plot(sxlf, 'r', label ='female')
plt.plot(sxlm, 'b', label = 'male')
plt.plot([4,5,6,7],sxlr, 'yo', label = 'Replicate Male')
plt.plot([4,5,6,7],sxlg, 'go', label ='Replicate Female')
plt.legend(loc='upper left')
plt.xlabel('developmental stage')
plt.ylabel('mRNA absorbace (RPKM)')
plt.xticks(range(len(sxlm)),['10','11', '12','13','14A','14B', '14C','14D'], rotation = 90)
plt.ylim((0,300))
plt.savefig('timecourse.png')











df = pd.read_table("~/qbb2015/stringtie/SRR072893/t_data.ctab")



df2 = pd.read_table("~/qbb2015/stringtie/SRR072915/t_data.ctab")

plt.figure()
plt.scatter(df['FPKM'], df2['FPKM'])
plt.xlabel('893-male10')
plt.ylabel('915 female14')
plt.savefig('scatterplot.png')




chromosomes = {}  ##define/call dictionary

for i, line in df.iterrows():   ##pull out the first row and return it to you
    if line['chr'] in ['2L', '2R', '3L', "3R", "X", "y"]:
        if line["chr"] not in chromosomes:
            chromosomes [line["chr"]]=1   ####if not in chromosomes then add it to dictionary
        else:
            chromosomes[line["chr"]]+=1
#range(len(chromosomes))   #pulls out the x range        ###left
#chromosomes.values()  ### gives the values             ###right
#chromosomes.key()     ### get the keys


   
plt.figure
plt.bar(range(len(chromosomes)), chromosomes.values())
plt.xticks(range(len(chromosomes)), chromosomes.keys())
plt.savefig("barplot.png")
