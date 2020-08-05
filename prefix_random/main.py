import numpy as np
import matplotlib.pyplot as plt
import os

class KeyRangeCounter:
    def __init__(self, bits, filename):
        self.bits = bits
        self.hash_dict = dict()
        self.filename = "phase" + filename.replace(".txt", "")

    def add(self, k, v):
        index = k >> (64 - self.bits)
        if index in self.hash_dict:
            record = self.hash_dict[index]
            record[0] += 1
            record[1] += v
            self.hash_dict[index] = record
        else:
            self.hash_dict[index] = [1, v]

    def write_stats(self):
        out_file = open("out/" + self.filename + str(self.bits) + ".txt", "w")
        access_stats = []
        for k in self.hash_dict:
            access_stats.append((k,self.hash_dict[k]))

        access_stats.sort(key=lambda x: x[0])

        prefix_range = []
        prefix_range_count = []
        prefix_range_sum = []

        for v in access_stats:
            out_file.write(str(v[0]) + "," + str(v[1]) + "\n")
            if v[1][0] > 0 and True: #v[0] < 50:
                prefix_range.append(v[0])
                prefix_range_count.append(v[1][0])
                prefix_range_sum.append(v[1][1])

        fig, ax = plt.subplots()
        counts = ax.bar(prefix_range, prefix_range_count,)
        sums = ax.bar(prefix_range, prefix_range_sum, bottom=prefix_range_count)
        ax.legend((counts, sums), ("different keys", "overall lookups"))
        ax.set_title("prefix ranges: " + str(self.bits) + " bit")
        fig.savefig("out/" + self.filename + str(self.bits) + ".pdf")
        plt.close()
        out_file.close()


if __name__ == "__main__":
    for filename in os.listdir("./workload_phases"):
        print(filename)
        f = open("workload_phases/" + filename)
        content = f.readlines()
        f.close()

        d = dict()
        for l in content:
            l = l.replace("\n", "")
            if int(l) in d:
                d[int(l)] += 1
            else:
                d[int(l)] = 1

        access_counter = []
        keys_with_access = []
        for k in d:
            access_counter.append(d[k])
            keys_with_access.append((k, d[k]))


        for bits in range(40, 49):
            print("bits: " + str(bits))
            key_range_counter = KeyRangeCounter(bits, filename)
            for k,v in keys_with_access:
                key_range_counter.add(k,v)
            key_range_counter.write_stats()


        access_counter.sort()
        print(access_counter[10:])
        print(len(d))
