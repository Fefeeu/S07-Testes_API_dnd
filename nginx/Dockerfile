FROM nginx:alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf

# TODO: mudar a linha para integração com o 'report.html' correto
COPY ./relatorio_para_testar/report.html /usr/share/nginx/html/report.html

EXPOSE 80