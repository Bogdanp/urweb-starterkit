FROM bogdanp/urweb:20150214

RUN apt-get update
RUN apt-get install -y libpq-dev gawk python
RUN ln -s /usr/include/postgresql/* /usr/include/
