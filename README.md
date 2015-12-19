# Ur/Web Starter Kit

A simple Docker setup for playing around w/ [Ur/Web](http://www.impredicative.com/ur/).

## Getting up and running

Assuming you're on OS X:

1. Install the [Docker Toolbox](https://www.docker.com/docker-toolbox)
1. `cd urweb-starterkit`
1. `docker-compose up -d`
1. `docker-compose run postgres createdb -Upostgres -h$(docker-machine ip default) urweb_starterkit`
1. `open http://$(docker-machine ip default):8080/App/main`

You can run `docker-compose logs app` to tail the app compilation and server logs.
