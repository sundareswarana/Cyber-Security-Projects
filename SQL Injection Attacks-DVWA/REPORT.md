#Experiment: Exploiting a Vulnerable Web Application (DVWA on Metasploitable)
#This experiment focus:
•	Port scanning
•	Web vulnerability identification
•	Exploitation basics
•	Understanding SQL Injection
#Objective:
  Discover a vulnerable web server
  Access a vulnerable login page
  Perform a basic SQL Injection
  Understand why it works
  Learn how to prevent it
#Ensure both VMs are:
•	In Host-Only Adapter OR same NAT Network
•	Can ping each other
#Assume
  Kali Linux (Attacker)
  Metasploitable 2 (Target)
  Both in VirtualBox
#Metasploitable IP address
  Inet 192.168.56.101 //my IP address (find yours)
#Kali linux IP address
  Inet 192.168.56.102  //my IP address (find yours)
#Reconnaissance:
From Kali:
	Ping < metasploitable IP address>
Scan Target from Kali:
	nmap -sV <target_ip>
  nmap -sV 192.168.56.101
#We will see information like:
•	Port 21 (FTP)
•	Port 22 (SSH)
•	Port 80 (HTTP)
•	Port 3306 (MySQL)
•	Many others
#Access Web Application:
Open browser in Kali:
http:// <target_ip>
http:// 192.168.56.101
	click on DVWA (Damn Vulnerable Web Application)
#Login:
Username: admin
Password: password
#Perform SQL Injection
Go to:
DVWA->Settings-> Set Security level-> low
DVWA → SQL Injection
Enter in User ID field:
1' OR '1'='1
Click-SUBMIT
#It will display all users
Query:
SELECT * FROM users WHERE id = '1' OR '1'='1';
Since '1'='1' is TRUE, database returns all records.
#Conclusion:
Concept	Learned 
  Port Scanning	Nmap
  Reconnaissance	Service detection
  Web Vulnerability	DVWA
  SQL Injection	Login bypass
  Input Validation	Why attack works


