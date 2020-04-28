FROM openjdk:8

WORKDIR /tmp

# Install Ruby
RUN apt-get update \
 && apt-get -y install build-essential \
                       automake \
                       zlib1g-dev \
                       libssl-dev \
 && apt-get clean \
 && wget --no-check-certificate -q https://cache.ruby-lang.org/pub/ruby/2.6/ruby-2.6.3.tar.gz \
 && tar zxvf ruby-2.6.3.tar.gz \
 && cd ruby-2.6.3 \
 && ./configure \
 && make \
 && make install \
 && cd .. \
 && rm -fr ruby-2.6.3*

# SoapUI Version
ENV   SOAPUI_VERSION  5.4.0

# Download and unarchive SoapUI
RUN mkdir -p /opt &&\
    curl  https://s3.amazonaws.com/downloads.eviware/soapuios/${SOAPUI_VERSION}/SoapUI-${SOAPUI_VERSION}-linux-bin.tar.gz \
    | gunzip -c - | tar -xf - -C /opt && \
    ln -s /opt/SoapUI-${SOAPUI_VERSION} /opt/SoapUI

# Set working directory
WORKDIR /opt/bin

# Set environment
ENV PATH ${PATH}:/opt/SoapUI/bin
