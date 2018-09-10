FROM continuumio/miniconda3:4.5.4
MAINTAINER Luis Bronchal "lbcommer@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
# Python packages from conda
RUN conda install -y \
    scikit-learn \
    flask
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]
