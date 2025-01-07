#pip install pydub
#pip install ffmpeg
from pydub import AudioSegment

'''
Dans pydub les fichiers audio sonrt exportés sous forme de audiosegment qui sont des objets immutables
a number of AudioSegment methods are in 
the pydub/effects.py module, and added to AudioSegment via the effect registration process (the register_pydub_effect() decorator function)
Core functionality is mostly in pydub/audio_segment.py – 
pydub can only play .wav format audio and doesn't play "well" audio (simpleaudio package can work for this kind of task)
pydub can work with multiple files formats (including mp3...)
On peut seulement "append" des audiosegemnt entre eux et faire des crossfades
https://github.com/jiaaro/pydub/blob/master/API.markdown

'''

def add_intro_song(audio_segment, intro_song, cf_threshold=20000):
    """
    Ajoute une musique d'introduction
    IL est possible de spécifiER dans cette foncrion la durée de la fondue(crossfade) entre l'intro et le début du podcast)
    """
    xxx = audio_segment
    audio_segment = intro_song.append(xxx, crossfade=20000)
    return audio_segment

def add_ending_theme_song(audio_segment, ending_song, cf_threshold=10000):
    """
    Ajoute une musique d'introduction
    IL est possible de spécifidans cette foncrion la durée de la fondue(crossfade) entre l'intro et le début du podcast)
    """
    xxx = audio_segment
    audio_segment = xxx.append(ending_song, crossfade=10000)

    return audio_segment  

def add_effect(audio_segment, crossfade=False,time_placement, effect, cf_threshold=10000):
    """
    Ajoute une musique d'introduction
    IL est possible de spécifidans cette foncrion la durée de la fondue(crossfade) entre l'intro et le début du podcast)
    """
    before_effect = audio_segment[:time_placement]
    after_effect = audio_segment[time_placement:]
    audio_segment = before_effect.append(effect).append(after_effect)
    return audio_segment  


def detect_silence(audio_segment, silence_thresh=-50.0, chunk_size=10):
    """
    Détecte les périodes de silence dans un fichier audio.
    audio_segment=segment dans lequel enlever les silences
    chaunk_size= taille des morceaux de audio_segment à nanalyser pout rles silences
    silence_thresh
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
    Supprime les silences de plus de 12 secondes du fichier audio fourni
    et enregistre le résultat.
    """
    # Chargement de l'audio
    audio = AudioSegment.from_file(audio_path)
    print(f"Longueur totale du fichier audio : {len(audio)} ms")

    # Détection des silences
    silence_chunks = detect_silence(audio, silence_thresh)
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

introduction_song = AudioSegment.from_file("C:\\Users\\samue\\Downloads\\intro_cilantro_patricia_taxxon.wav") 
input_file = f"C:\\Users\\samue\\Downloads\\podcast_son.wav"  # Remplacez par le chemin de votre fichier source
output_path = "C:\\Users\\samue\\Downloads\\PODCAST_sans_silences.wav"  # Nom du fichier de sortie
output_path_test= "C:\\Users\\samue\\Downloads\\test_done.wav"

#FICHIER TEST POUR L4AJOUT D4INTRO
sound_test = AudioSegment.from_file(f"C:\\Users\\samue\\Downloads\\Enregistrement_test.wav")
sound_test = add_intro_song(sound_test, introduction_song)
sound_test.export(output_path_test, format="wav")

#input_file = remove_long_silences(input_file, output_file)

sound_test.export(output_path_test, format="wav")

#input_file = add_intro_song(input_file, introduction_song)

#input_file.export(output_path, format="wav")


# Exemple d'utilisation
#if __name__ == "__main__":
 #   input_file = f"C:\\Users\\samue\\Downloads\\podcast_son.wav"  # Remplacez par le chemin de votre fichier source
  #  output_file = "PODCAST_sans_silences.wav"  # Nom du fichier de sortie
   # remove_long_silences(input_file, output_file)


#1er commit : definition des fonctions
#2ème commit : definition de la version de pyhton nécéssaire et des dépendances
#3ème commit : Definition de la fonctiondetect_silence
#4ème commit : definition de la fonction remove_long_silence
#5ème commit : ajout de add_effect
#6ème commit : ajout de tests pour les différentes fo ctions
#7ème commit : ajout d'un fonction permettant le test et l'écoute pour un peu de fine tuning
#8ème commit : organisation  du package en quelque chose de cohérent avec les bonne pratiques 