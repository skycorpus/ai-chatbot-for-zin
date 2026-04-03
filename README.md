# ai-chatbot-for-zin
AI Chatbot for Zin

아키텍처
[사내 규정 문서 (PDF/Word)]
        ↓ 임베딩
[Vector DB - ChromaDB or FAISS]
        ↓ 검색
[Claude API] ←→ [FastAPI 백엔드]
        ↓
[Streamlit or React 프론트]
        ↓
[사용자 채팅 UI + 예상 질문 버튼]

핵심 기술 스택
역할기술이유언어PythonClaude SDK, LangChain 생태계백엔드FastAPI비동기, REST API벡터DBChromaDB로컬 구동, 설치 간단RAG 프레임워크LangChain문서 로딩~검색 파이프라인프론트React or Streamlit채팅 UI + 버튼 제안배포GitHub Actions + DockerCI/CD문서 파싱PyMuPDF, python-docxPDF/Word 지원
<img width="718" height="396" alt="image" src="https://github.com/user-attachments/assets/7225b22f-f0a0-4104-819f-eeba99a6aceb" />
