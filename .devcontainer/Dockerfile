ARG VARIANT="rawhide"
FROM fedora:${VARIANT}

RUN useradd -m vscode
RUN groupadd mock
RUN usermod -aG mock vscode
RUN echo vscode ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/vscode
RUN curl -Lo /etc/yum.repos.d/terra.repo https://raw.githubusercontent.com/terrapkg/subatomic-repos/main/terra.repo
RUN dnf -y install git mock createrepo_c anda terra-mock-configs
