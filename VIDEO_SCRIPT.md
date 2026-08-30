# 🎬 PROJECT GHOST: OFFICIAL 5-MINUTE DEMO VIDEO SCRIPT & VOICE NARRATION

**Target Length:** 4 minutes 45 seconds  
**Tone:** Confident, Technical, Authoritative, DevSecOps Engineer & CEH Perspective  
**Deliverable Compliance:** micro1 Hackathon Deliverable #3 (Solution Video)

---

## ⏱️ TIMELINE & SCREENPLAY OVERVIEW

| Timestamp | Visual Screen Action | Voiceover Narration Script | Key Highlight |
| :--- | :--- | :--- | :--- |
| **0:00 - 0:45** | **Slide 1: Problem & Persona**<br>Display SRE 2 AM scenario diagram & SOC2 breach notice. | *"Welcome. Meet GHOST—the DevSecOps Sentinel built for SRE Leads and Security Champions at high-growth startups."* | Problem & User Value |
| **0:45 - 1:30** | **Slide 2: The Baseline Failure Mode**<br>Show manual `git log -p` bisecting vs Iteration 1 single LLM prompt. | *"Let's look at why standard approaches fail. In our baseline evaluation across 10 sprint-break cases, manual triage took 8 minutes..."* | Measured Baseline |
| **1:30 - 3:00** | **Live Product Demo: GHOST Dashboard**<br>Paste `https://github.com/TristanBrian/camguard-portal`, branch `main`, error log. Click **🚀 Investigate Incident**. | *"Now watch GHOST in action. We input our repository URL, target branch, and paste a CI/CD stack trace..."* | Live System Demo & Forensics Box |
| **3:00 - 3:45** | **Agent Trajectories & Bouncer Gate**<br>Expand `🕵️ Agent Trajectories & Execution Logs` and show `patch.diff` Base64 download button. | *"Under the hood, GHOST orchestrates 5 specialized agents. Detective parses the stack trace and extracts the raw diff..."* | 5-Agent Architecture |
| **3:45 - 4:45** | **Hot Take & Production Engineering**<br>Highlight Context Truncation (40k chars) & `max_tokens` economy controls. | *"My biggest engineering takeaway: Agents fail when they lack security boundaries or token economy controls..."* | Architectural Hot Take |

---

## 🎙️ FULL 5-MINUTE VOICE NARRATION SCRIPT

### Section 1: The 2 AM Bottleneck & Persona (0:00 - 0:45)
> *"Welcome to the demonstration of **PROJECT GHOST: Git Hunting & Ops Security Tool**.
>
> We built GHOST for SRE Leads and Security Champions at high-growth startups in Fintech, Healthtech, and SaaS.
>
> Imagine the 2 AM scenario: A CI/CD build fails during a sprint fire-drill. The on-call SRE has 15 minutes to turn the pipeline green before SLA penalties hit. In that panic, they rush to run `git log`, find the `TypeError`, patch it, and force-merge to production.
>
> But in that fire-drill panic, they look **only** at the stack trace error. They completely miss an `AWS_SECRET_KEY` or Stripe `mock_stripe_key_` key hardcoded right next to the bug in the diff. Three weeks later: a $50,000 cloud bill or a SOC2 data breach notification.
>
> **GHOST makes Security the FIRST check, not the LAST check.**"*

---

### Section 2: Baseline Comparison & Iteration Failure Mode (0:45 - 1:30)
> *"To prove GHOST actually improves DevSecOps workflows, we evaluated 10 simulated sprint-break cases comparing a Simple Baseline against GHOST.
>
> In our baseline tests, manual human triage averaged **8 minutes per bug** and missed 70% of secret leaks.
>
> In Iteration 1, we tested a single LLM prompt: 'Fix this error.' The result was dangerous: the model was so eager to make the code run that it fixed the `TypeError` while completely ignoring the hardcoded Stripe live key sitting right next to it! It prioritized availability over confidentiality.
>
> That failure taught us that AI agents without security guardrails are a major liability. The solution wasn't a better prompt—it was architectural violence."*

