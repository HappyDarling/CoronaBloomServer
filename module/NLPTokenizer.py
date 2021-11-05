# JS에서 Python을 사용하기 위한 방법
# !pip uninstall keras -y
# !pip uninstall keras-nightly -y
# !pip uninstall keras-Preprocessing -y
# !pip uninstall keras-vis -y
# !pip uninstall tensorflow -y
# !pip install tensorflow==2.3.0
# !pip install keras==2.4

# NLP 처리할 때 Konlpy 모듈 사용 (이하의 순서를 반드시 지켜야한다.)
# 1. JAVA 설치 후 환경변수 등록
# 2. 파이썬 버전 확인 후 Jpype 모듈 설치 (1.1.2)
#    https://www.lfd.uci.edu/~gohlke/pythonlibs/#jpype
# 3. tweepy 3.7.0 ~ 3.10.0 사이의 버전으로 설치
# 4. konlpy 설치

# https://maruzzing.github.io/study/nodejs/node.js%EC%97%90%EC%84%9C-python-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0/

import re
import sys
import json
from konlpy.tag import Okt
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

# 디버그를 위해 JS거치지 않고 바로 실행하기 위한 open
# with open('NLP_DATA/myConv.json', 'r', encoding='UTF-8') as fp:
#     conv = json.load(fp)

with open('NLP_DATA/token.json', 'r', encoding='UTF-8') as fp:
    token = json.load(fp)

tokenizer = Tokenizer(num_words=10000)
tokenizer.fit_on_texts(token)

okt = Okt() # Okt 모듈을 사용하기 위한 처리

with open('ML\stopWords\stopwords.word.txt', 'r', encoding='UTF-8') as fp:
    stopwords_Lib = fp.readlines()

for ct in range(len(stopwords_Lib)):
    stopwords_Lib[ct] = stopwords_Lib[ct].rstrip('\n')

stopwords = stopwords_Lib + ['도', '게', '만', '께', '는', '수', '은', '거', '고', '이니', '런가', '엔', '서', '히', '테']

def sentiment_predict(rootword, i):
    rootword = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣 ]','', rootword)
    rootword = okt.morphs(rootword, stem=True) # 토큰화
    nsWord = []
    for word in rootword:
        if not word in stopwords:
            nsWord.append(word)
    encoded = tokenizer.texts_to_sequences([nsWord]) # 정수 인코딩
    pad_new = pad_sequences(encoded, maxlen = 15) # 패딩
    res[i].append(pad_new.tolist())

conv = json.loads(sys.argv[1])['conv']
userConv = conv["userConv"]

res = {} # Return DICT
index = [] # 20XX.XX userConv의 년월을 가리키는 Key 값의 인덱스

for uc in userConv:
    index.append(uc)
    res[uc] = []

for i in index: # userConv의 년월을 순회
    for d in userConv[i]: # 날짜를 순회
        sentiment_predict(userConv[i][d], i)

print(json.dumps(res))