In these implementations we are going to
.......Install MySQL on my two web1 and web 2 servers
.......Create a new user on both the two web servers
.......Create a database in my web1 server(master) to replicate from
.......Create a new user for the replica(slave)
.......Setup primary replica infrastructure using MySql
.......Create a MySql back up 
INSTALLING MYSQL 5.7
 Download the MySQL repository by executing the following command:

wget https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb
fter the MySQL package has been successfully downloaded, install it:

sudo dpkg -i mysql-apt-config_0.8.12-1_all.deb

Next, update the APT repository:

sudo apt update
Now that you have a MySQL 5.7 repository in your system, you can proceed to install it. For this, run the following command:

sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*