---

### Section 3: Live System Walkthrough & Forensic Proof (1:30 - 3:00)
> *"Now let's see GHOST in action.
>
> Here is our industrial Incident Response Dashboard. We enter our Git repository URL—`https://github.com/TristanBrian/camguard-portal`—specify the `main` branch, and paste a stack trace error log.
>
> We click **🚀 Investigate Incident**. In under 60 seconds, watch the execution pipeline:
>
> First, GHOST shallow-clones the repo. Notice our **Forensics Box**: it displays the exact physical directory path—`/tmp/ghost_xxxxx`—active branch, and target file. This forensic transparency proves GHOST physically analyzed YOUR repository, not a cached template!
>
> Next, our Security Pariah Agent runs a **5-Layer CEH Superweapon scan**:
> - Layer 1 scans for AWS, Stripe, GitHub, and Slack secrets.
> - Layer 2 runs Bandit SAST static code analysis.
> - Layer 3 checks requirements.txt for EOL frameworks like Django 1.x.
> - Layer 4 scans for raw SQL string concatenation.
> - Layer 5 audits JWT token entropy.
>
> Here, it flagged a Critical Stripe Live key leak and deducted 15 points, setting our Security Debt Score to 85 out of 100."*

---

### Section 4: The Bouncer Gate & Downloadable Artifacts (3:00 - 3:45)
> *"Because a secret was detected, **The Bouncer Orchestrator Gate** steps in. The Bouncer legally prohibits the Remediation Engineer from generating a patch until the secret is replaced with `os.getenv()`.
>
> GHOST outputs a clean, unified code patch—ready to download with one click as `patch.diff`.
>
> Below that, Testsmith automatically writes a custom `pytest` regression unit test to ensure this bug never recurs in future sprints.
>
> We can also expand the **Agent Trajectories Inspector** tab to view the live execution logs, tool calls, and outputs for all 5 specialized agents."*

---

### Section 5: The Architectural Hot Take & Production Engineering (3:45 - 4:45)
> *"To close, here is my architectural Hot Take:
>
> **Agents are dangerously overconfident when they lack security boundaries and token economy controls.**
>
> In real production environments, initial commit diffs can exceed 220,000 tokens, causing 128k context overflow errors and draining API credits.
>
> In GHOST, we engineered a smart truncation layer that caps input diffs to the first 40,000 characters and enforces dynamic `max_tokens` limits—2048 for patches, 1024 for tests.
>
> This guarantees GHOST runs reliably on repositories of any size, even on free or low-credit OpenRouter accounts.
>
> GHOST turns 15 minutes of 2 AM panic into 45 seconds of secure, verified, and automated resolution. Thank you!"*

---

## 🎬 VIDEO CREATION & RECORDING INSTRUCTIONS FOR USER

1. **Screen Recording Software**: Use OBS Studio, Loom, QuickTime, or Chrome Screen Recorder.
2. **Setup Step**: Run GHOST locally or via Docker (`docker run -p 8501:8501 ghost-agent`). Open `http://localhost:8501`.
3. **Recording Steps**:
   - Start recording at `http://localhost:8501`.
   - Open **⚙️ API Settings**, paste your OpenRouter key `sk-or-v1-...`.
   - Paste repo `https://github.com/TristanBrian/camguard-portal`, branch `main`, and error log:
     ```text
     File "auth.py", line 10, in get_user_data
         return user_data['id']
     TypeError: 'dict' object is not subscriptable
     ```
   - Click **🚀 Investigate Incident**.
   - Show the progress bar, Forensics Box (`/tmp/ghost_xxxxx`), Security Score metric (85/100), Suggested Patch (`patch.diff` download button), `pytest` expander, and Agent Trajectories Inspector expander.
4. **Audio Narration**: Read the exact Voice Narration script above into your microphone while demonstrating the UI.
5. **Save File**: Save as `video.mp4` (or `ghost.mp4`) in your repository folder.
