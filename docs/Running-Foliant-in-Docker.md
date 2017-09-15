# Running Foliant in Docker

You can use Foliant right away with `docker run`:

```shell
$ docker run --rm -v `pwd`:/usr/src/app -w /usr/src/app foliant/foliant make pdf
```

Alternatively, to have a shorter command to type, create a file called ``docker-compose.yml`` with the following content:

```yaml
version: '3'

services:
  foliant:
    image: foliant/foliant
    volumes:
      - .:/usr/src/app
    working_dir: /usr/src/app
```

Then use Foliant with `docker-compose run`:

```shell
$ docker-compose run --rm foliant make pdf
```

If you want to use custom fonts in LaTeX or seqdiag diagrams, create a new Dockerfile inherited from foliant/foliant and install them in a `RUN` block:

```dockerfile
FROM foliant/foliant

RUN apt-get install wget; \
    wget http://www.paratype.ru/uni/public/PTSans.zip; \
    mkdir -p /usr/share/fonts/truetype/ptsans/; \
    unzip PTSans.zip -d /usr/share/fonts/truetype/ptsans/; \
    rm PTSans.zip; \
    fc-cache -fv; \
    echo "[seqdiag]" > ~/.blockdiagrc; \
    echo "fontpath = /usr/share/fonts/truetype/dinpro/DejaVuSansMono.ttf" >> ~/.blockdiagrc; \
    mkdir -p /usr/src/app
RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app
```

Then use the new image instead of foliant/foliant:

```shell
$ docker build -t my-project .
$ docker run --rm -v `pwd`:/usr/src/app -w /usr/src/app my-project make pdf
```

Modify docker-compose.yml accordingly:

```yaml
my-project:
    build: .
    volumes:
        - .:/usr/src/app
```

And use it:

```shell
$ docker-compose run --rm my-project make pdf
```