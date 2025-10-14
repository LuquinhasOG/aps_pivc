import numpy as np
import tensorflow as tf
from tensorflow.keras import models, layers, datasets, preprocessing
from tensorflow.keras.losses import SparseCategoricalCrossentropy

path_treino = "imagens/treino"
path_teste = "imagens/teste"
path_validacao = "imagens/validacao"
epochs = 20
classes = ['vazia', 'bispo_branco', 'cavalo_branco', 'dama_branca', 'peao_branco', 'rei_branco', 'torre_branca',
           'bispo_preto', 'cavalo_preto', 'dama_preta', 'peao_preto', 'rei_preto', 'torre_preta']


def build_model():
    modelo = models.Sequential()
    modelo.add(layers.Input((50, 50, 1)))
    # modelo.add(layers.Rescaling(1. / 255, input_shape=(50, 50, 1)))  # normalizar as imagens de entrada
    modelo.add(layers.Conv2D(32, (3, 3), activation='relu'))  # conv3_32, relu para evitar vanishing do gradiente
    modelo.add(layers.MaxPooling2D((2, 2)))  # maxpool2
    modelo.add(layers.Flatten())  # flatten
    modelo.add(layers.Dense(32, activation='relu'))  # dense32
    modelo.add(layers.Dense(13, activation='softmax'))  # dense13

    return modelo


if __name__ == "__main__":
    # datasets
    treino_ds = preprocessing.image_dataset_from_directory(
        path_treino,
        image_size=(50, 50),
        batch_size=32,
        color_mode='grayscale',
        labels='inferred',
        label_mode='int',
        shuffle=True,
        class_names=classes
    )

    validacao_ds = preprocessing.image_dataset_from_directory(
        path_validacao,
        image_size=(50, 50),
        batch_size=32,
        color_mode='grayscale',
        labels='inferred',
        label_mode='int',
        shuffle=True,
        class_names=classes
    )

    teste_ds = preprocessing.image_dataset_from_directory(
        path_teste,
        image_size=(50, 50),
        batch_size=32,
        color_mode='grayscale',
        labels='inferred',
        label_mode='int',
        shuffle=True,
        class_names=classes
    )

    modelo = build_model()
    modelo.load_weights("deteccao.weights.h5")
    modelo.compile(optimizer='adam', loss=SparseCategoricalCrossentropy(), metrics=['accuracy'])
    modelo.fit(treino_ds, validation_data=validacao_ds, epochs=epochs)

    loss, accuracy = modelo.evaluate(teste_ds)
    print(f"Acurácia: {accuracy:.4f} | Loss: {loss:.4f}")

    modelo.save_weights("deteccao.weights.h5")  # 95%

    # rotulos = []
    # previsoes = []
    # for imgs, labels in teste_ds:
    #     rotulos.extend(labels.numpy())
    #     for i in imgs:
    #         i = tf.expand_dims(i, axis=0)
    #         previsoes.append(np.argmax(modelo.predict(i)))
    #
    # print(len(rotulos))
    # print(len(previsoes))
    #
    # matriz = tf.math.confusion_matrix(rotulos, previsoes)
    # print(matriz)
