### 1. JFrog CLI Build
JFrog CLI 的命令接受两个可选的命令选项:--build-name 和 --build-number。当添加了这些选项后，JFrog CLI 将在本地为这些命令收集和记录构建信息。
当使用相同的 build name 和 build number 运行多个命令时，JFrog CLI 将收集的构建信息聚合到一个构建中。
之后使用 build-publish 命令将记录的构建信息发布到 Artifactory。

```

jf rt dl slash-generic-local/slash/app/1.1/app-1.1.war --build-name=slash-generic-build --build-number=1

// 以 build 方式上传制品
jf rt u app-1.1.war slash-generic-local --build-name=slash-generic-build --build-number=1

// 收集当前环境变量到指定的 build info 中
jf rt bce slash-generic-build 1

// 发布 build
jf rt bp slash-generic-build 1

// Promote build
jf rt bpr slash-generic-build 3 slash-generic-release-local

```

### 2. Maven Build
```
// 下载示例代码仓库
git clone git@github.com:slash-l/app-maven.git
cd app-maven

jf mvnc --server-id-resolve=JFrogChina-Server --server-id-deploy=JFrogChina-Server --repo-resolve-releases=slash-maven-virtual --repo-resolve-snapshots=slash-maven-virtual --repo-deploy-releases=slash-generic-local --repo-deploy-snapshots=slash-generic-local

jf mvn clean install -f pom.xml --build-name=slash-generic-build --build-number=5
jf rt sp "slash-generic-local/org/jfrog/test/multi3/2.0-SNAPSHOT/*.war" "deploy.tool=manual"
jf rt bp slash-generic-build 5
```

### 3. Docker Build
先确保 docker 命令可以正常使用 Artifactory
```
docker pull hello-world
docker tag hello-world:latest demo.jfrogchina.com/slash-docker-dev-local/hello-world:latest
docker login 
docker push demo.jfrogchina.com/slash-docker-dev-local/hello-world:latest
```

使用 JFrog CLI docker
```
jf docker pull demo.jfrogchina.com/slash-docker-dev-local/hello-world:latest --build-name=slash-docker-build --build-number=1
jf rt bp slash-docker-build 1

jf docker push demo.jfrogchina.com/slash-docker-dev-local/hello-world:latest --build-name=slash-docker-build --build-number=2
jf rt bp slash-docker-build 2

jf rt docker-promote hello-world --source-tag=latest slash-docker-dev-local slash-docker-release-local
```


