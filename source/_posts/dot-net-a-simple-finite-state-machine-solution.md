---
layout: post
title: ".NET - A Simple Finite State Machine Solution"
date: 2014-05-15 13:20:00
comments: true
tags: [.NET, C#]
keywords: "State Machine, C#, .NET"
description: ".NET - A Simple Finite State Machine Solution"
---

想要用實現有限狀態機的功能，看了一下網路上的解決方案以及 State Pattern，覺得都不怎麼適用，因此利用 Tuple 與 Dictionary 去實作了一個簡易又可重複使用的 State Machine：  

<!-- More -->

{% codeblock lang:c# %} 
public sealed class StateMachine<TState, TCommand>
{
    #region  Fields
    Dictionary<Tuple<TState, TCommand>, TState> _transitions;
    #endregion  Fields

    #region  Properties
    /// <summary>
    /// Gets the m_ transitions.
    /// </summary>
    /// <value>
    /// The m_ transitions.
    /// </value>
    private Dictionary<Tuple<TState, TCommand>, TState> m_Transitions
    {
        get
        {
            return _transitions ?? (_transitions = new Dictionary<Tuple<TState, TCommand>, TState>());
        }
    }
    /// <summary>
    /// Gets the state of the current.
    /// </summary>
    /// <value>
    /// The state of the current.
    /// </value>
    public TState CurrentState { get; private set; }
    #endregion  Properties

    #region  Constructors
    /// <summary>
    /// Initializes a new instance of the <see cref="StateMachine{TState, TCommand}"/> class.
    /// </summary>
    /// <param name="state"> The state.</param>
    public StateMachine(TState state)
    {
        this.CurrentState = state;
    }
    #endregion  Constructors

    #region  Methods
    /// <summary>
    /// Adds the translation.
    /// </summary>
    /// <param name="baseState"> State of the base.</param>
    /// <param name="command"> The command.</param>
    /// <param name="targetState"> State of the target.</param>
    /// <returns></returns>
    public StateMachine<TState, TCommand> AddTranslation(TState baseState, TCommand command, TState targetState)
    {
        var key = new Tuple<TState, TCommand>(baseState, command);

        if (m_Transitions.ContainsKey(key))
            throw new Exception("Duplicated translation!!");

        m_Transitions.Add(key, targetState);

        return this;
    }

    /// <summary>
    /// Triggers the command.
    /// </summary>
    /// <param name="command"> The command.</param>
    public void Trigger(TCommand command)
    {
        var key = new Tuple<TState, TCommand>(this.CurrentState, command);

        if (!m_Transitions.ContainsKey(key))
            throw new Exception("Translation not found!!");

        var state = m_Transitions[key];

        this.CurrentState = state;
    }
    #endregion  Methods
}
{% endcodeblock %}


使用時只要宣告狀態的列舉以及用來觸發狀態轉換的命令列舉，然後帶入初始狀態去建立狀態機的物件實體。接著設定狀態機內所內含的狀態轉換，設定時需指定觸發時的狀態、用來觸發的命令、以及轉換後的狀態。最後在程式中適當的時機點插入觸發適當的命令即可，程式寫起來會像下面這樣：

{% codeblock lang:c# %} 
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
var stateMachine = new StateMachine<State, Command>(State.State1)
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
{% endcodeblock %}
