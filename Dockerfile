FROM        ubuntu:16.04
MAINTAINER  darkblank1990@gmail.com

RUN         apt-get -y update
RUN         apt-get -y dist-upgrade
RUN         apt-get install -y python-pip git vim

# pyenv Common-build-problems(https://github.com/pyenv/pyenv/wiki/Common-build-problems)
RUN         apt-get install -y make build-essential libssl-dev zlib1g-dev \
            libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
            libncursesw5-dev xz-utils tk-dev postgresql postgresql-contrib libpq-dev

# pyenv
RUN         curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
ENV         PATH /root/.pyenv/bin:$PATH
RUN         pyenv install 3.7.1

# zsh
RUN         apt-get install -y zsh

# oh-my-zsh
RUN         wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true
RUN         chsh -s /usr/bin/zsh

# pyenv settings
RUN         echo 'export PATH="/root/.pyenv/bin:$PATH"' >> ~/.zshrc
RUN         echo 'eval "$(pyenv init -)"' >> ~/.zshrc
RUN         echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc

# pyenv virtualenv
RUN         pyenv virtualenv 3.7.1 url-converter

# pip
ENV         LANG C.UTF-8
COPY        requirements.txt /srv/requirements.txt
RUN         /root/.pyenv/versions/url-converter/bin/pip install -r /srv/requirements.txt

# 파일 복사 및 requirements 설치
COPY        . /srv/app

# pyenv local 설정
WORKDIR     /srv/app
RUN         pyenv local url-converter

# runserver
WORKDIR     /srv/app
ENV APP_ENV='production'
CMD /root/.pyenv/versions/url-converter/bin/python create_db.py && /root/.pyenv/versions/url-converter/bin/python run.py