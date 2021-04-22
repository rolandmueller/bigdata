


```bash
python3 -m venv env
```

```bash
source env/bin/activate
```

```bash
touch requirements.txt
mkdir app
touch app/app.py
```

requirements.txt:
```txt
streamlit
pandas
```
Dockerfile:
```dockerfile
FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8501
ENTRYPOINT ["streamlit","run"]
CMD ["app.py"]
```
