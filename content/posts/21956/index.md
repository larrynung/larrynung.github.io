---
title: "[C#]IEnumerable型態回傳注意事項"
slug: "[CSharp]IEnumerable型態回傳注意事項"
date: "2011-03-19 08:44:03"
description: "[C#]IEnumerable型態回傳注意事項"
tags: [CSharp]
---自Linq出來以後，個人的程式撰寫習慣又因此有了些許的改變，變得習慣會盡量用IEnumerable型態去傳遞集合的資料，因為透過這樣的型態可以將集合真正的型態隱含在背後，若某天有需求要替換集合類型，動到的部份會比較少，也可以實現像Linq一樣具延遲載入的效果。

在前陣子開發時才發現，這樣的做法會隱藏著一些必需注意到的細節。像是使用Linq查詢： using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;

namespace ConsoleApplication20
{
    class Program
    {
        static void Main(string[] args)
        {
            IEnumerable allDatas = GetDatas(@"c:\");

            foreach (FileInfo item in allDatas)
            {
                item.;
            }

            foreach (FileInfo item in allDatas)
            {
                Console.WriteLine(item.Name);
            }
        }
        public static IEnumerable GetDatas(String path)
        {
            var linq = from file in Directory.GetFiles(path)
                       select new FileInfo() { };
            return linq;
        }

    }

    class FileInfo
    {
        private string _name;
        public string Name
        {
            get { return _name; }
            set
            {
                if (_name != value)
                {
                    _
                }
            }
        }
    }
}

或是透過yield實現IEnumerable型態的回傳時

...

public static IEnumerable GetDatas(String path)
{
    foreach (var file in Directory.GetFiles(path))
    {
        yield return new FileInfo() { };
    }
}
...

我們都可以注意到ㄧ開始從GetDatas取得的物件實體跟後續透過臨時變數取得的都不同...

必須要在取得IEnumerable型態的資料時透過ToArray、或是ToList之類的方法先行處理過，或是盡量避免使用Linq與yield去獲取IEnumerable型態的資料後直接回傳：

...

IEnumerable allDatas = GetDatas(@"c:\").ToArray();

...

目前這問題尚無確切的定論，個人暫時姑且推測應該是因為yield的特性所導致的效果。