FROM debian:bullseye-slim

LABEL MAINTAINER="Xijun Dai <daixijun1990@gmail.com>"

ARG VERSION
ENV FILENAME=aliyun-cli-linux-amd64.tar.gz

RUN apt-get update \
    && apt-get install -y -qq --no-install-recommends  ca-certificates curl \
    && micro_version=${VERSION##*.} \
    && if [ "${micro_version}" -gt "15" ]; then FILENAME=aliyun-cli-linux-${VERSION##*v}-amd64.tgz; fi  \
    && curl --silent -L https://github.com/aliyun/aliyun-cli/releases/download/${VERSION}/${FILENAME} -o /tmp/aliyun-cli.tgz \
    && tar xf /tmp/aliyun-cli.tgz -C /usr/local/bin/ \
    && rm -rf /tmp/aliyun-cli.tgz \
    && rm -fr /var/cache/apt/*

ENTRYPOINT [ "/usr/local/bin/aliyun" ]
CMD [ "--help" ]
