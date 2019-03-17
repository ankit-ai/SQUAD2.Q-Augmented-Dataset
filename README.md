# SQuAD 2.Q - Augmented-Dataset
#### Developers - Ankit Chadha (ankitrc@stanford.edu) and Rewa Sood (rrsood@stanford.edu)


------

This is a release of an Augmented dataset we produced on top of [Stanford Question Answering Dataset (SQuAD) 2.0](https://rajpurkar.github.io/SQuAD-explorer/).

The repository is called SQuAD 2.Q since only the *questions* out of the SQuAD 2.0 dataset have been augmented using the process of [Back Translation](http://ankit-ai.blogspot.com/2019/03/future-of-natural-language-processing.html). The work can easily be extended to Context paragraphs using the python script (augment.py).

------
## Why just Questions?
SQuAD 2.0 is a dataset where the context come from Wikipedia paragraphs and the questions are written by Cloud workers. When questions are written by cloud workers it inherently adds syntatic variance and grammar usage of human cloud workers. The idea here is to help the network generalize to the syntatic variance in the question to generalize better at:
1. Understanding Questions
2. Understanding interactions between Question and Context (Attention)

<img src="https://github.com/ankit-ai/SQUAD2.Q-Augmented-Dataset/blob/master/img/backtrans.png">

------
## How does SQuAD 2.Q help?
We present our model called BertQA : Attention on Steroids where SQuAD 2.Q50 helped the same model achieve 2 point F1 improvement over SQuAD 2.0.

![BertQA](https://github.com/ankit-ai/SQUAD2.Q-Augmented-Dataset/blob/master/img/bert.png "BertQA for SQuAD 2.Q - Attention on Steroids")

------
## Release notes:
1. SQuAD 2Q (100% Augmented - for every question in the dataset there is an augmented question)
2. SQuAD 2Q50 (50% Augmented)
3. SQuAD 2Q35 (35% Augmented)
4. augment.py (Python code to use Google Cloud API to augment the dataset)

------
## Usage:
```
python augment.py
```
------
## Back Translation:
![Backtranslation](https://4.bp.blogspot.com/--sRxCag7jdk/XIsDaTeTNjI/AAAAAAAAGzE/hF13dvMBR5I4btKSpAPzbE3iuivQcVl8gCLcBGAs/s320/Screen%2BShot%2B2019-03-14%2Bat%2B4.57.45%2BPM.png "Backtranslation process used for SQuAD 2.Q")

Read more:
http://ankit-ai.blogspot.com/2019/03/future-of-natural-language-processing.html
