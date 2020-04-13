import random
import matplotlib.pylab as plt

#number of throws required to fill all the urns
def collect_ones(n):
    urns = [0] * n
    ball = 0
    placesLeft = n
    while True:
        rand = random.randrange(0, n, 1)
        ball += 1
        if urns[rand] == 0:
            placesLeft -= 1
        urns[rand] += 1
        if placesLeft == 0:
            return ball

#number of throws required to fill with two balls at least one urn
def collect_two(n):
    urns = [0]*n
    ball = 0
    while True:
        rand = random.randrange(0,n,1)
        urns[rand] += 1
        ball += 1
        if urns[rand] == 2:
            return ball

list1 = []
list2 = []
nlist = []
exp = 500
urnlen = 500
n=1
while n < urnlen:
    asum = 0
    bsum = 0
    print(n)
    for e in range(1,exp):
        asum += collect_ones(n)
        bsum += collect_two(n)
    nlist.append(n)
    n+=1
    list1.append(asum/exp)
    list2.append(bsum/exp)


print(nlist)
plt.plot(nlist,list1,'.')
plt.xlabel("Number of urns")
plt.ylabel("Number of throws")
plt.title("Empty urns, n = %d" % n)
plt.show()

plt.plot(nlist, list2, '.')
plt.xlabel("Number of urns")
plt.ylabel("Number of throws")
plt.title("Urn with two, n = %d" % n)
plt.show()






