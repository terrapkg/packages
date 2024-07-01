# just a Makefile parallel_test.sh uses to run stuff in parallel with make
%:
	$(MAKE) -j1 -C .test/tree/$* $*

t-exec-%:
	$(MAKE) -j1 -C ".test/tree/t-exec-$*" \
		TEST_SSH_PORT=10$*0 \
		SKIP_LTESTS="$(shell cat .test/ltests/not-in/$*)" \
		BUILDDIR="$(shell pwd)/.test/tree/t-exec-$*" \
		TEST_SHELL=sh \
		MAKE=make \
		TEST_SSH_TRACE=yes \
		TEST_SSH_FAIL_FATAL=yes \
		t-exec \
