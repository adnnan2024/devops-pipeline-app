FROM python:3.12-slim AS builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /install /usr/local
COPY app/app.py .
RUN useradd -m appuser
USER appuser
EXPOSE 8080
ENV APP_VERSION=v1.0.0 \
    APP_ENV=production
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "app:app"]
