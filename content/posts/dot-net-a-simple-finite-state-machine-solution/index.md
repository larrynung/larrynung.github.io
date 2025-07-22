---
title: ".NET - A Simple Finite State Machine Solution"
date: "2014-05-15 13:20:00"
description: ".NET - A Simple Finite State Machine Solution"
tags: [.NET, CSharp]
---

想要用實現有限狀態機的功能，看了一下網路上的解決方案以及 State Pattern，覺得都不怎麼適用，因此利用 Tuple 與 Dictionary 去實作了一個簡易又可重複使用的 State Machine：  

```c# 
public sealed class StateMachine
{
    #region  Fields
    Dictionary, TState> _transitions;
    #endregion  Fields

    #region  Properties
    /// 
    /// Gets the m_ transitions.
    /// 
    /// 
    /// The m_ transitions.
    /// 
    private Dictionary, TState> m_Transitions
    {
        get
        {
            return _transitions ?? (_transitions = new Dictionary, TState>());
        }
    }
    /// 
    /// Gets the state of the current.
    /// 
    /// 
    /// The state of the current.
    /// 
    public TState CurrentState { get; private set; }
    #endregion  Properties

    #region  Constructors
    /// 
    /// Initializes a new instance of the  class.
    /// 
    ///  The state.
    public StateMachine(TState state)
    {
        this.CurrentState = state;
    }
    #endregion  Constructors

    #region  Methods
    /// 
    /// Adds the translation.
    /// 
    ///  State of the base.
    ///  The command.
    ///  State of the target.
    /// 
    public StateMachine AddTranslation(TState baseState, TCommand command, TState targetState)
    {
        var key = new Tuple(baseState, command);

        if (m_Transitions.ContainsKey(key))
            throw new Exception("Duplicated translation!!");

        m_Transitions.Add(key, targetState);

        return this;
    }

    /// 
    /// Triggers the command.
    /// 
    ///  The command.
    public void Trigger(TCommand command)
    {
        var key = new Tuple(this.CurrentState, command);

        if (!m_Transitions.ContainsKey(key))
            throw new Exception("Translation not found!!");

        var state = m_Transitions[key];

        this.CurrentState = state;
    }
    #endregion  Methods
}
```

使用時只要宣告狀態的列舉以及用來觸發狀態轉換的命令列舉，然後帶入初始狀態去建立狀態機的物件實體。接著設定狀態機內所內含的狀態轉換，設定時需指定觸發時的狀態、用來觸發的命令、以及轉換後的狀態。最後在程式中適當的時機點插入觸發適當的命令即可，程式寫起來會像下面這樣：

```c# 
public enum Command
{
    Next,
    Reset
}

public enum State
{
    State1,
    State2,
    State3
}

...
var stateMachine = new StateMachine(State.State1)
    .AddTranslation(State.State1, Command.Reset, State.State1)
    .AddTranslation(State.State2, Command.Reset, State.State1)
    .AddTranslation(State.State3, Command.Reset, State.State1)
    .AddTranslation(State.State1, Command.Next, State.State2)
    .AddTranslation(State.State2, Command.Next, State.State3);

Console.WriteLine(stateMachine.CurrentState);

stateMachine.Trigger(Command.Next);
Console.WriteLine(stateMachine.CurrentState);

stateMachine.Trigger(Command.Reset);
Console.WriteLine(stateMachine.CurrentState);
...
```