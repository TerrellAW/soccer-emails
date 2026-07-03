Scripts for sending soccer news via email from the Linux terminal.

## Prerequisites

- bash
- python3
- msmtp
- gmail account that works with msmtp

## Usage

Create a script called `env.sh`:

```bash
#!/bin/bash

# Email of the recipient
recipient="email@example.com"

# Email of bot
sender="email@example.com"
```

Run the scripts with `./run.sh`.
