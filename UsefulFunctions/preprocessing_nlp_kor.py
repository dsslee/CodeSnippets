import re
import kss
from pykospacing import spacing
from hanspell import spell_checker
from soynlp.normalizer import *
from khaiii import KhaiiiApi
api = KhaiiiApi()


'''
[Content]
 - 가장 기초적인 전처리
 - html tag 제거
 - 숫자 제거
 - Lowercasing
 - "@%*=()/+ 와 같은 punctuation 제거
* Spell check
 - 사전 기반의 오탈자 교정
 - 줄임말 원형 복원 (e.g. I'm not happy -> I am not happy)
* Part-of-Speech
 - 형태소 분석
 - Noun, Adjective, Verb, Adverb만 학습에 사용
* Stemming
 - 형태소 분석 이후 동사 원형 복원
* Stopwords
 - 불용어 제거
* Negation
 - [논문](https://dl.acm.org/doi/pdf/10.5555/2392701.2392703)
 - 부정 표현에 대한 단순화 (e.g. I'm not happy -> I'm sad)
 - 한국어에서의 적용이 어려워, 추후 추가할 예정
'''

# ===== BASIC PREPROCESSING =====
#-- 한국어 위키 데이터 load
data = open('/content/wiki_20190620.txt', 'r', encoding='utf-8')
lines = data.readlines()

for i in range(0, 10):
    print(lines[i])

#-- `sentence_tokenized_text`에 문장 단위로 분리된 corpus가 저장
sentence_tokenized_text = []
for i, line in enumerate(lines):
    if i > 100:     # 전체 wikipedia 문서는 사이즈가 크므로, 일부만 테스트.
        break
    line = line.strip()
    for sent in kss.split_sentences(line):
        sentence_tokenized_text.append(sent.strip())

punct = "/-'?!.,#$%\'()*+-/:;<=>@[\\]^_`{|}~" + '""“”’' + '∞θ÷α•à−β∅³π‘₹´°£€\×™√²—–&'

punct_mapping = {"‘": "'", "₹": "e", "´": "'", "°": "", "€": "e", "™": "tm", "√": " sqrt ", "×": "x", "²": "2", "—": "-", "–": "-", "’": "'", "_": "-", "`": "'", '“': '"', '”': '"', '“': '"', "£": "e", '∞': 'infinity', 'θ': 'theta', '÷': '/', 'α': 'alpha', '•': '.', 'à': 'a', '−': '-', 'β': 'beta', '∅': '', '³': '3', 'π': 'pi', }

def clean_punc(text, punct, mapping):
    for p in mapping:
        text = text.replace(p, mapping[p])
    
    for p in punct:
        text = text.replace(p, f' {p} ')
    
    specials = {'\u200b': ' ', '…': ' ... ', '\ufeff': '', 'करना': '', 'है': ''}
    for s in specials:
        text = text.replace(s, specials[s])
    
    return text.strip()

cleaned_corpus = []
for sent in sentence_tokenized_text:
    cleaned_corpus.append(clean_punc(sent, punct, punct_mapping))

for i in range(0, 10):
    print(cleaned_corpus[i])


def clean_text(texts):
    corpus = []
    for i in range(0, len(texts)):
        review = re.sub(r'[@%\\*=()/~#&\+á?\xc3\xa1\-\|\.\:\;\!\-\,\_\~\$\'\"]', '',str(texts[i])) #remove punctuation
        review = re.sub(r'\d+','', str(texts[i]))# remove number
        review = review.lower() #lower case
        review = re.sub(r'\s+', ' ', review) #remove extra space
        review = re.sub(r'<[^>]+>','',review) #remove Html tags
        review = re.sub(r'\s+', ' ', review) #remove spaces
        review = re.sub(r"^\s+", '', review) #remove space from start
        review = re.sub(r'\s+$', '', review) #remove space from the end
        corpus.append(review)
    return corpus

basic_preprocessed_corpus = clean_text(cleaned_corpus)

for i in range(0, 10):
    print(basic_preprocessed_corpus[i])
    

# ===== SPELL CHECK =====
spacing("김형호영화시장분석가는'1987'의네이버영화정보네티즌10점평에서언급된단어들을지난해12월27일부터올해1월10일까지통계프로그램R과KoNLP패키지로텍스트마이닝하여분석했다.")
 
sent = "대체 왜 않돼는지 설명을 해바"
spelled_sent = spell_checker.check(sent)
checked_sent = spelled_sent.checked
print(checked_sent)


print(repeat_normalize('와하하하하하하하하하핫', num_repeats=2))

lownword_map = {}
lownword_data = open('/content/confused_loanwords.txt', 'r', encoding='utf-8')

lines = lownword_data.readlines()

for line in lines:
    line = line.strip()
    miss_spell = line.split('\t')[0]
    ori_word = line.split('\t')[1]
    lownword_map[miss_spell] = ori_word

