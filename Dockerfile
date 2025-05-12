#docker multistage build (throws build tools from first stage, so final container is small and lighweight)
FROM python:3.10-slim-bullseye AS builder

# Set working directory
WORKDIR /app

# Install dependencies into a temporary location
#local install for root user
COPY requirements.txt .

#this removes cache and temp files, making smaller image
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage 2: Final lightweight image
FROM python:3.10-slim-bullseye

WORKDIR /app

# Copy installed packages from builder stage (only user installed ones)
COPY --from=builder /root/.local /root/.local

# Copy application code
COPY ./app ./app
COPY ./model ./model

# Set PATH so Streamlit finds installed packages
ENV PATH=/root/.local/bin:$PATH

# Streamlit runs on port 8501
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
