#!/bin/sh
echo "Переходим в roor"
cd ~/
echo "root:"
ls
echo "Переходим в /home/irina"
cd /home/irina
echo "/home/irina:"
ls
echo "Переходим в папку с проектом"
cd Рабочий\ стол/Learn/WEB/webproject/phphandmade
echo "/phphandmade:"
ls
docker-compose stop
echo "База остановлена"