def spell_check_text(texts):
    corpus = []
    for sent in texts:
        spaced_text = spacing(sent)
        spelled_sent = spell_checker.check(sent)
        checked_sent = spelled_sent.checked
        normalized_sent = repeat_normalize(checked_sent)
        for lownword in lownword_map:
            normalized_sent = normalized_sent.replace(lownword, lownword_map[lownword])
        corpus.append(normalized_sent)
    return corpus

spell_preprocessed_corpus = spell_check_text(basic_preprocessed_corpus)


# ===== Part-of-Speech =====
test_sents = ["나도 모르게 사버렸다.", "행복해야해!", "내가 안 그랬어!", "나는 사지 않았어.", "하나도 안 기쁘다.", "상관하지마", "그것 좀 가져와"]

for sent in test_sents:
    for word in api.analyze(sent):
        for morph in word.morphs:
            print(morph.lex + '/' + morph.tag)
    print('\n')

significant_tags = ['NNG', 'NNP', 'NNB', 'VV', 'VA', 'VX', 'MAG', 'MAJ', 'XSV', 'XSA']

def pos_text(texts):
    corpus = []
    for sent in texts:
        pos_tagged = ''
        for word in api.analyze(sent):
            for morph in word.morphs:
                if morph.tag in significant_tags:
                    pos_tagged += morph.lex + '/' + morph.tag + ' '
        corpus.append(pos_tagged.strip())
    return corpus


pos_tagged_corpus = pos_text(spell_preprocessed_corpus)

for i in range(0, 30):
    print(pos_tagged_corpus[i])
    

# ===== STEMMING =====
#-- 규칙
# 1. NNG|NNP|NNB + XSV|XSA --> NNG|NNP|NNB + XSV|XSA + 다
# 2. NNG|NNP|NNB + XSA + VX --> NNG|NNP + XSA + 다
# 3. VV --> VV + 다
# 4. VX --> VX + 다

p1 = re.compile('[가-힣A-Za-z0-9]+/NN. [가-힣A-Za-z0-9]+/XS.')
p2 = re.compile('[가-힣A-Za-z0-9]+/NN. [가-힣A-Za-z0-9]+/XSA [가-힣A-Za-z0-9]+/VX')
p3 = re.compile('[가-힣A-Za-z0-9]+/VV')
p4 = re.compile('[가-힣A-Za-z0-9]+/VX')

def stemming_text(text):
    corpus = []
    for sent in text:
        ori_sent = sent
        mached_terms = re.findall(p1, ori_sent)
        for terms in mached_terms:
            ori_terms = terms
            modi_terms = ''
            for term in terms.split(' '):
                lemma = term.split('/')[0]
                tag = term.split('/')[-1]
                modi_terms += lemma
            modi_terms += '다/VV'
            ori_sent = ori_sent.replace(ori_terms, modi_terms)
        
        mached_terms = re.findall(p2, ori_sent)
        for terms in mached_terms:
            ori_terms = terms
            modi_terms = ''
            for term in terms.split(' '):
                lemma = term.split('/')[0]
                tag = term.split('/')[-1]
                if tag != 'VX':
                    modi_terms += lemma
            modi_terms += '다/VV'
            ori_sent = ori_sent.replace(ori_terms, modi_terms)

        mached_terms = re.findall(p3, ori_sent)
        for terms in mached_terms:
            ori_terms = terms
            modi_terms = ''
            for term in terms.split(' '):
                lemma = term.split('/')[0]
                tag = term.split('/')[-1]
                modi_terms += lemma
            if '다' != modi_terms[-1]:
                modi_terms += '다'
            modi_terms += '/VV'
            ori_sent = ori_sent.replace(ori_terms, modi_terms)

        mached_terms = re.findall(p4, ori_sent)
        for terms in mached_terms:
            ori_terms = terms
            modi_terms = ''
            for term in terms.split(' '):
                lemma = term.split('/')[0]
                tag = term.split('/')[-1]
                modi_terms += lemma
            if '다' != modi_terms[-1]:
                modi_terms += '다'
            modi_terms += '/VV'
            ori_sent = ori_sent.replace(ori_terms, modi_terms)
        corpus.append(ori_sent)
    return corpus

stemming_corpus = stemming_text(pos_tagged_corpus)

for i in range(0, 30):
    print(stemming_corpus[i])
    
    
# ===== STOPWORDS =====
stopwords = ['데/NNB', '좀/MAG', '수/NNB', '등/NNB']

def remove_stopword_text(text):
    corpus = []
    for sent in text:
        modi_sent = []
        for word in sent.split(' '):
            if word not in stopwords:
                modi_sent.append(word)
        corpus.append(' '.join(modi_sent))
    return corpus

removed_stopword_corpus = remove_stopword_text(stemming_corpus)
for i in range(0, 30):
    print(removed_stopword_corpus[i])