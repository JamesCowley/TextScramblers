# Make text unsearchable

### Quick implementation of [this idea](https://www.reddit.com/r/Lightbulb/comments/6vw75m)

Includes 2 scripts:

1. [l33tify.py](l33tify.py), which replaces 30% of the letters in a user-supplied string with non-letter characters. Example usage:

```bash
$> ./l33tify.py An app that scrambles your text like this to keep it from being searchable
Scrambled version:
@n @pp +hat $(®@mble$ you® +e><+ |_ike this to |<e€p it f®0m being $€archable
```

2. [scramble.py](scramble.py), which simply randomizes the order of letters within each word, leaving the first and last letters in place, thus rendering the words unsearchable but easily understandable, in accordance with [this meme](http://knowyourmeme.com/memes/aoccdrnig-to-rscheearch).

```bash
$> ./scramble.py According to research at Cambridge University it doesnt matter what order the letters in a word are
Scrambled version:
Aircncdog to rseeacrh at Cdarmgibe Urisitveny it dosnet mttear waht oerdr the lretets in a wrod are
```
