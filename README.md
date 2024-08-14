# Terra Sources

[![Repository status](https://repology.org/badge/repository-big/terra_39.svg?header=Terra+39)](https://repology.org/repository/terra_39)
[![Repository status](https://repology.org/badge/repository-big/terra_40.svg?header=Terra+40)](https://repology.org/repository/terra_40)
[![Repository status](https://repology.org/badge/repository-big/terra_rawhide.svg?header=Terra+Rawhide)](https://repology.org/repository/terra_rawhide)

Terra is a rolling-release Fedora repository for all the software you need.
With Terra, you can install the latest packages knowing that quality and security are assured.

See the introduction at [our website](https://terra.fyralabs.com).

This monorepo contains the package manifests for all packages in Terra.

## Installation

```bash
sudo dnf install --repofrompath 'terra,https://repos.fyralabs.com/terra$releasever' --setopt='terra.gpgkey=https://repos.fyralabs.com/terra$releasever/key.asc' terra-release
```

If you are using immutable/atomic editions of Fedora, run the following commands instead:

```bash
curl -fsSL https://github.com/terrapkg/subatomic-repos/raw/main/terra.repo | pkexec tee /etc/yum.repos.d/terra.repo
sudo rpm-ostree install terra-release
```

## Documentation

Our documentation can be found on our [Devdocs](https://developer.fyralabs.com/terra/).

## Questions?

Feel free to reach out by [joining our community](https://wiki.ultramarine-linux.org/en/community/community/). We're always happy to help!

- [Contribution Guide](https://developer.fyralabs.com/terra/contributing)
- [FAQ](https://developer.fyralabs.com/terra/faq)
- [Policy](https://developer.fyralabs.com/terra/policy)
