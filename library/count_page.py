#!/usr/bin/python 
# -*- coding: utf-8 -*-
#example from openclassroom adapted to my context


import pymysql as pm

from ansible.module_utils.basic import AnsibleModule  


DOCUMENTATION='''
module: count_page
author: Openclassroom
description: Module that executes a mysql SQL statement
 
options: 
  db_name: 
    description: database name 
    required: yes 
  request: 
    description: SQL statement to execute
    required: yes 
 
'''

EXAMPLES='''
- name: "SQL" 
  count_page: 
    db_name: "BDD" 
    request: "select * from user;" 
'''

RETURN = '''
results: 
    description: return the result of SQL statement executed 
'''



def main(): 
    module = AnsibleModule( 
        argument_spec=dict( 
            db_name    = dict(required=True, type="str"), 
            request    = dict(required=True, type="str"), 
        ) 
    )    
    db_name_local = module.params.get("db_name") 
    request_local = module.params.get("request")

    db = pm.connect(host="localhost", user="root", password="my_password", port=3306, db=db_name_local) 
    cur = db.cursor() 
    cur.execute(request_local) 
    resultat = cur.fetchall() 
    db.close()
    module.exit_json(changed=False, results=resultat)  

if __name__ == "__main__": 
    main()