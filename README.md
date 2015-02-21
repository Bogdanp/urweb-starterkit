# Ur/Web Starter Kit

A simple Docker setup for playing around w/ [Ur/Web](http://www.impredicative.com/ur/).

## Getting up and running

Assuming you're on OS X:

1. Install [Fig](http://www.fig.sh/install.html)
2. `cd urweb-starterkit`
3. `fig up -d`
4. `fig run postgres createdb -Upostgres -h192.168.59.103 urweb_starterkit`
5. `open http://192.168.59.103:8080/App/main`
