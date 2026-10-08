# The Archive

**Pair:** *(Rugero Baruch,Kibe Ndungu,Tuyisenge Denys Prince)* **Repository:** *[(link)](https://github.com/baruchr-ctrl/Baba-yaga)*

> This file is Part E of the assignment — **15 marks**. Replace every placeholder below. Delete the instruction lines in italics as you go. Marks come from the reasoning, not the length.

---

## 1\. The record *(3 marks)*

*What one manuscript looks like in our system, and what we do when a field is unknown.*

| Field | Type | Example | If it is unknown, we… |
| --- | --- | --- | --- |
| id | string | `MS001` | `We give a string explaining that it is Invalid` |
| title | string |`Kibe`  | `We give a string explaining that it is Invalid`  |
| city | string | `Timbuktu` |  `We give a string explaining that it is Invalid` |
| year |  string or integer| `1700 `  |`We give a string explaining that it is Invalid` |
| condition |string| `fragile` |`We give a string explaining that it is Invalid`  |

---

## 2\. Our validation rules *(4 marks)*

| Field | Rule(s) | Rejects (example) |
| --- | --- | --- |
| id | `Length check : the string should be of length 5, format check: the first two characters and the last three have an exact format`|`Ms001` |
| title | `the string should not be less than 3 letters,empty or have random numbers in it` | `pn `|
| city | `the city given should already be in the list of cities given and should not be empty` | `lalaland` |
| year |  `the year should be in the accepted range`| `100` |
| condition |  `the condition should be in the list of conditions already given`|`meh`  |

### Who decided the year range?
I cant really change them because i would assume that since its easier to write ,alot of records would be clustered somewhere after 1900. this would make the conditions in 1100 look like outliers. we are losing the manuscripts but we have less biased data. there is no exact reason we couldnt go back but i would also assume that the manuscripts before 1100 we too few to be ignored.

---
### Cost of ignoring some cities
*When we ignore some cities we may be losing a lot of manuscripts and data from those cities
*Hence if we had the option to add cities depending on the data ,i think that would be a good option

## 3\. The `c.1590` decision *(3 marks)*

*Record MS009 in* `data/messy.csv` has the year `c.1590` — circa, approximately. Manuscript dating is often approximate, and a scholar may genuinely only know the decade. Your program currently rejects it, so the record is lost.

*Choose one and argue for it:*

- **(a)** Reject it. Only exact years enter the catalogue.
- **(b)** Store the year as text, so anything can be recorded.
- **(c)** Store `1590` plus a separate `approximate` flag.

**Our choice:**
We chose to ignore the whole number. 
**Why:**
if we were to accept a number like that then it would reduce the accurrancy of our info. we would rather have little precise info than have alot of inaccurate info
**What it costs us:**
ofcourse we would have less data to consider which might bias our conclusions

---

## 4\. Our test table *(3 marks)*

### `validate_year`

| Test data | Value | Expected | Actual | Pass? |
| --- | --- | --- | --- | --- |
| Normal | 1655 | valid |  |  |
| Abnormal | abc | invalid |  |  |
| Extreme (low) | 1000 | invalid |  |  |
| Extreme (high) | 1901 | invalid |  |  |
| Boundary (below) | 1100 | valid |  |  |
| Boundary (above) | 1900 | valid |  |  |

### `_______________` *(one other field of your choice)*

| Test data | Value | Expected | Actual | Pass? |
| --- | --- | --- | --- | --- |

---

## 5\. Collaboration reflection *(2 marks)*

*One paragraph each, written separately and signed. Do not write these together — the point is two honest accounts.*

***(Denys)*:** One thing my partner did that I will steal: Kibe found a slick mistake in my code which i found really cool.  One thing I would do differently next time: I will double check the branch and the repository i am pushing to 

***(Baruch)*:** One thing my partner did that I will steal:Not really steal but my partners are really cool. They like found a lot of errors in what i did and gave suggestions on what to do with them. Validate year was a tough one.
One thing I would do differently next time:Most of the things. checking what branch im on , what im commiting , if i had the auto save on and where my pull requests go beacuse these silly mistakes took alot of time to fix.

***(Kibe)*:** slicing technique by Denys is something Im planning to use:One thing i would do differently is how i make my pull requests and where they go.

## 6\. Declaration

*Required. See the integrity section of the brief.*

- [ ok] Both of us can explain every line in this repository.

- [ ok] AI assistants used for explanation only, not to generate our implementation or our tests.

**If you used an AI assistant, say what you asked and what you did with the answer:**
I asked it to help me with github at first. it gave me new commands like switch which actually worked. ( switch is to switch branches)
I also asked it to help me with storage especially how the code reads the file. i learnt a new key word "utf-8" which is practically an system which encodes all characters.

---

## Running this project

```bash
pytest -v                              # all tests
pytest tests/test_provided.py -v       # the given suite
pytest tests/test_yours.py -v          # your suite
python tools/check_collaboration.py    # your Part C report
```

[Link to the submission form](https://docs.google.com/forms/d/e/1FAIpQLSdO4trwNU4zPusr33LfYRhH2jvijj7sY42svbumH6f_15rCAQ/viewform?usp=preview)
