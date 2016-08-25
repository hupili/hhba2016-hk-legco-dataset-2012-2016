import pandas as pd

files = [{
            'input': 'party-to-camp-mapping.csv',
            'output': 'party-to-camp-mapping-en.csv',
            },{
            'input': 'member-profile-2012-2016.csv',
            'output': 'member-profile-2012-2016-en.csv'
            }
        ]
dict_file = 'dict.csv'

df_dict = pd.read_csv(dict_file).set_index('from')
#print(df_dict)

def translate_term(term):
    if term in df_dict['to']:
        #print(df_dict['to'][term])
        return df_dict['to'][term]
    else:
        return term

for fn in files:
    df_input = pd.read_csv(fn['input'], header=None)
    df_output = df_input.applymap(translate_term)
    df_output.to_csv(fn['output'], index=None, header=None)

