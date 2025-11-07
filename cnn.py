import numpy as np
import tensorflow as tf
from tensorflow.keras import models, layers, datasets, preprocessing
from tensorflow.keras.losses import SparseCategoricalCrossentropy
from util import classes

path_treino = "imagens/treino"
path_teste = "imagens/teste"
path_validacao = "imagens/validacao"
epochs = 20


def build_model():
    modelo = models.Sequential()
    modelo.add(layers.Input((64, 64, 1)))
    modelo.add(layers.Rescaling(1./255))  # normalização das imagens
    modelo.add(layers.Conv2D(32, (3, 3), activation='relu'))  # conv3_32, relu para evitar vanishing do gradiente
    modelo.add(layers.MaxPooling2D((3, 3), strides=2))  # maxpool3_stride2
    modelo.add(layers.Conv2D(64, (3, 3), activation='relu'))  # conv3_64, relu para evitar vanishing do gradiente
    modelo.add(layers.MaxPooling2D((2, 2)))  # maxpool2
    modelo.add(layers.Conv2D(128, (3, 3), activation='relu'))  # conv3_128, relu para evitar vanishing do gradiente
    modelo.add(layers.Conv2D(64, (3, 3), activation='relu'))  # conv3_64, relu para evitar vanishing do gradiente
    modelo.add(layers.Flatten())  # flatten
    modelo.add(layers.Dense(128, activation='relu'))  # dense128
    modelo.add(layers.Dense(128, activation='relu'))  # dense128
    modelo.add(layers.Dense(128, activation='relu'))  # dense128
    modelo.add(layers.Dense(13, activation='softmax'))  # dense13

    return modelo


def classificar(modelo, imagens):
    print(imagens.shape)
    # imagem = imagem.reshape((64, 64, 1))
    # imagem = np.expand_dims(imagem, axis=0)

    return np.argmax(modelo.predict(imagens), axis=1)


if __name__ == "__main__":
    # datasets
    treino_ds = preprocessing.image_dataset_from_directory(
        path_treino,
        image_size=(64, 64),
        batch_size=32,
        color_mode='grayscale',
        labels='inferred',
        label_mode='int',
        shuffle=True,
        class_names=classes
    )

    validacao_ds = preprocessing.image_dataset_from_directory(
        path_validacao,
        image_size=(64, 64),
        batch_size=32,
        color_mode='grayscale',
        labels='inferred',
        label_mode='int',
        shuffle=True,
        class_names=classes
    )

    teste_ds = preprocessing.image_dataset_from_directory(
        path_teste,
        image_size=(64, 64),
        batch_size=32,
        color_mode='grayscale',
        labels='inferred',
        label_mode='int',
        shuffle=True,
        class_names=classes
    )

    modelo = build_model()
    modelo.compile(optimizer='adam', loss=SparseCategoricalCrossentropy(), metrics=['accuracy'])
    modelo.fit(treino_ds, validation_data=validacao_ds, epochs=epochs)

    loss, accuracy = modelo.evaluate(teste_ds)
    print(f"Acurácia: {accuracy:.4f} | Loss: {loss:.4f}")

    modelo.save_weights("deteccao.weights.h5")
