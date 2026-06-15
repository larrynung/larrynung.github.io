---
title: "[C#]簡易的Backoff window實現類別"
slug: "[CSharp]簡易的Backoff window實現類別"
date: "2013-11-06 12:00:00"
description: "[C#]簡易的Backoff window實現類別"
tags: [CSharp]
---
在無線網路的領域中，若是節點間要進行傳輸，會試圖嚐試發送RTS訊號，當接收端收到且允許傳送時，接收端會發送CTS訊號，傳送端就會知道可以進行傳送的動作。但若是傳送端發送了RTS後過段時間沒收到CTS訊號，代表訊號被碰撞掉了，這時會挑選個backoff值，決定要多久後再重試傳輸。這邊的backoff值會隨著碰撞而變大backoff值的區間，也就是無線網路領域所謂的Backoff window機制。

這樣的機制很簡單，但卻能分散碰撞，並將重試的時間調在適當的區間。這樣的機制一樣可以拿來套用在我們一般程式的開發，就像有時後訂Delay time時不知道該設多少，訂多訂少都會有不好的影響，那倒不如導入這樣的一個機制讓它自我調適。

這邊筆者憑著印象刻了一個簡單的BackOff類別。

程式碼如下：

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Collections.ObjectModel;

namespace ConsoleApplication12
{
public class BackOff
{
#region Var
private int _level;
private Random _random;
#endregion

#region Private Property
private ReadOnlyCollection m_BackOffWindows { get; set; }

private Random m_Random
{
get
{
if (_random == null)
_random = new Random(Guid.NewGuid().GetHashCode());
return _random;
}
}
#endregion

#region Public Property
///
/// Gets or sets the level.
///
/// The level.
public int Level
{
get
{
return _level;
}
set
{
if (value m_BackOffWindows.Count)
throw new Exception("Level value incorrect!");

_level = value;
}
}
#endregion

#region Constructor
///
/// Initializes a new instance of the class.
///
/// The back off windows.
public BackOff(params int[] backOffWindows)
{
CheckBackOffWindows(backOffWindows);

this.m_BackOffWindows = new ReadOnlyCollection(backOffWindows.ToList());
ResetLevel();
}
#endregion

#region Private Method
///
/// Checks the back off windows.
///
/// The back off windows.
private void CheckBackOffWindows(params int[] backOffWindows)
{
if (backOffWindows == null)
throw new ArgumentNullException("backOffWindows");

if (backOffWindows.Length == 0)
throw new ArgumentException("backOffWindows must contains elements!");

if (backOffWindows.First() backOffWindow)
throw new ArgumentOutOfRangeException("backOffWindows must order by increase!");

if (minValue == backOffWindow)
throw new ArgumentOutOfRangeException("Can't contains duplicated elements!");

minValue = backOffWindow;
}
}
#endregion

#region Public Method
///
/// Increases the level.
///
///
public Boolean IncreaseLevel()
{
if (Level >= m_BackOffWindows.Count)
return false;

Level += 1;
return true;
}

///
/// Decreases the level.
///
///
public Boolean DecreaseLevel()
{
if (Level
/// Gets the next value.
///
///
public int NextValue()
{
var minValue = (Level == 1) ? 0 : m_BackOffWindows[Level - 2];
var maxValue = m_BackOffWindows[Level - 1];

return m_Random.Next(minValue, maxValue);
}
#endregion
}
}

實際使用時只要建立物件實體，並帶入backoff window的區間值，透過NextValue取得backoff值就可以了，若是碰撞則呼叫IncreaseLevel去將區間上調。

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication12
{
class Program
{
static void Main(string[] args)
{
BackOff backoff = new BackOff(16,32,64);

Console.WriteLine("Level1...");
Console.WriteLine(backoff.NextValue().ToString());
Console.WriteLine(backoff.NextValue().ToString());
Console.WriteLine(backoff.NextValue().ToString());
Console.WriteLine(new string('=', 50));

backoff.IncreaseLevel();
Console.WriteLine("Level2...");
Console.WriteLine(backoff.NextValue().ToString());
Console.WriteLine(backoff.NextValue().ToString());
Console.WriteLine(backoff.NextValue().ToString());
Console.WriteLine(new string('=', 50));

backoff.IncreaseLevel();
Console.WriteLine("Level3...");
Console.WriteLine(backoff.NextValue().ToString());
Console.WriteLine(backoff.NextValue().ToString());
Console.WriteLine(backoff.NextValue().ToString());
Console.WriteLine(new string('=', 50));
}
}
}