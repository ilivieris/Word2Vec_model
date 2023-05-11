# Train a Word2Vec model

This repository contains the implementation for training a word2vec model. The utilized data were collected from Greek Wikipedia and Greek National Printing House.
After the data are cleaned, they are tokenized and fed to a Word2Vec model. The model as well as the unique words used for training are stored in directory ``model``.

*Note*: The user is able to select if he/she wishes to perform the stemming procedure to each word before the development of Word2Vec model.

## Data
---

The utilized data are from

- Wikipedia: https://dumps.wikimedia.org/elwiki/latest/
- Greek National Printing House: [Google drive](https://drive.google.com/drive/folders/1tg8nexlZ8hbCexPtsNFJHM_uPJWVyx0l)

<br/>

## Get started
--- 

1. Run jupyter notebook for creating the Word2Vec model
```
    01. Train Word2Vec model.ipynb
```

2. Run jupyter notebook for saving the vocabulary and create the embeddings of each word contained in the vocabulary.
```
    02. Create embeddings.ipynb
```

<br/>


## Embeddings
---

The developed embeddings with/without the application of stemming can be found in [Google drive](https://drive.google.com/drive/folders/1USaxs_O0WBduOMHxpxS2MsqR_cIqJgtC)


<br/>

## :mailbox: Contact
---

Ioannis E. Livieris (livieris@novelcore.eu)
