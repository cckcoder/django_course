echo "...Delete all tables from the postgres db"
docker exec -i postgres /bin/bash -c "export PGPASSWORD=dev2original && /usr/bin/psql -U root tutorial_pg -c  'DROP SCHEMA public CASCADE; CREATE SCHEMA public'"
echo "...Import init/tutorial_pg.sql.gz to postgress"
gunzip < init/tutorial_pg.sql.gz | docker exec -i postgres /bin/bash -c "export PGPASSWORD=dev2original && /usr/bin/psql -U root tutorial_pg"

