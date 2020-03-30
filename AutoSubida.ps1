docker-compose build
docker tag examendocker fjimenezjob/examendocker
docker push  fjimenezjob/examendocker
heroku login
heroku create examendocker
heroku container:login 
heroku container:push web --app examendocker
heroku container:release web --app examendocker
exit