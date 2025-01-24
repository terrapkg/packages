if [ -x /usr/bin/cuda-g++ ]; then
  export HOST_COMPILER=/usr/bin/cuda-g++
fi

if [ -d /usr/include/cuda ]; then
  export CUDA_INCLUDE_DIRS=/usr/include
  export CUDA_INC_PATH=/usr/include
fi

export CUDA_ROOT=/usr
