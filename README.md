Benchmarking workflow for data science algorithms
======

### Pre-steps/ configuration

1) [Install Docker](https://docs.docker.com/v17.09/engine/installation/) on your various servers/systems
2) Make sure the software (data science algorithm) you are developing is version controlled so you can push newer versions to GitHub
3) Create a benchmarking script that tells you what you want to know about your software's performance in terms of speed and accuracy
    - How well does it perform for a particular task, given a specific dataset

### Benchmarking steps

1) Release a version of your software - repeat subsequent steps for each new version
2) Create a docker image for installing your software on a linux distribution with the bare essential dependencies and running the benchmarks
    - Give it a name and a tag related to your software version and tag latest: ```docker build -t whenry/fedora-jboss:latest -t whenry/fedora-jboss:v2.1 .```
    - Make sure the benchmark script is identical
    - OR have an [automatic build](https://docs.docker.com/docker-hub/builds/) from GitHub set up
3) Push an image to Docker Hub and write an appropriate description
    - You may want a separate image for each machine you want to benchmark on, with the benchmarking script configured differently
4) Pull this image and run on your various systems/machines
5) Collect the performance stats from these machines and compare these with previous versions of the software
    - Perhaps have some kind of graph/chart that you update each time
    - We could save the benchmark results data in JSON files, similar to however [airspeed velocity](https://asv.readthedocs.io/en/stable/using.html) does it

Benchmarking infrastructure/ tool
=======

### Ideas

- [Incorporate benchmarks into continuous integration such as Jenkins](https://www.researchgate.net/publication/274738961_Including_Performance_Benchmarks_into_Continuous_Integration_to_Enable_DevOps)
 - There is a tool called [airspeed velocity](https://asv.readthedocs.io/en/stable/index.html) for benchmarking Python packages over their lifetime that generates an interactive web frontend for results e.g. for [numpy](https://pv.github.io/numpy-bench/) - perhaps this interface style is useful as inspiration?
 - We want a tool where you can submit a new algorithm to “compete” at a (data science) task that older algorithms have been benchmarked for. This could be a newer version of the same thing that’s supposed to be more efficient and/or accurate, or it could be a competing approach
