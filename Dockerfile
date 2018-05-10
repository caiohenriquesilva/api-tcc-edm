FROM 978827181454.dkr.ecr.us-east-1.amazonaws.com/qa-ecs-gnr-ms-py:latest
COPY /APP/ /sites/APP
COPY /config/requirements.txt /tmp/
COPY /kdump.out /srv/kdump.out

ARG MSNAME
RUN source /var/www/py36_venv/bin/activate \
    && /var/www/py36_venv/bin/pip install -r /tmp/requirements.txt \
    && mkdir -p /var/log/httpd/APP \
    && sed -i "/WSGIScriptAlias/s/MS-PATH/$MSNAME/" /etc/httpd/conf.d/APP.conf

EXPOSE 80 443
