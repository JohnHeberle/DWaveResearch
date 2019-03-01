# DWaveResearch

The goal of this repository is to document my usage of the DWave quantum computer and to provide a complete reference for those begining to use the DWave Leap SDK. I will document any useful documentation, YouTube vidoes, or forumns that will allow individuals who have no prior expirence  with quantum computers to effectively leverage the benefits of quantum computation and the DWave Leap SDK for traditional programs.

## Getting Started

In order to begin interacting with the quantum computer, a virtual environment must be created. A great resource to walk a new user through this process is:

```
MacOS: https://www.youtube.com/watch?v=tCrbGO5oTDs
Windows: https://www.youtube.com/watch?v=Kdy3TOu6Lx4
Linux: https://www.youtube.com/watch?v=4L7fMdBMqVU
```
Once the steps outlined in this video are complete, within the virtual environment, the user should be able to execute the code below and recieve something similar to the following output.
```
dwave ping
```
```
Using endpoint: https://cloud.dwavesys.com/sapi
Using solver: DW_2000Q_2_1
Submitted problem ID: Redacted

Wall clock time:
 * Solver definition fetch: 799.372 ms
 * Problem submit and results fetch: 2108.534 ms
 * Total: 2907.906 ms

QPU timing:
 * total_real_time = 7752 us
 * qpu_access_overhead_time = 3958 us
 * anneal_time_per_run = 20 us
 * post_processing_overhead_time = 409 us
 * qpu_sampling_time = 164 us
 * readout_time_per_run = 123 us
 * qpu_delay_time_per_sample = 21 us
 * qpu_anneal_time_per_sample = 20 us
 * total_post_processing_time = 409 us
 * qpu_programming_time = 7588 us
 * run_time_chip = 164 us
 * qpu_access_time = 7752 us
 * qpu_readout_time_per_sample = 123 us
```

## First Program
After successfully setting up a virtual environment, the user can begin to expirament with writting python scripts to execute on the DWave quantum computer. An useful resource for this process is the following video provided by DWave:
```
https://www.youtube.com/watch?v=ckJ59gsFllU
```
The code used in the example in the video is contained within the repository under the ocean_tools_suite_Example directory. The python script can be executed by `python ocean_tools_suite_Example.py` and should produce and output similar to the following ![antenasresult1](https://user-images.githubusercontent.com/30187786/53666059-18e66480-3c3b-11e9-9653-244f9f0492b6.png)

