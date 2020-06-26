I’ll try to explain the easiest way to use a .pfx file that can be used to install SSL on NGINX.

We’ll start by extracting the CRT file using openssl with the following command

openssl pkcs12 -in ./YOUR-PFX-FILE.pfx -clcerts -nokeys -out domain.crt
Followed by extracting the private key with the following command

openssl pkcs12 -in ./YOUR-PFX-FILE.pfx -nocerts -nodes -out domain.rsa

[original](https://blog.knoldus.com/easiest-way-to-setup-ssl-on-nginx-using-pfx-files/)

from web
test

Retrofit2


docker 
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)


centos安装vim8
sudo yum install ruby ruby-devel lua lua-devel luajit \
luajit-devel ctags git python python-devel \
python36 python36-devel tcl-devel \
perl perl-devel perl-Extutils-ParseXS \
perl-ExtUtils-XSpp perl-ExtUtils-CBuilder \
perl-ExtUtils-Embed libX* ncurses-devel gtk2-devel

	./configure \
	  --enable-fail-if-missing \
	  --disable-nls \
	  --enable-cscope \
	  --enable-gui=no \
	  --enable-multibyte  \
	  --enable-python3interp=yes \
	  --enable-rubyinterp \
	  --prefix=/root/dypan/.local/vim \
	  --with-python3-command=python3.6 \
	  --with-python3-config-dir=/usr/lib64/python3.6/config-3.6m-x86_64-linux-gnu/ \
	  --with-features=huge  \
	  --with-tlib=ncurses \
	  --without-x
  
docker run -it --rm -v pgdata:/var/lib/postgresql/data -p 5432:5432 postgres:9.6


Caused by: org.apache.kafka.clients.consumer.CommitFailedException: Commit cannot be completed since the group has already rebalanced and assigned the partitions to another member. This means that the time between subsequent calls to poll() was longer than the configured max.poll.interval.ms, which typically implies that the poll loop is spending too much time message processing. You can address this either by increasing the session timeout or by reducing the maximum size of batches returned in poll() with max.poll.records.

https://twitter.com/bryanl/status/1218999339311386628?s=12

链接地址：https://pan.baidu.com/s/10jD8Odq1Cx9WpzR98lqOkQ
提取密码：rqnw
