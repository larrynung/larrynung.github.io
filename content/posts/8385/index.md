---
title: "[WPF]FlowDocument"
date: "2009-05-12 12:02:38"
description: "命名空間 System.Windows.Documents XMLNS http://schemas.microsoft.com/winfx/xaml/presentation Assemble PresentationFramework (在 PresentationFramework.dll)…"
tags: [WPF]
---

## 命名空間

System.Windows.Documents

## XMLNS

http://schemas.microsoft.com/winfx/xaml/presentation

## Assemble

PresentationFramework (在 PresentationFramework.dll)

## 功能

使用進階文件功能裝載及格式化非固定格式內容，例如分頁與欄。

## Paragraph

用來將內容分組成段落的區塊層級非固定格式內容項目。

```
<Paragraph FontSize="18">Flow Format Example</Paragraph>
```

![image_thumb_3.png](/images/posts/8385/image_thumb_3.png)

## List

區塊層級非固定格式內容項目，提供用於呈現排序清單或未排序清單內容的機能。

```
<List>
    <ListItem>
        <Paragraph>ListItem 1</Paragraph>
    </ListItem>
    <ListItem>
        <Paragraph>ListItem 2</Paragraph>
    </ListItem>
    <ListItem>
        <Paragraph>ListItem 3</Paragraph>
    </ListItem>
    <ListItem>
        <Paragraph>ListItem 4</Paragraph>
    </ListItem>
    <ListItem>
        <Paragraph>ListItem 5</Paragraph>
    </ListItem>
</List>
```

![image_thumb_4.png](/images/posts/8385/image_thumb_4.png)

## 範例

```
<Window x:Class="Window1"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    Title="Window1" Height="300" Width="300">
    <FlowDocument
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
>
        <Paragraph FontSize="18">Flow Format Example</Paragraph>

        <Paragraph>
            Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy
      nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi
      enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis
      nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure.
        </Paragraph>
        <Paragraph>
            Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh
      euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim
      ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl
      ut aliquip ex ea commodo consequat. Duis autem vel eum iriure.
        </Paragraph>

        <Paragraph FontSize="18">More flow elements</Paragraph>
        <Paragraph FontSize="15">Inline, font type and weight, and a List</Paragraph>

        <List>
            <ListItem>
                <Paragraph>ListItem 1</Paragraph>
            </ListItem>
            <ListItem>
                <Paragraph>ListItem 2</Paragraph>
            </ListItem>
            <ListItem>
                <Paragraph>ListItem 3</Paragraph>
            </ListItem>
            <ListItem>
                <Paragraph>ListItem 4</Paragraph>
            </ListItem>
            <ListItem>
                <Paragraph>ListItem 5</Paragraph>
            </ListItem>
        </List>

        <Paragraph>
            <Bold>Bolded</Bold>
        </Paragraph>
        <Paragraph>
            <Underline>Underlined</Underline>
        </Paragraph>
        <Paragraph>
            <Bold>
                <Underline>Bolded and Underlined</Underline>
            </Bold>
        </Paragraph>
        <Paragraph>
            <Italic>Italic</Italic>
        </Paragraph>

        <Paragraph>
            <Span>The Span element, no inherent rendering</Span>
        </Paragraph>
        <Paragraph>
            <Run>The Run element, no inherent rendering</Run>
        </Paragraph>

        <Paragraph FontSize="15">Subscript, Superscript</Paragraph>

        <Paragraph>
            <Run Typography.Variants="Superscript">This text is Superscripted.</Run> This text isn't.
        </Paragraph>
        <Paragraph>
            <Run Typography.Variants="Subscript">This text is Subscripted.</Run> This text isn't.
        </Paragraph>
        <Paragraph>
            If a font does not support a particular form (such as Superscript) a default font form will be displayed.
        </Paragraph>

        <Paragraph FontSize="15">Blocks, breaks, paragraph</Paragraph>

        <Section>
            <Paragraph>A block section of text</Paragraph>
        </Section>
        <Section>
            <Paragraph>Another block section of text</Paragraph>
        </Section>

        <Paragraph>
            <LineBreak/>
        </Paragraph>
        <Section>
            <Paragraph>... and another section, preceded by a LineBreak</Paragraph>
        </Section>

        <Section BreakPageBefore="True"/>
        <Section>
            <Paragraph>... and another section, preceded by a PageBreak</Paragraph>
        </Section>

        <Paragraph>Finally, a paragraph. Note the break between this paragraph ...</Paragraph>
        <Paragraph TextIndent="25">... and this paragraph, and also the left indention.</Paragraph>

        <Paragraph>
            <LineBreak/>
        </Paragraph>

    </FlowDocument>

</Window>
```

執行結果

![image_thumb.png](/images/posts/8385/image_thumb.png)

![image_thumb_1.png](/images/posts/8385/image_thumb_1.png)

![image_thumb_2.png](/images/posts/8385/image_thumb_2.png)
