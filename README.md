Benchmarking workflow
======

1) Install Docker
2) Release a version of your software
3) Create a benchmarking script that tells you what you want to know about your software's performance and accuracy
3) Create a docker image for installing your software on a linux distribution with the bare essential dependencies and running the benchmarks
4) Upload a container to Docker Hub
5) Run this container on various systems
6) Collect the performance stats from these machines and compare these with previous versions of the software
