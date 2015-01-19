FROM aexea/py2-django-base
MAINTAINER Aexea Carpentry

USER root

RUN apt-get install -y software-properties-common python-git supervisor
RUN add-apt-repository -y ppa:saltstack/salt
RUN apt-get update
RUN apt-get install -y salt-master=2014.7.0+ds-2trusty1

ADD docker_files/supervisor.conf /etc/supervisor/conf.d/supervisor.conf

VOLUME ["/etc/salt/pki", "/var/cache/salt", "/var/log/salt", "/etc/salt/master.d", "/srv/salt"]

EXPOSE 4505 4506 8000

CMD ["supervisord", "-n"]
