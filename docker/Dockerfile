# Base on latest CentOS image
#FROM master:4999/centos7-ssh:1.0
FROM python:3.7.4-alpine3.10

MAINTAINER "xialei" <xialei@gcbi.com.cn>

# Define environment variables
ENV TZ "Asia/Shanghai" \
    LC_ALL=en_US.utf-8 \
    LANG=en_US.utf-8 \
    PYTHON_VERSION=3.7.4 \
    DIR_INSTALL=/juhui \
    HOME=/home/juhui

RUN apk add --no-cache bash

RUN pip3 install toml==0.10.0 \
    && pip3 install Click==7.0 \
    && pip3 install Flask==1.0.3 \
    && pip3 install SQLAlchemy==1.3.4 \
    && pip3 install	Flask-Cors==3.0.7 \
    && pip3 install	PyJWT==1.4.2 \
    && pip3 install	flask-restplus==0.12.1 \
    && pip3 install	Flask-SQLAlchemy==2.4.0 \
    && pip3 install	PyMySQL==0.9.3 \
    && pip3 install	requests==2.22.0 \
    && pip3 install	urllib3==1.25.3

RUN apk add --no-cache python3-dev libstdc++ \
    && apk add --no-cache g++ \
    && ln -s /usr/include/locale.h /usr/include/xlocale.h
#    && pip3 install numpy \
#    && pip3 install pandas==0.24.2

RUN apk add --no-cache gcc make libc-dev linux-headers pcre-dev \
    && pip3 install uwsgi==2.0.18


RUN pip install aniso8601==6.0.0 \
    && pip install attrs==19.1.0 \
    && pip install certifi==2019.9.11 \
    && pip install chardet==3.0.4 \
    && pip install Click==7.0 \
    && pip install enum34==1.1.6 \
    && pip install Flask==1.0.2 \
    && pip install Flask-Cors==3.0.7 \
    && pip install Flask-JWT==0.3.2 \
    && pip install flask-restplus==0.12.1 \
    && pip install Flask-SQLAlchemy==2.4.0 \
    && pip install idna==2.8 \
    && pip install inflect==2.1.0 \
    && pip install itsdangerous==1.1.0 \
    && pip install Jinja2==2.10.1 \
    && pip install jsonschema==3.0.1 \
    && pip install MarkupSafe==1.1.1 \
    && pip install Pillow==6.1.0 \
    && pip install PyJWT==1.4.2 \
    && pip install PyMySQL==0.9.3 \
    && pip install pyrsistent==0.15.2 \
    && pip install python-dotenv==0.10.3 \
    && pip install pytz==2019.1 \
    && pip install requests==2.22.0 \
    && pip install six==1.12.0 \
    && pip install sqlacodegen==2.0.1 \
    && pip install SQLAlchemy==1.3.2 \
    && pip install toml==0.10.0 \
    && pip install urllib3==1.25.5 \
    && pip install Werkzeug==0.15.2


RUN echo "LC_ALL=en_US.UTF-8" >> /etc/environment && \
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
    echo "LANG=en_US.UTF-8" > /etc/locale.conf

# Install application to docker
ADD jh-coupon.tar.gz $DIR_INSTALL
RUN mkdir -p $DIR_INSTALL/jh-coupon/logs

RUN groupadd -g 1818 juhui && \
    useradd -g juhui -u 1818 juhui && \
    chown -R juhui:juhui $DIR_INSTALL


USER juhui

WORKDIR $DIR_INSTALL/jh-coupon

ENV HOME=/home/juhui
ENV FLASK_ENV=production
ENV LANGUAGE=en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8


ENTRYPOINT ["uwsgi"]
CMD ["--http","0.0.0.0:6000","--file","/juhui/jh-coupon/manager.py","--callable","app","--logto","/juhui/jh-product/logs/uwsgi-jh-coupon.log"]
