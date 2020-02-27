FROM ubuntu:18.04
# docker build -t face2data .
# docker run -p 5000:5000 face2data
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn
EXPOSE 5000
COPY . /app
ENTRYPOINT ["gunicorn", "face2data.app:app", "-b", "0.0.0.0:5000"]
