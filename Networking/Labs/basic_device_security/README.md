# Cisco Router – Basic Password Security

## Project Overview

A basic Cisco Packet Tracer security lab focused on securing router privileged EXEC access using password protection and understanding the differences between Cisco password types.

The lab explores Type 7 password obfuscation, Type 5 MD5-based password hashing, and configuration persistence.

## 1. Password Configuration

### Enable Password

```cisco
enable password weak_encryption
```

Configures a password for accessing privileged EXEC mode.

However, this command stores the password in plaintext by default.

### Service Password Encryption

```cisco
service password-encryption
```

Enables Cisco Type 7 password obfuscation for plaintext passwords stored in the router configuration.

**Security note:**

- Uses Cisco Type 7 obfuscation.
- Very weak security.
- Easily reversible using publicly available tools.
- Should not be considered secure password encryption.

### Enable Secret

```cisco
enable secret strong-encryption
```

Configures a protected password for privileged EXEC mode using Cisco Type 5 hashing by default on this platform.

**Security note:**

- Uses a salted MD5-based hash (Type 5).
- More secure than Type 7 obfuscation.
- Not reversible in the same way as Type 7, but vulnerable to offline password cracking.
- Modern configurations should use stronger supported password-hashing algorithms.

**Important:** If both `enable password` and `enable secret` are configured, `enable secret` takes precedence for privileged EXEC authentication.

## 2. Running Configuration

After applying the commands, the relevant entries in the running configuration were:

```cisco
enable secret 5 $1$mERr$PsukJEDpSGF7zDdQY4zTr.

enable password 7 0836494F02260019111915143E222B26
```

### Understanding the Output

| Configuration | Type | Protection |
|---|---|---|
| `enable password` | Type 7 | Reversible obfuscation |
| `enable secret` | Type 5 | Salted MD5-based hash |

The numbers `7` and `5` identify the password protection formats used in the configuration.

## 3. Saving the Configuration

To preserve the configuration after a router restart, the running configuration was copied to startup configuration.

```cisco
copy running-config startup-config
```

**Explanation:**

- `running-config`: Current active router configuration stored in RAM.
- `startup-config`: Configuration saved in NVRAM and loaded when the router starts.

This ensures that the configured security settings persist after a reboot.

## 4. Commands Summary

| Command | Purpose |
|---|---|
| `enable password` | Configures a privileged EXEC password |
| `service password-encryption` | Obfuscates plaintext passwords using Type 7 |
| `enable secret` | Configures a protected privileged EXEC password |
| `show running-config` | Displays the active configuration |
| `copy running-config startup-config` | Saves the active configuration |

## 5. Security Concepts Learned

- Cisco privileged EXEC authentication
- Password protection
- Type 7 password obfuscation
- Type 5 salted MD5-based hashing
- Difference between password obfuscation and hashing
- Running configuration vs. startup configuration
- Configuration persistence

## Project Objective

Understand basic Cisco router password security, identify the weaknesses of legacy password protection methods, and learn how to securely manage and save router configurations.
