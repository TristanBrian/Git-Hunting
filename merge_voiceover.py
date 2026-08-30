import os
import subprocess

print("🎙️ Starting GHOST Voiceover Merge...")

script_text = """
Welcome to GHOST—the DevSecOps Sentinel. Built for SRE leads and Security Champions.
Imagine the 2 AM scenario: A CI/CD build fails during a sprint fire-drill. The on-call engineer has 15 minutes to turn the pipeline green. In that panic, they rush to fix the bug, but they completely miss an AWS secret key hardcoded right next to the bug in the diff.
Three weeks later: a fifty-thousand dollar cloud bill or a SOC2 data breach notification.
GHOST stops this by making Security the FIRST check, not the last check.
As you can see in this demonstration, we input our repository URL, target branch, and paste the error log.
Under the hood, GHOST orchestrates 5 specialized agents. Our Detective parses the stack trace and extracts the raw diff.
Next, our Security Pariah Agent runs a 5-Layer Certified Ethical Hacker scan, checking for secrets, static vulnerabilities, and dependency flaws.
If a secret is detected, our Orchestrator—The Bouncer Gate—steps in. It legally prohibits the Remediation Engineer from generating a patch until the secret is securely replaced.
GHOST then outputs a clean, unified code patch, ready to download.
Finally, Testsmith automatically writes a custom pytest regression unit test, ensuring this bug never recurs.
With smart context truncation and strict API token economy controls, GHOST turns 15 minutes of 2 AM panic into 45 seconds of secure, verified, and automated resolution. Thank you.
"""

# Generate TTS Voice
print("1️⃣ Generating high-quality Neural TTS voice...")
tts_cmd = [
    os.path.expanduser("~/.local/bin/edge-tts"),
    "--text", script_text.strip(),
    "--write-media", "voice.mp3",
    "--voice", "en-US-ChristopherNeural"
]
subprocess.run(tts_cmd, check=True)

# Speed up the voice to fit exactly 94 seconds
print("2️⃣ Adjusting voice tempo to fit exactly with the screen recording (atempo=1.12)...")
speed_cmd = [
    "ffmpeg", "-hide_banner", "-loglevel", "error",
    "-i", "voice.mp3",
    "-filter:a", "atempo=1.12",
    "-y", "voice_fast.mp3"
]
subprocess.run(speed_cmd, check=True)

# Merge with user's GHOSTmp4 (replace original silent audio)
print("3️⃣ Merging Voiceover with Video...")
merge_cmd = [
    "ffmpeg", "-hide_banner", "-loglevel", "error",
    "-i", "GHOSTmp4",
    "-i", "voice_fast.mp3",
    "-c:v", "copy",
    "-c:a", "aac",
    "-map", "0:v:0",
    "-map", "1:a:0",
    "-shortest",
    "-y", "final_demo.mp4"
]
subprocess.run(merge_cmd, check=True)

# Cleanup
os.remove("voice.mp3")
os.remove("voice_fast.mp3")

print("✅ SUCCESS! Final Demo Video created: final_demo.mp4")
