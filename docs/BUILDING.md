# Building packages

To build packages from Fedora, you need to install `anda`, and also add the Terra repostories onto your system.


## Installing Terra repos

Install the Terra repositories by adding it using DNF
```
sudo dnf config-manager --add-repo https://github.com/terrapkg/subatomic-repos/raw/main/terra.repo
```

## Installing Andaman

After adding the repositories above, install Andaman using DNF
```
sudo dnf install anda
```

## Building packages

To build packages using Andaman, you will need to use the `anda` mock configuration.

Install the mock configurations
```
sudo dnf install anda-mock-configs
```

Then specify the mock config everytime you build a package
```
anda build -c anda-37-x86_64 $PROJECT
```

Substitute `37` with the version of Fedora you want to build for, same goes for the architecture.

To list all available Andaman projects you can build, run:
```
anda list
```

# Packaging SOP

Project names should always be `pkg` inside the `anda` directory.
To build it, specify the path to the project then /pkg

For example, to build the `dart` package, you would run:
```
anda build -c anda-37-x86_64 anda/dart/pkg
```
