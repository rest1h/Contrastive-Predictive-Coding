# Reproducing Contrastive-Predictive-Coding
### Original code: https://github.com/jefflai108/Contrastive-Predictive-Coding-PyTorch

## Dataset
### Download below files from http://www.openslr.org/12/, and unzip files in ./LibriSpeech/  

dev-clean.tar.gz  
dev-clean.tar.gz    
dev-other.tar.gz  
test-clean.tar.gz  
test-other.tar.gz  
train-clean-100.tar.gz  
  
### Obtain the appropriate subsets of the LibriSpeech dataset, and convert all flac files to wav format.  

```
wget http://www.openslr.org/resources/12/dev-clean.tar.gz  
tar -xzvf dev-clean.tar.gz  
wget http://www.openslr.org/resources/12/test-clean.tar.gz  
tar -xzvf test-clean.tar.gz
mv flac_to_wav.sh LibriSpeech
cd LibriSpeech
./flac_to_wav.sh
```

### Run wav2raw.py and generate_txt.py
https://github.com/jefflai108/Contrastive-Predictive-Coding-PyTorch/issues/1  
https://github.com/jefflai108/Contrastive-Predictive-Coding-PyTorch/issues/9

## Requirements (mac os)
Using python=3.8, miniconda, and 
```
pip3 install torch torchvision
conda install -y -c conda-forge h5py
pip install scipy  
brew install libav
```


## Getting started 
```
./run.sh
```

## CPC Models
CDCK2: base model from the paper 'Representation Learning with Contrastive Predictive Coding'.  
CDCK5: CDCK2 with a different decoder.  
CDCK6: CDCK2 with a shared encoder and double decoders.  