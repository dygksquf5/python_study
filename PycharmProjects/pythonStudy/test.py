import time
import matplotlib.pyplot as plt
import pandas as pd
import requests

# a = [[1,2,3,4,],[1,2,3,4],['a','b','c','d'], [3,2,1,4,3]]
#
# b = pd.DataFrame(a)
# print(b.head())
#
# c = pd.DataFrame(a,columns=['하나','둘','셋','넷','다섯'])
#
# print(c.head())

resp = requests.get(url='https://blockchain.info/latestblock')
data = resp.json()
nHeight = data['height']
# print(data)

mining = []

for n in range(nHeight, nHeight-10, -1):
    url = 'https://blockchain.info/block-height/'+ str(n) + '?format=json'
    resp = requests.get(url=url)
    data = resp.json()
    block = data['blocks'][0]

    stime = block['time']
    addr = block['tx'][0]['out'][0]['script']
    value = block['tx'][0]['out'][0]['value']

    ts = time.gmtime(stime)
    date = time.strftime("%Y-%m-%d %H:%M:%S", ts)

    mining.append([date,addr,value])
    print("#%d : %s\t%s\t%f" % (n, date, addr, value*1e-8))

df = pd.DataFrame(mining, columns=['Date','Address','Reward'])
grp = df.groupby('Address').Address.count()
print()
print(grp)

print(plt.figure(figsize=(6,3)))
print(plt.title("Miner's Address"))
x = list(range(1, len(grp.values)+1))
plt.bar(x, grp.values, width=1, color="red", edgecolor='black', linewidth=0.5, alpha=0.5)
plt.show()


