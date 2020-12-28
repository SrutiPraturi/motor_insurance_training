FROM python:3.8
WORKDIR /app
COPY data_pipeline.py data_pipeline.py
COPY feature_engg.py feature_engg.py
COPY model_train.py model_train.py
COPY SwedishMotorInsurance.csv SwedishMotorInsurance.csv
COPY git_shell.sh git_shell.sh
RUN pip install --upgrade pip
RUN apt-get update 
RUN apt-get install git
RUN pip install numpy
RUN pip install pandas
RUN pip install sklearn
RUN pip install pickle-mixin
RUN pip install pyyaml
RUN pip install Flask-gunicorn
RUN python ./data_pipeline.py  
RUN python ./feature_engg.py training
RUN python ./model_train.py
RUN sh ./git_shell.sh
CMD ["gunicorn", "app:app"]
