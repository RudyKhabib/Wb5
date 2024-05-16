from fastapi import FastAPI
import torch
from torch.utils.data import Dataset, DataLoader
import numpy as np
from nltk.tokenize import WordPunctTokenizer
import easyocr
import vit_embeds
import get_models
import w2v_embeds
from PIL import Image
import io
from pydantic import BaseModel 


app = FastAPI()
vit = get_models.vit()
w2v = get_models.w2v()
boosting = get_models.catboostclassifier()


class ImgBytes(BaseModel):
    imgbytes: bytes


@app.post('/get_answer')
def get_answer(img_bytes: ImgBytes):
    image_path = img_bytes.imgbytes
    img_bytes = img_bytes.imgbytes
    img = Image.open(io.BytesIO(img_bytes))
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    transform = vit_embeds.get_transformations()
    dataset = vit_embeds.FraudDataset([img], transform)
    dataloader = DataLoader(
        dataset, batch_size=1, shuffle=False)
    vit_embed = vit_embeds.get_vit_embeds(vit, dataloader, device)
    reader = easyocr.Reader(['ru', 'en'])
    wrds_lst = reader.readtext(img, detail=0)
    tokenizer = WordPunctTokenizer()
    w2v_embed = w2v_embeds.get_phrase_embedding(tokenizer, wrds_lst, w2v)
    embeds_full = np.concatenate((vit_embed.squeeze(), w2v_embed))
    predict = boosting.predict(embeds_full), 
    probs = boosting.predict_proba(embeds_full)
    return {'prob': list(probs), 'verdict': predict[0]}