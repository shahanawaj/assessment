FROM python:3.6-alpine
RUN adduser -D john
USER john

WORKDIR /home/webapp


COPY main.py main.py
RUN python3 -m pip install Flask




# run-time configuration
EXPOSE 8080
ENTRYPOINT ["python3" , "main.py"]