FROM jupyter/pyspark-notebook:latest

# Passer à l'utilisateur root pour obtenir les droits d'administration
USER root  

# Télécharger et installer le connecteur JDBC MySQL
RUN wget -q https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-8.0.30.tar.gz && \
    tar -xzf mysql-connector-java-8.0.30.tar.gz && \
    cp mysql-connector-java-8.0.30/mysql-connector-java-8.0.30.jar /usr/local/spark/jars/ && \
    rm -rf mysql-connector-java-8.0.30 mysql-connector-java-8.0.30.tar.gz

# Revenir à l'utilisateur jovyan (utilisateur par défaut)
USER $NB_UID  
