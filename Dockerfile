# We're using Alpine Edge
FROM alpine:edge

#
# We have to uncomment Community repo for some packages
#
RUN sed -e 's;^#http\(.*\)/edge/community;http\1/edge/community;g' -i /etc/apk/repositories

# Installing Core Components
RUN apk add --no-cache --update \
    git \
    dash \
    libffi-dev \
    openssl-dev \
    bzip2-dev \
    zlib-dev \
    readline-dev \
    sqlite-dev \
    build-base \
    bash \
    python3 \ 
    py-pillow \
    py-requests \
    libpq \
    curl \
    sudo \
    neofetch \
    musl \
    py-tz \
    py3-aiohttp \
    py-six \
    py-click \
    redis \
    libxslt-dev \
    libxml2 \
    libxml2-dev \
    py-pip \
    linux-headers \
    jpeg-dev \
    gcc \
    g++ \
    python-dev \
    python3-dev \
    sqlite \
    ffmpeg \
    figlet \
    libwebp-dev \
    openssl \
    pv \
    jq \
    wget \
    chromium \
    chromium-chromedriver

RUN python3 -m ensurepip \
    && pip3 install --upgrade pip setuptools \
    && rm -r /usr/lib/python*/ensurepip && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

#
# Clone staging by default
#
RUN git clone -b staging https://github.com/PainKiller3/Telegram-UserBot.git /root/userbot

#
# !!! NOT FOR PRODUCTION !!!
# Copy Userbot components from Local
#
# COPY . /home/userbot/userbot

#
# Make binary folder and include in PATH
#
RUN mkdir /root/userbot/bin
ENV PATH="/root/userbot/bin:$PATH"
WORKDIR /root/userbot/

#
# Copies session and config(if it exists)
#
COPY ./sample_config.env ./userbot.session* ./config.env* /root/userbot/

#
# Install dependencies
#
RUN pip3 install -r requirements.txt

#
# Finalization
#
RUN curl -s https://raw.githubusercontent.com/yshalsager/megadown/master/megadown -o /root/userbot/bin/megadown && sudo chmod a+x /root/userbot/bin/megadown
RUN curl -s https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py -o /root/userbot/bin/cmrudl && sudo chmod a+x /root/userbot/bin/cmrudl
CMD ["bash","init/start.sh"]
