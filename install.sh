if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi
echo checking dependencies...
apt install python3
echo checking pip dependencies...
pip install -r requirements.txt
mkdir /opt/mdb/
cp src/ /opt/mdb/
cp mdb.service /etc/systemd/system/
echo starting bot service...
systemctl start mdb.service
echo service started! install completed
