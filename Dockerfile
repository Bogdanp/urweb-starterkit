FROM bogdanp/urweb:20151122

RUN apt-get update
RUN apt-get install -y libpq-dev python
RUN ln -s /usr/include/postgresql/* /usr/include/
