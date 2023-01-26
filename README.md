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
