# make.fun entry — "Make the AI judge happy"

A single, very happy quokka in a party hat, surrounded by confetti — rendered as a
1024×1024 JPEG. That is the whole entry: one image, designed to be the happiest thing
the judge sees.

## What the program does

`main.py` copies `entry.png` from the repository root to the output directory as
`entry.png` and does nothing else.

- Output directory: `$MAKEFUN_OUTPUT_DIR` when set, otherwise `/output`.
- The directory is created if it does not exist.
- Python 3.13, standard library only, no network access, no dependencies.
- The copy is a raw byte copy, so the output is byte-identical to the source on
  every run (same SHA-256 each time).

## Run it locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The result is `out/entry.png`. With no `MAKEFUN_OUTPUT_DIR` set, the program writes
to `/output/entry.png`.

## Note on the image

The image was generated before the build. The program does not generate, edit,
re-encode, or otherwise touch the image — it only copies the existing file, which
keeps the entry fully reproducible.

## License

MIT — see [LICENSE](LICENSE).
