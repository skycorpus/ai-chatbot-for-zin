# ai-chatbot-for-zin
AI Chatbot for Zin

# 아키텍처
```plaintext
[사내 규정 문서 (PDF/Word)]

        ↓ (임베딩)
        
[Vector DB - ChromaDB / FAISS]

        ↓ (검색)
        
[Claude API] ←→ [FastAPI 백엔드]

        ↓
        
[Streamlit / React 프론트]

        ↓
        
[사용자 채팅 UI + 예상 질문 버튼]
```

# 핵심 기술 스택
| 역할        | 기술                      | 이유                                |
| --------- | ----------------------- | --------------------------------- |
| 언어        | Python                  | Claude SDK 및 LangChain 생태계 활용에 적합 |
| 백엔드       | FastAPI                 | 비동기 처리 및 REST API 구축에 최적화         |
| 벡터 DB     | ChromaDB                | 로컬 실행 가능, 설치 및 사용 간편              |
| RAG 프레임워크 | LangChain               | 문서 로딩부터 검색까지 파이프라인 구성             |
| 프론트엔드     | React / Streamlit       | 채팅 UI 및 빠른 프로토타이핑 지원              |
| 배포        | Docker + GitHub Actions | 환경 일관성 및 CI/CD 자동화                |
| 문서 파싱     | PyMuPDF, python-docx    | PDF 및 Word 문서 처리 지원               |

# 화면 샘플

### 1. 메인 페이지
<img width="1162" height="956" alt="진_챗봇_메인페이지" src="https://github.com/user-attachments/assets/fa8e2682-fc76-4188-9c53-ffe308d393c8" />
<img src="https://github.com/user-attachments/assets/a4c9434f-ca5f-44ad-ba50-ed9b3b0cedb1" width="1000"/>

### 2. 자주 묻는 질문
<img width="1154" height="956" alt="진_챗봇_자주묻는질문페이지" src="https://github.com/user-attachments/assets/b76d49a3-fc3f-4183-b34a-fbe097674f5b" />
<img src="https://github.com/user-attachments/assets/4694a259-1ee3-43cd-ab0a-db37723797ed" width="1000"/>

### 3. 규정 문서 페이지
<img width="1144" height="954" alt="진_챗봇_규정문서페이지" src="https://github.com/user-attachments/assets/e4751d08-791c-4a24-a7e3-10bdd94fa02b" />
<img src="https://github.com/user-attachments/assets/ee6e3508-9c10-4a41-b2e9-20cacc620a0a" width="1000"/>

### 4. 관리자 페이지
<img width="1129" height="963" alt="진_챗봇_관리자페이지" src="https://github.com/user-attachments/assets/f845c2cf-10a4-4916-9080-a572a352295c" />
<img src="https://github.com/user-attachments/assets/64f19525-27f2-4f82-9b66-b6ef450156d2" width="1000"/>

