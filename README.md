# Ur/Web Starter Kit

A simple Docker setup for playing around w/ [http://www.impredicative.com/ur/](Ur/Web).

## Getting up and running

Assuming you're on OS X:

1. Install [http://www.fig.sh/install.html](Fig)
2. Clone this repo and then
3. `cd urweb-starterkit`
4. `fig up -d`
5. `fig run postgres createdb -Upostgres -h192.168.59.103 urweb_starterkit`
6. `open http://192.168.59.103:8080/App/main`
