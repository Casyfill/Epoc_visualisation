
import pandas as pd
from pandas import DataFrame, read_csv
import numpy as np
import matplotlib.pyplot as plt


basePath = "/Users/casy/Dropbox (RN&IA'N)/Projects/Kats/Afisha/2014_05_27_Epoch/data"
patients = ['patient1','patient2','patient3']

tracks = {u'1. И.С. Бах. Оратория "Страсти по Иоанну". Хор первый':1,
u'2. Стас Михайлов - Посланница небес':2,
u"3. James Brown - Papa's Got A New Bag":3,
u'4. Behemoth - Slaves Shall Serve':4,
u'5. The Velvet Underground - Candy Says':5,
u"6. Coil - It's In My Blood":6,
u'7. Daft Punk - Get Lucky':7,
u'8. Skrillex - Go On':8,
u'9. Мумий Тролль - Непокой':9,
u'10. The Knife - Fracking Fluid Injection':10,
u'11. Гражданская Оборона - Все совсем не то':11,
u'12. The Thing - Snusvisan':12,
u'13. Oxxxymiron - Долгий путь домой':13}

base_result = "/Users/casy/Dropbox (RN&IA'N)/Projects/Kats/Afisha/2014_05_27_Epoch/graphs/"
for track in tracks:
	fig = plt.figure(figsize=(8, 10))
	fig.suptitle(track, fontsize=15)

	for patient in patients:
		n = int(patient[-1])
		if tracks[track]<10:
			trackNum = '0' + str(tracks[track])
		else:
			trackNum = str(tracks[track])
		path = '/'.join([basePath, patient, (trackNum+'.csv')])
		
		df = pd.read_table(path, sep=',')
		
		xs = df['position']
		xLim = xs.max(numeric_only=True)

		bored = df['bored']
		excitement = df['excitement'] 
		meditation = df['meditation']
		frustration = df['frustration']
		plt.subplot(3,1,n)
		plt.xlim(0,xLim)
		plt.ylim(-0.1,1.1)
		plt.title(patient)
		plt.grid(alpha=0.4)   
		plt.plot(xs, bored, 'b-', xs, excitement, 'r-', xs, meditation, 'g-', xs, frustration, 'y-')
	
	fig.legend( ('b-', 'r-', 'g-', 'y-'),
           ('label1', 'label2', 'label3', 'label4'),
           'upper right' )
	rPath = base_result + str(tracks[track]) + '.png'
	print tracks[track], ' saved'
	# plt.show()
	plt.savefig(rPath,dpi=100)
	print


