import numpy as np
import matplotlib as mpl
mpl.use('Agg') #silent mode
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker

#------------------ FONT_setup ----------------------
font = {'family' : 'arial', 
    'color'  : 'black',
    'weight' : 'normal',
    'size' : 13.0,
    }

#------------------- Data Read ----------------------
Greek_alphabets=['Alpha','Beta','Gamma','Delta','Epsilon','Zeta','Eta','Theta', 'Iota','Kappa','Lambda','Mu','Nu','Xi','Omicron','Pi','Rho','Sigma','Tau','Upsilon','Phi','Chi','Psi','Pega']
group_labels=[];xtick=[]
with open('KLABELS','r') as reader:
    lines=reader.readlines()[1:]
for i in lines:
    s=i.encode('utf-8')#.decode('latin-1')
    if len(s.split())==2 and not s.decode('utf-8','ignore').startswith('*'):
        klabel=str(s.decode('utf-8','ignore').split()[0])
        for j in range(len(Greek_alphabets)):
            if (klabel.find(Greek_alphabets[j].upper())>=0):
                latex_exp=r''+'$\\'+str(Greek_alphabets[j])+'$'
                klabel=klabel.replace(str(Greek_alphabets[j].upper()),str(latex_exp))
        if (klabel.find('_')>0):
           n=klabel.find('_')
           klabel=klabel[:n]+'$'+klabel[n:n+2]+'$'+klabel[n+2:]
        group_labels.append(klabel)
        xtick.append(float(s.split()[1]))
datas=np.loadtxt('BAND.dat',dtype=np.float64)

#--------------------- PLOTs ------------------------
axe = plt.subplot(111)
axe.axhline(y=0, xmin=0, xmax=1,linestyle= '--',linewidth=0.5,color='0.5')
for i in xtick[1:-1]:
    axe.axvline(x=i, ymin=0, ymax=1,linestyle= '--',linewidth=0.5,color='0.5')
colormaps=['blue','red']
spin_labels=['Spin-up','Spin-down']
nspin=datas.shape[1]-1
for i in range(nspin):
    axe.plot(datas[:,0],datas[:,i+1],linewidth=1.0,color=colormaps[i],label=spin_labels[i])
if (nspin >1):
    axe.legend(loc='best',shadow=False,labelspacing=0.1)
axe.set_ylabel(r'$\mathrm{Energy}$ (eV)',fontdict=font)
axe.set_xticks(xtick)
plt.yticks(fontsize=font['size']-2,fontname=font['family'])
axe.set_xticklabels(group_labels, rotation=0,fontsize=font['size']-2,fontname=font['family'])
axe.set_xlim((xtick[0], xtick[-1]))
plt.ylim((  -2,   8)) # set y limits manually
fig = plt.gcf()
fig.set_size_inches( 8, 6)
plt.savefig('band.png',dpi= 300)
