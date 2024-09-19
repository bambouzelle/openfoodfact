FROM jupyter/pyspark-notebook

USER root

# Download the MySQL JDBC driver
RUN wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-8.0.26.tar.gz \
    && tar xzf mysql-connector-java-8.0.26.tar.gz \
    && mv mysql-connector-java-8.0.26/mysql-connector-java-8.0.26.jar /usr/local/spark/jars/ \
    && rm -rf mysql-connector-java-8.0.26 mysql-connector-java-8.0.26.tar.gz