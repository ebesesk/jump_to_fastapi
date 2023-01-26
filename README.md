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