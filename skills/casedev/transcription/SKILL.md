---
name: transcription
description: Transcribes audio and video files through case.dev with speaker diarization. Supports MP3, WAV, M4A, FLAC, OGG, WEBM, MP4 up to 5GB. Use when the user mentions "transcribe", "transcription", "deposition recording", "hearing audio", "speaker labels", or needs to convert audio/video to text.
---

# case.dev Transcription

Audio and video transcription with speaker diarization, ideal for depositions, hearings, and recorded proceedings. Supports MP3, WAV, M4A, FLAC, OGG, WEBM, and MP4 up to 5GB.

Requires the `casedev` CLI. See `setup` skill for installation and auth.

## Start a Transcription

The source file must be in a vault:

```bash
casedev transcribe run --vault VAULT_ID --object OBJECT_ID --json
```

Flags: `--speaker-labels` (diarization), `--speakers-expected N`, `--language`, `--format`, `--auto-highlights`.

## Check Status

```bash
casedev transcribe status TRANSCRIPTION_ID --json
```

Statuses: `queued` -> `processing` -> `completed` or `failed`.

## Get Result

```bash
casedev transcribe result TRANSCRIPTION_ID --json
```

Fetches transcript text. Fails if the job is not yet completed.

## Watch Until Complete

```bash
casedev transcribe watch TRANSCRIPTION_ID --json
```

Flags: `--interval` (default: 3s), `--timeout` (default: 900s).

## Common Workflow

```bash
# 1. Upload to vault
casedev vault object upload ./deposition-recording.mp3 --vault VAULT_ID --json

# 2. Start transcription with speaker labels
casedev transcribe run --vault VAULT_ID --object OBJECT_ID --speaker-labels --speakers-expected 4 --json

# 3. Watch until complete
casedev transcribe watch TRANSCRIPTION_ID --json
```

## Troubleshooting

**"Invalid file type for transcribe"**: Only audio/video MIME types accepted. Check with `casedev vault object list`.

**Transcription failed**: Check `casedev transcribe status TRANSCRIPTION_ID --json` for error details. Common causes: corrupted file, unsupported codec, file too large.

**Long audio (2+ hours)**: Increase timeout with `--timeout 3600`.
