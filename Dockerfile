# 1. 공식 Python 이미지를 기반으로 설정
FROM python:3.9-slim

# 2. 작업 디렉토리를 설정합니다
WORKDIR /app

# 3. 현재 디렉토리의 모든 파일을 컨테이너의 /app 디렉토리로 복사합니다
COPY . /app

# 4. 필요한 Python 패키지를 설치합니다
RUN pip install --no-cache-dir -r requirements.txt

# 5. 컨테이너에서 사용할 포트를 지정합니다
EXPOSE 8501

# 6. Streamlit 애플리케이션을 실행합니다
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]

