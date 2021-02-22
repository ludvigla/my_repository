
from mpi4py import MPI
import numpy as np
import sys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n = int(sys.argv[1])

if rank == 0:
    sendbuf = np.arange(float(n))
    
    # count: the size of each sub-task
    ave, res = divmod(sendbuf.size, size)
    count = [ave + 1 if p < res else ave for p in range(size)]
    count = np.array(count)
    
    # displacement: the starting index of each sub-task
    displ = [sum(count[:p]) for p in range(size)]
    displ = np.array(displ)
else:
    sendbuf = None
    # initialize count on worker processes
    count = np.zeros(size, dtype=np.int)
    displ = None
    
# broadcast count
comm.Bcast(count, root=0)

# initialize recvbuf on all processes
recvbuf = np.zeros(count[rank])

comm.Scatterv([sendbuf, count, displ, MPI.DOUBLE], recvbuf, root=0)

partial_sum = np.zeros(1)
partial_sum[0] = sum(recvbuf)
print('Partial sum on process {} is:'.format(rank), partial_sum[0])

total_sum = np.zeros(1)
comm.Reduce(partial_sum, total_sum, op=MPI.SUM, root=0)
if comm.Get_rank() == 0:
    print('After Reduce, total sum on process 0 is:', total_sum[0])
