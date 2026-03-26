FROM node:20

WORKDIR /app

RUN npm install -g pnpm

RUN pnpm config set node-linker hoisted

COPY package.json pnpm-lock.yaml ./

RUN pnpm install

COPY . .

EXPOSE 3000

CMD ["pnpm", "dev"]