# examples for IBMi

several playbooks and example about how we can do with IBMi target (notice that some playbooks can require additional packages on the target like db2util...) Perhaps I'll use to IBM collection to provide more examples about what we can do with Ansible and IBM i.

# PUB400.yml

first playbook connecting to PUB400.com and executing hello world!

# pre-requisites

having configured the ssh keys and inventory file with correct information to connect to PUB400.COM

- To execute : (replace .../hosts by your inventory file that defines the port, and other ansible ssh parameters to use)
  ansible-playbook -i .../hosts pub400.yml

# output example

PLAY [ibmi] ************************************\*\*\*\*************************************\*\*\*************************************\*\*\*\*************************************

TASK [echo hello world] **********************************\*\***********************************\*\*\***********************************\*\***********************************
changed: [PUB400.COM]

PLAY RECAP ************************************\*\*\*\*************************************\*\*\*\*************************************\*\*\*\*************************************
PUB400.COM : ok=1 changed=1 unreachable=0 failed=0 skipped=0 rescued=0 ignored=0
