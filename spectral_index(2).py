#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 16:48:32 2019

@author: f90
"""


import numpy as np
#import matplotlib.pyplot as plt
# from lmfit.models import PowerLawModel
import pandas as pd

# def npfit():
# 	x = np.array([4.3, 7.6])
# 	y = np.array([0.0765, 0.0156])
# 	x = np.log(x)
# 	y = np.log(y)
# 	p = np.polyfit(x, y, 1)
# 	print(' %.2f' % p[0])
	
# def PLfit():
# 	nu = np.array([4.3, 7.6])
# 	S = np.array([0.0765, 0.0156])
# 	mod = PowerLawModel()
# 	pars = mod.guess(S, x=nu)
# 	out = mod.fit(S, pars, x=nu)
# #	print(out.fit_report())
# 	print(' %.2f' % out.params['exponent'].value)
# #	alpha = out.params['']
#imstat_rms(fname)
#PLfit()
#npfit()
def npfit2():
	fname = 'ips-spec4.xlsx'
	df = pd.read_excel(fname)
	#print(df)
	x1 = df['v2'].values
	x2 = df['v1'].values
	y1 = df['s2'].values
	y2 = df['s1'].values
	alpha = []
	for i in range(x1.size):
		x = np.array([x1[i], x2[i]])
		y = np.array([y1[i], y2[i]])
	#	print(i,y)
		x = np.log(x)
		y = np.log(y)
		p = np.polyfit(x, y, 1)
		alpha.append(p[0])
	#print(alpha)
	df['Spectral index'] = alpha
	df.to_excel(fname.replace('.xlsx','-all5.xlsx'))
npfit2()