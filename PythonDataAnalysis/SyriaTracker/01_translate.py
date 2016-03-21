import csv
import StaticPath as SP

origin_path_str = r'C:\Users\huina_000\OneDrive\Projects\ProjectSyria\Project\PythonDataAnalysis\PythonDataAnalysis\SyriaTracker\Origin' + '\\'
origin_file_str = r'origin2.csv'
output_path_str = r'C:\Users\huina_000\OneDrive\Projects\ProjectSyria\Project\PythonDataAnalysis\PythonDataAnalysis\SyriaTracker\Output' + '\\'
trans_file_str = r'translated.csv'

#csvfile = open(origin_path_str + origin_file_str, newline='', encoding='utf-8')
#reader = csv.reader(csvfile)
import pandas
df = pandas.read_csv(origin_path_str + origin_file_str)

import time
from textblob import TextBlob
import textblob

# test translate
text = TextBlob('반갑습니다.')
text.translate()

desc_col = 'DESCRIPTION'

error_idx = 0
err_list = []
idx = 0
cols = [4]
for index, row in df.iterrows():
    for col in cols:
        print('idx : ', idx, ' // col : ', col)
        str = df.iloc[idx, col]
        try:
            text = TextBlob(str)            
            trans = text.translate('ar', 'en')
            df.iloc[idx,col] = trans.string
            print(trans.string)
        except textblob.exceptions.NotTranslated:
            print('Nottranslated error')
            err_list.append(idx)
            break
        except:
            print('err')
            error_idx = idx            
            err_list.append(idx)
            break
    idx += 1
    # test comment
    #break
print('error : ', error_idx)

df.to_csv(output_path_str + trans_file_str, encoding='utf-8')