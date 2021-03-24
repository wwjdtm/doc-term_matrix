# doc-term_matrix

- 입력: 한글 문서 집합 (첨부파일: n개)

- 출력: document-term matrix

- 상세 설명 — 아래 파이썬 함수를 순서대로 작성

​

[준비작업] n개의 텍스트 문서 파일들을 폴더명 “docs”에 저장

​

1) 각 파일들에 대한 형태소 분석 함수 text2terms 작성(결과: docs2에 저장)

docs에 있는 각 파일들에 대해 각각 형태소 분석기 index2018.exe를 이용하여 term 추출(text file ->list of terms)하여 그 결과를 1.txt, 2.txt, ..., n.txt로 저장하는 함수 “text2terms” 작성하고 결과 파일 1.txt, ..., n.txt는 폴더명 docs2에 저장

<참고> index2108.exe을 파이썬 코드로 실행할 때

index2018.exe를 실행하려면 hdic 폴더가 현재 폴더에 있어야 함. 코딩작업을 KLT2000의 index2018.exe가 있는 EXE 폴더에서 작업을 하면 됨.

​

2) 형태소 분석 결과(list of terms)를 한 라인으로 재구성 함수 terms2oneLine 작성(결과: docs3에 저장)

docs2의 각 파일들에 대해 각각 “bag of terms” 형태로 재구성(한 라인에 모든 term들을 나열)하여 폴더명 docs3에 저장(파일명은 동일: 1.txt ... n.txt)하는 함수 “terms2oneLine” 작성

​

3) 모든 문서를 corpus 변수에 읽어 들임 --- TfidfVectorizer 사용 준비작업

docs3의 각 파일들을 하나씩 읽어들여 corpus 변수에 n개의 스트링 배열을 구성하는 함수 “files2array” 작성

​

4) Document-term 행렬 구성 함수 buildDocTermMatrix 작성

corpus 변수의 각 문서들에 대해 TfidfVectorizer를 이용하여 document-term matrix를 작성하는 함수 “buildDocTermMatrix” 작성

​

5) 유사도 행렬(similarity matrix) 구성 함수 buildSimilarityMatrix 작성

Document-term 행렬로부터 각 문서쌍에 대한 코사인 유사도를 계산하여 유사도 행렬을 구성하는 함수 “buildSimilarityMatrix” 작성

<참고> 유사도 행렬은 symmertric matrix임 --> sim(i,j) = sim(j,i)이고 sim(i,i)=1

​

6) 유사도 행렬 출력 함수 putSimMatrix 작성 (결과: sim-matrix.txt에 저장)

유사도 행렬을 파일명 sim-matrix.txt에 아래 형식으로 출력하는 함수 “putSimMatrix” 작성.

<출력 포맷> 첫 라인에 (n m)을 출력. 2번째 라인부터 행렬값을 n x m 형태로 유사도값 출력

​

7) 유사도가 가장 높은 상위 n개를 출력하는 함수 “printDocPairs(n)” 작성

<참고> 출력내용: 한 라인에 “i, j, 유사도값” --> i, j는 DocID(문서번호)
