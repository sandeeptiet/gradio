FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy dependency file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code
COPY . .

# Expose port (Gradio typically runs on 7860 by default)
EXPOSE 8012

# Start the Gradio application
CMD ["python", "app.py"]
