# 두개의 AI 훈련 데이터를 깔끔하게 파싱하기 위해서 감정 분류 대분류 몇개는 묶어주고 한개의 JSON 데이터로 추출하는 작업
# 본 훈련에 사용하는 데이터셋은 AIHUB의 "한국어 감정 정보가 포함된 연속적 대화 데이터셋" 과 "감성 대화 말뭉치" 가 사용되었으며 
# 이 데이터는 사용하기 위해서는 한국지능정보사회진흥원의 AIHUB에 신청하여야 하고 사용 사실을 알려야 한다.
import pandas as pd
import numpy as np

df_SNSconv = pd.read_excel('sns_conversation.xlsx', engine='openpyxl')
df_conv = pd.read_excel('conversation_train.xlsx', engine='openpyxl')

import json

file_path = "./conv.json"

data = {}
data[0] = [] # 부정
for w in range(len(df_conv[df_conv['감정_대분류'].isin(['불안'])])):
    if not (pd.isnull(df_conv[df_conv['감정_대분류'].isin(['불안'])].iloc[w, 7])):
        data[0].append(df_conv[df_conv['감정_대분류'].isin(['불안'])].iloc[w, 7])
    if not (pd.isnull(df_conv[df_conv['감정_대분류'].isin(['불안'])].iloc[w, 9])):
        data[0].append(df_conv[df_conv['감정_대분류'].isin(['불안'])].iloc[w, 9])
    if not (pd.isnull(df_conv[df_conv['감정_대분류'].isin(['불안'])].iloc[w, 11])):
        data[0].append(df_conv[df_conv['감정_대분류'].isin(['불안'])].iloc[w, 11])
    if not (pd.isnull(df_conv[df_conv['감정_대분류'].isin(['불안'])].iloc[w, 13])):
        data[0].append(df_conv[df_conv['감정_대분류'].isin(['불안'])].iloc[w, 13])
for w in range(len(df_conv[df_conv['감정_대분류'].isin(['분노'])])):
    if not (pd.isnull(df_conv[df_conv['감정_대분류'].isin(['분노'])].iloc[w, 7])):
        data[0].append(df_conv[df_conv['감정_대분류'].isin(['분노'])].iloc[w, 7])
    if not (pd.isnull(df_conv[df_conv['감정_대분류'].isin(['분노'])].iloc[w, 9])):
        data[0].append(df_conv[df_conv['감정_대분류'].isin(['분노'])].iloc[w, 9])
    if not (pd.isnull(df_conv[df_conv['감정_대분류'].isin(['분노'])].iloc[w, 11])):
        data[0].append(df_conv[df_conv['감정_대분류'].isin(['분노'])].iloc[w, 11])
    if not (pd.isnull(df_conv[df_conv['감정_대분류'].isin(['분노'])].iloc[w, 13])):
        data[0].append(df_conv[df_conv['감정_대분류'].isin(['분노'])].iloc[w, 13])
for w in range(len(df_conv[df_conv['감정_대분류'].isin(['슬픔'])])):
    if not (pd.isnull(df_conv[df_conv['감정_대분류'].isin(['슬픔'])].iloc[w, 7])):
        data[0].append(df_conv[df_conv['감정_대분류'].isin(['슬픔'])].iloc[w, 7])
    if not (pd.isnull(df_conv[df_conv['감정_대분류'].isin(['슬픔'])].iloc[w, 9])):
        data[0].append(df_conv[df_conv['감정_대분류'].isin(['슬픔'])].iloc[w, 9])
    if not (pd.isnull(df_conv[df_conv['감정_대분류'].isin(['슬픔'])].iloc[w, 11])):
        data[0].append(df_conv[df_conv['감정_대분류'].isin(['슬픔'])].iloc[w, 11])
    if not (pd.isnull(df_conv[df_conv['감정_대분류'].isin(['슬픔'])].iloc[w, 13])):
        data[0].append(df_conv[df_conv['감정_대분류'].isin(['슬픔'])].iloc[w, 13])

data[1] = [] # 긍정
for w in range(len(df_conv[df_conv['감정_대분류'].isin(['기쁨'])])):
    if not (pd.isnull(df_conv[df_conv['감정_대분류'].isin(['기쁨'])].iloc[w, 7])):
        data[1].append(df_conv[df_conv['감정_대분류'].isin(['기쁨'])].iloc[w, 7])
    if not (pd.isnull(df_conv[df_conv['감정_대분류'].isin(['기쁨'])].iloc[w, 9])):
        data[1].append(df_conv[df_conv['감정_대분류'].isin(['기쁨'])].iloc[w, 9])
    if not (pd.isnull(df_conv[df_conv['감정_대분류'].isin(['기쁨'])].iloc[w, 11])):
        data[1].append(df_conv[df_conv['감정_대분류'].isin(['기쁨'])].iloc[w, 11])
    if not (pd.isnull(df_conv[df_conv['감정_대분류'].isin(['기쁨'])].iloc[w, 13])):
        data[1].append(df_conv[df_conv['감정_대분류'].isin(['기쁨'])].iloc[w, 13])
for w in range(len(df_SNSconv[df_SNSconv['Emotion'].isin(['놀람'])])):
    if not (pd.isnull(df_SNSconv[df_SNSconv['Emotion'].isin(['놀람'])].iloc[w, 0])):
        data[1].append(df_SNSconv[df_SNSconv['Emotion'].isin(['놀람'])].iloc[w, 0])
for w in range(len(df_SNSconv[df_SNSconv['Emotion'].isin(['중립'])])):
    if not (pd.isnull(df_SNSconv[df_SNSconv['Emotion'].isin(['중립'])].iloc[w, 0])):
        data[1].append(df_SNSconv[df_SNSconv['Emotion'].isin(['중립'])].iloc[w, 0])
for w in range(len(df_SNSconv[df_SNSconv['Emotion'].isin(['공포'])])):
    if not (pd.isnull(df_SNSconv[df_SNSconv['Emotion'].isin(['공포'])].iloc[w, 0])):
        data[1].append(df_SNSconv[df_SNSconv['Emotion'].isin(['공포'])].iloc[w, 0])
for w in range(len(df_SNSconv[df_SNSconv['Emotion'].isin(['혐오'])])):
    if not (pd.isnull(df_SNSconv[df_SNSconv['Emotion'].isin(['혐오'])].iloc[w, 0])):
        data[1].append(df_SNSconv[df_SNSconv['Emotion'].isin(['혐오'])].iloc[w, 0])

with open(file_path, 'w') as outfile:
    json.dump(data, outfile)