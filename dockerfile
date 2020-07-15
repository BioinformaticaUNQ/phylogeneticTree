FROM python:slim

WORKDIR /TMP

RUN /bin/bash -c "apt update; apt install -y unzip curl; apt update"
RUN /bin/bash -c "curl --location https://github.com/Cibiv/IQ-TREE/releases/download/v1.6.12/iqtree-1.6.12-Linux.tar.gz --output iqtree-1.6.12-Linux.tar.gz && \
 gunzip iqtree-1.6.12-Linux.tar.gz && \
 tar xvf iqtree-1.6.12-Linux.tar && \
 cp iqtree-1.6.12-Linux/bin/iqtree /bin/iqtree"
RUN /bin/bash -c "cd ..; rm -rf TMP"

WORKDIR /data
VOLUME ["/data"]

WORKDIR /phylogeneticTree

COPY src .
RUN /bin/bash -c "pip install biopython"

ENTRYPOINT ["/bin/bash", "./start.sh"]
