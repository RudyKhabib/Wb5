import numpy as np
from collections import Counter


# Эмбеддинг для текста
def get_phrase_embedding(tokenizer, wrd_lst, model):
    """
    Convert phrase to a vector by aggregating it's word embeddings. See description above.
    """
    # 1. lowercase phrase
    # 2. tokenize phrase
    # 3. average word vectors for all words in tokenized phrase
    # skip words that are not in model's vocabulary
    # if all words are missing from vocabulary, return zeros
    tokens = tokenizer.tokenize(' '.join(wrd_lst))
    
    vector = np.zeros([model.vector_size], dtype='float32')
    dct_count = Counter(tokens)

    tokens = [word for word in tokens if word in model]
    dct_tok  = {token: model.get_vector(token) for token in tokens}

    for tok in dct_tok:
        vector += dct_tok[tok] * dct_count[tok] / len(tokens)

    return vector