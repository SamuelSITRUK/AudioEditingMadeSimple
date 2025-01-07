

def add_intro_song(audio_segment, intro_song):
    """
    Ajoute une musique d'introduction
    IL est possible de spécifier dans cette foncrion la durée de la fondue(crossfade) entre l'intro et le début du podcast
    """
   

def add_ending_theme_song(audio_segment, ending_song):
    """
    Ajoute une musique d'introduction
    IL est possible de spécifier dans cette foncrion la durée de la fondue(crossfade) entre l'intro et le début du podcast)
    """
   

def add_effect(audio_segment, crossfade=False,time_placement, effect, cf_threshold=10000):
    """
    Ajoute une musique d'introduction
    Il est possible de spécifier dans cette foncrion si il faut un crossfade  et la durée de cette fondue(crossfade) entre l'intro et le début du podcast)
    """
    


def remove_long_silences(audio_path, output_path, silence_thresh=-50.0):
    """
    Supprime les silences de plus de xx secondes du fichier audio fourni
    et enregistre le résultat.
    """
   


#1er commit : definition des fonctions
#2ème commit : definition de la version de pyhton nécéssaire et des dépendances
#3ème commit : Definition de la fonctiondetect_silence
#4ème commit : definition de la fonction remove_long_silence
#5ème commit : ajout de add_effect
#6ème commit : ajout de tests pour les différentes fo ctions
#7ème commit : ajout d'un fonction permettant le test et l'écoute pour un peu de fine tuning
#8ème commit : organisation  du package en quelque chose de cohérent avec les bonne pratiques 