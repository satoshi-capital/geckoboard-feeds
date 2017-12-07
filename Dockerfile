FROM mhart/alpine-node:9

WORKDIR /app

COPY ./app .

RUN apk add --no-cache bash make gcc g++ python curl

RUN npm install --production

EXPOSE 3000

CMD ["node", "server.js"]
