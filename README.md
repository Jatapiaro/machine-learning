# Using Spyder with Docker

1. `vi /etc/hosts` and add `127.0.0.1 spydocker-localhost.dev.com`
2. Run docker container and build the image `docker-compose up -d --build`
3. Activate the spyder kernel on the container by running `ssh root@spydocker-localhost.dev.com python -m spyder_kernels.console -f=/usr/src/app/remote-machine.json`
4. End the spyder kernel by doing `ctrl+4`
5. On Spyder, look for `Consoles > Connect to existing Kernel`
6. Fill the details.

    Connection File: Select the file in `src/python/remote-machine.json`
    Check this is a remote kernel via SSH
    Hostname: spydocker-localhost.dev.com
    Port: 22
    Username: root
    Password: password

**Note: Each time you restart the container, you must run the steps 3 and 4.**

