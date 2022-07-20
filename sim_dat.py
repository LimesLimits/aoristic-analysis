import numpy as np
import random

dat_array = np.genfromtxt("dat_vondst_cum.txt")
simres_site_file = open('simres_site.txt', 'w')
simres_sum_file = open('simres_sum.txt', 'w')
simres_cum_file = open('simres_cum.txt', 'w')

#selection of subset per site number

for site_num in range(1,5006):
    sim_set = dat_array[dat_array[:, 0] == site_num]

#count number of records in subset

    nrecs = sim_set.shape[0]

#run simulations for this site

    nsims = 1000

#create 2 empty arrays to hold the results of simulation for this site

    simres_site = np.zeros([nsims,9])

    for m in range(0,nsims):

#update the site number in the corresponding row of the results array

        simres_site[m,0] = site_num

#check for the occurrence of finds in each of the 7 periods
        
#if a random number in the range (0,1) is smaller than the probability for the period,
#then increase the number of artefacts for this period by 1
        
#repeat this for each row in the subset and for the number of finds per row

        for n in range(0,nrecs):

#find the number of finds for this row
            
             nfinds = int(sim_set[n,8])
             if nfinds == 9999:
                  nfinds = 1

             for p in range(0,nfinds):

#register the total number of finds for this site in the last column as a check
                 
                simres_site[m,8] = simres_site[m,8] + 1

# create a random number in the range (0,1)

                rand_num = random.random()

# now check each record (columns 1 thru 7) per row and number of finds in the subset for the *cumulative* probability of this period containing a find
# if this is the case, then skip the remaining columns

                col_found = 0
                
                for q in range(1,8):

                    if (rand_num < sim_set[n,q] and col_found == 0):
                          simres_site[m,q] = simres_site[m,q] + 1
                              
                          col_found = 1

# write the result to the output text file (np.savetxt appends)

    np.savetxt(simres_site_file, simres_site, fmt="%i")


# summarize the results and store them in a new array
# make sure that the range of possible results is between zero and the total number of finds

    simres_sum = np.zeros([int(simres_site[0,8]) + 1,9])
    simres_cum = np.zeros([int(simres_site[0,8]) + 1,9])

    for r in range(0, int(simres_site[0,8]) + 1):
        simres_sum[r, 0] = site_num
        simres_sum[r, 1] = r
        
        simres_cum[r, 0] = site_num
        simres_cum[r, 1] = r

# run through each column in the simulation results

        for s in range (1, 8):
            find_count = 0

            for t in range (0, nsims):

                if int(simres_site[t, s]) == r:
                    find_count = find_count + 1

            simres_sum[r, s + 1] = find_count
            if r == 0:
                simres_cum[r, s + 1] = simres_sum[r, s + 1]
            else:
                simres_cum[r, s + 1] = simres_cum[r - 1, s + 1] + simres_sum[r, s + 1]

    for t in range(0, int(simres_site[0,8]) + 1):
        for u in range (2, 9):
            simres_cum[t, u] = nsims - simres_cum[t, u]

    print ("Results stored for site ", site_num)

# save summary of results to text file

    np.savetxt(simres_sum_file, simres_sum, fmt="%i")
    np.savetxt(simres_cum_file, simres_cum, fmt="%i")

# close the text files

simres_site_file.close()
simres_sum_file.close()
simres_cum_file.close()
