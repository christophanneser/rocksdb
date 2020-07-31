# generate prefix random workload as described here https://www.usenix.org/system/files/fast20-cao_zhichao.pdf

# fill database with 50 M (k,v)-pairs
./fill_db.sh

# generate actual prefix random workload
./prefix_random.sh
