echo "...Export from docker and save to init/shininglight.sql.gz"
docker run -i --rm  --net=host -e PGPASSWORD=dev2original  postgres /usr/bin/pg_dump -h localhost -U root tutorial_pg | gzip -9 -f  > init/tutorial_pg.sql.gz
