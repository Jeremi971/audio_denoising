import os
from pydub import AudioSegment # type: ignore

def convert_mp3_to_wav(mp3_path, wav_path):
    """Convertit un fichier MP3 en WAV."""
    sound = AudioSegment.from_mp3(mp3_path)
    sound.export(wav_path, format="wav")
    print("Conversion terminée avec succès!")

if __name__ == "__main__":
    # Récupérer le répertoire courant
    current_directory = os.getcwd()

    # Chemins des fichiers
    mp3_path = os.path.join(current_directory, "data", "radiobruite.mp3")
    wav_path = os.path.join(current_directory, "data", "radiobruite.wav")

    # Convertir le fichier MP3 en WAV
    convert_mp3_to_wav(mp3_path, wav_path)
