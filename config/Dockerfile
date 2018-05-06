FROM centos:7

COPY ./requirements.txt /tmp/

RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm \
    && yum -y install python36u httpd24u python36u-mod_wsgi \
    && yum clean all \
    && mkdir -p /var/www/py36_venv \
    && /usr/bin/python3.6 -m venv /var/www/py36_venv --system-site-packages \
    && source /var/www/py36_venv/bin/activate \
    && /var/www/py36_venv/bin/pip install -r /tmp/requirements.txt

COPY ./000-default.conf /etc/httpd/conf.d/000-default.conf
COPY ./dados.env /data/

EXPOSE 80 443

CMD httpd -D FOREGROUND