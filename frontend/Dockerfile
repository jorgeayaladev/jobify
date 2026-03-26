# Imagen base
FROM node:20

# Instalar pnpm
RUN npm install -g pnpm

# Directorio de trabajo
WORKDIR /app

# Copiar archivos de dependencias
COPY package.json pnpm-lock.yaml ./

# Instalar dependencias
RUN pnpm install

# Copiar el resto del código
COPY . .

# Construir la app
RUN pnpm build

# Exponer puerto
EXPOSE 3000

# Comando de ejecución
CMD ["pnpm", "start"]