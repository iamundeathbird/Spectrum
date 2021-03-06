import cv2
from pydub import AudioSegment
import numpy as np

class mappingSpectrum:

    colormap=[  [	255	,	0	,	0	],
                [	255	,	3	,	0	],
                [	255	,	6	,	0	],
                [	255	,	9	,	0	],
                [	255	,	12	,	0	],
                [	255	,	15	,	0	],
                [	255	,	18	,	0	],
                [	255	,	21	,	0	],
                [	255	,	24	,	0	],
                [	255	,	27	,	0	],
                [	255	,	30	,	0	],
                [	255	,	33	,	0	],
                [	255	,	36	,	0	],
                [	255	,	39	,	0	],
                [	255	,	42	,	0	],
                [	255	,	45	,	0	],
                [	255	,	48	,	0	],
                [	255	,	51	,	0	],
                [	255	,	54	,	0	],
                [	255	,	57	,	0	],
                [	255	,	60	,	0	],
                [	255	,	63	,	0	],
                [	255	,	66	,	0	],
                [	255	,	69	,	0	],
                [	255	,	72	,	0	],
                [	255	,	75	,	0	],
                [	255	,	78	,	0	],
                [	255	,	81	,	0	],
                [	255	,	84	,	0	],
                [	255	,	87	,	0	],
                [	255	,	90	,	0	],
                [	255	,	93	,	0	],
                [	255	,	96	,	0	],
                [	255	,	99	,	0	],
                [	255	,	102	,	0	],
                [	255	,	105	,	0	],
                [	255	,	108	,	0	],
                [	255	,	111	,	0	],
                [	255	,	114	,	0	],
                [	255	,	117	,	0	],
                [	255	,	120	,	0	],
                [	255	,	123	,	0	],
                [	255	,	126	,	0	],
                [	255	,	129	,	0	],
                [	255	,	132	,	0	],
                [	255	,	135	,	0	],
                [	255	,	138	,	0	],
                [	255	,	141	,	0	],
                [	255	,	144	,	0	],
                [	255	,	147	,	0	],
                [	255	,	150	,	0	],
                [	255	,	153	,	0	],
                [	255	,	156	,	0	],
                [	255	,	159	,	0	],
                [	255	,	162	,	0	],
                [	255	,	165	,	0	],
                [	255	,	168	,	0	],
                [	255	,	171	,	0	],
                [	255	,	174	,	0	],
                [	255	,	177	,	0	],
                [	255	,	180	,	0	],
                [	255	,	183	,	0	],
                [	255	,	186	,	0	],
                [	255	,	189	,	0	],
                [	255	,	192	,	0	],
                [	255	,	195	,	0	],
                [	255	,	198	,	0	],
                [	255	,	201	,	0	],
                [	255	,	204	,	0	],
                [	255	,	207	,	0	],
                [	255	,	210	,	0	],
                [	255	,	213	,	0	],
                [	255	,	216	,	0	],
                [	255	,	219	,	0	],
                [	255	,	222	,	0	],
                [	255	,	225	,	0	],
                [	255	,	228	,	0	],
                [	255	,	231	,	0	],
                [	255	,	234	,	0	],
                [	255	,	237	,	0	],
                [	255	,	240	,	0	],
                [	255	,	243	,	0	],
                [	255	,	246	,	0	],
                [	255	,	249	,	0	],
                [	255	,	252	,	0	],
                [	255	,	255	,	0	],
                [	255	,	255	,	0	],
                [	252	,	255	,	3	],
                [	249	,	255	,	6	],
                [	246	,	255	,	9	],
                [	243	,	255	,	12	],
                [	240	,	255	,	15	],
                [	237	,	255	,	18	],
                [	234	,	255	,	21	],
                [	231	,	255	,	24	],
                [	228	,	255	,	27	],
                [	225	,	255	,	30	],
                [	222	,	255	,	33	],
                [	219	,	255	,	36	],
                [	216	,	255	,	39	],
                [	213	,	255	,	42	],
                [	210	,	255	,	45	],
                [	207	,	255	,	48	],
                [	204	,	255	,	51	],
                [	201	,	255	,	54	],
                [	198	,	255	,	57	],
                [	195	,	255	,	60	],
                [	192	,	255	,	63	],
                [	189	,	255	,	66	],
                [	186	,	255	,	69	],
                [	183	,	255	,	72	],
                [	180	,	255	,	75	],
                [	177	,	255	,	78	],
                [	174	,	255	,	81	],
                [	171	,	255	,	84	],
                [	168	,	255	,	87	],
                [	165	,	255	,	90	],
                [	162	,	255	,	93	],
                [	159	,	255	,	96	],
                [	156	,	255	,	99	],
                [	153	,	255	,	102	],
                [	150	,	255	,	105	],
                [	147	,	255	,	108	],
                [	144	,	255	,	111	],
                [	141	,	255	,	114	],
                [	138	,	255	,	117	],
                [	135	,	255	,	120	],
                [	132	,	255	,	123	],
                [	129	,	255	,	126	],
                [	126	,	255	,	129	],
                [	123	,	255	,	132	],
                [	120	,	255	,	135	],
                [	117	,	255	,	138	],
                [	114	,	255	,	141	],
                [	111	,	255	,	144	],
                [	108	,	255	,	147	],
                [	105	,	255	,	150	],
                [	102	,	255	,	153	],
                [	99	,	255	,	156	],
                [	96	,	255	,	159	],
                [	93	,	255	,	162	],
                [	90	,	255	,	165	],
                [	87	,	255	,	168	],
                [	84	,	255	,	171	],
                [	81	,	255	,	174	],
                [	78	,	255	,	177	],
                [	75	,	255	,	180	],
                [	72	,	255	,	183	],
                [	69	,	255	,	186	],
                [	66	,	255	,	189	],
                [	63	,	255	,	192	],
                [	60	,	255	,	195	],
                [	57	,	255	,	198	],
                [	54	,	255	,	201	],
                [	51	,	255	,	204	],
                [	48	,	255	,	207	],
                [	45	,	255	,	210	],
                [	42	,	255	,	213	],
                [	39	,	255	,	216	],
                [	36	,	255	,	219	],
                [	33	,	255	,	222	],
                [	30	,	255	,	225	],
                [	27	,	255	,	228	],
                [	24	,	255	,	231	],
                [	21	,	255	,	234	],
                [	18	,	255	,	237	],
                [	15	,	255	,	240	],
                [	12	,	255	,	243	],
                [	9	,	255	,	246	],
                [	6	,	255	,	249	],
                [	3	,	255	,	252	],
                [	0	,	252	,	255	],
                [	0	,	249	,	255	],
                [	0	,	246	,	255	],
                [	0	,	243	,	255	],
                [	0	,	240	,	255	],
                [	0	,	237	,	255	],
                [	0	,	234	,	255	],
                [	0	,	231	,	255	],
                [	0	,	228	,	255	],
                [	0	,	225	,	255	],
                [	0	,	222	,	255	],
                [	0	,	219	,	255	],
                [	0	,	216	,	255	],
                [	0	,	213	,	255	],
                [	0	,	210	,	255	],
                [	0	,	207	,	255	],
                [	0	,	204	,	255	],
                [	0	,	201	,	255	],
                [	0	,	198	,	255	],
                [	0	,	195	,	255	],
                [	0	,	192	,	255	],
                [	0	,	189	,	255	],
                [	0	,	186	,	255	],
                [	0	,	183	,	255	],
                [	0	,	180	,	255	],
                [	0	,	177	,	255	],
                [	0	,	174	,	255	],
                [	0	,	171	,	255	],
                [	0	,	168	,	255	],
                [	0	,	165	,	255	],
                [	0	,	162	,	255	],
                [	0	,	159	,	255	],
                [	0	,	156	,	255	],
                [	0	,	153	,	255	],
                [	0	,	150	,	255	],
                [	0	,	147	,	255	],
                [	0	,	144	,	255	],
                [	0	,	141	,	255	],
                [	0	,	138	,	255	],
                [	0	,	135	,	255	],
                [	0	,	132	,	255	],
                [	0	,	129	,	255	],
                [	0	,	126	,	255	],
                [	0	,	123	,	255	],
                [	0	,	120	,	255	],
                [	0	,	117	,	255	],
                [	0	,	114	,	255	],
                [	0	,	111	,	255	],
                [	0	,	108	,	255	],
                [	0	,	105	,	255	],
                [	0	,	102	,	255	],
                [	0	,	99	,	255	],
                [	0	,	96	,	255	],
                [	0	,	93	,	255	],
                [	0	,	90	,	255	],
                [	0	,	87	,	255	],
                [	0	,	84	,	255	],
                [	0	,	81	,	255	],
                [	0	,	78	,	255	],
                [	0	,	75	,	255	],
                [	0	,	72	,	255	],
                [	0	,	69	,	255	],
                [	0	,	66	,	255	],
                [	0	,	63	,	255	],
                [	0	,	60	,	255	],
                [	0	,	57	,	255	],
                [	0	,	54	,	255	],
                [	0	,	51	,	255	],
                [	0	,	48	,	255	],
                [	0	,	45	,	255	],
                [	0	,	42	,	255	],
                [	0	,	39	,	255	],
                [	0	,	36	,	255	],
                [	0	,	33	,	255	],
                [	0	,	30	,	255	],
                [	0	,	27	,	255	],
                [	0	,	24	,	255	],
                [	0	,	21	,	255	],
                [	0	,	18	,	255	],
                [	0	,	15	,	255	],
                [	0	,	12	,	255	],
                [	0	,	9	,	255	],
                [	0	,	6	,	255	],
                [	0	,	3	,	255	],
                [	0	,	0	,	255	]]
    def __init__(self,filepath,targetfolder='./',audiotype='wav'):
        self.filepath=filepath
        self.targetfolder=targetfolder
        self.sound=None
        self.sample1=None
        self.sample2=None
        self.audiotype=audiotype
    def getSample(self):
        try:
            self.sound=AudioSegment.from_file(self.filepath,self.audiotype)
            samples=np.array(self.sound.get_array_of_samples())
            if(self.sound.sample_width==4):
                samples=samples>>16
            elif(self.sound.sample_width==3):
                samples=samples>>8  
            if(self.sound.channels==2):
                self.sample1=samples[::2]
                self.sample2=samples[1::2]   
            else:
                self.sample1=samples[::]           
        except  Exception as err:     
             raise err
    def getSample_from_wav_array(self,wav_array):
        try:
            self.sound=AudioSegment(wav_array)
            samples=np.array(self.sound.get_array_of_samples())
            if(self.sound.sample_width==4):
                samples=samples>>16
            elif(self.sound.sample_width==3):
                samples=samples>>8  
            if(self.sound.channels==2):
                self.sample1=samples[::2]
                self.sample2=samples[1::2]   
            else:
                self.sample1=samples[::]           
        except  Exception as err:     
             raise err                
    def makespectrum(self,sample,span=1,start=0,window=1024,shift=256,save_key='spec'):
        try: 
            if span=='all':
                span=int(self.sound.duration_seconds)  
                start=0
            hammingWindow = np.hamming(window)
            while start <= (int)(self.sound.duration_seconds):
                temp= sample[int(self.sound.frame_rate*start):int(self.sound.frame_rate*start)+int(self.sound.frame_rate*span)]
                total=int((temp.shape[0]- window) / shift)
                if total<=0:
                    break
                blank_image = np.zeros((384,(int)(total),3), np.uint8)
                for i in range(total):
                    data = temp[i*shift:i*shift+window]*hammingWindow
                    spec = np.fft.fft(data)
                    spec = spec[:int(spec.shape[0]/2)] 
                    y=0
                    for m in spec:
                        lm=np.log(m+1)
                        if(lm>15):
                            lm=15
                        if(lm<0):
                            lm=0
                        color_index=(int)(lm*255/16)
                        blank_image[y,i]=(self.colormap[color_index][0],self.colormap[color_index][1],self.colormap[color_index][2])
                        y=y+1
                        if y>383:
                            break
                cv2.cv2.imwrite(r'{0}\{2}_{1:06d}.png'.format(self.targetfolder,start,save_key),blank_image)
                start=start+span  
        except Exception as err:
            raise err
    def makespectrum_to_array(self,sample,span=1,start=0,window=1024,shift=256):
        try: 
            list=[]
            if span=='all':
                span=int(self.sound.duration_seconds)  
                start=0
            hammingWindow = np.hamming(window)
            while start <= (int)(self.sound.duration_seconds):
                temp= sample[int(self.sound.frame_rate*start):int(self.sound.frame_rate*start)+int(self.sound.frame_rate*span)]
                total=int((temp.shape[0]- window) / shift)
                if total<=0:
                    break
                blank_image = np.zeros((384,(int)(total),3), np.uint8)
                for i in range(total):
                    data = temp[i*shift:i*shift+window]*hammingWindow
                    spec = np.fft.fft(data)
                    spec = spec[:int(spec.shape[0]/2)] 
                    y=0
                    for m in spec:
                        lm=np.log(m+1)
                        if(lm>15):
                            lm=15
                        if(lm<0):
                            lm=0
                        color_index=(int)(lm*255/16)
                        blank_image[y,i]=(self.colormap[color_index][0],self.colormap[color_index][1],self.colormap[color_index][2])
                        y=y+1
                        if y>383:
                            break
                #cv2.cv2.imwrite(r'{0}\{2}_{1:06d}.png'.format(self.targetfolder,start,save_key),blank_image)
                list.append(blank_image)
                start=start+span
            return list    
        except Exception as err:
            raise err                      
            


    
        
