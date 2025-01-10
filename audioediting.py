'''
python_version = "3.8.0"
pydub_version = "0.25.1"
ffmpeg_version = "1.4"
'''

def add_intro_song(audio_segment, intro_song):
    """
    Ajoute une musique d'introduction
    Il est possible de spécifier dans cette fonction la durée de la fondue(crossfade) entre l'intro et le début du podcast
    """
   

def add_ending_theme_song(audio_segment, ending_song):
    """
    Ajoute une musique d'introduction
    Il est possible de spécifier dans cette fonction la durée de la fondue(crossfade) entre l'intro et le début du podcast
    """
   

def add_effect(audio_segment, crossfade=False,time_placement, effect, cf_threshold=10000):
    """
    Ajoute une musique d'introduction
    Il est possible de spécifier dans cette foncrion si il faut un crossfade et la durée de cette fondue(crossfade) entre l'intro et le début du podcast
    """
    
def detect_silence(audio_segment, silence_thresh=-50.0, chunk_size=10):
    """
    Détecte les périodes de silence dans un fichier audio.
    
    audio_segment=segment dans lequel enlever les silences
    chunk_size= taille des morceaux de audio_segment à analyser pout détecter les silences (en mmilisecondes)
    silence_thresh= volume audio à partir duquel on est considéré en silence
    
    Retourne une liste de tuples (start, end) pour les périodes de silence.
    """
    silence_starts = []
    in_silence = False
    silence_start = 0

    for i in range(0, len(audio_segment), chunk_size):
        chunk = audio_segment[i:i + chunk_size]
        # Vérifie si le volume du morceau est inférieur au seuil
        if chunk.dBFS < silence_thresh:
            if not in_silence:
                silence_start = i
                in_silence = True
        else:
            if in_silence:
                # Vérifie si la durée du silence est supérieure ou égale à 1.5 secondes
                if i - silence_start >= 1500:  # 1.5 secondes en millisecondes
                    silence_starts.append((silence_start, i))
                in_silence = False

    # Gère le cas où le fichier se termine par un long silence
    if in_silence and len(audio_segment) - silence_start >= 2000:
        silence_starts.append((silence_start, len(audio_segment)))

    return silence_starts


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
