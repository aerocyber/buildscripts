FROM ubuntu:noble --platform linux/arm64 AS scratch

COPY sitemarker /

FROM 
RUN apt update; \
	apt upgrade -y;\
	apt install git curl wget -y

RUN git clone https://github.com/flutter/flutter.git /flutter; \
	export PATH="$PATH:/flutter/bin"; \
	exec $SHELL

RUN flutter config --no-analytics; dart --no-analytics

FROM scratch AS sitemarkerBuilder
RUN cd /sitemarker; \
	rm -fr build/; \
	flutter pub get; \
	python3 ./build-linux-release.py

