---
title: "使用Extension Method計算漢字筆畫"
date: "2010-11-10 09:00:10"
description: "使用Extension Method計算漢字筆畫"
tags: [CSharp,VB.NET]
---

<p>看到網友Jeff的計算漢字的筆劃這篇有趣的文章，整理了一下裡面所提到的實作概念，其原理主要是把漢字轉為hex，再去判斷屬於哪個區間，並由所屬區間取得對應的筆劃就可以了。這邊將其整理為Char類型的擴充方法，方便後續直接使用。</p>  <p> </p>  <p>C#</p>  <div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:f16cb0a0-454f-4922-a813-62dd4695c24a" style="padding-right: 0px; display: inline; padding-left: 0px; float: none; padding-bottom: 0px; margin: 0px; padding-top: 0px"><pre name="code" class="c#">    static class CharExtension
    {
        private static string[][] _strokesNumberData = { 
                                              new string[] { "A440", "A441" } ,                                   //1 
                                              new string[] { "A442", "A453","C940", "C944"} ,                     //2 
                                              new string[] { "A454", "A47E","C945", "C94C"} ,                     //3 
                                              new string[] { "A4A1", "A4FD","C94D", "C95C"} ,                     //4 
                                              new string[] { "A4FE", "A5DF","C95D", "C9AA"} ,                     //5 
                                              new string[] { "A5E0", "A6E9","C9AB", "C959"} ,                     //6 
                                              new string[] { "A6EA", "A8C2","CA5A", "CBB0"} ,                     //7 
                                              new string[] { "A8C3", "AB44","CBB1", "CDDC"} ,                     //8 
                                              new string[] { "AB45", "ADBB","CDDD", "D0C7","F9DA","F9DA"} ,       //9 
                                              new string[] { "ADBC", "B0AD","D0C8", "D44A"} ,                     //10
                                              new string[] { "B0AE", "B3C2","D44B", "D850"} ,                     //11
                                              new string[] { "B3C3", "B6C3","D851", "DCB0","F9DB","F9DB"} ,       //12
                                              new string[] { "B6C4", "B9AB","DCB1", "E0EF","F9D6","F9D8"} ,       //13
                                              new string[] { "B9AC", "BBF4","E0F0", "E4E5"} ,                     //14
                                              new string[] { "BBF5", "BEA6","E4E6", "E8F3","F9DC","F9DC"} ,       //15
                                              new string[] { "BEA7", "C074","E8F4", "ECB8","F9D9","F9D9"} ,       //16
                                              new string[] { "C075", "C24E","ECB9", "EFB6"} ,                     //17
                                              new string[] { "C24F", "C35E","EFB7", "F1EA"} ,                     //18
                                              new string[] { "C35F", "C454","F1EB", "F3FC"} ,                     //19
                                              new string[] { "C455", "C4D6","F3FD", "F5BF"} ,                     //20
                                              new string[] { "C3D7", "C56A","F5C0", "F6D5"} ,                     //21
                                              new string[] { "C56B", "C5C7","F6D6", "F7CF"} ,                     //22
                                              new string[] { "C5C8", "C5C7","F6D6", "F7CF"} ,                     //23
                                              new string[] { "C5F1", "C654","F8A5", "F8ED"} ,                     //24
                                              new string[] { "C655", "C664","F8E9", "F96A"} ,                     //25
                                              new string[] { "C665", "C66B","F96B", "F9A1"} ,                     //26
                                              new string[] { "C66C", "C675","F9A2", "F9B9"} ,                     //27
                                              new string[] { "C676", "C67A","F9BA", "F9C5"} ,                     //28
                                              new string[] { "C67B", "C67E","F9C6", "F9DC"} ,                     //29
                                          };

        public static int GetStrokesNumber(this char c)
        {
            String hex = BitConverter.ToString(Encoding.GetEncoding("Big5").GetBytes(new char[] { c })).Replace("-", string.Empty);
            for (int i = 0; i &lt; _strokesNumberData.Length; ++i)
            {
                for (int j = 0; j &lt; _strokesNumberData[i].Length; j += 2)
                {
                    if (hex.CompareTo(_strokesNumberData[i][j]) &gt;= 0 &amp;&amp; hex.CompareTo(_strokesNumberData[i][j + 1]) &lt;= 0)
                        return i+1;
                }
            }
            return 0;
        }
    }</pre></div>

