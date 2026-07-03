Scripts for sending soccer news via email from the Linux terminal.

## Prerequisites

- bash
- python3
- msmtp
- gmail account that works with msmtp

## Setup

### Setting up `msmtp`:

**Install the software:**

Ubuntu/Debian:

```bash
sudo apt update && sudo apt install mailutils
```

Fedora/RHEL:

```bash
sudo dnf install msmtp
```

Arch:

```bash
pacman -S msmtp
```

**Configuration:**

Create `~/.msmtprc` if it doesn't exist:

```bash
defaults
auth           on
tls            on
tls_trust_file /etc/ssl/certs/ca-certificates.crt
logfile        ~/.msmtp.log

account        gmail
host           smtp.gmail.com
port           587
from           your_gmail_address@gmail.com
user           your_gmail_address@gmail.com
password       your_app_password_here
tls_starttls   on

account default : gmail
```

> [!NOTE]
> If port `587` does not work it is possible to use port `465` instead, though I haven't tested it:
>
>   ```bash
>   defaults
>   auth           on
>   tls            on
>   tls_trust_file /etc/ssl/certs/ca-certificates.crt
>   logfile        ~/.msmtp.log
>
>   account        gmail465
>   host           smtp.gmail.com
>   port           465
>   from           your_gmail_address@gmail.com
>   user           your_gmail_address@gmail.com
>   password       your_app_password_here
>   tls            on
>   tls_starttls   off
>
>   account default : gmail465
>   ```

### Connecting a GMail account:

- Create or use an existing gmail account
- Ensure 2 factor authentication is enabled
- Search for 'App Password' in your Google Account settings
- Copy the password to the `password` field in your `.msmtprc`

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

You can setup a [cron job](https://wiki.archlinux.org/title/Cron) or 
[systemd timer](https://wiki.archlinux.org/title/Systemd/Timers) 
to schedule automated emails.

## Resources

This [tutorial](https://www.digitalocean.com/community/tutorials/send-email-linux-command-line#6-send-email-with-smtp-authentication-msmtp).

This [google post](https://support.google.com/mail/thread/205453566?hl=en&msgid=205453795).

