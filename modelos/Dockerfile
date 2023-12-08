FROM python:3.9

WORKDIR /app

COPY api.py /app/
COPY requirements.txt /app/
COPY content_based_filtering /app/content_based_filtering/
COPY item_based_collaborative_filtering /app/item_based_collaborative_filtering/


# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando para executar sua aplicação quando o contêiner iniciar
CMD ["python", "api.py"]
