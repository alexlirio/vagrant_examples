# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # https://docs.vagrantup.com.

  config.vm.hostname = "app"
  
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "alexlirio/centos7"
  
  # accessing "localhost:8000" will access port 8000 on the guest machine.
  config.vm.network "forwarded_port", guest: 8000, host: 8000   # Django
  # config.vm.network "forwarded_port", guest: 3306, host: 3306   # MySQL

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on your network.
  config.vm.network "public_network", bridge: [
    "en6: Broadcom NetXtreme Gigabit Ethernet Controller",
  ]

  # Share an additional folder to the guest VM.
  # The first argument is the path on the host to the actual folder.
  # The second argument is the path on the guest to mount the folder.
  # And the optional third argument is a set of non-required options.
  config.vm.synced_folder ".", "/app",  type: "virtualbox"
  config.vm.synced_folder "../", "/code",  type: "virtualbox"

  config.vm.provider "virtualbox" do |vb|
    vb.name = "vagrant_examples"
    vb.memory = "512"
  end
  
  config.vm.provision "shell", inline: <<-SHELL
    sudo yum install -y sshpass net-tools dos2unix libxml2 libxml2-devel libxml2-python libxslt libxslt-devel postgresql-devel
  SHELL
end
