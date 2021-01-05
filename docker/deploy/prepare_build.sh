set -x
rm -fr codelab/docker/deploy/server_deploy.jar codelab/docker/deploy/client_deploy.jar
bazel build codelab/docker/java:server_deploy.jar
bazel build codelab/docker/java:client_deploy.jar
cp -fr bazel-bin/codelab/docker/java/server_deploy.jar codelab/docker/deploy/
cp -fr bazel-bin/codelab/docker/java/client_deploy.jar codelab/docker/deploy/


docker build ./
docker run -p 5300:5300 -tdi --privileged {image_id} /bin/bash
docker exec -it {container_id} java -jar /data/service/server_deploy.jar

