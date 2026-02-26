# Terra Sources

[![Repository status](https://repology.org/badge/repository-big/terra_rawhide.svg?header=Terra+Rawhide)](https://repology.org/repository/terra_rawhide)

Terra is a rolling-release Fedora repository for all the software you need.
With Terra, you can install the latest packages knowing that quality and security are assured.

See the introduction at [our website](https://terra.fyralabs.com).

This monorepo contains the package manifests for all packages in Terra.

## Installation

The latest detailed instructions are available in our Devdocs: https://developer.fyralabs.com/terra/installing

### Fedora

```bash
sudo dnf install --nogpgcheck --repofrompath 'terra,https://repos.fyralabs.com/terra$releasever' terra-release
```

If you are using immutable/atomic editions of Fedora, run the following commands instead:

```bash
curl -fsSL https://github.com/terrapkg/subatomic-repos/raw/main/terra.repo | pkexec tee /etc/yum.repos.d/terra.repo
sudo rpm-ostree install terra-release
```
#### Subrepos

On Fedora, you can optionally install the Terra subrepos. Extra care and caution may be needed as some of these packages may conflict with other repositories such as RPM Fusion.

- Install `terra-release-extras` to enable the Extras subrepo. This repo contains packages which conflict with Fedora packages in some way, such as being a patched version of the same package.
- Install `terra-release-mesa` to install the Mesa subrepo which contains a patched and codec complete Mesa.
- Install `terra-release-nvidia` to install the NVIDIA subrepo which contains NVIDIA drivers.
- Install `terra-release-multimedia` for multimedia packages in Terra. This repository is currently considered a work in progress.

### Enterprise Linux (EL)

Only EL10 is supported. Not all packages available in Terra are available in Terra EL at this time.

Terra EL requires the EPEL repos, which may be installed with:

```bash
sudo dnf install 'https://dl.fedoraproject.org/pub/epel/epel-release-latest-$releasever.noarch.rpm'
```

And Terra EL itself can be installed with:

```bash
sudo dnf install --nogpgcheck --repofrompath 'terra,https://repos.fyralabs.com/terrael$releasever' terra-release
```

## Contributions

First of all, thanks for being interested in contributing to Terra! If you have any questions about contributing, please [join our chats](https://wiki.ultramarine-linux.org/en/community/community/).

- [Contribution Guide](https://developer.fyralabs.com/terra/contributing)
- [FAQ](https://developer.fyralabs.com/terra/faq)
- [Guidelines](https://developer.fyralabs.com/terra/guidelines)

## Documentation

Our documentation can be found on our [Devdocs](https://developer.fyralabs.com/terra/).

## Searching Packages

[pkgs.org](https://fedora.pkgs.org/rawhide/terra/) and [Repology](https://repology.org/) provide a list of the packages available in Terra.

## Questions?

Feel free to reach out by [joining our community](https://wiki.ultramarine-linux.org/en/community/community/). We're always happy to help!

- [Contribution Guide](https://developer.fyralabs.com/terra/contributing)
- [FAQ](https://developer.fyralabs.com/terra/faq)
- [Guidelines](https://developer.fyralabs.com/terra/guidelines)
