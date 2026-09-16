FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive \
    WAZUH_MANAGER=wazuh.manager \
    WAZUH_REGISTRATION_SERVER=wazuh.manager \
    WAZUH_AGENT_NAME=si084_portal_testigo

RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates curl procps && \
    curl -fsSL -o /tmp/wazuh-agent.deb https://packages.wazuh.com/4.x/apt/pool/main/w/wazuh-agent/wazuh-agent_4.9.0-1_amd64.deb && \
    apt-get install -y --no-install-recommends /tmp/wazuh-agent.deb && \
    rm -f /tmp/wazuh-agent.deb && rm -rf /var/lib/apt/lists/*

COPY iniciar-agente.sh /usr/local/bin/iniciar-agente.sh
RUN chmod +x /usr/local/bin/iniciar-agente.sh
CMD ["/usr/local/bin/iniciar-agente.sh"]
