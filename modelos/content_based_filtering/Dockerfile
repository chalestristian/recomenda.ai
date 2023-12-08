FROM python:3.9

WORKDIR /app

# Copie os arquivos do dataset
COPY dataset/ratings.csv /app/dataset/
COPY dataset/movies.csv /app/dataset/
COPY requirements.txt /app/
COPY main/dataset.py /app/
COPY validator/hyperparameters.py /app/
COPY main/main.py /app/

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando para executar sua aplicação quando o contêiner iniciar
CMD ["python", "main.py"]
