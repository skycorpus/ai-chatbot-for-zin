# ai-chatbot-for-zin
AI Chatbot for Zin

# 아키텍처
[사내 규정 문서 (PDF/Word)]
        ↓ (임베딩)
[Vector DB - ChromaDB / FAISS]
        ↓ (검색)
[Claude API] ←→ [FastAPI 백엔드]
        ↓
[Streamlit / React 프론트]
        ↓
[사용자 채팅 UI + 예상 질문 버튼]

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

