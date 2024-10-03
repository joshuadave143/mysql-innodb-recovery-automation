# mysql-innodb-recovery-automation
Todo
1. show menu 
    = Create database and import data after recover
    = Recover the database structure and data only
2. Recover the table schema and save it to SQL file /
3. Use the result of the recovery to recover the data from data directory
4. Create the database
5. Import the data that recover to the database
<!-- ./stream_parser -f ../../rasp-img/raspi-app/var/lib/mysql/pisofi/users.ibd  -->
<!-- ./c_parser -f pages-users.ibd/FIL_PAGE_INDEX/0000000000002322.page -t psiofi/users.sql > users 2> users.sql -->
<!-- ./c_parser -f pages-users.ibd/FIL_PAGE_INDEX/0000000000002322.page -t psiofi/users.sql -b pages-users.ibd/FIL_PAGE_TYPE_BLOB > users 2> users.sql -->
https://github.com/joshuadave143/undrop-for-innodb/tree/master
https://github.com/abg/dbsake