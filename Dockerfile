# Usa una imagen base de Python
FROM python:3.12-slim
RUN apk update
RUN apk add git

RUN git clone https://github.com/um-computacion-tm/ajedrez-2024-FedericoPalumbo294

WORKDIR /ajedrez-2024-FedericoPalumbo294

RUN pip install -r requirements.txt

CMD [ "sh", "-c", "coverage run -m unittest && coverage report -m && python -m game.cli " ]
