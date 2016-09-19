n=5
for i in `seq 1 ${n}`
do
  echo $i;
  adduser --gecos "" --disabled-password test${i}
  echo test${i}:SoftwareC | chpasswd

  mkdir -p /home/test${i}/.ssh
  echo 'Host *\n  StrictHostKeyChecking no\n  ForwardX11 yes' > /home/test${i}/.ssh/config
  ssh-keygen -f /home/test${i}/.ssh/id_rsa -t rsa -N ''
  cp /home/test${i}/.ssh/id_rsa.pub /home/test${i}/.ssh/authorized_keys
  chown -R test${i}:test${i} /home/test${i}/.ssh
  chmod 600 /home/test${i}/.ssh/config
  
  echo 'export PATH=$PATH:/opt/openlava-3.3/bin/' >> /home/test${i}/.profile
  touch /home/test${i}/.Xauthority
  chown -R test${i}:test${i} /home/test${i}/.Xauthority
  
done
