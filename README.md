# The Archive

**Pair:** *(Rugero Baruch,Kibe Ndungu,Tuyisenge Denys Prince)* **Repository:** *[(link)](https://github.com/baruchr-ctrl/Baba-yaga)*

> This file is Part E of the assignment — **15 marks**. Replace every placeholder below. Delete the instruction lines in italics as you go. Marks come from the reasoning, not the length.

---

## 1\. The record *(3 marks)*

*What one manuscript looks like in our system, and what we do when a field is unknown.*

| Field | Type | Example | If it is unknown, we… |
| --- | --- | --- | --- |
| id | string | `MS001` | `Invalid` |
| title | string |`Kibe`  | `Invalid` |
| city | string | `Timbuktu` |  `Invalid`|
| year |  string or integer| `1700 `  |`Invalid`  |
| condition |string| `fragile` |`Invalid`  |

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

*The brief gave you 1100–1900. That was a decision someone made, and it has costs. 1900 excludes a modern copy of an old text. 1100 excludes anything earlier. State whether you accept these bounds or would change them, and say what your choice throws away. An undefended range scores 1 of the 4 marks.*

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

**Why:**

**What it costs us:**

---

## 4\. Our test table *(3 marks)*

### `validate_year`

| Test data | Value | Expected | Actual | Pass? |
| --- | --- | --- | --- | --- |
| Normal | 1655 | valid |  |  |
| Abnormal |  |  |  |  |
| Extreme (low) | 1100 | valid |  |  |
| Extreme (high) |  |  |  |  |
| Boundary (below) | 1099 | invalid |  |  |
| Boundary (above) |  |  |  |  |

### `_______________` *(one other field of your choice)*

| Test data | Value | Expected | Actual | Pass? |
| --- | --- | --- | --- | --- |

---

## 5\. Collaboration reflection *(2 marks)*

*One paragraph each, written separately and signed. Do not write these together — the point is two honest accounts.*

***(Denys)*:** One thing my partner did that I will steal: Kibe found a slick mistake in my code which i found really cool.  One thing I would do differently next time: I will double check the branch and the repository i am pushing to 

***(partner 2 name)*:** One thing my partner did that I will steal: One thing I would do differently next time:

***(Kibe)*:**slicing technique by Denys is something Im planning to use:One thing i would do differently is how i make my pull requests and where they go.

## 6\. Declaration

*Required. See the integrity section of the brief.*

- [ ok] Both of us can explain every line in this repository.

- [ ok] AI assistants used for explanation only, not to generate our implementation or our tests.

**If you used an AI assistant, say what you asked and what you did with the answer:**

---

## Running this project

```bash
pytest -v                              # all tests
pytest tests/test_provided.py -v       # the given suite
pytest tests/test_yours.py -v          # your suite
python tools/check_collaboration.py    # your Part C report
```

[Link to the submission form](https://docs.google.com/forms/d/e/1FAIpQLSdO4trwNU4zPusr33LfYRhH2jvijj7sY42svbumH6f_15rCAQ/viewform?usp=preview)
