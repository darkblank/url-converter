# URL-converter

## Docker 이용한 실행
#### database setting
local 환경에 postgresql이 있다면 아래와 같이 DB 생성
```
create database dev_shortener;
create user aiden with encrypted password 'apfhd';
grant all privileges on database dev_shortener to aiden;
```
local 환경에 postgresql 없을 시 postgresql docker image를 활용하여 postgresql 사용하기 위해 postgres image pull
```
$ docker pull postgres
```
다음 명령어로 postgresql 컨테이너 실행
```
$ docker run --rm -it --net=host -e POSTGRES_USER='aiden' -e POSTGRES_DB='dev_shortener' -e POSTGRES_PASSWORD='apfhd' postgres
```
#### project docker image
porject docker image pull 받기
```
$ docker pull darkblank/eb
```
docker image pull이 안될 경우 프로젝트 내 Dockerfile을 사용하여 image 생성
```
$ docker build -t <image_name> .
```
위의 pull 받거나 생성한 image로 컨테이너 실행
```
$ docker run --rm -it --net=host <image_name>
```
