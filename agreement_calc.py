## Calculating agreement between three coders
#%%
import pandas
import krippendorff_alpha

def import_values(filename, coder):
    ## Values we care about: ID, Coded By, Contextual Risk factors, practices and attitudes
    data = pandas.read_csv(filename)
    data.columns = data.iloc[0]
    data = data.drop(data.index[0])
    data = data[['ID', 'Coded by', 'newline separated list', 'Protective', 'Risky']]
    data = data.rename(columns={'newline separated list':'Factors', 'Coded by':'Coder'})
    
    data['Coder'] = coder

    return data

def factors_agreement(c1, c2, c3):
    combined = c1.merge(c2, on='ID')[['ID','Factors_x','Factors_y']].rename(columns={
        'Factors_x':'c1', 'Factors_y':'c2'
    })
    combined = combined.merge(o, on='ID')[['ID','c1','c2','Factors']].rename(columns={
        'Factors':'c3'
    })

    return combined

""" Legal or Political
Knowledge 
Oppressed or stigmatized by adversaries 
Prominence
Relationship with the attacker 
Reliance on a third party
Resource or time constrained 
Stress (ongoing or past attack or other stressors)
Susceptibility to radicalization or risk-seeking 
Access to a sensitive resource or person
Social expectations and norms
 """

key_factors = {
    'Legal':1,
    'Knowledge':2,
    'Oppressed':3,
    'Prominence':4,
    'Relationship':5,
    'Reliance':6,
    'Resource':7,
    'Stress':8,
    'Suseceptibility':9,
    'Access':10,
    'Social':11,
}
has_key = lambda a,d: any(k in a for k in d)

def replace_factors(codes):
    result = []
    codes = codes.split("\n")
    for code in codes:
        result.append([val for key, val in key_factors.items() if key in code][0])

    result.sort()
    return result

# input is combined [ID:[coder1, coder2, coder3],...]
def numerical_values(data):
    result = []
    for index,row in data.iterrows():
        c1 = replace_factors(row['c1'])
        c2 = replace_factors(row['c2'])
        c3 = replace_factors(row['c3'])

        result.append(c1)

import_values("Reliability checks - Kaitlyn.csv", 'Kaitlyn')

# %%
