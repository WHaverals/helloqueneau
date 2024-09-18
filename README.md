# Hello, Queneau?

<img src="img/ex_in_style-COLOR2.png" width="600">

<sub>Stefan Themerson's cover for the 1958 edition of Raymond Queneau's "Exercises in Style", vectorized and colorized by Wouter Haverals.</sub>

**Note** -- this repo is a work in progress and serves as a viable proof of concept. Beware of bugs! 🐞

## Overview

While much of the research around **style transfer** in AI focuses on transforming or generating text with specific stylistic goals, it often fails to critically examine what **style** means from a literary perspective. More importantly, it overlooks how well AI can **recognize and classify** different **literary styles**.

This project draws on **Raymond Queneau**'s famous work *Exercices de Style* (originally published in 1947), a collection of **99 retellings of a single simple story**: someone gets on a bus and is annoyed by another passenger. Each retelling is written in a different style, or showcasing variations in register, tone, narrative perspective, linguistic play, etc.

We’ve gathered these 99 versions in different languages and are using them to explore how well **large language models (LLMs)** can recognize and classify different literary styles.

Things we are exploring:

- Can LLMs **discern** between different styles?
- Do they **recognize** and maintain stylistic nuances when generating text?
- How do they **handle cross-linguistic consistency** when translating or interpreting style across different languages?

## What we've done so far

- We have built a **multilingual dataset** from various translations of *Exercices de Style*, which includes **annotations** on stylistic elements, narrative structure, and rhetorical devices.
- We are also testing the ability of LLMs to recognize style consistently across multiple languages, which has proven to be one of the major limitations so far!

Early experiments show that LLMs can indeed differentiate between styles; they perform well in terms of recognizing 'genre' and 'register', but they struggle when confronted with more intricate features like focatlisation or linguistic play.
