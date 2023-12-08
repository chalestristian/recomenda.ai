FROM python:3.9

WORKDIR /app

# Copie os arquivos do dataset
COPY content_based_filtering/dataset/ratings.csv /app/dataset/
COPY content_based_filtering/dataset/movies.csv /app/dataset/
COPY requirements.txt /app/
COPY content_based_filtering/main/dataset.py /app/
COPY content_based_filtering/validator/hyperparameters.py /app/
COPY content_based_filtering/main/main.py /app/

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando para executar sua aplicação quando o contêiner iniciar
CMD ["python", "main.py"]
