FROM ghcr.io/terrapkg/builder:f43

ARG USERNAME=$USERNAME
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Do not do this outside of a container for the love of God.
RUN groupadd --gid $USER_GID $USERNAME && \
useradd --uid $USER_UID --gid $USER_GID -m $USERNAME --groups mock && \
echo "$USERNAME ALL = (ALL) NOPASSWD: ALL" > /etc/sudoers.d/$USERNAME && \
mkdir -p /workspaces/devcontainer && \
chown -R $USERNAME /workspaces/devcontainer

USER 1000:1000
WORKDIR /workspaces/devcontainer
