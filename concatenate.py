# -*- coding: utf-8 -*-

import os
import glob
import pandas

def concatenate(indir='/home/zelgius/Github/FAST_times/',outfile='/home/zelgius/Documents/concatenated.csv'):
	os.chdir(indir)
	fileList=glob.glob('*.csv')
	dfList=[]
	colnames=['ARK','JSON_response','DAMS_Label']
	for filename in fileList:
		print filename
		df=pandas.read_csv(filename, header=None)
		dfList.append(df)
	concatDf=pandas.concat(dfList, axis=1)
	concatDf.columns=colnames
	concatDf.to_csv(outfile, index=None)

concatenate()