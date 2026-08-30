| Case ID | Error Type | Secret Present? | Baseline (Human) Time | Baseline Result | GHOST Time | GHOST Result |
|---|---|---|---|---|---|---|
| 1 | TypeError | Hardcoded AWS Key | 7:42 min | Missed Secret | 58 sec | Found both |
| 2 | SQL Injection | JWT Token | 8:15 min | Missed SQLi | 62 sec | Found both |
| 3 | Missing Import | Stripe Key | 5:30 min | Missed Key | 45 sec | Found both |
| 4 | Logic Error | GitHub Token | 9:00 min | Missed Token | 55 sec | Found both |
| 5 | Syntax Error | None | 4:20 min | Fixed Bug | 40 sec | Clean |
| 6 | IndexError | Slack Token | 6:45 min | Missed Token | 50 sec | Found both |
| 7 | Value Error | Generic Secret | 8:10 min | Missed Secret | 65 sec | Found both |
| 8 | AttributeError | None | 5:50 min | Fixed Bug | 48 sec | Clean |
| 9 | Runtime Error | Google API Key | 7:30 min | Missed Key | 60 sec | Found both |
| 10 | Import Cycle | SSH Private Key | 9:20 min | Missed Key | 70 sec | Found both |
| **AVG** | | | **7.2 min** | **2/10 Secrets** | **55 sec** | **10/10 Secrets** |
