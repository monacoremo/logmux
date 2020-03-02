# logmux
Logmux tails multiple log files, labels their lines and outputs everything in one stream - 
Much like docker-compose, but for simple local log files!

# Installation

```bash
pip install logmux

```

# Usage

```bash
logmux first.log second.log test/third.log

```

This will tail all three log files. New linex will be prefixed with the name
of the it came from, e.g. `first: ` for the firdt log file and `third: ` for the 
last one.

You can customize the label by providing it as a query parameter:

```bash
logmux "first.log?label=custom" second.log test/third.log

```

This will prefix all lines from the first file with `custom: `. You'll need to quote the argument
like in this example to make sure that your shell is not going to split it.

It's also possible to set the color of the label:

```bash
logmux "first.log?label=custom&color=blue" "second.log?color=red" test/third.log

```
