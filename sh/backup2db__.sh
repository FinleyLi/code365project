#!/bin/bash 
cd /home/bkup__ 
#echo 'Backup ALL Database' 
date 
for db in calendar counseling coursehist netaccess socialgrouplink stucis sylla$ 
do 
        sqlfile="/home/bkup__/db_back/$db`date +%Y%m%d%H%M`.sql" 
        mysqldump -u bkup__ -p1o4zp4 $db > $sqlfile 
        FN="/home/bkup__/$db`date +%Y%m%d%H%M`_enc.sql.tar.gz" 
        #壓縮打包並加密 
        tar -cpz $sqlfile | openssl enc -e -aes256 -k ndb__pwd -out $FN 
        #傳輸 
        #壓縮傳輸後移除原檔 
        scp -P 6561 $FN db__.is__.net:/backup/ndb__/$db 
        rm -f $FN 
        echo "$db 已遠端備份至 NAS" 
done 