import openai
import sys
import os

# Get the API key from your environment.
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

# Enter the name of the file in /audio when running this script
filename = sys.argv[1]

# Transcribe the audio file
audio_file= open(f"Audio/{filename}", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
with open("transcript.txt", "w") as file:
    file.write(str(transcript))

# Create the prompt.
prompt = f"""Summarise this recording into a slide format, including a headline, bullet points for the slides and speaker notes underneath each slide.

Headlines should be interesting and engaging.

Content: {transcript}"""

# Generate the summary using completions
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

# Write completion to a text file
with open("summary.txt", 'w') as f:
    f.write(completion.choices[0].message.content)

# Print the estimated cost of the completion (excludes Whisper API cost)
print("Summary Cost: $", ((completion.usage.prompt_tokens / 1000 * 0.03) + completion.usage.prompt_tokens / 1000 * 0.09))