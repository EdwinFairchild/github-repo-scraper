# github-repo-scraper
![pylint workflow](https://github.com/EdwinFairchild/github-repo-scraper/actions/workflows/pylint.yml/badge.svg)
<br>
Simple script to  scrape info from a github repo. Since this  is simple web scraping. <br>
there is no need for web api or auth tokens, the intended use here is to track repos <br>
you are not an owner of. The obvious caveat here is that the repo needs to be public.

### Example output
This example scrapes the main landing page and displays some info about the repo.
```
last_user           EdwinFairchild
date                Apr 20, 2023
time                2023-04-20T15:37:00
 * Builds a specific RF Phy closed branch as a temp fixrds in separate stepiltering
commits             937
issues              12
pull_requests       13
forks               28
stars               18
```
### Example output
This example scrapes the pull request tab and displays each pull request's author <br>
time and title as well as passing failing check and any labels given to the PR.
```
Title: testing
Author: EdwinFairchild
Time: 2023-04-18T17:04:23Z
Check Status: X
Label: N/A
--------------------------------
Title: Documentation: Adding pull request template.
Author: sihyung-maxim
Time: 2023-04-17T20:11:03Z
Check Status: OK
Label: documentation, help wanted, WIP
--------------------------------
Title: MAX78000, MAX78002: Checkpoint update for FaceID database generation
Author: aniktash
Time: 2023-04-14T20:56:12Z
Check Status: OK
Label: MAX78000, MAX78002
--------------------------------
Title: Update LittleFS Library
Author: Jacob-Scheiffler
Time: 2023-04-12T19:13:15Z
Check Status: OK
Label: enhancement
--------------------------------
Title: MAX32662, MAX32665, MAX32672: Added new Hello_World/TFT Examples and TFT_ST7735S Driver.
Author: sihyung-maxim
Time: 2023-04-07T16:18:38Z
Check Status: X
Label: API Change, MAX32662, MAX32665, MAX32672
--------------------------------
Title: MAX32655, MAX32680: Renaming registers with TX/RX LDO to RF/BB LDO.
Author: kevin-gillespie
Time: 2023-04-04T14:42:00Z
Check Status: X
Label: Register Change, WIP
--------------------------------
Title: MAX32672: Updated AESKEYS and SYS Registers, Deprecated GPIO SetVSSEL and Pad Options.
Author: sihyung-maxim
Time: 2023-03-31T17:40:24Z
Check Status: X
Label: API Change, MAX32672
--------------------------------
Title: string terminate pointer buffer since were treating it as string
Author: EdwinFairchild
Time: 2023-03-28T14:50:30Z
Check Status: OK
Label: N/A
--------------------------------
Title: MAX32655: Updated board LP setting.
Author: kevin-gillespie
Time: 2023-03-21T20:02:40Z
Check Status: OK
Label: MAX32655
--------------------------------
Title: Tools: Adding BLE power calculator tool for MAX32690.
Author: victor-levi-maxim
Time: 2023-03-15T14:00:17Z
Check Status: OK
Label: MAX32690, Tools
```
