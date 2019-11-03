# Tracing Recipes!

Code snippets from the [Paged Out #2](https://pagedout.institute/?page=issues.php) article.

## Dependencies

### GDB
Required GDB and basic shell tools.

### DTrace and FreeBSD
Just load the DTrace module:

```
kldload dtraceall.ko
```

### eBPF
For systems with apt:
```
sudo apt install bpfcc-tools linux-headers-$(uname -r)
```

For systems with Vagrant:
```
```

For other Linux distro please refer [INSTALL.md](https://github.com/iovisor/bcc/blob/master/INSTALL.md).

## Author
[Mariusz Zaborski](https://oshogbo.vexillium.org)

## Thanks
[Disconnect3d](https://github.com/disconnect3d) for review of the article.

## License
BSD
