---
title: GitLab - Cherry-pick changes
date: 2018-11-29 00:13:38
tags: [GitLab]
---

要使用 GitLab 做 Cherry-pick，先要進入要 Cherry-pick 的 commit。  

<!-- More -->

{% asset_img 1.png %}

<br/>


展開右上方的 Options 下拉清單點選 Cherry-pick 選單選項。  

{% asset_img 2.png %}

<br/>


在 Cherry-pick this commit 對話框中選取要 merge 到的 branch，如果要發送 Merge request 可勾選下方的 Start a new merge request with these changes 勾選框，最後按下下方的 Cherry-pick 按鈕。  

{% asset_img 3.png %}

<br/>


如果沒有勾選 Start a new merge request with these changes 勾選框，則 Cherry-pick 會立即 merge。  

<br/>


如果有勾選，則會走回一般 Merge request 的流程。  

{% asset_img 4.png %}

<br/>


{% asset_img 5.png %}

<br/>


{% asset_img 6.png %}

<br/>


Link
----
* [Cherry-pick changes | GitLab](https://docs.gitlab.com/ee/user/project/merge_requests/cherry_pick_changes.html)
