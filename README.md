# ai-chatbot-for-zin

AI Chatbot for Zin

사내 규정 PDF를 기반으로 답변하는 챗봇입니다.

## 아키텍처

```text
[사내 규정 문서 (PDF/Word)]
        |
        v
[Vector DB - ChromaDB / FAISS]
        |
        v
[LLM API] <-> [FastAPI 백엔드]
        |
        v
[웹 프론트엔드]
        |
        v
[사용자 채팅 UI + 자주 묻는 질문 + 규정 문서 + 관리자]
```

## 기술 스택

| 영역 | 기술 |
| --- | --- |
| 언어 | Python |
| 백엔드 | FastAPI |
| 벡터 DB | ChromaDB |
| 문서 파싱 | PyMuPDF |
| 프론트엔드 | HTML, CSS, JavaScript |
| API | 그록 https://console.groq.com/keys |

## 설치

```bash
pip install -r requirements.txt
```

## API 키 설정

`backend/.env.example` 파일을 복사해서 `backend/.env` 파일을 만든 뒤, API 키만 입력하면 됩니다.

```env
GROQ_API_KEY=your_groq_api_key_here
```

## 실행

프로젝트 루트에서 실행합니다.

```bash
uvicorn backend.main:app --reload
```

프론트는 `frontend/index.html`을 브라우저에서 열면 됩니다.

## 참고

- 규정 PDF는 `backend/docs/`에 저장됩니다.
- 업로드/삭제 후에는 벡터DB가 자동으로 다시 생성됩니다.
- API 키가 없으면 서버 실행 시 바로 오류가 발생합니다.

## 화면 샘플

### 1. 메인 페이지
<img width="1162" height="956" alt="메인 페이지" src="https://github.com/user-attachments/assets/fa8e2682-fc76-4188-9c53-ffe308d393c8" />
<img src="https://github.com/user-attachments/assets/a4c9434f-ca5f-44ad-ba50-ed9b3b0cedb1" width="1000"/>

### 2. 자주 묻는 질문
<img width="1154" height="956" alt="자주 묻는 질문" src="https://github.com/user-attachments/assets/b76d49a3-fc3f-4183-b34a-fbe097674f5b" />
<img src="https://github.com/user-attachments/assets/4694a259-1ee3-43cd-ab0a-db37723797ed" width="1000"/>

### 3. 규정 문서 페이지
<img width="1144" height="954" alt="규정 문서 페이지" src="https://github.com/user-attachments/assets/e4751d08-791c-4a24-a7e3-10bdd94fa02b" />
<img src="https://github.com/user-attachments/assets/ee6e3508-9c10-4a41-b2e9-20cacc620a0a" width="1000"/>

### 4. 관리자 페이지
<img width="1129" height="963" alt="관리자 페이지" src="https://github.com/user-attachments/assets/f845c2cf-10a4-4916-9080-a572a352295c" />
<img src="https://github.com/user-attachments/assets/64f19525-27f2-4f82-9b66-b6ef450156d2" width="1000"/>
