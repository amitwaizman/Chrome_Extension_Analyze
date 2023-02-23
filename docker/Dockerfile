FROM python:3.9.13

WORKDIR /app
RUN apt-get update && apt-get install -y apache2 && apt-get clean && rm -rf /var/lib/apt/lists/* 
RUN apt-get update && \
    apt-get install -y --no-install-recommends p7zip-full && \
    7z -h
RUN pip install joblib
RUN pip install streamlit
RUN pip install Image
RUN pip install -U scikit-learn
RUN pip install obfuscation_detection
RUN pip install nltk
RUN pip install gensim
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash - 
RUN apt-get install -y nodejs
ADD . /app 
EXPOSE 8501
COPY . /app



CMD streamlit run app.py --server.maxUploadSize=1024
