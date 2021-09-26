"""
    Author : Thibault Chenevière
    Date : 24/09/2021
"""

from pathlib import Path


def get_path():
    """
        Fonction qui permet de retrouver le chemin
        d'accès du fichier bot_discord.py
        Returns :
            - cwd (string) : chemin d'accès de bot_discord.py
    """

    cwd = Path(__file__).parents[1]
    cwd = str(cwd)
    return cwd