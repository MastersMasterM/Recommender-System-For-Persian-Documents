# Use an official Node.js runtime as the base image
FROM node:14-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files to the working directory
COPY package*.json ./

# Install the project dependencies
RUN npm install

# Copy the entire project directory to the working directory
COPY . .

# Build the React app for production
RUN npm run build

# Set the command to run when the container starts
CMD ["npm", "start"]