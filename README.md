# tarantula

![Python Version](https://img.shields.io/badge/python-3.x-blue?style=flat&logo=python)
![OS](https://img.shields.io/badge/OS-GNU%2FLinux-red?style=flat&logo=linux)
![GitHub](https://img.shields.io/github/license/rlyonheart/tarantula?style=flat)
![GitHub repo size](https://img.shields.io/github/repo-size/rlyonheart/tarantula)
![CodeFactor](https://www.codefactor.io/repository/github/rlyonheart/tarantula/badge)
![Twitter](https://img.shields.io/twitter/follow/rly0nheart?&style=flat&logo=twitter)

Python web crawler tool.
scrapes internal and external urls

# Installation
**Clone this repo:**
> git clone https://github.com/rlyonheart/tarantula

> cd tarantula

> pip3 install -r requirements.txt

# Usage
> python3 tarantula [target url] -C [number of links to crawl]
  
**example;**
> python3 tarantula https://github.com -C 1

**sample output:**

[12:59:14PM] Starting new HTTPS connection (1): github.com:443                                 
[12:59:35PM] https://github.com:443 "GET / HTTP/1.1" 200 None
[12:59:39PM] INTERNAL LINK: https://github.com
[12:59:39PM] INTERNAL LINK: https://docs.github.com/articles/supported-browsers
[12:59:39PM] INTERNAL LINK: https://github.com/
[12:59:39PM] INTERNAL LINK: https://github.com/signup
[12:59:39PM] INTERNAL LINK: https://github.com/features
[12:59:39PM] INTERNAL LINK: https://github.com/mobile
[12:59:39PM] INTERNAL LINK: https://github.com/features/actions
[12:59:39PM] INTERNAL LINK: https://github.com/features/codespaces
[12:59:39PM] INTERNAL LINK: https://github.com/features/packages
[12:59:39PM] INTERNAL LINK: https://github.com/features/security
[12:59:39PM] INTERNAL LINK: https://github.com/features/code-review/
[12:59:39PM] INTERNAL LINK: https://github.com/features/issues/
[12:59:39PM] INTERNAL LINK: https://github.com/features/integration/
[12:59:39PM] INTERNAL LINK: https://github.com/sponsors
[12:59:39PM] INTERNAL LINK: https://github.com/customer-stories
[12:59:39PM] INTERNAL LINK: https://github.com/team
[12:59:39PM] INTERNAL LINK: https://github.com/enterprise
[12:59:39PM] INTERNAL LINK: https://github.com/explore
[12:59:39PM] INTERNAL LINK: https://github.com/topics
[12:59:39PM] INTERNAL LINK: https://github.com/collections
[12:59:39PM] INTERNAL LINK: https://github.com/trending
[12:59:39PM] INTERNAL LINK: https://lab.github.com/
[12:59:39PM] EXTERNAL LINK: https://opensource.guide
[12:59:39PM] INTERNAL LINK: https://github.com/readme
[12:59:39PM] INTERNAL LINK: https://github.com/events
[12:59:39PM] INTERNAL LINK: https://github.community
[12:59:39PM] INTERNAL LINK: https://education.github.com
[12:59:39PM] INTERNAL LINK: https://stars.github.com
[12:59:39PM] INTERNAL LINK: https://github.com/marketplace
[12:59:39PM] INTERNAL LINK: https://github.com/pricing
[12:59:39PM] INTERNAL LINK: https://enterprise.github.com/contact
[12:59:39PM] INTERNAL LINK: https://github.com/login
[12:59:39PM] INTERNAL LINK: https://github.com/account/organizations/new
[12:59:39PM] EXTERNAL LINK: https://www.npmjs.com
[12:59:39PM] EXTERNAL LINK: https://apps.apple.com/app/github/id1477376905
[12:59:39PM] EXTERNAL LINK: https://play.google.com/store/apps/details
[12:59:39PM] INTERNAL LINK: https://desktop.github.com/
[12:59:39PM] INTERNAL LINK: https://cli.github.com/
[12:59:39PM] INTERNAL LINK: https://github.com/marketplace/actions
[12:59:39PM] INTERNAL LINK: https://docs.github.com/github/managing-security-vulnerabilities/configuring-dependabot-security-updates
[12:59:39PM] INTERNAL LINK: https://docs.github.com/discussions
[12:59:39PM] INTERNAL LINK: https://github.com/tensorflow/tensorflow
[12:59:39PM] INTERNAL LINK: https://github.com/gatsbyjs/gatsby
[12:59:39PM] INTERNAL LINK: https://github.com/home-assistant/core
[12:59:39PM] INTERNAL LINK: https://github.com/rust-lang/rust
[12:59:39PM] INTERNAL LINK: https://github.com/flutter/flutter
[12:59:39PM] INTERNAL LINK: https://github.com/kubernetes/kubernetes
[12:59:39PM] INTERNAL LINK: https://github.com/apple/swift
[12:59:39PM] INTERNAL LINK: https://github.com/ansible/ansible
[12:59:39PM] INTERNAL LINK: https://github.com/hashicorp/terraform
[12:59:39PM] INTERNAL LINK: https://github.com/ohmyzsh/ohmyzsh
[12:59:39PM] INTERNAL LINK: https://github.com/facebook/react
[12:59:39PM] INTERNAL LINK: https://github.com/npm/cli
[12:59:39PM] INTERNAL LINK: https://github.com/security
[12:59:39PM] INTERNAL LINK: https://resources.github.com
[12:59:39PM] INTERNAL LINK: https://github.com/github/roadmap
[12:59:39PM] INTERNAL LINK: https://docs.github.com
[12:59:39PM] INTERNAL LINK: https://partner.github.com/
[12:59:39PM] EXTERNAL LINK: https://atom.io
[12:59:39PM] EXTERNAL LINK: https://www.electronjs.org
[12:59:39PM] INTERNAL LINK: https://services.github.com/
[12:59:39PM] EXTERNAL LINK: https://www.githubstatus.com/
[12:59:39PM] INTERNAL LINK: https://support.github.com
[12:59:39PM] INTERNAL LINK: https://github.com/about
[12:59:39PM] EXTERNAL LINK: https://github.blog
[12:59:39PM] INTERNAL LINK: https://github.com/about/careers
[12:59:39PM] INTERNAL LINK: https://github.com/about/press
[12:59:39PM] INTERNAL LINK: https://github.com/about/diversity
[12:59:39PM] INTERNAL LINK: https://socialimpact.github.com/
[12:59:39PM] INTERNAL LINK: https://shop.github.com
[12:59:39PM] EXTERNAL LINK: https://twitter.com/github
[12:59:39PM] EXTERNAL LINK: https://www.facebook.com/GitHub
[12:59:39PM] EXTERNAL LINK: https://www.youtube.com/github
[12:59:39PM] EXTERNAL LINK: https://www.linkedin.com/company/github
[12:59:39PM] INTERNAL LINK: https://github.com/github
[12:59:39PM] INTERNAL LINK: https://docs.github.com/en/github/site-policy/github-terms-of-service
[12:59:39PM] INTERNAL LINK: https://docs.github.com/en/github/site-policy/github-privacy-statement
[12:59:39PM] INTERNAL LINK: https://github.com/site-map
[12:59:39PM] INTERNAL LINK: https://github.com/git-guides
[12:59:39PM] https://github.com Crawled.
 
Tarantula stopped in 8.58306884765625e-06 seconds.

# Developer 
**Richard Mwewa**

**Alias:** rly0nheart
  
