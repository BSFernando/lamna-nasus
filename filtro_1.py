import pandas as pd

tabela = pd.read_excel(".../_tagPOR_20200611.xlsx",
        sheet_name="tagPOR", header=4)

tab = pd.DataFrame(tabela)

tab = tab.drop(columns=['TagGrpID', 'SpecimenID', 'InProcID', 'RC', 'RCStageCode', 'strTags1',
       'strTags2', 'strTags3', 'strTags4', 'SpeciesCode', 'ReFleetCode',
       'ReGearCode', 'ReLenType', 'ReLenMethod', 'ReWgtType', 'ReWgtMethod', 'ReQcErrorID', 'RcFleetCode',
       'RcGearCode', 'Sex', 'RcWgt', 'RcWgtUnit', 'ReWgtUnit', 'RcLen', 'RcLenUnit', 'ReLenUnit', 'ReWgt',
        'ReLen','RcLenType', 'RcLenMethod', 'RcWgtType', 'RcWgtMethod', 'RcQcErrorID','RcYear', 'RcDate',
        'RcLatY', 'RcLonX', 'RcLenCM','RcWgtKG']) #retirando colunas indesejaveis

tab = tab[(tab["ReLatY"].notna()) & (tab["ReLonX"].notna()) & (tab["ReYear"].notna()) &
      (tab['ReYear'] != 'Unk') & (tab["ReLatY"] > 0) & (tab["ReLonX"] < -30)] #filtrando valores de lat, long e ano

tab = tab.sort_values('ReYear')

tab.index = range(0,len(tab),1)
  
tab.to_csv(".../TAB.csv")

