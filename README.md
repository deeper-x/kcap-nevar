# Kcap Nevar - version 0.0.1

> Sign up and vote for pizza. Vote and become one of the top ten pizza lovers. 


## Deploy
 
```sh
$ cd <root_dir>
# first create db structure
$ sudo docker-compose run web python3 manage.py migrate
# run compose
$ sudo docker-compose up
```

## Requirements and features

* A user can signup and login, and tell how much he loves pizza, by clicking the "I love pizza" button
* When vote is registered, barchart is updated showing real time data. 
* Chart is updated also at regular intervals. 
* As _anonymous_ user, you can view the top-ten chart. If you want to vote, you can sign up, log in and express your vote.
* As a logged in user, you can vote clicking on the "I love pizza" button.
* Bar chart shows: in Y number of votes, in X voters.
* In home page, on the top menu bar:
1. If logged in, user will have VOTE and SIGN OUT links 
2. If not logged in, user will have SIGN IN, RESULTS and SIGN UP links


## Release History
* 0.0.1
    * express love for pizza: log in and vote

## Author

Alberto de Prezzo – [@deep_erx](https://twitter.com/deep_erx) – albertodeprezzo@gmail.com

[https://gitlab.com/deep_erx/kcap-nevar](https://gitlab.com/deep_erx/)

