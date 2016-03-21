import StaticPath as SP

output_path_str = r'C:\Users\huina_000\OneDrive\Projects\ProjectSyria\Project\PythonDataAnalysis\PythonDataAnalysis\SyriaTracker\Output' + '\\'
trans_file_str = r'translated.csv'
groups_file_str = r'groups.csv'

import pandas
data_df = pandas.read_csv(output_path_str + trans_file_str)

involved_groups_rex = {
        'UN':
        [r'\bu\.?n\b',    
            r'\bunited.?nation\b'],
        'US':
        [r'\busa\b',
            r'\bunited.?state\b'],
        'RS':
        [r'\brussia\b',
            r'\brussian\b',],
        'IR':
        [r'\biran\b'],
        'HZB':
        [r'\bhezbollah\b'],
        'YPG':
        [r'\bkruds\b',
            r'\bkrudish\b',
            r'\bpyd\b',
            r'\bypg\b'],
        'IS':
        [r'\bisis\b',
            r'\bisil\b',
            r'\bislamic.?state\b',
            r'\bstate.?islamic\b',
            r'\bdaesh\b'],
        'IC':
        [r'\binternational.?coalition\b',
            r'\bcoalition\b'],
        'FSA':
        [r'\bfsa\b',
            r'\bopposition\b',
            r'\bfree.?syria\b',
            r'\bfree.?syrian\b'],
        'ANF':
        [r'\bal.?busra.?front\b',
            r'\bal.?nosra.?front\b',
            r'\bfront.?victory\b'],
        'ASS':
        [r'\bassad\b',
            r'\bregime\b',
            r'\bsyrian.?army\b']
    }

import re
def extract_Desc_to_groups(desc_str):
    involved_groups = ['']
    for key in involved_groups_rex.keys():
        for rex in involved_groups_rex[key]:
            copy_desc = desc_str.lower()
            m = re.search(rex, copy_desc)
            if m is None:
                continue
            #span = m.span()
            #str = desc_str[span[0]:span[1]]
            involved_groups.append(key)            
            break
    return involved_groups

data_df['involved groups'] = list(map(lambda str : ' '.join(extract_Desc_to_groups(str)), data_df['DESCRIPTION']))

for key in involved_groups_rex.keys():
    data_df[key] = list(map(lambda arg : (type(arg) is str) & (arg.find(key) > 0), data_df['involved groups']))

groups_df = pandas.DataFrame()

import datetime
import calendar
from dateutil.relativedelta import relativedelta
import dateutil.parser

data_df['PyDate'] = data_df['INCIDENT DATE'].map(dateutil.parser.parse)

months_list = []
start_date = datetime.datetime(2011,4,1)
idx = 0
while idx < 12 * 5:        
    mod_date = start_date + relativedelta(months=idx)
    months_list.append(mod_date)
    idx += 1

# Insert DateTime list to PyDate Column
groups_df['PyDate'] = months_list

# fill 0
for key in involved_groups_rex.keys():
    groups_df[key] = list(map(lambda arg : 0, range(len(groups_df))))

# About groups.  if key, add count in group field.
for row in data_df.iterrows():
    row_date = row[1]['PyDate']
    groups_str = row[1]['involved groups']
    for key in involved_groups_rex.keys():
        if groups_str.find(key) > 0:
            key
            groups_date_idx = groups_df['PyDate'].searchsorted(datetime.datetime(row_date.year,row_date.month,1))[0]
            groups_date_idx
            groups_df[key].iloc[groups_date_idx] += 1
    break

groups_df.to_csv(output_path_str + groups_file_str, encoding='utf-8')

# set category
groups_category = {
    'International_groups':['UN','US','RU','IC'],
    'Islamic_power':['IR','HZB','YPG','IS','ANF'],
    'Assard':['ASS'],
    'Opposition':['FSA']
    }

# fill 0
for key in groups_category.keys():
    groups_df[key] = list(map(lambda arg : 0, range(len(groups_df))))

for row in data_df.iterrows():
    row_date = row[1]['PyDate']
    groups_str = row[1]['involved groups']
    for key in involved_groups_rex.keys():
        if groups_str.find(key) > 0:
            print('key : ', key)
            groups_date_idx = groups_df['PyDate'].searchsorted(datetime.datetime(row_date.year,row_date.month,1))[0]
            print('groups_date_idx : ', groups_date_idx)
            for key_cate in groups_category.keys():
                if key in key_cate:
                    groups_df[key].iloc[key_cate] += 1
    break
