# Spectrum
Class of Audio reading using AudioSegment and creation of spectrogram using STFT
# Instructions
need install cv2,pydub,numpy

## Fuction: 
###    __init__(filepath,targetfolder='./',audiotype='wav') 

     need input audio file path and floder path for output spectrum image and audio type

     audio type is like 'wav','mp3','m4a'....


## Function: 
###    makespectrum(sample,span=1,start=0,window=1024,shift=256,save_key='spec')

      sample is the self.sample1(for single channel and stereo channel-1) 
      
      and the self.sample2(for stereo channel-2)


# Example

     from specstrum import mappingSpectrum as ms
     
     spec=ms('test.wav',r'./output','wav')
     
     spce.getSample()
     
     spec.makespectrum(k.sample1,save_key='ch1')
