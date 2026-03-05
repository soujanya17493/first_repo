# import whisper

# model = whisper.load_model("tiny.en")



import whisper

# Load tiny model
model = whisper.load_model("tiny")

# Transcribe audio
result = model.transcribe("/home/soujanyamutapuram/Documents/Soujanya_python /1stbook/WhatsApp Audio 2026-02-20 at 2.27.17 PM.mp3")

# Print result
print("\nTranscription:")
print(result["text"])