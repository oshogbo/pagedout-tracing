Vagrant.configure("2") do |config|
    config.vm.define "linux" do |linux|
        linux.vm.box = "generic/ubuntu1810"
        linux.vm.provision :shell, inline: <<~PROVISION

	sudo apt update
	sudo DEBIAN_FRONTEND=noninteractive apt upgrade -y
	sudo DEBIAN_FRONTEND=noninteractive apt install -y bpfcc-tools linux-headers-$(uname -r)
    PROVISION
  end

  config.vm.define "freebsd" do |freebsd|
	freebsd.ssh.shell = "sh"

	freebsd.vm.synced_folder ".", "/vagrant", type: :rsync
	freebsd.vm.box = "freebsd/FreeBSD-12.0-RELEASE"

	freebsd.vm.provision :shell, inline: <<~PROVISION
		su -m root -c 'kldload dtraceall.ko'
	PROVISION
  end
end
