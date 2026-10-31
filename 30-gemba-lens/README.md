# GEMBA LENS

Status: not started. Planned for July to October 2027.

## The question

Time studies are still mostly done with a stopwatch, ergonomic checks by eye, and work instructions are written by hand. How much of that can be done from one video of the task?

## How I plan to build it

1. Track hands with MediaPipe, split the video into work elements, and time every cycle. Compare the results with a 30-cycle stopwatch study I do by hand in the foundations phase.
2. Score ergonomic risk (REBA) from body posture on every frame and flag the worst moments.
3. Use a vision-language model to label each element and draft standard work instructions with screenshots.
4. Balance the task across two to four stations to meet a target takt time.
5. Wrap it in an app: upload a video, get the report back.

## Data

Videos of me doing repetitive tasks (LEGO assembly, packing). Nobody else is filmed.
