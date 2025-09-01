{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPXa73Guw4/tM13zYHFKsny",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/guizn31/Projeto-teste/blob/main/colabteste.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3hhbfXXTaetA",
        "outputId": "4fd40f90-ecef-45f8-ef3e-b08a589e80d9"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o nome da pessoa: gui\n",
            "digite sua idade: 14\n",
            "nome:  gui idade:  14\n",
            "nome: gui, idade: 14\n"
          ]
        }
      ],
      "source": [
        "nome = input(\"Digite o nome da pessoa: \")\n",
        "idade = input(\"digite sua idade: \")\n",
        "print(\"nome: \",nome,\"idade: \", idade)\n",
        "print(f\"nome: {nome}, idade: {idade}\")"
      ]
    }
  ]
}
