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
cd Рабочий\ стол/Learn/WEB/webproject/phphandmade/frontend
echo "/phphandmade/frontend:"
ls
echo "Запускаем сервер"
npm run serve
