# logmux
Logmux tails multiple log files, labels their lines and outputs everything in
one stream - Much like docker-compose, but simply for local log files!

# Installation

```bash
pip install logmux

```

# Usage

```bash
logmux first.log second.log test/third.log

```

This will tail all three log files. New lines will be prefixed with the name of
the log file it came from, e.g. `first: ` for the first log file and `third: `
for the last one.

You can customize the labels by providing them as a query parameter for each
file:

```bash
logmux "first.log?label=custom" second.log test/third.log

```

This will prefix all lines from the first file with `custom: `. You'll need to
quote the argument like in this example to make sure that your shell is not
going to split it.

It's also possible to set the color of the label:

```bash
logmux "first.log?label=custom&color=blue" "second.log?color=red" test/third.log

```

# Similar solutions

In no particular order:

* [MultiTail](https://www.vanheusden.com/multitail/) uses ncurses to tail multiple
  log files in one or more windows. Logmux takes a more simple approach by just
  printing to stdout.
