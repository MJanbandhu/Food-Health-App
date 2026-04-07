# Step 1: Build the Vite production bundle
FROM node:18-alpine AS build

WORKDIR /app
COPY package.json package-lock.json* ./
RUN npm install

COPY . .
# We build specifying that Vite should expect API traffic using a relative path,
# or injected via environment variables if CI/CD exists.
# For demo purposes without a domain, the Nginx container will proxy requests.
RUN npm run build

# Step 2: Serve the app using Nginx
FROM nginx:alpine

# Copy the built React app into nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Overwrite default nginx config to handle React router fallback & proxying API
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
