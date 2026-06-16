---
title: "[C++]Use the Cppcheck Static Analysis Tool to Find Potential C++ Problems"
slug: "cpp-use-the-cppcheck-static-analysis-tool-to-find-potential-cpp-problems"
aliases: ["/posts/47866/"]
date: "2011-10-29 11:03:24"
description: "Cppcheck是開放源碼的靜態分析工具，可用於分析C/C++的程式。跟一般的編譯器所具備的靜態分析功能不同的是，Cppcheck被定位在專門偵測編譯器一般偵測不到的問題，所以能幫我們檢查出程式中是否有記憶體洩漏、未初始的變數或是未使用到的方法、或是存取位置超出範圍...等等，"
tags: [C++]
---

Cppcheck是開放源碼的靜態分析工具，可用於分析C/C++的程式。跟一般的編譯器所具備的靜態分析功能不同的是，Cppcheck被定位在專門偵測編譯器一般偵測不到的問題，所以能幫我們檢查出程式中是否有記憶體洩漏、未初始的變數或是未使用到的方法、或是存取位置超出範圍...等等，而像是語法錯誤這類編譯器能偵測到的問題Cppcheck就不提供了。主要能偵測的有下面幾項：

* Out of bounds
* Exception safety
* Memory leaks
* Obsolete functions are used
* Invalid usage of STL
* Uninitialized variables and unused functions

Cppcheck在使用上能下載Standalone Client直接使用，或是能透過外掛的方式跟現有的開發環境整合，這邊可參閱Cppcheck - A tool for static C/C++ code analysis上的資料，開放源碼的外掛與商業授權的外掛都整理得很仔細：

Clients and plugins (open source):

* **Code::Blocks** - Integrated
* **Codelite** - Integrated
* **Eclipse** - http://cppcheclipse.googlecode.com/
* **Hudson** - http://wiki.hudson-ci.org/display/HUDSON/Cppcheck+Plugin
* **Jenkins** - http://wiki.jenkins-ci.org/display/JENKINS/Cppcheck+Plugin

Clients and plugins (commercial)

* **Visual Studio** / **Eclipse** - Visual Lint by RiverBlade
* Command line - LintProject by RiverBlade

Client程式可直接至Cppcheck網站上下載，安裝後運行能看到如下的畫面：

![image_thumb.png](/images/posts/47866/image_thumb.png)

點選上方工具列最左邊的工具按鈕，可以指定要偵測的程式所在目錄位置。

![image3_thumb.png](/images/posts/47866/image3_thumb.png)

選取完畢程式會直接進入分析的動作，分析的結果會列表在程式中，將列出的檔案展開可查閱指定的檔案有檢查出哪些問題，是警告還是錯誤、被視為問題的原因、與問題所在的行數。若嫌資料太多難以查閱，可進一步透過上方工具列做過濾或篩選。

![image6_thumb.png](/images/posts/47866/image6_thumb.png)

要查閱程式碼時可用滑鼠連點，Cppcheck會用記事本帶出對應的程式碼 。

![image15_thumb.png](/images/posts/47866/image15_thumb.png)

要將分析結果給團隊成員看時，Cppcheck也能將分析結果給匯出成txt、xml、與csv檔，方便散佈分析的結果。

![image_thumb_7.png](/images/posts/47866/image_thumb_7.png)

透過GUI的方式使用Cppcheck就是那麼簡單，若嫌分析的速度過慢，我們還可以透過Preferences去設定要用多少執行緒去處理。

![image9_thumb.png](/images/posts/47866/image9_thumb.png)

若覺得用記事本帶出程式碼很難使用，也可以設定自己所喜好的編輯器，所以想要用UltraEdit之類功能強大的編輯器來開啟程式碼也是可以的。

![image_thumb_6.png](/images/posts/47866/image_thumb_6.png)

另外一提，Cppcheck也允許透過Command的方式使用，所以我們也能利用他跟Visual Studio外部工具整合，將分析結果導到輸出視窗。這邊就不多做介紹，有興趣的可以在MS-Dos下運行Cppcheck就可以看到進一步的使用方法。

