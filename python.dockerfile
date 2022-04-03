FROM python:slim-buster

WORKDIR /usr/src/app
COPY src/python/requirements.txt /usr/src/app/

# See https://towardsdatascience.com/how-to-build-slim-docker-images-fast-ecc246d7f4a7
RUN apt-get update \
&& apt-get install gcc -y \
&& apt install  openssh-server sudo -y \
&& apt-get clean

RUN pip install --no-cache-dir -r requirements.txt

RUN  echo 'root:password' | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config
RUN service ssh start
EXPOSE 22
CMD ["/usr/sbin/sshd","-D"]