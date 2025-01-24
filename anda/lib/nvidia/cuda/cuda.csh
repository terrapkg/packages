if ( -x /usr/bin/cuda-g++ ) then
  setenv HOST_COMPILER /usr/bin/cuda-g++
endif

if ( -d /usr/include/cuda ) then
  setenv CUDA_INCLUDE_DIRS /usr/include
  setenv CUDA_INC_PATH /usr/include
endif

setenv CUDA_ROOT /usr
