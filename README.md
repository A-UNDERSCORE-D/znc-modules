# Snoonet ZNC Modules

- [Setup](#setup)
- [CheckConfig](#checkconfig)
- [ForceChan](#forcechan)
- [Push](#push)
- [UserIPs](#userips)

---

### Setup

#### About

Modules are global ZNC modules written Python (requires [modpython](http://wiki.znc.in/Modpython)) that checks that a module is loaded for all users.

#### Installing

Place `module.py` in `~/.znc/modules`. `userips.py` also requires the `userips` folder in the same location.

#### Loading

All modules are written in Python (requires [modpython](http://wiki.znc.in/Modpython)). Modules can be loaded with `/znc loadmod <module>`

#### Accessing

All commands should be sent to `*checkconfig` as a private message

---

## CheckConfig

Checks that various options are configured for all users.

### Usage

`checknetwork <network>` will output all users who do not have the specified network configured

`checkchan <network> <channel>` will output all users who do not have the specified channel in the given network

`checkusermod <module>` will output `*controlpanel LoadModule` command for all users who do not have the module enabled

`checknetmod <module> <network>` will output `*controlpanel LoadNetModule` for all users who do not have the module enabled on the specified network

---

## ForceChan

Prevents a user from parting a channel.

### Usage

`/msg *forcechan forcechan` will force users into the preconfigured channel

---

## Push

Sends push notifications to users on mention or PM via PushBullet

### Usage

See [Snoonet BNC Push Notifications](https://snoonet.org/push) for instructions and setup

---

## UserIPs

Provides a web-interface for viewing IP addresses of connected users

### Usage

The module can be accessed from the ZNC webadmin by going to `User IPs` under `Global Modules`
