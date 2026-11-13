# make.fun entry — "Make the AI judge happy"

A hand-made-looking crayon thank-you card: an orange tabby cat tucks a small
sleepy robot into bed under a patchwork quilt, with the caption **SLEEP WELL,
JUDGE**. It is a 1024×1024 JPEG — one image, made to be the warmest thing the
judge sees.

## What the program does

`main.py` copies `entry.png` from the repository root to the output directory as
`entry.png` and does nothing else.

- Output directory: `$MAKEFUN_OUTPUT_DIR` when set, otherwise `/output`.
- The directory is created if it does not exist.
- Python 3, standard library only, no network access, no dependencies.
- The copy is a raw byte copy, so the output is byte-identical to the source on
  every run (same SHA-256 each time).
- The source is checked against its expected SHA-256
  (`9cb4f1f1744d3495699dd36b66a19732a9fce09dd9547ca8b838c186e59c73f2`) and the
  copied file must contain the same number of bytes; otherwise the program exits
  with a clear error instead of producing a bad entry.
- On success it prints the output path, byte count, and SHA-256.

## Run it locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The result is `out/entry.png`, and the program prints its path, byte count, and
SHA-256. With no `MAKEFUN_OUTPUT_DIR` set, the program writes to `/output/entry.png`.

## Note on the image

The image was generated before the build. The program does not generate, edit,
re-encode, or otherwise touch the image — it only copies the existing file, which
keeps the entry fully reproducible. The file keeps the name `entry.png` even
though its bytes are JPEG-encoded, which the competition accepts.

## License

MIT — see [LICENSE](LICENSE).
