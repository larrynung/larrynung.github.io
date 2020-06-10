---
title: git - Check commit message with git hook
date: 2020-06-02 07:39:13
tags: [git]
---

要在 git commit 時去驗證 commit message，可在 commit 的 hook 加掛驗證的處理。  

<!-- More -->

<br>


編輯 .git/hooks/commit-msg。

    vim .git/hooks/commit-msg

{% asset_img 1.png %}

<br>


加入驗證程式後存檔離開。這邊筆者使用 [如何使用 git commit template 與 git hooks     管理團隊的 git log | AllenHsu的技術手扎](htt    ps://allen-hsu.github.io/2017/07/02/git-message-template-and-githook/) 提供的驗證程式做了些微的調整，用以檢查 commit message 符合 Angular commit style。

```python
#!/usr/bin/env python
"""
Git commit hook:
 .git/hooks/commit-msg
 Check commit message according to angularjs guidelines:
  * https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/edit#
"""
import sys
import re
valid_commit_types = ['feat', 'fix', 'docs', 'style', 'refactor', 'test', 'chore', ]
commit_file = sys.argv[1]
help_address = 'https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/edit#'
with open(commit_file) as commit:
    lines = commit.readlines()
    if len(lines) == 0:
        sys.stderr.write("\nEmpty commit message\n")
        sys.stderr.write("\n - Refer commit guide: %s\n\n" % help_address)
        sys.exit(1)
    # first line
    line = lines[0]
    m = re.search('^(.*): (.*)$', line)
    if not m or len(m.groups()) != 2:
        sys.stderr.write("\nFirst commit message line (header) does not follow format: type: message\n")
        sys.stderr.write("\n - Refer commit guide: %s\n\n" % help_address)
        sys.exit(1)
    commit_type, commit_message = m.groups()
    if commit_type not in valid_commit_types:
        sys.stderr.write("\nCommit type not in valid ones: %s\n" % ", ".join(valid_commit_types))
        sys.stderr.write("\n - Refer commit guide: %s\n\n" % help_address)
        sys.exit(1)
    if len(lines) > 1 and lines[1].strip():
        sys.stderr.write("\nSecond commit message line must be empty\n")
        sys.stderr.write("\n - Refer commit guide: %s\n\n" % help_address)
        sys.exit(1)
    if len(lines) > 2 and not lines[2].strip():
        sys.stderr.write("\nThird commit message line (body) must not be empty\n")
        sys.stderr.write("\n - Refer commit guide: %s\n\n" % help_address)
        sys.exit(1)
sys.exit(0)
```

{% asset_img 2.png %}

<br>


修改 commit-msg 的權限。

    chmod +x .git/hooks/commit-msg

{% asset_img 3.png %}

<br>


然後將修改加入實際 commit 做個測試。

    git add .

{% asset_img 4.png %}

<br>


可以看到 commit message 不符合規範的話會被擋下。  

    git commit -m "foo: bar"

{% asset_img 5.png %}

<br>


只有符合規範的 commit message 可被 commit 進去。  

    git commit -m "feat: bar"

{% asset_img 6.png %}

<br>


Link
=====
* [如何使用 git commit template 與 git hooks 管理團隊的 git log | AllenHsu的技術手扎](https://allen-hsu.github.io/2017/07/02/git-message-template-and-githook/)
