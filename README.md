# quiz01-scrapper (python script)

![Tests](https://github.com/moisesjurad0/quiz01-scrapper.py.selenium/actions/workflows/main-pipeline.yml/badge.svg)

Python proyect designed to interact with and scrap data out of a specific quizzes web site.
Build to be deployed on docker :thumbsup::whale:

## Python script is builded with

- [selenium](https://www.selenium.dev/)
- beautifulsoup4 (bs4) => [get it](https://pypi.org/project/beautifulsoup4/), [read the docs](https://beautiful-soup-4.readthedocs.io/en/latest/).
- requests => [get it](https://pypi.org/project/requests/), [read the docs](https://requests.readthedocs.io/en/latest/).

## It interacts with its own Serverless API on AWS

- AWS API => <https://github.com/moisesJurad0/quiz01-scrapper.aws.serverless>
  - [AWS SAM](https://docs.aws.amazon.com/serverless-application-model/?icmpid=docs_homepage_compute)
  - [AWS Lambda](https://docs.aws.amazon.com/lambda/index.html)
  - [AWS Dynammo](https://docs.aws.amazon.com/dynamodb/index.html)  
  - [BOTO3](https://docs.aws.amazon.com/serverless-application-model/?icmpid=docs_homepage_compute)

## Docker image is builded with

- [python3.9:alpine](https://hub.docker.com/layers/library/python/3.9-alpine3.17/images/sha256-de1fbc63ac86f6a65d160df2bc4f31affd1c3fdbe9ea0f68e1ba85054f8d1c6e?context=explore)
- [chromium](https://pkgs.alpinelinux.org/package/edge/community/x86_64/chromium)
- [chromium-chromedriver](<https://pkgs.alpinelinux.org/package/edge/community/x86_64/chromium-chromedriver>)

### To run the imagen follow this steps

```sh
# build the image
docker build -t <pick-a-name-for-image> .

# run the image
# --env-file => pass a file with environmental variables needed in the config.ini file
docker run -dt --env-file .env --name <pick-a-name-for-container> <pick-the-image-you-build-in-previous-step>

# get inside the container and execute as you need 
docker exec -it <pick-the-container-you-build-in-previous-step> sh
```

### Or use compose

```docker
# on the proyect path
docker compose up
```
