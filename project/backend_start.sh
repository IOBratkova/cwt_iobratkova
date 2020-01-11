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
echo "DEBUG=1" > .env
#if [[ $1 == 1 ]]
#    then echo "Режим тестов"
#else
echo "Тестовый режим"
#fi
docker-compose up -d
echo "База запущена"

