# scraper.quiz01.BOT (python)

![Tests](https://github.com/moisesjurad0/quiz01-scrapper.py.selenium/actions/workflows/main-pipeline.yml/badge.svg)

Python proyect designed to interact with and scrap data out of a specific quizzes web site.
Build to be deployed on docker :thumbsup::whale:

- scraper.quiz01.BOT-API
- scraper.quiz01.BOT-CLI

## Python script is builded with

- [Playwright](https://playwright.dev/python/)
- [Selenium](https://www.selenium.dev/)
- Beautiful Soup (bs4) => [get it](https://pypi.org/project/beautifulsoup4/), [read the docs](https://beautiful-soup-4.readthedocs.io/en/latest/).
- Requests (Py) => [get it](https://pypi.org/project/requests/), [read the docs](https://requests.readthedocs.io/en/latest/).
- Swagger (python-client-generated)
- FastAPI (Run Interface 1)
- Typer  (Run Interface 2)

## It interacts with its own Serverless API on AWS

- AWS API => <https://github.com/moisesJurad0/quiz01-scrapper.aws.serverless>
  - [AWS SAM](https://docs.aws.amazon.com/serverless-application-model/)
  - [AWS Lambda](https://docs.aws.amazon.com/lambda/)
  - [AWS Dynammo](https://docs.aws.amazon.com/dynamodb/)  
  - [AWS API Gateway](https://docs.aws.amazon.com/apigateway/)
  - [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

## Docker Image

This image is compatible with dotenv files.

Docker Image available on

1. Docker Image - Docker Hub
    1. <https://hub.docker.com/repository/docker/squartle/scraper.quiz01.bot-api/general>

        ```sh
        docker pull squartle/scraper.quiz01.bot-api:latest
        ```

    1. <https://hub.docker.com/repository/docker/squartle/scrapper-1/general>

        ```sh
        docker pull squartle/scrapper-1:latest
        ```

1. Docker Image - GitHub Packages

    1. <https://github.com/moisesjurad0/quiz01-scrapper.py.selenium/pkgs/container/scrapper-1>

        ```sh
        docker pull ghcr.io/moisesjurad0/scrapper-1:latest
        ```

### Docker Image - Dependencies

Playwrigth

- [playwright/python:v1.34.0-jammy](https://mcr.microsoft.com/en-us/product/playwright/python/about)

Selenium

- [3.11-alpine](https://hub.docker.com/layers/library/python/3.11-alpine/images/sha256-219923ca7ebe7aa6cabdd241c8a42fcd72a7ac5b5ad55151dec9bd11bc04c99a?context=explore)
- [chromium](https://pkgs.alpinelinux.org/package/edge/community/x86_64/chromium)
- [chromium-chromedriver](https://pkgs.alpinelinux.org/package/edge/community/x86_64/chromium-chromedriver)

### Docker Image - Run

To run the Image follow this steps

```sh
# build the image
docker build -t <pick-a-name-for-image> .

# run the image
# --env-file => pass a file with environmental variables needed in the config.ini file
docker run -dt --env-file .env --name <pick-a-name-for-container> <pick-the-image-you-build-in-previous-step>

# get inside the container and execute as you need 
docker exec -it <pick-the-container-you-build-in-previous-step> sh
```

Or use compose

```docker
# on the proyect path
docker compose up

# also can rebuild it before running up
docker-compose up --build

# detached mode
docker-compose up --build -d
```

### Docker Build

```sh
# docker tag my-image:original my-image:new-tag
docker tag squartle/scraper.quiz01.bot-api:latest squartle/scraper.quiz01.bot-api:selenium
docker build -t squartle/scraper.quiz01.bot-api:playwright .
docker tag squartle/scraper.quiz01.bot-api:playwright squartle/scraper.quiz01.bot-api:latest

# run
docker run --env-file .env -p 80:80  squartle/scraper.quiz01.bot-api
```
