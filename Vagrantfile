# -*- mode: ruby -*-

Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/xenial64"

  config.vm.network "forwarded_port", guest: 8000, host: 8000, host_ip: "127.0.0.1"

  config.vm.provision "shell", inline: <<-SHELL
    # Update and upgrade the server packages
    sudo apt-get update
    sudo apt-get -y upgrade
    # Set Ubuntu Language
    sudo locale-gen en_GB.UTF-8
    # Install Python, SQLite and pip
    sudo apt-get install -y python3-dev sqlite python3-pip python-pip
    # Upgrade pip
    python -m pip install --upgrade pip
    python3 -m pip install --upgrade pip
    # Install and configure python virtual environment wrapper
    sudo python -m pip install virtualenvwrapper
    '''
    echo "# VIRTUALENV_ALREADY_ADDED" >> ~/.bashrc
    echo "export WORKON_HOME=~/.virtualenvs" >> ~/.bashrc
    echo "export PROJECT_HOME=/vagrant" >> ~/.bashrc
    echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
    '''
  SHELL
end
