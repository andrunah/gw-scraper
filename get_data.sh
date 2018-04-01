#!/usr/bin/env bash

USERAGENT="Mozilla/5.0 (Windows; U; Windows NT 5.1; ru; rv:1.9.2) Gecko/20100115 Firefox/3.6"
LOGIN=$1
PASSWD=$2

PAGE="http://www.ganjawars.ru/object.php?id=69403&page=oncoming1&sid=116"
PAGE_WARS="http://www.ganjawars.ru/wargroup.php?war=attacks"
SITE="https://www.ganjawars.ru"; curl -A "$USERAGENT" -e "$SITE"/login.php "$SITE"/login.php > login
LOGINKEY=`grep "loginkey " login | cut -d "'" -f 2`; LOGINKEYMD=`grep "loginkeymd " login | cut -d "'" -f 2`; sleep 1; curl -A "$USERAGENT" -d "resl=Null.&time=Null.&date=Null.&pwdmd5=Null.&pass1=&loginkey=$LOGINKEY&loginkeymd=$LOGINKEYMD&login=$LOGIN&pass=$PASSWD" "$SITE"/login.php -e "$SITE"/login.php -D headers_cookies
curl -b headers_cookies "$PAGE" -A "$USERAGENT" -e "$PAGE" > port_list.html
# curl -b headers_cookies "$PAGE_WARS" -A "$USERAGENT" -e "$PAGE_WARS" > wars.html ; iconv -f cp1251 -t utf-8 wars.html > attack_list.html
rm login headers_cookies port_116.html