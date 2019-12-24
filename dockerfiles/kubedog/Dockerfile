FROM alpine:3.10

LABEL MAINTAINER="Xijun Dai <daixijun1990@gmail.com>"

ARG VERSION

RUN apk update \
    && apk add --no-cache ca-certificates curl \
    && curl --silent -L https://dl.bintray.com/flant/kubedog/${VERSION}/kubedog-linux-amd64-${VERSION} -o /usr/local/bin/kubedog \
    && chmod +x /usr/local/bin/kubedog \
    && rm -fr /var/cache/apk/* /root/.cache

ENTRYPOINT [ "/usr/local/bin/kubedog" ]
CMD [ "--help" ]
