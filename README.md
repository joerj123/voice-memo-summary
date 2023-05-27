# OpenAI Transcription and Summary Script

This script leverages the OpenAI's GPT-3.5-turbo model for summarizing transcriptions of audio files. It first transcribes the audio using the OpenAI Whisper ASR API, then summarizes the transcript into a slide format including headlines, bullet points, and speaker notes.

## Requirements

- Python 3.6 and above
- OpenAI Python v0.27.0
- An OpenAI API key with permissions to use the Whisper ASR API and the GPT-3.5-turbo model.

## Installation

1. Clone this repository to your local machine.

2. Install the required Python packages. You can do this by running `pip install openai`.

## Setup

To use this script, you need to set up your OpenAI API key. 

You can set it as an environment variable with the name `OPENAI_API_KEY`:

```bash
export OPENAI_API_KEY=your-api-key-here
```

Ensure that this environment variable is set in the same environment from which you'll run the script.

## Usage

The script takes the filename of the audio file as a command-line argument. The audio file should be located in the "Audio" directory. It then transcribes the audio and summarizes it, writing the results to "transcript.txt" and "summary.txt", respectively.

Here's an example of how to run the script:

```bash
python script.py your-audio-file.mp3
```

Remember to replace "your-audio-file.mp3" with the name of your actual audio file.

The prompt can be easily modified to alter the output to a format of your choice. 

## Output

The script writes the transcript of the audio file to a file called "transcript.txt". It then writes a summarized version of the transcript, in slide format, to a file called "summary.txt". It also prints the estimated cost of the summary.

## Note

Please be aware that the usage of OpenAI's APIs incurs costs as per OpenAI's pricing. The printed cost estimate only covers the summary and does not include the cost of the Whisper API for transcribing the audio file.