# Linux

## Overview

Selecting a Linux distribution is a bit complicated, as there are quite any options with different features. There is even [a website that automatically recommends you what to install based on your needs](https://distrochooser.de/en/).

If you already have Linux installed and you want to quickly get a feeling for a different distribution without going through a full installation or VM try out [distrobox](https://github.com/89luca89/distrobox). It lets you use the [most common distros](https://github.com/89luca89/distrobox/blob/main/docs/compatibility.md#containers-distros) in a shell via Docker or Podman. This gives you a quick to launch and persistent container with most of your file system mounted and the ability to launch GUI applications.

Do you want our opinion? You cannot go wrong with any of:

- [Ubuntu](https://ubuntu.com/): The distribution with the largest user base and maybe the system most commonly used in continuous integration environments. Based on [Debian](https://www.debian.org/).
  - Pro: [AskUbuntu](https://askubuntu.com/) (similar to StackOverflow), many packages (also of proprietary software), LTS releases quite stable and not so outdated.
  - Contra: new "snap" packages often slow and not very well integrated with the rest of the system (but offer seamless updates), classical "deb" packages typically months behind since the date of release and most of them getting only bugfix updates.
  - Note: There is a new LTS version every two years (supported for five years), and a "regular" version every six months (supported for nine months). Version upgrades are typically easy, with potential issues if proprietary drivers are involved, depending on the level of support by the vendor.
- [Mint](https://linuxmint.com/): A safe choice for the absolute beginner, especially coming from Windows. Based on Ubuntu.
  - Pro: The interface looks closer to Windows in comparison to Ubuntu, ships a few additional drivers.
  - Contra: While most of the packages and documentation/Q&A from Ubuntu also work here, the community that maintains Mint (and other derived distributions) is smaller. Which is not necessarily an issue, especially since Mint has been around for several years.
- [Fedora](https://getfedora.org/): A polished, up-to-date alternative to Ubuntu, with main focus on desktop applications.
  - Pro: Closely connected to the development of the GNOME desktop environment, offers "flatpak" packages, which seem to work a bit better for UI applications.
  - Contra: You have to upgrade to new releases more often than in LTS distributions (shorter [release life cycle](https://docs.fedoraproject.org/en-US/releases/lifecycle/#_end_of_life_eol), after which there are no package updates), but upgrades should usually go smoothly. The package management and several other aspects are a bit different from Ubuntu, which may make it slightly more complicated to find documentation or third-party packages.
- [Arch](https://archlinux.org/): A rolling-release distribution that nowadays offers easier installation than it used to.
  - Pro: Offers the latest versions of every package. Rich documentation in the [Arch Wiki](https://wiki.archlinux.org/). Great way to learn a lot about Linux.
  - Contra: Probably not so beginner-friendly. Rolling distributions continuously update even major versions of packages, which may bring breaking dependencies for your code.
  - Note: Arch provides the [AUR](https://aur.archlinux.org/), a very large collection of user-contributed packages. These may not be that stable.
  - Note: There are also other Arch-based distributions, such as [Manjaro](https://manjaro.org/) and [EndeavourOS](https://endeavouros.com/). Since the Arch installation [is now easier](https://wiki.archlinux.org/title/Archinstall), these may add limited value nowadays.

Do you like what you read about a distribution but prefer the aesthetics of another? Most distributions offer alternative versions with different desktop environments. Most commonly [GNOME](https://www.gnome.org/), [KDE Plasma](https://kde.org/plasma-desktop/), and [Xfce](https://xfce.org/) (but there are many more). Many desktop applications are designed primarily for one of these systems.

You will find many more distributions out there, but you may prefer to stick with a major one, as derivatives are often not well-maintained. Most distributions are based on either of Debian/Ubuntu, Fedora (Red Hat), or Arch. See the [family tree](https://en.wikipedia.org/wiki/List_of_Linux_distributions).

Honorable mentions: [Elementary OS](https://elementary.io/), [Pop!_OS](https://pop.system76.com/), [OpenSUSE](https://www.opensuse.org/), and [many many more](https://distrowatch.com/). For macBooks with Apple Silicon processors, there is [Asahi Linux](https://asahilinux.org/).

## Tips for common distributions

### Ubuntu

Ubuntu offers long-term support releases every two years in (end of) April: 20.04, 22.04, 24.04, etc. These offer five year support with new packages and security updates. After that time, you will not be able to install or update anything (unless you subscribe to [Ubuntu Pro](https://ubuntu.com/pro), which extends support to ten years). This will be generally fine to get you through your studies, and you can always upgrade to a new release. Your milage with older package versions may vary.

Alternatively, you can install one of the intermediate releases that come every six months (22.04, 22.10, 23.04, ...). These offer support for only nine months, so you have to upgrade along the way. This will offer a nice balance of stability and relatively new packages, and you get to select when you will upgrade (you don't want to do this next to your project submission deadline).

Ubuntu, built on top of Debian, uses the APT package manager and gets many packages from Debian, often in frozen versions. As a way of updating user-facing packages more often, Ubuntu also offers snap as a package manager and [snapcraft.io](https://snapcraft.io/) as an additional "app store". These applications are often sandboxed for secutity reasons and they carry all their dependencies in the same package. This allows them to update independently of the rest of your system, but at the same time they may be slow to start, or may not be able to access your files in every way you are used to (e.g., click-to-open).

A few survival tips:

- In recent Ubuntu releases, it looks like one cannot open links from a PDF to Firefox ([askubuntu discussion](https://askubuntu.com/questions/1390520/evince-can-not-open-links-in-snap-firefox)). Consider replacing Firefox from snap with the package from APT, or switching from the default PDF reader to Okular: `sudo apt install okular`.
- Inkscape from snap may not be able to open files in some ways. In that case, consider installing Inkscape from APT: `sudo apt install inkscape`.
