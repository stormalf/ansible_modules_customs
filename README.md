# example from openclassroom
# https://openclassrooms.com/fr/courses/2035796-utilisez-ansible-pour-automatiser-vos-taches-de-configuration/6373909-creez-votre-propre-module-ansible-personnalise-avec-python

# This module sample did a call to mediawiki database 
# in mysql and returns the result of sql statement
# no security any statement is executed (not to use in production!)
# connection hard-coded : it's possible to define other ansible parameters instead of defining hard-coded values

# prerequisites
* having a docker mysql installed (see docker-compose.yml) : to generate the container : docker-compose up
* having the mediawiki database imported into mysql (see mediawiki.sql) use url http://localhost:8080 
* having some data imported into page table (see page.csv)

# to execute needs to have in local directory the library folder with module count_page.py
to execute in command line : 
ansible-playbook  module.yml
