# VitalMetrics: A Simple Health & Nutrition Calculator

## Overview
VitalMetrics is a lightweight Python program that runs in the terminal and brings four commonly
used health numbers — **BMI**, **BMR**, **TDEE**, and **Body Fat Percentage** — into a single
menu, so you don't have to hunt across separate websites for each one.

## Features
- **BMI Calculator** – Enter your height and weight to get your BMI along with a plain-language
  label: underweight, healthy weight, overweight, or obese.
- **BMR Calculator** – Enter your gender, height, weight, and age to find your Basal Metabolic
  Rate (the calories your body burns while completely at rest).
- **TDEE Calculator** – Builds on the BMR figure by factoring in your activity level to estimate
  your total daily calorie needs.
- **Body Fat Percentage Calculator** – Choose a category (Adult male / Adult female / Boy /
  Girl), enter your height, weight, and age, and get an estimated body fat percentage.
- The menu keeps looping, so you can run several calculators back-to-back without restarting
  the program.

## Technologies / Tools Used
- Python 3 (only the built-in input()/print() functions — no extra libraries needed)
- Terminal / command line

## Steps to Install & Run
1. **Install Python 3** (skip if it's already installed):
   - Download it from [python.org/downloads](https://www.python.org/downloads/) and install it.
   - Confirm it's working by opening a terminal (Command Prompt / PowerShell on Windows,
     Terminal on Mac/Linux) and running:
     ```
     python3 --version
     ```
     If that isn't recognized, try `python --version` — some systems default to `python` for
     Python 3.

2. **Grab the project files.** Either clone the repository with git, or download it directly:
   - **Option A — clone with git:**
     ```
     git clone https://github.com/SouM-exe/Vityarthi_Project.git
     cd Vityarthi_Project
     ```
   - **Option B — download without git:** open the repository page, click the green **Code**
     button → **Download ZIP**, unzip it, and open a terminal inside the unzipped folder.

3. **Launch the program** from inside that folder:
   ```
   python3 vitalmetrics.py
   ```
   (If `python3` isn't recognized, try `python vitalmetrics.py` instead.)

4. **Using it:** pick a number from the menu (`1`–`4` for a calculator, `0` to quit), then answer
   the prompts that follow (height, weight, age, and so on).

## Instructions for Testing
Testing was done by hand — running each menu option with realistic values and checking the
output against a separate calculator:
- **BMI**: tested values just above and below 18.5 / 24.9 / 29.9 to confirm the label changes
  correctly.
- **BMR**: ran identical height/weight/age figures as both `male` and `female` to confirm the
  two formulas produce different results.
- **TDEE**: ran the same profile through all five activity levels to confirm each one changes
  the output.
- **Body Fat**: tried each of the four categories once.

> Note: the program currently expects exact input formatting (e.g. `male`, `Adult male`) and
> doesn't validate bad input, so entering letters where a number is expected will crash it. This
> is noted as a known limitation in the project report.

## Screenshots
_Add a couple of terminal screenshots here (main menu + one sample run) before submitting._

## Project Files
- `vitalmetrics.py` — the main program (menu + all four calculators)
- `statement.md` — problem statement and scope
- `README.md` — this file
