FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

# Comando para rodar python run.py que por sua vez roda o Streamlit
CMD ["python", "run.py"]
