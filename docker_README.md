# Docker Build and Run

## Setup Scrapper config
Edit the following file as needed : `journals2data/src/journals2data/conf/journals2data.docker.conf`

NOTE : the [ general filepaths ] attributes are fixed paths designed according to the container's file structure,  and **are not intended to be modified** for a standard usage of the scrapper.



Refer to Docker Run section for more details concerning volumes

## Docker Build

Run the following command in the `python/journals2data` directory (where `Dockerfile` is located)

```shell
 sudo docker build -t scrapper . 
```

It may take a while. Make sure that the process ends with an output message such as : 
```shell
Successfully built d72eed7a2836
Successfully tagged scrapper:latest
```



## Docker Run

### Run Parameters

In order to avoid re-building the whole docker image each time we need to change the newspaper sources or the models,
the corresponding files are not built-in, we mount them when we run the docker container as follows

Just run your container : 
```bash
sudo docker run --rm -i -t  \
-network=host \
--name scrapper \
--mount type=bind,source=<absolute_path_to_local_models-directory>,target=/models \
-v <absolute_path_to_local_newspaper_sources_csv_file>:/journals2data/src/journals2data/conf/csv/csv_docker_config.csv \
-v <absolute_path_to_local_config_file>:/journals2data/src/conf/journals2data.docker.conf
scrapper \
```

NOTE : For a standard usage, `<absolute_path_to_local_config_file>` shoud be `<absolute_path_to_repo>/journals2data/src/journals2data/conf/journals2data.docker.conf`


In this case :

* `-network=host` is used to make the programs inside the Docker container look like they are running on the host itself, from the perspective of the network. Use this parameter if you index data in an Elasticsearch cluster.
* `--name` defines the name we give to the running container
* `--mount` allows to mount the model directory externaly, instead of building it into the image
* `-v` allows to mount the file containing newspaper sources and the config, as follows
  * `-v <host_file_path>:/<container_file_path>`

Example : 
```bash
sudo docker run --rm -i -t  \
-network=host \
--name scrapper \
--mount type=bind,source=$HOME/PycharmProjects/journals2data/models/,target=/models \ 
-v $HOME/csv_docker_config.csv:/journals2data/src/journals2data/conf/csv/csv_docker_config.csv \ 
-v $HOME/PycharmProjects/python/journals2data/src/journals2data/conf/journals2data.docker.conf
scrapper \
```

### Run as a background task

To run the container as a background task, just add the `-d` flag to the previous docker run command.

To list the containers running, just run  :
```bash
sudo docker ps
```

You should see the container in the output

```bash
CONTAINER ID   IMAGE      COMMAND                  CREATED          STATUS          PORTS     NAMES
291b0213025e   scrapper   "conda run --no-capt…"   12 seconds ago   Up 11 seconds             scrapper
```



If you want to attach to the running container in your terminal, just run :

```bash
docker attach --name scrapper
```

To detach from the container, press `CTRL+P` and `CTRL+Q`