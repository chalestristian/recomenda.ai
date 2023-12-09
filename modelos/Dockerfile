FROM python:3.9

WORKDIR /app

COPY api.py /app/
COPY requirements.txt /app/
COPY content_based_filtering /app/content_based_filtering/
COPY item_based_collaborative_filtering /app/item_based_collaborative_filtering/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "api.py"]
