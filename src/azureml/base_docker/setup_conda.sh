# Go to home directory
apt-get update
apt-get upgrade -y
apt-get install -y wget
cd ~
wget https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh
bash Anaconda3-4.2.0-Linux-x86_64.sh -b -p ~/anaconda
rm Anaconda3-4.2.0-Linux-x86_64.sh
echo 'export PATH="~/anaconda/bin:$PATH"' >> ~/.bashrc 
