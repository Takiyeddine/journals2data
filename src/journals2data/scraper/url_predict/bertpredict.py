import pandas as pd
from transformers import DistilBertTokenizerFast
from transformers import TFDistilBertForSequenceClassification
import tensorflow as tf
import os
import journals2data
from journals2data import data

def apply_BERT_prediction(
    dataframe: pd.DataFrame,
    source: data.Source,
    config: journals2data.J2DConfiguration
) -> pd.DataFrame:
    """
    Apply BERT prediction layer based on BERT classifier.
    """

    # get model_path depending on the language
    model_dirpath: str =  os.path.join(config.params["BERT_MODEL_BASEPATH"],
        config.params["BERT_LANGUAGE_DIRS"][source.language])
    model = TFDistilBertForSequenceClassification.from_pretrained(
        model_dirpath
    )
    tokenizer = DistilBertTokenizerFast.from_pretrained(
        'distilbert-base-uncased'
    )

    def predict(model, tokenizer, sentence):
        predict_input = tokenizer.encode(
            sentence,
            truncation=True, 
            padding=True, 
            return_tensors="tf"
        )
        tf_output = model.predict(predict_input)[0]
        tf_prediction = tf.nn.softmax(tf_output, axis=1).numpy()[0]
        return tf_prediction[1]

    dataframe['BERT'] = 0 # add column for results
    # HACK: this code bloc distinction is just because
    # I have a pb with tensorflow on my machine.
    # TODO: remove for release
    if(config.params["USER"] == "onyr"):
        import random
        dataframe['BERT'] = dataframe.apply(
            lambda x: random.random(), axis=1
        )
    else:
        dataframe['BERT'] = dataframe.apply(
            lambda x: predict(model,tokenizer, x.title), axis=1
        ) # add a column for results

    return dataframe
