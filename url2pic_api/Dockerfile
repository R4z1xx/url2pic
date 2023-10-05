FROM python:3.8-slim

ENV CHROME_DRIVER_VERSION 117.0.5938.92
ENV CHROME_BIN /usr/bin/google-chrome

RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    fonts-liberation \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libatspi2.0-0 \
    libcairo2 \
    libcups2 \
    libcurl3-gnutls \
    libgbm1 \
    libgtk-3-0 \
    libpango-1.0-0 \
    libu2f-udev \
    libvulkan1 \
    libxdamage1 \
    libxkbcommon0 \
    xdg-utils \
    xvfb \
    libasound2 \
    libnspr4 \
    libnss3 \
    && apt-get clean

RUN wget -q https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_${CHROME_DRIVER_VERSION}-1_amd64.deb && \
    dpkg -i google-chrome-stable_${CHROME_DRIVER_VERSION}-1_amd64.deb && \
    apt-get -y --no-install-recommends install && \
    rm google-chrome-stable_${CHROME_DRIVER_VERSION}-1_amd64.deb

RUN wget -q https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/${CHROME_DRIVER_VERSION}/linux64/chromedriver-linux64.zip && \
    unzip chromedriver-linux64.zip && \
    chmod +x chromedriver-linux64/chromedriver && \
    mv chromedriver-linux64/chromedriver /usr/local/bin && \
    rm -r chromedriver-linux64 chromedriver-linux64.zip

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

COPY . /app/

CMD ["python", "app.py"]