docker-compose build
docker tag sorteofinal fjimenezjob/sorteofinal
docker push  fjimenezjob/sorteofinal
heroku login
heroku create sorteofinal
heroku container:login 
heroku container:push web --app sorteofinal
heroku container:release web --app sorteofinal
exit