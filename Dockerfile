FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Add this line to upgrade pip and reinstall requirements
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

CMD ["python", "app/main.py"]