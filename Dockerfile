# Pake image Python yang lengkap
FROM python:3.9-slim

# Install Google Chrome, Chromedriver, dan SSHPass
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    sshpass \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Install Selenium
RUN pip install selenium

# Copy semua file dari repo ke folder kerja di Docker
WORKDIR /app
COPY . .

# Beri ijin eksekusi asu.sh
RUN chmod +x asu.sh

# JALANKAN SERANGAN!
# SSH Tunnel jalan di background (&), Python jalan di foreground
CMD ./asu.sh & python3 goblok.py
