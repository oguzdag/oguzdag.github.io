Put the py file under filter_plugins

and call the function using below ansible code

```
- name: calling custom function
  set_fact: my_dict="{{ mule_gw_instances | createmylist(clustername, hostvars, play_hosts, first_mule_instance, last_mule_instance) }}"
  run_once: true
  delegate_to: "{{ delegate_host }}"
```
