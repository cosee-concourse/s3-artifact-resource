FROM alpine:3.5

COPY requirements.txt .

RUN mkdir -p /aws && \
    apk -Uuv add groff less python3 && \
    pip3 install -r requirements.txt && \
    rm /var/cache/apk/*

COPY opt /opt