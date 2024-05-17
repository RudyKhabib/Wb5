import torch
import torch.nn as nn
from torchvision.models import vit_b_16, ViT_B_16_Weights
from gensim.models import KeyedVectors
import catboost

def vit():
    model = vit_b_16(weights=ViT_B_16_Weights.IMAGENET1K_V1)
    
    # Переопределим количество классов
    num_ftrs = model.heads.head.in_features
    model.heads.head = torch.nn.Linear(num_ftrs, 1)
    
    # Заморозка слоев
    for param in model.parameters():
        param.requires_grad = False
    
    # Разморозка предпоследнего и последнего конволюц слоя, а также FC
    for param in model.encoder.layers.encoder_layer_11.parameters():
        param.requires_grad = True
    
    for param in model.encoder.layers.encoder_layer_10.parameters():
        param.requires_grad = True
    
    for param in model.encoder.ln.parameters():
        param.requires_grad = True
    
    for param in model.heads.head.parameters():
        param.requires_grad = True

    if torch.cuda.is_available():
        map_location = 'cuda:%d' % torch.cuda.current_device()
    else:
        map_location = 'cpu'
    
    model.load_state_dict(torch.load('weights/Vit_weights.pth', map_location=map_location))
    
    model.heads = nn.Identity()

    return model


def w2v():
    return KeyedVectors.load("weights/Word2Vec.model")


def catboostclassifier():
    boosting = catboost.CatBoostClassifier()
    boosting.load_model('weights/boosting_w2v.bin')
    return boosting
