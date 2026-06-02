FROM node
RUN npm install -g newman
RUN npm install -g newman-reporter-htmlextra
WORKDIR /app
CMD ["newman", "run", "collection_tests.json", "--environment", "Environment dnd5e.postman_environment.json", "--reporters", "htmlextra", "--reporter-htmlextra-export", "./reports"]