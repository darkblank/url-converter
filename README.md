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
http://localhost:5000에 접속하여 작동 확인
## Docker 없이 실행
1. 로컬 환경에 postgresql이 설치되어 있어야 합니다.
2. python 3.7.1 을 설치합니다.(pyenv같은 가상환경을 사용하면 좋습니다.)
3. requirements 설치
```
$ pip install -r requirements.txt
```
4. 데이터베이스 세팅
```
create database dev_shortener;
create user aiden with encrypted password 'apfhd';
grant all privileges on database dev_shortener to aiden;

# 테스트 DB
create database test_shortener;
grant all privileges on database test_shortener to aiden;
```
5. 환경변수 설정
```
$ export APP_ENV='production'
```
6. DB table 생성
```
# root 폴더 위치에서 실행
$ python create_db.py
```
7. app 실행
```
# root 폴더 위치에서 실행
$ python run.py
```
---
8. Test
```
# 환경변수 변경
$ export APP_ENV='test'
# root 폴더 위치에서 실행
$ python -m pytest tests
```
http://localhost:5000에 접속하여 작동 확인
