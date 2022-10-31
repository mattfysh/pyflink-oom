# out of memory error

1. run `docker-compose up` to build and standup cluster
2. in another terminal, ssh into the job manager, e.g. `docker exec -it <jobmanager> bash`
3. once inside, run `./bin/flink run --python /opt/test/app.py`

you should see an outofmemoryerror occur
