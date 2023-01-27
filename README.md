##svelte 설치 실행
npm create vite@latest frontend -- --template svelte
cd frontend
npm install
jsconfig.json  "checkJs": false  # 자바스크립트 타입 체크 설정 끄기
 npm run dev


##alembic 설치
pip install alembic
초기화  alembic init migrations
설정  alembic.ini sqlalchemy.url = sqlite:///./myapi.db
      migrations/env.py import models  target_metadata=models.Base.metadata
리비전파일 생성 alembic revision --autogenerate
리비전파일 실행 alembic upgrade head


##svelte 라우터
npm install svelte-spa-router
routes/Home.svelte 작성
src/lib/Counter.svelte 삭제 lib/ap.js 작성 fetch 함수 같이 사용


##.env
frontend/.env VITE_SERVER_URL = http://192.168.0.43:7443


##답변 등록 API
api명: 답변등록
url: /api/answer/create/{question_id}
요청방법:  post
설명:  질문(question_id)에 대한 답변은 등록한다.


##부트스트랩 설치
npm install bootstrap
frontend/src/main.js 
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min.js'


##질문 등록 API 명세
API명: 질문 등록
URL: /api/question/create
요청방법: post

##질문 등록 API 입력항목
-subject 등록할 질문의 제목
-content 등록할 질문의 내용

##질문 등록 API 출력 항목
없음


##질문데이터 생성

python 셀

from database import SessionLocal
from models import Question
from datetiem import datetime

db = SessionLocal()
for i in range(300):
      q = Question(subject="테스트입니다:[%03d]"%i, content='내용무', create_data=datetime.now())
      db.add(q)
db.commit()


##스토어 변수 생성하기
frontend/src/lib/store.js
import { writable } from 'svelte/store'
export const page = writable(0) # 초기값 0
이전 페이지가 없으면 비활성   {page <= && 'disable'}
이전 페이지 번호              page - 1
다음 페이지가 없으면 비활성   {page >= total_page - 1 && 'disable'}
다음 페이지 번호              page +1
페이지 리스트 루프            {#each Array(total_page) as _, loop_page}
현재 페이지와 같으면 활성화   {loop_page === page && 'active}


##회원 가입


회원 모델
username    사용자이름(id)
password    비밀번호
email       이메일

모델 작성후 alembic revision --autogenerate alembic upgrade head

API
API명:      회원가입
URL:        /api/user/create
요청방법:   post
설명:       회원등록을 한다

회원가입 API 입력 항목
username, password1(비밀번호) password2(비밀번호확인) email

회원 가입 API 출력 항목
없음


#로그인 API

##로그인 API 명세
API명       로그인
URL         /api/user/login
요청방법    post
설명        로그인을 한다.


로그인 스키마

로그인 crud

로그인 라우터

로그인 API 테스트


#로그인 화면 만들기

로그인 라우터 등록하기

로그인 화면 작성하기

fastapi 함수 작성하기
http request 헤더 Content-type 을 application/json -> application/x-www-form-urlencoded 로 변환
qs패키지 설치

엑세스 토큰과 로그인 사용자명 저장하기

내비게이션 바에 로그인 여부 표시하기

로그아웃