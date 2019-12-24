FROM debian:buster-slim
LABEL MAINTAINER="Xijun Dai <daixijun1990@gmail.com>"

ARG VERSION
ENV TZ=Asia/Shanghai

RUN apt-get update \
    && apt-get install --no-install-recommends -y ca-certificates curl git unzip \
    && curl -sL https://deb.nodesource.com/setup_12.x | bash - \
    && apt-get install --no-install-recommends -y nodejs \
    && rm -rf /var/cache/apt/* \
    && ln -sf /usr/share/zoneinfo/${TZ} /etc/locatime \
    && echo "${TZ}" > /etc/timezone

RUN curl -sSL https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${VERSION}-linux.zip -o sonar-scanner.zip \
    && unzip sonar-scanner.zip \
    && mv sonar-scanner-${VERSION}-linux  /usr/local/sonar-scanner \
    && rm -r sonar-scanner.zip

ENV SONAR_RUNNER_HOME=/usr/local/sonar-scanner/
ENV PATH=$PATH:${SONAR_RUNNER_HOME}/bin

ENTRYPOINT ["sonar-scanner"]

CMD ["--version"]
