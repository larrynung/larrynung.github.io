---
title: "[Extension Method]使用擴充方法來做二維陣列排序"
date: "2010-04-08 06:28:41"
description: "[Extension Method]使用擴充方法來做二維陣列排序"
tags: [VB.NET,CSharp]
---整理一下回問題所寫的二維陣列排序擴充方法 

static class ArrayExtension
{
public static void Sort(this T[,] array,int d2Idx)
{
int count = array.GetLength(0);

T[] tempArray = new T[count];
for (int idx = 0; idx (this T[,] array, int idx1, int idx2, int targetIdx1, int targetIdx2)
{
T temp;
temp = array[targetIdx1, targetIdx2];
array[targetIdx1, targetIdx2] = array[idx1, idx2];
array[idx1, idx2] = temp;
}

 使用上呼叫Sort方法，並傳入要排序依據的索引即可。