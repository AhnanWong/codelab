FROM registry-img.weizhipin.com/kz-algo/kz-wyn:1.0
RUN rm -rf /data/service
WORKDIR /data/service
ADD run /data/service
ADD server_deploy.jar /data/service
ADD client_deploy.jar /data/service
ADD run /data/service
RUN chmod +x /data/service/run
CMD ["/bin/bash", "/data/service/run"]
#ENTRYPOINT ["/data/service/run"]
EXPOSE 8081