import json
import pandas as pd
import numpy as np

# JSON Data로 되어있는 훈련 데화 데이터 불러오기
with open('conv_train.json', 'r') as fp:
    data = json.load(fp)

# train_data라는 이름으로 빈 DataFrame을 생성
# 컬럼명은 [Emotion, Conv] 으로 이루어졌으며 [감정 레이블, 대화문] 의 형식
train_data = pd.DataFrame(columns=['Emotion', 'Conv'])

# JSON To DataFrame
for emo in data:
    # DataFrame에 넣는 동안 제대로 작동이 되는지 보여줄 print문
    # 당황, 상처, 분노, 슬픔, 기쁨, 불안, 놀람, 중립, 혐오 순서대로 DataFrame으로 정렬됨
    print(emo) 
    for conv in range(len(data[emo])): # 감정 하나당 있는 문장을 Loop하는 For 문장
        conv_listItem = [emo, data[emo][conv]] # [감정, 문장] 형태의 List형태로 만들어서 준비
        train_data.loc[len(train_data)] = conv_listItem # 준비된 Item을 DataFrame에 저장

# 데이터 전처리 (중복제거, 특수문자 등 제거, NULL 데이터 제거)
# AI 데이터셋 두개를 이어붙인 데이터를 사용하기 때문에 전처리가 필수적이다
train_data.drop_duplicates(subset=['Conv'], inplace=True) # 중복 제거
# 한글과 공백을 제외하고 모두 제거 (특문 등)
train_data['Conv'] = train_data['Conv'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","")
# 공백으로만 이루어진 데이터를 ""으로 변환
train_data['Conv'] = train_data['Conv'].str.replace('^ +', "")
# 훈련 데이터 중 "" 으로만 이루어진 데이터를 NAN으로 변환
train_data['Conv'].replace('', np.nan, inplace=True)
# NAN 데이터를 전부 Drop
train_data = train_data.dropna(how = 'any')