<p> </p>

<p>VB.NET</p>

<div class="wlWriterSmartContent" id="scid:812469c5-0cb0-4c63-8c15-c81123a09de7:18559b93-64a5-48d1-a9d8-28cb7d591f0c" style="padding-right: 0px; display: inline; padding-left: 0px; float: none; padding-bottom: 0px; margin: 0px; padding-top: 0px"><pre name="code" class="vb">Imports System.Runtime.CompilerServices
Imports System.Text

Module CharExtension

    Private _strokesNumberData As String()() = { _
    New String() {"A440", "A441"}, _
    New String() {"A442", "A453", "C940", "C944"}, _
    New String() {"A454", "A47E", "C945", "C94C"}, _
    New String() {"A4A1", "A4FD", "C94D", "C95C"}, _
    New String() {"A4FE", "A5DF", "C95D", "C9AA"}, _
    New String() {"A5E0", "A6E9", "C9AB", "C959"}, _
    New String() {"A6EA", "A8C2", "CA5A", "CBB0"}, _
    New String() {"A8C3", "AB44", "CBB1", "CDDC"}, _
    New String() {"AB45", "ADBB", "CDDD", "D0C7", "F9DA", "F9DA"}, _
    New String() {"ADBC", "B0AD", "D0C8", "D44A"}, _
    New String() {"B0AE", "B3C2", "D44B", "D850"}, _
    New String() {"B3C3", "B6C3", "D851", "DCB0", "F9DB", "F9DB"}, _
    New String() {"B6C4", "B9AB", "DCB1", "E0EF", "F9D6", "F9D8"}, _
    New String() {"B9AC", "BBF4", "E0F0", "E4E5"}, _
    New String() {"BBF5", "BEA6", "E4E6", "E8F3", "F9DC", "F9DC"}, _
    New String() {"BEA7", "C074", "E8F4", "ECB8", "F9D9", "F9D9"}, _
    New String() {"C075", "C24E", "ECB9", "EFB6"}, _
    New String() {"C24F", "C35E", "EFB7", "F1EA"}, _
    New String() {"C35F", "C454", "F1EB", "F3FC"}, _
    New String() {"C455", "C4D6", "F3FD", "F5BF"}, _
    New String() {"C3D7", "C56A", "F5C0", "F6D5"}, _
    New String() {"C56B", "C5C7", "F6D6", "F7CF"}, _
    New String() {"C5C8", "C5C7", "F6D6", "F7CF"}, _
    New String() {"C5F1", "C654", "F8A5", "F8ED"}, _
    New String() {"C655", "C664", "F8E9", "F96A"}, _
    New String() {"C665", "C66B", "F96B", "F9A1"}, _
    New String() {"C66C", "C675", "F9A2", "F9B9"}, _
    New String() {"C676", "C67A", "F9BA", "F9C5"}, _
    New String() {"C67B", "C67E", "F9C6", "F9DC"}}

    &lt;Extension()&gt; _
    Public Function GetStrokesNumber(ByVal c As Char) As Integer
        Dim hex As [String] = BitConverter.ToString(Encoding.GetEncoding("Big5").GetBytes(New Char() {c})).Replace("-", String.Empty)
        For i As Integer = 0 To _strokesNumberData.Length - 1
            For j As Integer = 0 To _strokesNumberData(i).Length - 1 Step 2
                If hex.CompareTo(_strokesNumberData(i)(j)) &gt;= 0 AndAlso hex.CompareTo(_strokesNumberData(i)(j + 1)) &lt;= 0 Then
                    Return i + 1
                End If
            Next
        Next
        Return 0
    End Function
End Module</pre></div>

<p> </p>

<h2>Link</h2>

<ul>
  <li>
    <h6>計算漢字的筆劃</h6>
  </li>

  <li>
    <h6>倚天中文字型筆劃順序內碼對照表</h6>
  </li>
</ul>
