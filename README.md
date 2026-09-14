# Do You Know Your Beyonce?
> A quiz fit for the best bee in the HIVE

## Overview
> This code will quiz users in knowledge of Beyonce. It will question
> the user on facts about the artist and the user will earn points.
> Their final score will determine which level of Beyhive they are.

## Sample Questions and Responses

> Where was Beyonce born? (Enter 1-3)
> 1. Houston, Tx
> 2. Little Rock, Ar
> 3. New York City, NY
>
> > What Girl Group was Beyonce in? (Enter 1-3)
> 1. Pussycat Dolls
> 2. Destiny's Child
> 3. SWV
>
> > What is Beyonce's husband name? (Enter 1-3)
> 1. Jay Z
> 2. Barrack Obama
> 3. Kanye West
>
> > What was Beyonce's first solo album? (Enter 1-3)
> 1. Channel Orange
> 2. Dangerously in Love
> 3. Pink Friday
>
> > Bonus: How many Grammys does Beyonce have? (Enter 1-3)
> 1. 12
> 2. 28
> 3. 35


## Variables
>
> - `score` (int): tracks all quiz points. A single variable works here
>   since results are cumulative and only one final score matters.
>
> - `birthplace` (str): asks for user input and stores the user's response to a question 1.
>    A single variable works here since results are specific to this question.
> - `girl_group` (str): asks for user input and stores the user's response to a question 2.
>    A single variable works here since results are specific to this question.
> - `husband` (str): asks for user input and stores the user's response to a question 3.
>    A single variable works here since results are specific to this question.
> - `album` (str): asks for user input and stores the user's response to a question 4.
>    A single variable works here since results are specific to this question.
> - `grammy` (str): asks for user input and stores the user's response to a question 5.
>    A single variable works here since results are specific to this question.

## Conditional Logic Outline
>
> - **Conditional statement 1** — Where was Beyonce born? (Enter 1-3)
> 1. Houston, Tx, 2. Little Rock, Ar, 3. New York City, NY
>   - `if` response is 1 (Houston, Tx): display "correct",
>     increase `score` by 1
>   - `else`: display "wrong" and print the correct answer
>
>
> - **Conditional statement 2** — What Girl Group was Beyonce in? (Enter 1-3)
> 1. Pussycat Dolls, 2. Destiny's Child, 3. SWV
>   - `if` response is 2 (Destiny's Child): display "correct",
>     increase `score` by 1
>   - `else`: display "wrong" and print the correct answer
>
>
> - **Conditional statement 3** — > What is Beyonce's husband name? (Enter 1-3)
> 1. Jay Z, 2. Curtis, 3. Kanye West
>   - `if` response is 1 (Jay Z): display "correct",
>     increase `score` by 1
>   - `else`: display "wrong" and print the correct answer
>
>
> - **Conditional statement 4** — > > What was Beyonce's first solo album? (Enter 1-3)
> 1. Channel Orange, 2. Dangerously in Love, 3. Pink Friday
>   - `if` response is 2 (Dangerously in Love): display "correct",
>     increase `score` by 1
>   - `else`: display "wrong" and print the correct answer
>
>
> - **Conditional statement 5** — Bonus: How many Grammys does Beyonce have? (Enter 1-3)
> 1. 12, 2. 28, 3. 35
>   - `if` response is 3 (35): display "correct",
>     increase `score` by 3
>   - `else`: display "wrong" and print the correct answer
>
>
> - **Conditional statement 6** — final results based on `score`
>   - `if` score is 7: print "THEE BUG A BOO" 
>   - `elif` score is 4 or 3: print "Barely Buzzin"
>   - `else`: print "Not a bee at all"

## How to Run
1. Clone this repo
2. Run `python3 main.py` or `python main.py`

## Demo Video
[DELETE AND REPLACE ME: link to your 5-minute explanation video]
