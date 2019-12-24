FROM alpine:3.10

LABEL MAINTAINER="Xijun Dai <daixijun1990@gmail.com>"

ARG VERSION
ARG KUSTOMIZE_VERSION=v3.5.3

RUN apk update \
    && apk add --no-cache ca-certificates curl \
    # kubectl
    && curl --silent -L https://storage.googleapis.com/kubernetes-release/release/${VERSION}/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl \
    && chmod +x /usr/local/bin/kubectl \
    # kustomize
    && curl --silent -L https://github.com/kubernetes-sigs/kustomize/releases/download/kustomize%2F${KUSTOMIZE_VERSION}/kustomize_${KUSTOMIZE_VERSION}_linux_amd64.tar.gz -o /tmp/kustomize.tar.gz \
    && tar xf /tmp/kustomize.tar.gz -C /usr/local/bin/ \
    && rm -rf /tmp/kustomize.tar.gz \
    && apk del curl \
    && rm -fr /var/cache/apk/* /root/.cache

ENTRYPOINT [ "/usr/local/bin/kubectl" ]
CMD [ "--help" ]
