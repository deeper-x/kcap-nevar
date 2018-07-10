# Kcap Nevar - version 0.0.6

> Sign up and vote for pizza. Become one of the top ten pizza lovers!

## Description and features list
User can signup, login and tell how much he loves pizza by clicking the "I love pizza" button

* When vote is registered, barchart is updated showing real time data. 
* Chart is updated also at regular intervals. 
* As _anonymous_ user, you can view the top-ten chart. If you want to vote, you can sign up, log in and express your vote.
* As a logged in user, you can vote clicking on the "I love pizza" button.
* Bar chart shows: in Y number of votes, in X voters.

In home page, on the top menu bar:
1. If logged in, user will have VOTE and SIGN OUT links 
2. If not logged in, user will have SIGN IN, RESULTS and SIGN UP links



## Deploy (with Docker) on Linux/OSX
Preliminary actions:
```sh
$ cd <project_root_dir>
$ export PYTHONPATH=${PYTHONPATH}:$( pwd )
```

Run migration on web services:  
```sh
$ # remember: una tantum action 
$ sudo docker-compose run web python3 manage.py migrate
```

Set-up ended, now build, (re)create, start services and attach to containers:
```sh
$ # run services with compose
$ sudo docker-compose up
```

Output should be very similar to:
```sh
db_1   | 2018-07-02 17:44:54.082 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
db_1   | 2018-07-02 17:44:54.082 UTC [1] LOG:  listening on IPv6 address "::", port 5432
db_1   | 2018-07-02 17:44:54.143 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
db_1   | 2018-07-02 17:44:54.254 UTC [20] LOG:  database system was shut down at 2018-07-02 17:37:29 UTC
db_1   | 2018-07-02 17:44:54.339 UTC [1] LOG:  database system is ready to accept connections
web_1  | Performing system checks...
web_1  | 
web_1  | System check identified no issues (0 silenced).
web_1  | July 02, 2018 - 17:48:04
web_1  | Django version 2.0, using settings 'pizza_lovers.settings'
web_1  | Starting development server at http://0.0.0.0:8000/
web_1  | Quit the server with CONTROL-C.
```

Docker is up, test it:
```sh
$ curl -I http://127.0.0.1:8000/auth_voters/login/
```

Status code should be 200. 
```sh
HTTP/1.1 200 OK
Date: Mon, 02 Jul 2018 17:50:39 GMT
Server: WSGIServer/0.2 CPython/3.6.6
Content-Type: text/html; charset=utf-8
Expires: Mon, 02 Jul 2018 17:50:39 GMT
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
```

Services are up and running. Open browser:
```sh
http://127.0.0.1:8000/auth_voters/login/
```

## Unit test
```sh
$ sudo docker-compose run web python3 manage.py test -k
```

Result should be something like that:
```sh
Starting pizza_lovers_db_1 ... done
Using existing test database for alias 'default'...
System check identified no issues (0 silenced).
.....
----------------------------------------------------------------------
Ran 5 tests in 1.330s

OK
Preserving test database for alias 'default'...
```

## Running on remote server
If you prefer remote instance, just log in via ssh and run dev server 

```sh
# ssh on remote server 
$ cd projects/kcap-nevar/pizza_lovers
$ export PYTHONPATH=$(pwd)
$ # activate shell o run pipenv directly
$ pipenv shell
$ pipenv run python3 manage.py runserver 0.0.0.0:8001
```
Now open your browser:

```sh
http://94.177.223.143:8001/auth_voters/login/
```


## Requirements 
* Docker (+ Compose)

##  Testing environment
* Docker version 18.03.1-ce, build 9ee9f40
* docker-compose version 1.21.2, build a133471
* OS: Ubuntu 16.04.3 LTS - Linux PC-dev 4.4.0-87-generic #110-Ubuntu SMP Tue Jul 18 12:55:35 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
* django 2.0
* PostgreSQL 9.5.10 on x86_64-pc-linux-gnu, compiled by gcc (Ubuntu 5.4.0-6ubuntu1~16.04.4) 5.4.0 20160609, 64-bit
* psycopg2 '2.7.5 (dt dec pq3 ext lo64)'
* Google chrome Version 67.0.3396.99 (Official Build) (64-bit)


## Python versions/details
* python 3.5, 3.6 (+ pipenv)

## Release History
* 0.0.6
    * cache file update optimization
* 0.0.5
    * data caching 
* 0.0.4
    * updated pizza_notify 
* 0.0.3
    * updated README
* 0.0.2
    * unittest on auth system and vote management
* 0.0.1
    * express love for pizza: log in and vote

## Author

Alberto de Prezzo – [@deep_erx](https://twitter.com/deep_erx) – albertodeprezzo@gmail.com

[https://gitlab.com/deep_erx/kcap-nevar](https://gitlab.com/deep_erx/)

