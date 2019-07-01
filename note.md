I’ll try to explain the easiest way to use a .pfx file that can be used to install SSL on NGINX.

We’ll start by extracting the CRT file using openssl with the following command

openssl pkcs12 -in ./YOUR-PFX-FILE.pfx -clcerts -nokeys -out domain.crt
Followed by extracting the private key with the following command

openssl pkcs12 -in ./YOUR-PFX-FILE.pfx -nocerts -nodes -out domain.rsa

[original](https://blog.knoldus.com/easiest-way-to-setup-ssl-on-nginx-using-pfx-files/)
