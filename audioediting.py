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
   

def add_effect(audio_segment, effect, time_placement, crossfade_beginning=False,crosffade_end=False, cf_threshold_beginning=3000, cf_threshold_end=3000):
    """
    Ajoute une musique d'introduction
    IL est possible de spécifidans cette foncrion la durée de la fondue(crossfade) entre l'intro et le début du podcast)
    """
    before_effect = audio_segment[:time_placement]
    after_effect = audio_segment[time_placement:]
    if crossfade_beginning & crossfade_end:
            audio_segment = before_effect.append(effect, crossfade=cf_threshold_beginning).append(after_effect, crossfade=cf_threshold_end)
    elif crossfade_beginning:
            audio_segment = before_effect.append(effect, crossfade=cf_threshold_beginning).append(after_effect)
    elif crossfade_ending:
            audio_segment = before_effect.append(effect).append(after_effect, crossfade=cf_threshold_end)
    else :
            audio_segment = before_effect.append(effect).append(after_effect)
    return audio_segment  
    
def detect_silence(audio_segment, silence_thresh=-50.0, chunk_size=10, silence_duration=1500):
    """
    Détecte les périodes de silence dans un fichier audio.
    
    audio_segment=segment dans lequel enlever les silences
    chunk_size= taille des morceaux de audio_segment à analyser pout détecter les silences (en mmilisecondes)
    silence_thresh= volume audio à partir duquel on est considéré en silence
    silence_duration= durée à partir duqel un silence est considéré et doit être placé dans la liste des tuples
    
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
                # Vérifie si la durée du silence est supérieure ou égale à silence_duration
                if i - silence_start >= silence_duration:  
                    silence_starts.append((silence_start, i))
                in_silence = False

    # Gère le cas où le fichier se termine par un long silence
    if in_silence and len(audio_segment) - silence_start >= 2000:
        silence_starts.append((silence_start, len(audio_segment)))

    return silence_starts


def remove_long_silences(audio_path, output_path, silence_thresh=-50.0, chunk_size=10, silence_duration=1500):
    """
    Supprime les silences de plus dsilence_duration du fichier audio fourni
    et enregistre le résultat.
    """
    # Chargement de l'audio
    audio = AudioSegment.from_file(audio_path)
    print(f"Longueur totale du fichier audio : {len(audio)} ms")

    # Détection des silences
    silence_chunks = detect_silence(audio, silence_thresh, chunk_size, silence_duration)
    print(f"Silences détectés : {silence_chunks}")

    # Reconstruction de l'audio sans les silences
    segments = []
    last_end = 0

    for start, end in silence_chunks:
        # Ajoute la partie audio entre la fin du dernier segment et le début du silence
        segments.append(audio[last_end:start])
        last_end = end

    # Ajoute la dernière portion de l'audio
    segments.append(audio[last_end:])

    # Combine les segments pour recréer l'audio
    output_audio = sum(segments)
    output_audio.export(output_path, format="wav")
    print(f"Le fichier audio sans les silences a été sauvegardé sous '{output_path}'.")

#Ajout d'une fonction background_sound pour ajouter une musique de fond
#Les paramètres seraient
#La musique à ajouter
#la fichier dans lequel ajouter la musique
#un time stamp pour quand l'ajouter
#un time stamp pour quand l'arrêter
#un  crossfade_beginning et cf_threshold_beginning
#un crosffade_end et cf_threshold_end

#Une fonction de test
