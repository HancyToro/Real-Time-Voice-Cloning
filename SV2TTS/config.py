from vlibs import fileio
import torch

librispeech_root = "E://Datasets/LibriSpeech"
librispeech_datasets = ["train-other-500"]
clean_data_root = "E://Datasets//SpeakerEncoder"

model_dir = "saved_models"

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')