# Problem Statement — VitalMetrics

## Problem Statement
Checking your BMI, BMR, TDEE, and Body Fat Percentage usually means visiting a different
website for each one, since no single place brings all four together. On top of that, most
online calculators just hand you a number without explaining what it means — for example,
whether your BMI actually falls in a healthy range. VitalMetrics is a simple Python program that
solves both problems: it puts all four calculations behind one menu and also translates the BMI
result into a plain-language category.

## Scope of the Project
- Covers four calculations: BMI, BMR, TDEE, and Body Fat Percentage.
- Terminal-only — no GUI, no database.
- Nothing is saved between runs — all data resets once the program is closed.
- A simple personal calculator, not a replacement for professional medical advice.

## Target Users
Basically anyone who just wants to quickly check their basic health stats without having to
Google around on a bunch of different sites.

## High-Level Features
- One menu that gives access to all four calculators.
- BMI results come with a simple label (Underweight / Healthy weight / Overweight / Obese).
- BMR is calculated differently depending on gender.
- TDEE adjusts the result based on activity level (5 options).
- Body Fat Percentage supports 4 categories: Adult male, Adult female, Boy, Girl.
- The menu keeps repeating until the user chooses to exit.
