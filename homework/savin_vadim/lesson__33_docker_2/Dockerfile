FROM jenkins/jenkins:lts-jdk17

USER root

# Установка основных зависимостей
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    wget \
    curl \
    gnupg \
    ca-certificates \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libc6 \
    libcairo2 \
    libcups2 \
    libdbus-1-3 \
    libgdk-pixbuf2.0-0 \
    libnspr4 \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    xdg-utils \
    --no-install-recommends

# Добавление ключа и репозитория Chrome
RUN curl -fsSL https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-chrome.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main" \
    > /etc/apt/sources.list.d/google-chrome.list

# Установка Chrome
RUN apt-get update && apt-get install -y google-chrome-stable
RUN git clone https://github.com/SZTVadim/API_meme.git
RUN pip install --break-system-packages --upgrade --no-cache-dir -r API_meme/requirements.txt
RUN chown -R jenkins:jenkins /API_meme
USER jenkins
RUN echo "" > /API_meme/.env