import demucs.separate
import os
import traceback
import assemblyai as aai
import dotenv

def getVocals(filepath):
    try:
        os.rename(filepath, "song.mp3")
        demucs.separate.main(["--mp3", "--two-stems", "vocals", "-n", "mdx_extra", "song.mp3"])
        
        # Get the vocals file and saves it to the data folder
        os.rename("separated/mdx_extra/song/vocals.mp3", "data/vocals.mp3")
        
        # Remove the separated folder (try for linux and windows)
        try:
            os.system("rm -rf separated")
        except:
            os.system("rmdir /s /q separated")
    except Exception as e:
        print(f"An error occurred during separation: {e}")
        traceback.print_exc()

def convertToWav(filepath):
    try:
        os.system(f"ffmpeg -i {filepath} -acodec pcm_u8 -ar 22050 data/vocals.wav")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")
        traceback.print_exc()

def getLyrics(vocals_filepath):
    aai.settings.api_key = dotenv.get_key("ASSEMBLYAI_API_KEY")
    transcriber = aai.Transcriber()
    
    transcript = transcriber.transcribe(vocals_filepath)
    
    return transcript.text


def main():
    if not os.path.exists("data"):
        os.makedirs("data")
    filepath = input("Enter the path to the song file: ")
    getVocals(filepath)  # Get the vocals filename
    convertToWav("data/vocals.mp3")
    lyrics = getLyrics("data/vocals.wav")
    
    with open("data/lyrics.txt", "w") as f:
        f.write(lyrics)
    
    print("Lyrics saved to data/lyrics.txt")
    print("The lyrics need to be cleaned up and formatted properly. This is just a raw output that most likely contains errors. \nThe lyrics content is: \n", lyrics)

if __name__ == "__main__":
    main() 
