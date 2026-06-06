#Objective To perform SQL Injection Attack of a vulnerable web login page on Metasploitable machine Steps Performed 

Assumption: Kali linux (Attacker), Metasploitable 2 Machine (Target) 

Metasploitable 2 machine: username, password: msfadmin 

#To access vulnerable web application on Metasploit on Kali linux: 

open browser: http://<metasploit_IP> http://192.168.56.101 

Click on DVWA(Damn Vulnerable Web Application) 

login: username: admin, password: password 

#Perform SQL injection: 

Navigate to: DVWA, settings, Security Level, set to Low 

user ID: 1' OR '1'='1' 

It returns all user records.
