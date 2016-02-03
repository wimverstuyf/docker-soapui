FROM edwxie/jdk
MAINTAINER Daniel Davison <sircapsalot@gmail.com>

#  Version
ENV   SOAPUI_VERSION  5.2.1

COPY entry_point.sh /opt/bin/entry_point.sh
RUN chmod +x /opt/bin/entry_point.sh

# Download and unarchive SoapUI
RUN mkdir -p /opt &&\
    curl  http://cdn01.downloads.smartbear.com/soapui/${SOAPUI_VERSION}/SoapUI-${SOAPUI_VERSION}-linux-bin.tar.gz \
    | gunzip -c - | tar -xf - -C /opt && \
    ln -s /opt/SoapUI-${SOAPUI_VERSION} /opt/SoapUI

# Set environment
ENV PATH ${PATH}:/opt/SoapUI/bin

CMD ["/opt/bin/entry_point.sh"]
