FROM bitnami/spark:3.5

USER root
RUN curl -L -o /opt/spark/jars/mysql-connector-j.jar https://repo1.maven.org/maven2/com/mysql/mysql-connector-j/8.4.0/mysql-connector-j-8.4.0.jar

COPY spark-jobs /opt/spark-apps

CMD ["/opt/bitnami/spark/bin/spark-submit", "--master", "spark://spark-master:7077", "/opt/spark-apps/job.py"]

