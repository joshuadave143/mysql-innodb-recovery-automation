for file in rasp-img/raspi-app/var/lib/mysql/pisofi/*.frm; do
    # Extract the base name (without extension) from the .frm file
    table_name=$(basename "$file" .frm)
    # Dump the structure using dbsake and save to a .sql file
    ./dbsake frmdump "$file" > "$table_name.sql"
done
