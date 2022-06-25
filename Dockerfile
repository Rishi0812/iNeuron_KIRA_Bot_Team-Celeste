FROM continuumio/anaconda3:4.4.0
COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/
RUN sudo apt-get install portaudio19-dev && pyaudio
RUN pip install -r requirements.txt
CMD python finalfile.py
