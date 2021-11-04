# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 17:32:09 2021

@author: user
"""

import pandas as pd
import numpy as np
import pickle
import statsmodels.api as sm
case = pd.read_excel('E:/DAY1/连问/case.xlsx', dtype={'Stkcd': str})
# case=case[case['Trddt']<'2020-09-22']
case = case[(case['Trddt'] > '2012-11-08') & (case['Trddt'] < '2020-09-22')]
data = pd.read_pickle('E:/DAY1/连问/data')
data['con'] = 1
caseout = pd.DataFrame()
for hi in range(0, len(case)):
    try:
        case01 = case.iloc[hi:hi+1]
        stk01 = case01.Stkcd.iloc[0]
        casedt = case01.Trddt.iloc[0]
        inddata = data[data.Stkcd == stk01]
        inddata = inddata.sort_values(by='Trddt', axis=0, ascending=True)
        dataq = inddata[inddata.Trddt < casedt]
        datah = inddata[inddata.Trddt >= casedt]
        regdata = dataq.iloc[-500:-251]
        model10 = sm.OLS(regdata['Dretwd'].astype(float), regdata[[
                         'con', 'RiskPremium1', 'SMB1', 'HML1']]).fit()
        par = model10._results.params
        a = par[0]
        b = par[1]
        c = par[2]
        d = par[3]
        stkrs01qsum = dataq[-250:]
        stkrs01hsum = datah[0:251]
        stkrs01all = stkrs01qsum.append(stkrs01hsum)
        stkrs01all = stkrs01all.sort_values(by='Trddt', axis=0, ascending=True)
        stkrs01all['RE'] = a+b*stkrs01all['RiskPremium1'] + \
            c*stkrs01all['SMB1']+d*stkrs01all['HML1']
        stkrs01all['AR'] = stkrs01all['Dretwd'].astype(float)-stkrs01all['RE']
        stkrs01all['CAR_qx'] = stkrs01all['AR'].cumsum()
        stkrs01all['day'] = range(-250, 251)
        car01 = stkrs01all[['CAR_qx', 'day']]
        car01 = car01.reset_index(drop=True)
        car01 = car01.set_index(['day'])
        car01 = car01.T
        car01 = car01.reset_index(drop=True)
        car01['Stkcd'] = stk01
        case01 = pd.merge(case01, car01, on=['Stkcd'], sort=True, how='left')
        print(hi)
        caseout = caseout.append(case01)
    except:
        continue
caseout.to_pickle('E:/DAY1/连问/caseout(250day)')
