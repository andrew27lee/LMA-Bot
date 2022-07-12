FROM python:3.8.9
WORKDIR /app
RUN apt-get update -y && apt-get install git-lfs -y && \
    git clone https://github.com/andrew27lee/GPT2-Little-Women.git
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
