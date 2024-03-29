FROM aexea/django-base-py2
MAINTAINER Aexea Carpentry

USER root

RUN apt-get update && apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:saltstack/salt
RUN apt-get update
RUN apt-get install -y salt-master python-pip libgit2-dev libffi-dev salt-cloud redis-server python-git supervisor python3-pip python3-dev

RUN easy_install -U pip
RUN pip install python-simple-hipchat apache-libcloud boto dnspython cli53 redis raven python-dateutil
RUN pip3 install python-dateutil

ADD docker_files/supervisor.conf /etc/supervisor/conf.d/supervisor.conf

VOLUME ["/etc/salt/pki", "/var/cache/salt", "/var/log/salt", "/etc/salt/master.d", "/srv/salt"]

EXPOSE 4505 4506 8000

CMD ["supervisord", "-n"]
