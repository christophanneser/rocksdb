../db_bench \
	-benchmarks=fillrandom –perf_level=3 \
	-use_direct_io_for_flush_and_compaction=true \
	-use_direct_reads=true \
	-cache_size=268435456 \
	-key_size=48 \
	-value_size=43 \
	-num=50000000
