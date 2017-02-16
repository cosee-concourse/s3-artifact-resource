FROM alpine:3.5

RUN mkdir -p /aws && \
    apk -Uuv add groff less python3 && \
    pip3 install boto3 semver && \
    rm /var/cache/apk/*

COPY opt /opt