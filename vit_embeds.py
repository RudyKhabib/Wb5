import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from torchvision.models import vit_b_16, ViT_B_16_Weights
import albumentations as A
from albumentations.pytorch import ToTensorV2
import cv2
import os
import numpy as np


def get_vit_embeds(model, loader, device):
    vit_embeds = []
    model = model.to(device)
    with torch.no_grad():
        for images in loader:
            embeds = model(images.to(device))
            vit_embeds += [embeds.squeeze().cpu()]

    return np.array(vit_embeds)


class FraudDataset(Dataset):
    def __init__(self, images, transform=None):
        self.images= images
        self.transform = transform

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        image = self.images[idx]
        image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
        if self.transform is not None:
            image = self.transform(image=image)["image"]
        return image


def get_transformations(): 
    transform = A.Compose(
        [
            A.SmallestMaxSize(max_size=300),
            A.CenterCrop(height=224, width=224),
            A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
            A.pytorch.ToTensorV2(),
        ]
    )
    return transform
