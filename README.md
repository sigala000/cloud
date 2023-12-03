#####

Question1
A) Dans un premier temps il s’agira de déployer une même image OVA (tinyVM). Le fichier de configuration en JSON indiquera le nombre d’instance à déployer sur votre ESXi local. Comme il s’agit du même OVA, pensez à le cloner.#####

Reponse
Here is the JSON

"node1":{
"host":"192.168.129.149" // here you put the IP address of your virtual machine,
"user":"root", // here you put your username of your virtual machine
"password":"sigalas", // here your password of your virtual machine
"ova_path":"/Users/ndansisigala/Downloads/yVM.ova", // here you put the path in which the ova_file is found in your machine
"instance_nbr":2,// here you choose the numnber of instances
"disable_ssl_verification":true,
"port":443,
"datastore_name":"",
"datacenter_name":"",
"resource_pool":""
},
when you are done setting up the machine in a cluster you run the command by writing python3 deploy_ova.py

#####
B)
Dans un deuxième temps nous souhaitons créer des VM from scracth. Le fichier de configuration devra être sous le format JSON. Les paramètres minimaux de configuration seront : La RAM, la taille Disk, le CD-ROM 
Reponse

{
    "host":"192.168.43.3", // here you put the IP address of your virtual machine,
    "user":"root", //  here you put your username of your virtual machine
    "password":"sigalas", // here your password of your virtual machine
    "name":"shabaaa",// here is the name you whish to give your virtual machine when creating it
    "memoryMB":1024, // here you define your memory size
    "numCPUs":1, // here you give thew number of CPUs you want
    "guestId":"otherGuest",
    "version":"vmx-07",
    "iso_path":"/Users/ndansisigala/Downloads/Core-5.4.iso", // here is the path of your iso file in your machine 
    "disable_ssl_verification":true,
    "port":443,
    "datastore_name":"",
    "datacenter_name":"",
    "resource_pool":""
}

and for you to run the "create_iso" you just need  to run the command python3 create_iso.py
#####

Question 2
Une fois que vous êtes capable de déployer plusieurs OVA sur votre ESXi, modifier votre code pour permette le déploiement sur plusieurs ESXi (le vôtre et celui des membres de votre groupe). Le fichier de configuration devra donc contenir l’IP des serveurs sur lequel l’OVA devra être déployé.

Reponse

go to the Config_ova_cluster.json and duplicate the "node1" to the number of users connected to your network

"node1":{
"host":"192.168.129.149" // here you put the IP address of your virtual machine,
"user":"root", // here you put your username of your virtual machine
"password":"sigalas", // here your password of your virtual machine
"ova_path":"/Users/ndansisigala/Downloads/yVM.ova", // here you put the path in which the ova_file is found in your machine
"instance_nbr":2,// here you choose the numnber of instances
"disable_ssl_verification":true,
"port":443,
"datastore_name":"",
"datacenter_name":"",
"resource_pool":""
},
"node2":{
"host":"192.168.129.249", // here you put the IP address of your partners virtual machine
"user":"root", // here you put the username of your partners virtual machine
"password":"aristide", // here your password of your partners virtual machine
"ova_path":"/Users/ndansisigala/Downloads/yVM.ova",// here you put the path in which the ova_file is found in your machine
"instance_nbr":2, //here you choose the numnber of instances to be deployed on your partners virtual machine
"disable_ssl_verification":true,
"port":443,
"datastore_name":"",
"datacenter_name":"",
"resource_pool":""
},

when you are done setting up the machine in a cluster you run the command by writing python3 deploy_ova.py