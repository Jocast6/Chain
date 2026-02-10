# Chain

**Chain** is a lightweight Python library for building **readable, composable data pipelines**—especially when your functions produce **multiple outputs**, operate on **structured data**, or represent **domain-specific workflows**.

It lets you write data logic as a **linear story**, not a tangle of loops, temporaries, and hidden side effects.

If your code often raises questions like:
- “Where did this DataFrame come from?”
- “Why does this function return three things?”
- “How do I name and persist intermediate results cleanly?”

Chain is built for exactly that.

---

## What makes Chain different?

Most functional libraries stop at `map` and `filter`.

Chain supports:
- 🔁 **Multi-output functions** (fan-out → fan-in)
- 🧩 **Tuple-aware composition** (outputs become inputs automatically)
- 🗂️ **Structured data flows** (lists, tuples, dicts, DataFrames)
- 💾 **Explicit side-effect stages** (saving CSVs, etc.)
- 🧠 **Domain-specific pipelines via inheritance**

This makes Chain especially useful for:
- analytics and reporting pipelines
- ETL-style batch jobs
- reproducible research
- internal data tooling

---

Design philosophy

Chain is built around a few core ideas:

Data flows forward

Shape matters (lists, tuples, dicts are explicit)

Side effects belong at the edges

Pipelines should read like intent

It is intentionally:

small

unopinionated

easy to extend

hard to misuse accidentally

## Quick example

```python
from chain import Chain

data = [1, 2, 3, 4, 5, 6]

result = (
    Chain()
    .filter(lambda x: x % 2 == 0)
    .map(lambda x: x * 10)
)(data)

# result -> [20, 40, 60]

# Chain automatically passes tuple outputs as arguments to the next stage. 
def duplicate_and_transform(xs, f):
    ys = list(map(f, xs))
    return xs, ys

def add_lists(x, y):
    return [a + b for a, b in zip(x, y)]

pipeline = (
    Chain()
    .filter(lambda x: x % 2 == 0)
    .pipe(duplicate_and_transform, lambda x: x * 2)
    .pipe(add_lists)
)

# Reusable pipelines
pipeline([86, 42, 12, 20, 6, 87, 1, 80, 7, 43])
# -> [258, 126, 36, 60, 18, 240]

# Domain-specific pipelines via inheritance ⭐
# One of Chain’s most powerful features is that you can subclass it to create a mini DSL for your domain.

class CrashChain(Chain):
    def pedestrian_only(self):
        return self.filter(lambda c: c["mode"] == "pedestrian")

    def severe(self):
        return self.filter(lambda c: c["severity"] in ("A", "K"))

    def downtown(self):
        return self.filter(lambda c: c["area"] == "Downtown")

results = (
    CrashChain()
    .pedestrian_only()
    .severe()
    .downtown()
    .pipe(summarize_crash_severity)
)(crash_data)

# This reads like policy, not plumbing—and that’s intentional.

