FROM alpine:3.10

LABEL MAINTAINER="Xijun Dai <daixijun1990@gmail.com>"

ARG VERSION

RUN apk update \
    && apk add --no-cache ca-certificates curl \
    && curl --silent -L https://get.helm.sh/helm-${VERSION}-linux-amd64.tar.gz -o /tmp/helm.tar.gz \
    && tar xf /tmp/helm.tar.gz -C /tmp/ \
    && mv /tmp/linux-amd64/helm /usr/local/bin/helm \
    && chmod +x /usr/local/bin/helm \
    && rm -rf /tmp/linux-amd64 /tmp/helm.tar.gz \
    && apk del curl \
    && rm -fr /var/cache/apk/* /root/.cache

ENTRYPOINT [ "/usr/local/bin/helm" ]
CMD [ "--help" ]
