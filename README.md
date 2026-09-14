# Do You Know Your Beyonce?
> A quiz fit for the best bee in the HIVE

## Overview
> This code will quiz users in knowledge of Beyonce. It will question
> the user on facts about the artist and the user will earn points.
> Their final score will determine which level of Beyhive they are.

## Sample Questions and Responses

> Where was Beyonce born?
> 1. Houston, Tx
> 2. Little Rock, Ar
> 3. New York City, NY
>
> > What Girl Group was Beyonce in?
> 1. Pussycat Dolls
> 2. Destiny's Child
> 3. SWV
>
> > What is Beyonce's husband name?
> 1. Jay Z
> 2. Barrack Obama
> 3. Kanye West
>
> > What was Beyonce's first album?
> 1. Channel Orange
> 2. Dangerously in Love
> 3. Pink Friday
>
> > How many Grammys does Beyonce have?
> 1. 12
> 2. 35
> 3. 28


## Variables
> **DELETE AND REPLACE ME:** List the variables your program uses. For
> each one, note what it stores and why you structured it that way,
> especially for variables tracking results, explain whether a single
> variable or multiple variables makes sense for your program's logic.
>
> Example:
> - `score` (int): tracks total quiz points. A single variable works here
>   since results are cumulative and only one final score matters.
> - `decade_1920s_points`, `decade_1960s_points`, `decade_1980s_points`
>   (int): separate variables needed since multiple decades can tie for
>   highest score, one combined variable couldn't represent that.
> - `user_choice` (str or int): stores the user's response to a question,
>   compared against expected options to decide which branch of the
>   conditional runs.

## Conditional Logic Outline
> **DELETE AND REPLACE ME:** Outline every conditional statement in your
> program, in the order they appear. For each one, describe it in plain
> language (no code needed): which question/condition it relates to,
> each branch (`if`/`elif`/`else`), the exact condition that triggers
> each branch, the action(s) that happen in each branch, and note any
> nested conditionals and why they're nested.
>
> Example:
> - **Conditional statement 1** — related to "Which of the following
>   painters is an Impressionist? 1-Monet 2-Warhol 3-Rembrandt"
>   - `if` response is 1 (Monet): display congratulatory message,
>     increment `score` by 1
>   - `else`: display incorrect message and explain the correct answer
>
> - **Conditional statement 2** — reveals final results based on `score`
>   - `if` score is 3: display high-knowledge message
>   - `elif` score is 1 or 2: display some-knowledge message
>   - `else`: display message encouraging the user to learn more

## How to Run
1. Clone this repo
2. Run `python3 main.py` or `python main.py`

## Demo Video
[DELETE AND REPLACE ME: link to your 5-minute explanation video]