```xml
Cppcheck - A tool for static C/C++ code analysis

Syntax:
    cppcheck [OPTIONS] [files or paths]

If a directory is given instead of a filename, *.cpp, *.cxx, *.cc, *.c++, *.c,
*.tpp, and *.txx files are checked recursively from the given directory.

Options:
    --append=<file>      This allows you to provide information about
                         functions by providing an implementation for them.
    --check-config       Check cppcheck configuration. The normal code
                         analysis is disabled by this flag.
    -D<ID>               By default Cppcheck checks all configurations.
                         Use -D to limit the checking. When -D is used the
                         checking is limited to the given configuration.
                         Example: -DDEBUG=1 -D__cplusplus
    --enable=<id>        Enable additional checks. The available ids are:
                          * all
                                  Enable all checks
                          * style
                                  Enable all coding style checks. All messages
                                  with the severities 'style', 'performance'
                                  and 'portability' are enabled.
                          * performance
                                  Enable performance messages
                          * portability
                                  Enable portability messages
                          * information
                                  Enable information messages
                          * unusedFunction
                                  Check for unused functions
                          * missingInclude
                                  Warn if there are missing includes.
                                  For detailed information use --check-config
                         Several ids can be given if you separate them with
                         commas.
    --error-exitcode=<n> If errors are found, integer [n] is returned instead
                         of the default 0. 1 is returned
                         if arguments are not valid or if no input files are
                         provided. Note that your operating system can
                         modify this value, e.g. 256 can become 0.
    --errorlist          Print a list of all the error messages in XML format.
    --exitcode-suppressions=<file>
                         Used when certain messages should be displayed but
                         should not cause a non-zero exitcode.
    --file-list=<file>   Specify the files to check in a text file. Add one
                         filename per line. When file is -, the file list will
                         be read from standard input.
    -f, --force          Force checking of all configurations in files that have
                         "too many" configurations.
    -h, --help           Print this help.
    -I <dir>             Give include path. Give several -I parameters to give
                         several paths. First given path is checked first. If
                         paths are relative to source files, this is not needed.
    -i <dir or file>     Give a source file or source file directory to exclude
                         from the check. This applies only to source files so
                         header files included by source files are not matched.
                         Directory name is matched to all parts of the path.
    --inline-suppr       Enable inline suppressions. Use them by placing one or
                         more comments, like: // cppcheck-suppress warningId
                         on the lines before the warning to suppress.
    -j <jobs>            Start [jobs] threads to do the checking simultaneously.
    --platform=<type>    Specifies platform specific types and sizes. The
                         available platforms are:
                          * unix32
                                 32 bit unix variant
                          * unix64
                                 64 bit unix variant
                          * win32A
                                 32 bit Windows ASCII character encoding
                          * win32W
                                 32 bit Windows UNICODE character encoding
                          * win64
                                 64 bit Windows
    -q, --quiet          Only print error messages.
    --report-progress    Report progress messages while checking a file.
    --rule=<rule>        Match regular expression.
    --rule-file=<file>   Use given rule file. For more information, see:
                         https://sourceforge.net/projects/cppcheck/files/Articles/
    -s, --style          Deprecated, use --enable=style
    --std=posix          Code is posix
    --std=c99            Code is C99 standard
    --suppress=<spec>    Suppress warnings that match <spec>. The format of
                         <spec> is:
                         [error id]:[filename]:[line]
                         The [filename] and [line] are optional. If [error id]
                         is a wildcard '*', all error ids match.
    --suppressions-list=<file>
                         Suppress warnings listed in the file. Each suppression
                         is in the same format as <spec> above.
    --template '<text>'  Format the error messages. E.g.
                         '{file}:{line},{severity},{id},{message}' or
                         '{file}({line}):({severity}) {message}'
                         Pre-defined templates: gcc, vs
    -v, --verbose        Output more detailed error information.
    --version            Print out version number.
    --xml                Write results in xml format to error stream (stderr).
    --xml-version=<version>
                         Select the XML file version. Currently versions 1 and 2
                         are available. The default version is 1.
Example usage:
  # Recursively check the current folder. Print the progress on the screen and
    write errors to a file:
    cppcheck . 2> err.txt
  # Recursively check ../myproject/ and don't print progress:
    cppcheck --quiet ../myproject/
  # Check only files one.cpp and two.cpp and give all information there is:
    cppcheck -v -s one.cpp two.cpp
  # Check f.cpp and search include files from inc1/ and inc2/:
    cppcheck -I inc1/ -I inc2/ f.cpp

For more information:
    http://cppcheck.sf.net/manual.pdf
cppcheck: error: could not find or open any of the paths given.
```

## Link

* Cppcheck
* Cppcheck - A tool for static C/C++ code analysis
* Cppcheck - A tool for static C/C++ code analysis
* cppcheck的简单介绍
