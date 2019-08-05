#!/usr/bin/python
'''
This script sets the MAX_NUM_THREADS variable and gets the configurable variables.
'''
import os
from subprocess import call
import math

N_EPOCHS = os.getenv("N_EPOCHS", 3)
SEED = os.getenv("SEED", 1337)


def set_env_variable(env_variable: str, value: str):
    call('export ' + env_variable + '="' + value + '"', shell=True)
    os.environ[env_variable] = value


# Dynamically set MAX_NUM_THREADS
ENV_MAX_NUM_THREADS = os.getenv("MAX_NUM_THREADS", None)
if ENV_MAX_NUM_THREADS:
    # Determine the number of availabel CPU resources, but limit to a max number
    if ENV_MAX_NUM_THREADS.lower() == "auto":
        ENV_MAX_NUM_THREADS = str(math.ceil(os.cpu_count()))
        try:
            # read out docker information - if docker limits cpu quota
            cpu_count = math.ceil(
                int(
                    os.popen('cat /sys/fs/cgroup/cpu/cpu.cfs_quota_us').read().
                    replace('\n', '')) / 100000)
            if cpu_count > 0 and cpu_count < os.cpu_count():
                ENV_MAX_NUM_THREADS = str(cpu_count)
        except:
            pass
        if not ENV_MAX_NUM_THREADS or not ENV_MAX_NUM_THREADS.isnumeric(
        ) or ENV_MAX_NUM_THREADS == "0":
            ENV_MAX_NUM_THREADS = "4"

        if int(ENV_MAX_NUM_THREADS) > 8:
            # there should be atleast one thread less compared to cores
            ENV_MAX_NUM_THREADS = str(int(ENV_MAX_NUM_THREADS) - 1)

        # set a maximum of 32, in most cases too many threads are adding too much overhead
        if int(ENV_MAX_NUM_THREADS) > 32:
            ENV_MAX_NUM_THREADS = "32"

    # only set if it is not None or empty
    set_env_variable("OMP_NUM_THREADS", ENV_MAX_NUM_THREADS)  # OpenMP
    set_env_variable("OPENBLAS_NUM_THREADS", ENV_MAX_NUM_THREADS)  # OpenBLAS
    set_env_variable("MKL_NUM_THREADS", ENV_MAX_NUM_THREADS)  # MKL
    set_env_variable("VECLIB_MAXIMUM_THREADS",
                     ENV_MAX_NUM_THREADS)  # Accelerate
    set_env_variable("NUMEXPR_NUM_THREADS", ENV_MAX_NUM_THREADS)  # Numexpr
    set_env_variable("NUMBA_NUM_THREADS", ENV_MAX_NUM_THREADS)  # Numba
