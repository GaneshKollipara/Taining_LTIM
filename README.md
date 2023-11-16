# Taining_LTIM
In this repository we are practicing the git hub demo at LTIM


data_list=[['Sushithi.Chakraborty_1','ITP',34],['Sushithi.Chakraborty_2','ITP',55]
           ,['Deepali.Gatade_1','ITP',77],['Mukul.kumar.Singh_1','NPV',65]]
score1=pd.DataFrame(data_list,columns=['Name','Subject','Score'])
score1


data_list2=[['Deepali.Gatade_1','SQL',74],['Deepali.Gatade_2','SLC',57]
           ,['Mukul.kumar.Singh_1','SLC','-'],['Rakesh.Sriramula_1','NPV',61]]
score2=pd.DataFrame(data_list2,columns=['Name','Subject','Score'])
score2


=================================================================================================
MONGODB INSTALL IN CENT_OS 
=================================================================================================

sudo nano /etc/yum.repos.d/mongodb-org.repo
#insert following lines in the file
[mongodb-org-6.0]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/6.0/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-6.0.asc
Save file using Ctrl+O > Enter > Ctrl+v
yum repolist
sudo yum install mongodb-org
sudo systemctl start mongod
sudo systemctl status mongod
sudo systemctl stop mongod
sudo tail /var/log/mongodb/mongod.log
mongosh
