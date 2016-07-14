# assumes docker container is local - otherwise pulls and runs
docker run -d -it --name=models -v $PWD:/code watrhub/dev_environment:1.1

docker exec -it models bash