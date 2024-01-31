#### Setup

1. Install the requirements
```bash
pip3 install -r requirements.txt
```

2. Build the index
```python
python3 build_index.py
```

#### Usage

Run `main.py --n-results 1` to access the embeddings index via a simple CLI interface.

```
> How do I get the first element in a list?
procedure(first lst) → any/c  lst : list?The same as (car lst), but only for lists (that are not empty).
Example:> (first '(1 2 3 4 5 6 7 8 9 10))1
------------------------------
> 
```
