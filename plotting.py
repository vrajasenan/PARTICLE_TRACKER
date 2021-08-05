import matplotlib.pyplot as plt
import numpy as np
import math
resultbefore=[]



resultafter=[]
















meanbefore = np.mean(resultbefore)
stdbefore = np.std(resultbefore)
meanafter = np.mean(resultafter)
stdafter = np.std(resultafter)
meanbefore = round(meanbefore, 4 - int(math. floor(math. log10(abs(meanbefore)))) - 1)
meanafter = round(meanafter, 4 - int(math. floor(math. log10(abs(meanafter)))) - 1)
stdbefore= round(stdbefore, 4 - int(math. floor(math. log10(abs(stdbefore)))) - 1)
stdafter= round(stdafter, 4 - int(math. floor(math. log10(abs(stdafter)))) - 1)




#print("mean in um :",meanbefore)
#print("std in um :",stdbefore)
#print("mean in um :",meanafter)
#print("std in um :",stdafter)

bins=range(0, 500 + 20, 20)

#plt.hist(resultbefore, bins, alpha=0.4, label='before expansion mu:'+str(meanbefore)+"um, std:"+str(stdbefore),density=True,cumulative=True)
#plt.hist(resultafter, bins, alpha=0.4, label='after expansion, mu:'+str(meanafter)+"um, std:"+str(stdafter),density=True,cumulative=True)
plt.hist(resultbefore, bins, alpha=0.5, label='before expansion',density=True,cumulative=True)
plt.hist(resultafter, bins, alpha=0.5, label='after expansion',density=True,cumulative=True)
plt.xticks(range(0, 500 + 50, 50))
plt.title("117:702ul/mn")
plt.xlabel('Spacing (um)')
plt.ylabel('% of instances')
plt.legend(loc='upper left')
plt.show()
