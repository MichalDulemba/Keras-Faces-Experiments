# KerasExperiments
Neural network experiments in keras

My collection of experiments, snippets and other keras-related stuff

In two gzip files you will find training and test examples - three very well known faces - Jackie Chan, Barack Obama and Rachel McAdams :) CSV files contain categories, but it is pretty easy to make it based on image names.
Images were pulled from google images and they are definitely not for commercial use (just for some AI fun).

Whole idea was to learn a lot about keras/cnn without using Mnist set which is beaten to death all over web :)

I'm mostly using this docker that supports keras and gpu (based on slaypni/keras-gpu) with some modfications (added imageio support and now both pythons 2 and 3 work in notebooks)

https://hub.docker.com/r/dulemba/kerasgpujpg/
