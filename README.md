# south_park_NLP
![AWESUM-O](https://github.com/Sujit27/south_park_NLP/blob/master/AWESUM-O.gif)

AWESUM-O , a chat bot, built with pytorch, that talks as if it were a south park character. 

GRU recurrent neural network is used to learn the language model. Details about this type of network [here](https://towardsdatascience.com/understanding-gru-networks-2ef37df6c9be)

Luong Attention mechanism is used for better modelling. Detail about this mechanism [here](https://blog.floydhub.com/attention-mechanism/)

South Park transcript for each episode available [here](https://southpark.fandom.com/wiki/Portal:Scripts)

## Getting Started
Create directories for saving transcripts of all episodes `south_park_NLP/south_park_episode_transcripts` and `south_park_NLP/data`

Run scrape_south_park_episode.py to create txt files of transripts from all episodes

`python3 scrape_south_park_episode.py`

Once the above command has executed, run prep_aggregate_SP_transcript.py to create the aggregated transcript file `south_park_NLP/data/south_park_subtitles.txt`
This file should have even number of lines i.e input-output dialogue pairs.

`python prep_aggregate_SP_transcript.py`

### Prerequisites

* Python 3.5+
* pytorch
* beautifulsoup4
* tqdm

### Installing pytorch

`pip install torch torchvision` [see here](https://pytorch.org/)

### Training
Creat directory for saving trained model 

`mkdir -p save/model/south_park_subtitles/1-1_512`

Start training with the following command. Change parameters as needed

`python main.py -tr data/south_park_subtitles.txt -la 1 -hi 512 -lr 0.0001 -it 50000 -b 64 -p 500 -s 1000`

Or continue training from a previously saved model with the following command

`python main.py -tr data/south_park_subtitles.txt -l <MODEL_FILE_PATH> -lr 0.0001 -it 50000 -b 64 -p 500 -s 1000

### Testing
Test the chatbot after training is completed in the iterative mode

`python main.py -te <MODEL_FILE_PATH> -c data/south_park_subtitles.txt -i

## Acknowledgments

* Got inspired and also borrowed some code from this wonderful [repository](https://github.com/ywk991112/pytorch-chatbot)
