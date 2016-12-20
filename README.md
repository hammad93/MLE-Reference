# MLE-Reference
### Running remote jupyter notebook using Cloud 9
* updated 12/19/16 *

1) Download proper libraries. Miniconda (http://conda.pydata.org/miniconda.html) is a good choice because its small
    - `wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh`
    - `bash Miniconda2-latest-Linux-x86_64.sh`
2) Download and install jupyter notebook after restarting terminal
    - `conda install jupyter`
3) Run the following command for remote access through http
    - `jupyter notebook --ip=0.0.0.0 --port=8080 --no-browser`