FROM alpine:3.10

LABEL MAINTAINER="Xijun Dai <daixijun1990@gmail.com>"

ARG VERSION

RUN apk update \
    && apk add --no-cache ca-certificates curl \
    && curl --silent -L https://github.com/tektoncd/cli/releases/download/${VERSION}/tkn_${VERSION##*v}_Linux_x86_64.tar.gz -o /tmp/tkn.tar.gz \
    && tar xf /tmp/tkn.tar.gz -C /usr/local/bin/ \
    && rm -rf  /tmp/tkn.tar.gz \
    && apk del curl \
    && rm -fr /var/cache/apk/*

ENTRYPOINT [ "/usr/local/bin/tkn" ]
CMD [ "--help" ]
