# ai-chatbot-for-zin

사내 규정 PDF를 기반으로 답변하는 챗봇입니다.

## 1. 설치

```bash
pip install -r requirements.txt
```

## 2. API 키 설정

`backend/.env.example` 파일을 복사해서 `backend/.env` 파일을 만든 뒤, API 키만 입력하면 됩니다.

```env
GROQ_API_KEY=여기에_본인_API_키
```

## 3. 실행

프로젝트 루트에서 아래 명령으로 백엔드를 실행합니다.

```bash
uvicorn backend.main:app --reload
```

프론트는 `frontend/index.html`을 브라우저에서 열면 됩니다.

## 참고

- 규정 PDF는 `backend/docs/`에 저장됩니다.
- 업로드/삭제 후에는 벡터DB가 자동으로 다시 생성됩니다.
- API 키가 없으면 서버 실행 시 바로 오류를 내도록 되어 있습니다.
