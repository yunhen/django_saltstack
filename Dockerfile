FROM aexea/py2-django-base
MAINTAINER Aexea Carpentry

USER root

RUN apt-get update && apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:saltstack/salt
RUN apt-get update
RUN apt-get install -y salt-master python-dateutil python-pip libgit2-dev libffi-dev salt-cloud redis-server python-git supervisor

RUN easy_install -U pip
RUN pip install python-simple-hipchat apache-libcloud boto dnspython cli53 redis raven

ADD docker_files/supervisor.conf /etc/supervisor/conf.d/supervisor.conf

VOLUME ["/etc/salt/pki", "/var/cache/salt", "/var/log/salt", "/etc/salt/master.d", "/srv/salt"]

EXPOSE 4505 4506 8000

CMD ["supervisord", "-n"]
