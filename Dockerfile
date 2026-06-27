FROM apache/spark:3.5.1

USER root

# Install system dependencies
RUN apt-get update && \
    apt-get install -y python3-pip python3-dev build-essential vim nano bash-completion && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    echo ". /usr/share/bash-completion/bash_completion" >> /etc/bash.bashrc

# Install Python packages (Removed redundant pyspark)
# RUN pip3 install --no-cache-dir \pip3 install pyspark\
#         jupyterlab \
#         numpy \
#         pandas \
#         pyarrow \
#         matplotlib \
#         ipython \
#         findspark


RUN pip3 install --no-cache-dir \
        pyspark==3.5.1 \
        jupyterlab \
        numpy \
        pandas \
        pyarrow \
        matplotlib \
        ipython \
        findspark

# Create directories and set correct ownership
RUN mkdir -p /home/spark/.local/share/jupyter/runtime && \
    mkdir -p /opt/ipl_project_spark_setup/spark-notebooks && \
    chown -R spark:spark /home/spark && \
    chown -R spark:spark /opt/ipl_project_spark_setup

# Switch to non-root user
USER spark

# Environment variables
ENV SHELL=/bin/bash
ENV PYSPARK_PYTHON=python3

# Set working directory
WORKDIR /opt/ipl_project_spark_setup/spark-notebooks

# Expose Jupyter port and Spark UI port
EXPOSE 8888 4040

# Start JupyterLab (Removed --allow-root)
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser"]
