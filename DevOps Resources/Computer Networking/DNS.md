## Domain Name System
DNS and how it works

## What is DNS

**DNS stands for Domain Name System**

- It is simply a technology that allows anyone to resolve hostname like google.com , microsoft.com something like IP-ADDRESS.
- For example -> google.com as 142.250.193.46.
- It’s the naming database that locates and translates internet domain names into IP addresses. Similar to a phone contact list which matches the contact name to it’s phone number.
- As more than 1 person can access the same domain name at the same time so a domain name can correspond to more than one IP address Each will receive a unique IP address from different servers.
- If we will have only one IP address then that will make everyone wait up for their turn for opening the domain name.
- The main task of DNS is to find the IP Address associated with the given domain name. The process of finding the IP Address is known as DNS Lookup.

## DNS Resolver
- Basically, DNS Resolver is the hard-coded IP Address that our computers use to connect to any site (ex — google.com)

## How DNS works
- When you will type www.example.com then it will search for www.example.com.(Dot at the end of the call). That Dot at the end represent's The ROOT the internet's namespace.


- When you will search for www.google.com. then our OS and Browser will search in themselves for that URL. It could be configured into a computer or it could be cache (memory).
- Now if both OS and Browser don’t know the IP address of this domain name then they are configured to ask for that to Resolving Name Server. RNS is configured both manually and automatically.
- It’s possible that RNSs don’t have IP addrress in their memory or cache but they do know whom to ask about this(The ROOT) and that is .com name server.
- .com name server or TLD a name server may don't know what's but they do know where to find that and that is Autorative Name Server (ANS).
- TLD knows which ANS we can ask for this Registrar as when someone buys a domain then the registrar is told which ANS to use for this domain. They notify the organization responsible for Top Level Domain which is Registry and tell them to update TLD Name Server.
- Now ANS tells us the IP address which we put into cache and pass to the OS and then OS will pass that to the Web Browser and the browser will make a connection to the IP address and displays our search.
- As we already have saved that IP address as cacheso that in the future if we will ever search for the same IP Address then it will save some time.

## Vulnerabilities
- Cache Poisoning
- Malicious creation of Misleading Domain Names for fishing attacks
