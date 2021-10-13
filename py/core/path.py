"""
    Author : Thibault Chenevière
    Date : 24/09/2021
"""

from pathlib import Path


def get_path(k):
    """
        Fonction qui permet de retrouver le chemin
        d'accès du fichier main.py
        Returns :
            - cwd (string) : chemin d'accès de bot_discord.py
    """

    cwd = Path(__file__).parents[k]
    cwd = str(cwd)
    return cwd