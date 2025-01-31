FROM python:3.11-slim-buster
WORKDIR /app
COPY requirement.txt requirement.txt
RUN pip install -r requirement.txt
COPY app.py app.py
EXPOSE 3000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:3000", "app:app"]