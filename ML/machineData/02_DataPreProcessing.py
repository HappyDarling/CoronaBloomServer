import json
import pandas as pd
import numpy as np

# JSON 데이터를 읽어서 변수에 할당
with open('conv.json', 'r') as fp:
    data = json.load(fp)

train_data = pd.DataFrame(columns=['Emotion', 'Conv'])

# 할당된 변수를 읽어서 데이터 처리하기 위한 형태로 가공
for emo in data:
    for conv in range(len(data[emo])):
        conv_listItem = [ emo , data[emo][conv]]
        train_data.loc[len(train_data)] = conv_listItem

# 데이터를 학습하기 위한 전처리
train_data.drop_duplicates(subset=['Conv'], inplace=True) # 중복된 데이터 제거
train_data['Conv'] = train_data['Conv'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","") # 한글과 공백을 제외하고 모두 제거
train_data['Conv'] = train_data['Conv'].str.replace('^ +', "") # 공백 데이터를 빈 값로 변경
train_data['Conv'].replace('', np.nan, inplace=True) # 빈 값을 Null 값으로 변경
train_data = train_data.dropna(how = 'any') # 전처리 과정에서 빈 데이터 샘플이 만들어졌으면 제거