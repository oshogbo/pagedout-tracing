# Tracing Recipes!

Code snippets from the [Paged Out #2](https://pagedout.institute/?page=issues.php) article.

## Dependencies

### GDB
Required GDB and basic shell tools.

### DTrace on FreeBSD
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
vagrant up linux && vagrant ssh linux
# inside the VM
cd /vagrant
```

For other Linux distro please refer [INSTALL.md](https://github.com/iovisor/bcc/blob/master/INSTALL.md).

## Usage

### GDB
You have to set `TRACE_BIN` environment variable to point to the binary you want to trace.

### DTrace on FreeBSD
```
dtrace -s script.d -p PROCESS\_PID
```

or

```
dtrace -s script.d -c BINARY
```

### eBPF
```
python script.py BINARY PROCESS\_PID
```

## Author
[Mariusz Zaborski](https://oshogbo.vexillium.org)

## Thanks
[Disconnect3d](https://github.com/disconnect3d) for review of the article.

## License
BSD
