# Python lyric extractor from audio

This project provides a convenient way to extract vocals from a song and generate a semi-accurate text transcription of the lyrics. It leverages the following tools:

-   **Demucs:** A powerful deep learning-based source separation model for isolating vocals from music. ([https://github.com/facebookresearch/demucs](https://github.com/facebookresearch/demucs))
-   **AssemblyAI:** An AI-powered transcription service. ([https://www.assemblyai.com/](https://www.assemblyai.com/))

## Dependencies

1. **demucs:** Install with `pip install demucs`.
2. **ffmpeg:** Install from your system's package manager or from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
3. **AssemblyAI API Key:**
    - Sign up for a free [AssemblyAI](https://www.assemblyai.com/) account.
    - Obtain your API key from your AssemblyAI dashboard.
    - Store your API key in a `.env` file in the project directory (see section below).
4. **Python libraries:** `assemblyai`, `dotenv`, `os`, `traceback` (install with `pip install assemblyai dotenv`)

## Environment Setup

1. **Open the `.env` file:** Then input your api key:

    ```
    ASSEMBLYAI_API_KEY="YOUR_API"
    ```

    **Important:** Make sure to replace `YOUR_API` with your actual API key.

2. **Install dependencies:** Run the script in your terminal.

```bash
pip install demucs torch assemblyai dotenv
```

## Usage

1. Place the song file you want to process in the root directory of the project.
2. Run the script from your terminal: `python main.py`
3. The script will prompt you to enter the full path to your song file.
4. After processing:
    - The isolated vocals will be saved as `data/vocals.wav`.
    - The generated lyrics will be saved as `data/lyrics.txt`.

## Important Notes

-   **Transcription Accuracy:** The provided transcription is a raw output and will likely contain errors. Manual cleanup, formatting, and editing will be required for optimal results.
-   **Audio Preprocessing:** The quality of vocal separation and transcription can depend on the original audio quality. If needed, consider pre-processing your audio (e.g., normalization, noise reduction) before running the script.

## Example

```bash
python main.py
Enter the path to the song file: /path/to/your/song.mp3
Lyrics saved to data/lyrics.txt
The lyrics need to be cleaned up and formatted properly. This is just a raw output that most likely contains errors.
The lyrics content is:
[Lyrics Text]
```
