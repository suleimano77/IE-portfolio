# 🎥 GEMBA LENS: AI time study and auto-written standard work

> **Status: planned for Jul–Oct 2027.** This page states the problem. Results will replace the targets below as they arrive.

## The problem
Time studies are still done with a stopwatch and clipboard, ergonomic assessments by eye, and standard work instructions are written by hand over days. Can a laptop camera do all three from one video?

## Approach (built in rungs; each rung is shippable)
1. **Automatic time study:** MediaPipe hand tracking → work-element boundaries → cycle-time distribution and bottleneck element, validated against a 30-cycle manual stopwatch study.
2. **Ergonomic risk:** REBA score from body pose on every frame; riskiest moments flagged.
3. **Standard work:** a vision-language model labels elements and drafts instructions with keyframes.
4. **Line balancing:** split the task across stations to meet a takt time.
5. **App:** upload a video, download the full report.

## Target headline
"Within X% of manual timing across 30 cycles; standard work generated in minutes instead of days."

## Data
Self-recorded videos of repetitive assembly tasks. No other people are filmed.
