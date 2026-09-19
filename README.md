# ClHostMap: A tool to check if your website has been impersonated. (Version 1.1.4)

**Source code at: [EndpointScanner Repository](https://github.com/SphericalFlower52811/clhostmap)**

The dev branch hosts new features that may not be the full update, main branch will only contain stable updates to install.

## What is ClHostMap?

ClHostMap (standing for Cloud Host Map) is a tool that checks many cloud providers, and many TLDs for whether your website has been registered by other people.

## Why use ClHostMap?

People often impersonate brands or companies by hosting it on a different TLD like `.net` instead of `.com`, or hosting a website with the same brand name but using a cloud hosting platform so that it is free, like using `.vercel.app` or `.pages.dev` because `.com` is registered.

Additionally, if your original company is hosted on a cloud provider for free instead of `.com`, other people can register a domain on `.com` and impersonate you.

ClHostMap allows you to input your brand name, and the tool automatically checks many TLDs and host providers. Check the features for more details.

## Features

Features of ClHostMap include:

- Using a hash to check every TLD and host provider, as some host providers return a 200 OK response code but on the frontend say it is fake. This ensures no false positives will be captured.
- 68 cloud host providers (like `.vercel.app`) and every TLD from IANA. (literally every TLD to ever exist)
- Asynchronous function so that it runs hundreds of checks all at once.

### All Arguments

| Flag / Argument       | Short                   | Default | Description                                                                                                                          |
| :-------------------- | :---------------------- | :------ | :----------------------------------------------------------------------------------------------------------------------------------- |
| `site`                | _None_                  | _None_  | URL or brand name to verify.                                                                                                         |
| `--show-unregistered` | `-su`                   | `False` | Display unregistered domains as well.                                                                                                |
| `--show_status`       | `-ss`                   | `False` | Provide status codes/errors for every domain checked (forces -su).                                                                   |
| `--self-registered`   | <code>&#8209;sr</code>  | _None_  | Domains that you yourself have registered, so that those domains will be ignored. Use comma-separated values or path to a text file. |
| `--only-results`      | <code>&#8209;or</code>  | `False` | Only print the result                                                                                                                |
| `--concurrent-req`    | <code>&#8209;ccr</code> | `100`   | Maximum number of async requests, default 100.                                                                                       |

## Installation and Usage

### Installation

To install on MacOS/Linux:

```bash
python3 -m pip install clhostmap
```

To install on Windows:

```
py -m pip install clhostmap
```

### Usage

Run default scan:

```
clhostmap example.com
```

Run scan with 240 concurrent requests and to see status codes:

```
clhostmap example.com -ss -ccr 240
```

## Release notes

Version 1.1.0 added

- More cloud host providers and changing hardcoded TLDs to a txt from IANA
- Added clearer messages

## Upcoming additions

New features include:

- Adding a flag to check for typosquatted versions of your website on every TLD and cloud provider, using multiple typosquatting algorithms.
