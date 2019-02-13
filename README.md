Benchmarking workflow for data science algorithms
======

### Pre-steps/ configuration

1) [Install Docker](https://docs.docker.com/v17.09/engine/installation/) on your various servers/systems
2) Make sure the software (data science algorithm) you are developing is version controlled so you can push newer versions to GitHub
3) Create a benchmarking script that tells you what you want to know about your software's performance in terms of speed and accuracy
    - How well does it perform for a particular task, given a specific dataset

### Benchmarking steps

1) Release a version of your software - repeat subsequent steps for each new version
2) Create a docker image for installing your software on a linux distribution with the bare essential dependencies and running the benchmarks (an alternative to Docker is Singularity and you can create either using [HPC container maker](https://github.com/NVIDIA/hpc-container-maker))
    - Give it a name and a tag related to your software version and tag latest: ```docker build -t whenry/fedora-jboss:latest -t whenry/fedora-jboss:v2.1 .```
    - Make sure the benchmark script is identical. This should be run at the end of the Dockerfile e.g. ```CMD python benchmarks.py``` but you may also want to include arguments, see step 4 below*
    - It is however possible to change the benchmark script at run: ```docker run -v path/to/replacement/benchmark.py:path/within/container/benchmarks.py -t edwardchalstrey/benchmark_test:latest python benchmarks.py``` (in this case you wouldn't need to add ```python benchmarks.py``` if that was what was already specified by CMD in the Dockerfile)
    - OR have an [automatic build](https://docs.docker.com/docker-hub/builds/) from GitHub set up
3) Push an image to Docker Hub and write an appropriate description
    - You may want a separate image for each machine you want to benchmark on, with the benchmarking script configured differently
4) Pull this image and run on your various systems/machines with ```docker run``` (* you can change the arguments if you have specified some e.g. ```docker run -t edwardchalstrey/benchmark_test:latest python benchmarks.py x y z``` where x, y and z are input/benchmark configuration values)
    - The CMD at the end of the Dockerfile (or in command line as in 4 above) can use mpi e.g. ```mpirun -n 4 python script.py``` - in this case you'd need ```mpi4py``` installed
5) Collect the performance stats from these machines and compare these with previous versions of the software
    - Perhaps have some kind of graph/chart that you update each time
    - We could save the benchmark results data in JSON files, similar to however [airspeed velocity](https://asv.readthedocs.io/en/stable/using.html) does it

Benchmarking infrastructure/ tool
=======

### Ideas

- [Incorporate benchmarks into continuous integration such as Jenkins](https://www.researchgate.net/publication/274738961_Including_Performance_Benchmarks_into_Continuous_Integration_to_Enable_DevOps)
 - There is a tool called [airspeed velocity](https://asv.readthedocs.io/en/stable/index.html) for benchmarking Python packages over their lifetime that generates an interactive web frontend for results e.g. for [numpy](https://pv.github.io/numpy-bench/) - perhaps this interface style is useful as inspiration?
 - We want a tool where you can submit a new algorithm to “compete” at a (data science) task that older algorithms have been benchmarked for. This could be a newer version of the same thing that’s supposed to be more efficient and/or accurate, or it could be a competing approach. Something similar to this has been done at Stanford called [DAWNBench](https://dawn.cs.stanford.edu/benchmark/)
 
 ### Challenges
 
 1. **Customisability and scope** - What is the scope of the benchmarking infrastructure in terms of the algorithms it tests
 2. **Metrics** - What does it actually measure? Consider performance (speed), correctness and convergence across different computing environments (how consistent are the metrics). What about cost and things like that? Look at the metrics used by [DAWNBench](https://dawn.cs.stanford.edu/benchmark/)
 3. Does the workflow/ infrastructure we develop hold up **at scale** and does it only alter native performance of the algorithms in a negligible capacity
 4. **Validation** - how many times is a benchmark run? Do we report median results or something like that? What about variance?
 5. **Presentation** - Are we going to build an interface and how do we show the results?
 
 
