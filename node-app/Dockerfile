FROM node:16

# Create app directory
WORKDIR /usr/src/app

# Copy to workdir to install dependencies
COPY package*.json ./

# Install app dependencies
RUN npm install

# Bundle app source
COPY . .

# COPY .env .

EXPOSE 3000
CMD [ "node", "server.js" ]