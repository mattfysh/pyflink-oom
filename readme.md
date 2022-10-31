# out of memory error

1. run `docker-compose up` to build and standup cluster
2. in another terminal, ssh into the task manager, e.g. `docker exec -it <container> bash`
3. run `./bin/flink --python /opt/test/app.py`

you should see an outofmemoryerror occur
