FROM alpine:3.10

LABEL maintainer="Xijun Dai <daixijun1990@gmail.com>"

ARG VERSION

RUN apk --no-cache add \
    sudo \
    python3 \
    openssl \
    ca-certificates \
    sshpass \
    openssh-client \
    rsync && \
    apk --no-cache add --virtual build-dependencies \
    libffi-dev \
    openssl-dev \
    python3-dev \
    build-base && \
    pip3 install --upgrade cffi mitogen && \
    pip3 install ansible==${VERSION} && \
    # pip install --upgrade pywinrm && \
    apk del build-dependencies && \
    rm -rf /root/.cache/pip \
    rm -rf /var/cache/apk/*

RUN mkdir -p /etc/ansible && \
    echo 'localhost' > /etc/ansible/hosts
COPY ansible.cfg /etc/ansible/ansible.cfg

CMD [ "ansible-playbook", "--version" ]
