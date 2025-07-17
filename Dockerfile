FROM python:3.11-slim

# Install system dependencies for sentencepiece and other C++ extensions
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libgoogle-perftools-dev \
    && apt-get clean

# Set work directory
WORKDIR /app

# Copy the app code into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir --prefer-binary -r requirements.txt

ENV PORT=10000

EXPOSE 10000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]
