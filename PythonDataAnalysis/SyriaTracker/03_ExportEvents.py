import StaticPath as SP

output_path_str = r'C:\Users\huina_000\OneDrive\Projects\ProjectSyria\Project\PythonDataAnalysis\PythonDataAnalysis\SyriaTracker\Output' + '\\'
trans_file_str = r'translated.csv'
events_file_str = r'events.csv'

import pandas
data_df = pandas.read_csv(output_path_str + trans_file_str)

event_keywords_rex ={
        'battle':
        [
            r'\bbattle\b',
        ],
        'shelling':
        [
            r'\bshelling\b',
        ],
        'air_strike':
        [
            r'\bair.?strike\b',
            r'\bair.?raids\b'
        ],
        'intervention':
        [
            r'\bintervention\b',
        ],
        'chemical':
        [
            r'\bchemical\b',
        ],
        'massacre':
        [
            r'\bmassacre\b'
        ],
        'agreement':
        [
            r'\bagreement\b'
        ],
        'remarkable_event':
        [
            r'\bremarkable.?event\b'
        ]
    }


def export_Desc_to_event(desc_str):
    events = ['']
    for key in event_keywords_rex.keys():
        for rex in event_keywords_rex[key]:
            copy_desc = desc_str.lower()
            m = re.search(rex, copy_desc)
            if m is None:
                continue
            events.append(key)            
            break
    return events

# test code
idx = 0
for row in data_df.iterrows():
    print('index : ', idx)
    str = row[1]['DESCRIPTION']
    copy_desc = str.lower()
    m = re.search('remark', copy_desc)
    idx += 1
    if m is None:
        continue
    else:
        copy_desc
        break
    break

# extract event keywords in DESCRIPTION field.
# input extracted keyword to 'events' field.
data_df['events'] = list(map(lambda str : ' '.join(export_Desc_to_event(str)), data_df['DESCRIPTION']))

# str to date
import dateutil.parser
data_df['PyDate'] = data_df['INCIDENT DATE'].map(dateutil.parser.parse)

# if 'events', input True, but False
for key in event_keywords_rex.keys():
    data_df[key] = list(map(lambda arg : (type(arg) is str) & (arg.find(key) > 0), data_df['events']))

# new DataFrame for groups on year & month
event_df = pandas.DataFrame()

import datetime
import calendar
from dateutil.relativedelta import relativedelta

# Create list 2011-04-01 ~ 2016-03-01
months_list = []
start_date = datetime.datetime(2011,4,1)
idx = 0
while idx < 12 * 5:        
    mod_date = start_date + relativedelta(months=idx)
    months_list.append(mod_date)
    idx += 1

# Insert DateTime list to PyDate Column
event_df['PyDate'] = months_list

# Create Columns for events key, fill '0'
for key in event_keywords_rex.keys():
    event_df[key] = list(map(lambda arg : 0, range(len(event_df))))

# About events. if key, add count in event field.
for row in data_df.iterrows():
    row_date = row[1]['PyDate']
    event_str = row[1]['events']
    for key in event_keywords_rex.keys():
        if event_str.find(key) > 0:
            key
            events_date_idx = event_df['PyDate'].searchsorted(datetime.datetime(row_date.year,row_date.month,1))[0]
            events_date_idx
            event_df[key].iloc[events_date_idx] += 1
    #break

event_df.to_csv(output_path_str + events_file_str, encoding='utf-8')