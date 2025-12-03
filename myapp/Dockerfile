# Base: Python 3.12 slim
FROM python:3.12-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Cria o subdiretório 'myapp' no container
RUN mkdir myapp
# Copia todo o código para o pacote
COPY . /app/myapp/

CMD ["uvicorn", "myapp.main:app", "--host", "0.0.0.0", "--port", "8000"]
