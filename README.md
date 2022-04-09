# examples using different targets/databases/os...

each folder contains some playbooks example and customized modules

# Ansible on windows

It's possible to have Ansible on Windows (but not directly working in Windows). It exists 3 ways :

- cygwin installation
- msys2 installation
- wsl on windows

WSL is more a linux environment than a windows environment. But cygwin and msys2 is more integrated with Windows. And you can easily install them on Windows and use your Windows as an Ansible server (control node).

Example in cygwin :

    $ ansible --version
    ansible 2.10.3
    config file = /etc/ansible/ansible.cfg
    configured module search path = ['/home/greatuser/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
    ansible python module location = /usr/local/lib/python3.8/site-packages/ansible
    executable location = /usr/local/bin/ansible
    python version = 3.8.12 (default, Nov 23 2021, 20:18:25) [GCC 11.2.0]

    greatuser@greatserver ~
    $ uname -a
    CYGWIN_NT-10.0 greatserver 3.3.4(0.341/5/3) 2022-01-31 19:35 x86_64 Cygwin

Example in msys2 :

    $ ansible --version
    ansible 2.9.21
    config file = /etc/ansible/ansible.cfg
    configured module search path = ['/home/greatuser/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
    ansible python module location = /usr/lib/python3.9/site-packages/ansible
    executable location = /usr/bin/ansible
    python version = 3.9.9 (main, Dec 28 2021, 11:05:23) [GCC 11.2.0]

    greatuser@greatserver MSYS ~
    $ uname -a
    MSYS_NT-10.0-22000 greatserver 3.3.4-341.x86_64 2022-02-15 17:24 UTC x86_64 Msys

Example in WSL :

    $ ansible --version
    ansible 2.10.8
    config file = None
    configured module search path = ['/home/greatuser/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
    ansible python module location = /usr/lib/python3/dist-packages/ansible
    executable location = /usr/bin/ansible
    python version = 3.9.9 (main, Dec 16 2021, 23:13:29) [GCC 11.2.0]
    greatuser@greatserver:~/ansible_modules_customs$ uname -a
    Linux greatserver 5.10.102.1-microsoft-standard-WSL2 #1 SMP Wed Mar 2 00:30:59 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux

I tested to download the Ansible and to change the tar file to remove the symbolic link and to be able to install it on Windows. But it struggles with different issues during execution including backslashes and impossible to install a collection due to comma in drive letters "C:\" and no tty and some python modules references files that doesn't exist in Windows.

That's why I recommend to use one of these 2 ways if you want to use Ansible on Windows (WSL is more an embedded linux with it's own IP address).

# Ansible on IBMi

It's also possible to have Ansible on IBMi and using IBMi as an Ansible server (control node). Follows the pre-requisites from IBM :
https://github.com/IBM/ansible-for-i.git

To be able to run ansible-playbook command, you can run it using putty or ssh in QP2TERM or QSH. Probably need to change the path or to add ansible to the user path or creating symbolic link.

The specificity on IBMi is that sometimes you need to do some actions in the same job. In this case you have 2 ways :

- creating a file with CL: commands and running SQL (you can find an example in ibmi-install-yum.yml playbook in the ansible-for-i repository)
- creating/compiling or calling a CLP that does the dependent parts

An excellent IBM collection that helps you to simplify your playbooks is the ibm.power_ibmi collection : https://galaxy.ansible.com/ibm/power_ibmi

You can extend the collection or create your own Ansible plugin to do what you need and what you want. It's not too hard! Think about idempotency some IBM commands doesn't manage correctly idempotency. Probably they will improve it in the future!

Example on IBMi :

    bash-5.1$ ansible --version
    ansible 2.9.10
    config file = None
    configured module search path = ['/home/GREATUSER/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
    ansible python module location = /QOpenSys/pkgs/lib/python3.6/site-packages/ansible
    executable location = /QOpenSys/pkgs/bin/ansible
    python version = 3.6.15 (default, Dec 17 2021, 09:57:34) [GCC 6.3.0]
    bash-5.1$ uname -a
    OS400 WWW 4 7 007800001B91 powerpc Os


    bash-5.1$ ansible-galaxy collection install ibm.power_ibmi
    Process install dependency map
    Starting collection install process
    Installing 'ibm.power_ibmi:1.7.0' to '/home/GREATUSER/.ansible/collections/ansible_collections/ibm/power_ibmi'

# Skytap Ansible modules

You can find interesting modules in the Skytap Ansible repository : https://github.com/skytap/ansible-skytap.git
Skytap provides IBMi.
