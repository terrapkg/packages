ARG VARIANT="rawhide"
FROM fedora:${VARIANT}

RUN useradd -m vscode
RUN groupadd mock
RUN usermod -aG mock vscode
RUN echo vscode ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/vscode
RUN dnf -y install git 'dnf-command(config-manager)' mock createrepo_c
RUN dnf config-manager --add-repo='https://raw.githubusercontent.com/terrapkg/subatomic-repos/main/terra.repo'
RUN dnf -y install anda terra-mock-configs
