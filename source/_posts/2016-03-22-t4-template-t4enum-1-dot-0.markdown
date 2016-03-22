---
layout: post
title: "T4 Template - T4Enum 1.0"
date: 2016-03-22 21:38
comments: true
categories: [T4, T4Enum]
keywords: "T4, T4Enum"
description: "T4 Template - T4Enum 1.0"
---

.NET 列舉的很多操作都會有難以避免的 Boxing/UnBoxing，像是要取得特定列舉值的列舉名，取得所有的列舉名，取得所有的列舉值，取得列舉值的 Attribute，都無法避免 Boxing/UnBoxing 的發生。   

<!-- More -->

<br/>


{% img /images/posts/T4Enum/1.png %}

<br/>


這邊筆者嘗試用 T4 來解這問題，撰寫了如下的 T4 範本：  

{% codeblock lang:c# %}
<#@ template language="C#" debug="true" hostspecific="true"#>
<#@ assembly name="System.Windows.Forms" #>
<#@ assembly name="System.Core" #>
<#@ assembly name="System.Xml" #>
<#@ assembly name="EnvDTE" #>
<#@ assembly name="Microsoft.VisualStudio.OLE.Interop" #>
<#@ assembly name="Microsoft.VisualStudio.Shell" #>
<#@ assembly name="Microsoft.VisualStudio.Shell.Interop" #>
<#@ assembly name="Microsoft.VisualStudio.Shell.Interop.8.0" #>
<#@ import namespace="System.Resources" #>
<#@ import namespace="System.Diagnostics" #>
<#@ import namespace="System.Collections" #>
<#@ import namespace="System.IO" #>
<#@ import namespace="System.Reflection" #>
<#@ import namespace="System.Text" #>
<#@ import namespace="System.Linq" #>
<#@ import namespace="System.Xml" #>
<#@ import namespace="System.Text.RegularExpressions" #>
<#@ import namespace="System.Collections.Generic" #>
<#@ import namespace="Microsoft.VisualStudio.Shell" #>
<#@ import namespace="Microsoft.VisualStudio.Shell.Interop" #>
<#@ import namespace="Microsoft.VisualStudio.TextTemplating" #>
<#@ import namespace="EnvDTE" #>
<#@ output extension=".cs"#>
/**
* T4Enum V1.0
* ---------
* 2016 LarryNung
**/

using System.Collections;
using System.Collections.Generic;
using System.Linq;
<#
foreach(var ns in GetUsingNamespeces())
{
#>
using <#=ns#>;
<#
}
#>

namespace T4Enum
{
    internal abstract class EnumClass<T> : IEnumerable<EnumElement<T>>
    {        	
        private IDictionary<T, EnumElement<T>> _elementPool;
        private string[] _names;
        private T[] _values;

		protected abstract EnumElement<T>[] m_Elements { get; }

        protected IDictionary<T, EnumElement<T>> m_ElementPool
        {
            get { return _elementPool ?? (_elementPool = m_Elements.ToDictionary(item => item.Value)); }
        }

        protected string[] m_Names
        {
            get
            {
                return _names ?? (_names = m_Elements.Select(item => item.Name).ToArray());
            }
        }

        protected T[] m_Values
        {
            get
            {
                return _values ?? (_values = m_Elements.Select(item => item.Value).ToArray());
            }
        }
    	
    	public EnumElement<T> this[int idx] 
    	{ 
    	    get
    		{
    		    return m_Elements[idx];
    		}
    	}
		
        public EnumElement<T> this[T value]
        {
            get
            {
                return GetElement(value);
            }
        }

		public EnumElement<T> GetElement(T value)
        {
            return m_ElementPool[value];
        }

        public string GetName(T value)
        {
            return GetElement(value).Name;
        }

        public string[] GetNames()
        {
            return m_Names;
        }

        public T[] GetValues()
        {
            return m_Values;
        }

        public IEnumerator<EnumElement<T>> GetEnumerator()
        {
            return ((IEnumerable<EnumElement<T>>)m_Elements).GetEnumerator();
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }
    }
    
    internal class EnumElement<T>
    {
        private string _name;
    
        public string Name 
    	{ 
    	    get
    		{
    		    return _name??(_name = string.Empty);
    		} 
    		private set
    		{
    		    _name = value;
    		}
    	}
    	public T Value { get; private set;}
    
    	public EnumElement(string name, T value)
    	{
    	    this.Name = name;
    		this.Value = value;
    	}
    }

<#
    var visualStudio = (this.Host as IServiceProvider).GetService(typeof(EnvDTE.DTE))
                      as EnvDTE.DTE;
  var project = visualStudio.Solution.FindProjectItem(this.Host.TemplateFile)
                                     .ContainingProject as EnvDTE.Project;

	var enumNames = new List<string>();
      foreach(var ns in GetNamespaceElements())
  {
    foreach(var cc in ns.Members.OfType<EnvDTE.CodeElement>())
{
if (cc.Kind != vsCMElement.vsCMElementEnum)
continue;
        var enumClass = (EnvDTE.CodeEnum)cc;
		var enumName = enumClass.Name;

		enumNames.Add(enumName);

#>
    internal sealed class <#= enumName#>EnumClass : EnumClass<<#=enumName#>>
	{
	    private EnumElement<<#=enumName#>>[] _elements;
<#
        var elementPropertyNames = new List<string>();
		foreach (CodeElement member in enumClass.Members)
		{
		var variable = member as CodeVariable;
		var elementName = variable.Name;
		var elementFieldName = "_" + elementName.ToLower();
		var elementPropertyName = elementName;

		elementPropertyNames.Add(elementPropertyName);

#>
		public EnumElement<<#=enumName#>> <#=elementFieldName#>;
        public EnumElement<<#=enumName#>> <#=elementPropertyName#> 
		{
		    get
			{
			    return <#=elementFieldName#>??(<#=elementFieldName#> = new EnumElement<<#=enumName#>>("<#=elementName#>", <#=variable.FullName#>));
			}
		}
<#
}
#>
        protected override EnumElement<<#=enumName#>>[] m_Elements 
		{ 
		    get
			{ 
			    return _elements??(_elements = new EnumElement<<#=enumName#>>[]{<#=String.Join(", ", elementPropertyNames.ToArray())#>});
			}
		}
    }
<#
		}
}
#>

    internal static class Enums
    {
<#
		foreach(var enumName in enumNames)
		{
		var fieldName = "_" + enumName.ToLower();
		var className = enumName + "EnumClass";
#>
		public static <#=className#> <#=fieldName#>;
		public static <#=className#> <#=enumName#>
		{
		    get
			{
			    return <#=fieldName#>??(<#=fieldName#> = new <#=className#>());
			}
		}
<#
		}
#>
	}

	namespace Extensions
	{
<#
		foreach(var enumName in enumNames)
		{
		var className = enumName + "Extension";
#>
	    internal static class <#=className#>
        {
            public static string GetName(this <#=enumName#> e)
            {
                return Enums.<#=enumName#>.GetName(e);
            }
        }
<#}#>
	}
}
<#+
public IEnumerable<string> GetUsingNamespeces()
{
      foreach(var ns in GetNamespaceElements())
  {
    foreach(var cc in ns.Members.OfType<EnvDTE.CodeElement>())
{
if (cc.Kind != vsCMElement.vsCMElementEnum)
continue;
yield return ns.FullName;
yield break;
}}
}
	 public IEnumerable<EnvDTE.CodeNamespace> GetNamespaceElements()
  {
    var visualStudio = (this.Host as IServiceProvider).GetService(typeof(EnvDTE.DTE))
                        as EnvDTE.DTE;
    var project = visualStudio.Solution.FindProjectItem(this.Host.TemplateFile)
                  .ContainingProject as EnvDTE.Project;

    var projItems = new List<EnvDTE.ProjectItem>();
    FillProjectItems(project.ProjectItems, projItems);
    var names = new HashSet<string>(projItems
      .Where(i => i.FileCodeModel != null)
      .SelectMany(i => i.FileCodeModel.CodeElements.OfType<EnvDTE.CodeElement>())
      .Where(e => e.Kind == EnvDTE.vsCMElement.vsCMElementNamespace)
      .Select(e => e.FullName));

    var codeNs = new List<EnvDTE.CodeNamespace>();
    FillCodeNamespaces(project.CodeModel.CodeElements.OfType<EnvDTE.CodeNamespace>(), codeNs);

    return codeNs.Where(ns => names.Contains(ns.FullName));
  }

  public void FillCodeNamespaces(IEnumerable<EnvDTE.CodeNamespace> parents, List<EnvDTE.CodeNamespace> all)
  {
    foreach (var parent in parents)
    {
      all.Add(parent);
      FillCodeNamespaces(parent.Members.OfType<EnvDTE.CodeNamespace>(), all);
    }
  }

  public void FillProjectItems(EnvDTE.ProjectItems items, List<EnvDTE.ProjectItem> ret)
  {
    if (items == null) return;
    foreach(EnvDTE.ProjectItem item in items)
    {
      ret.Add(item);
      FillProjectItems(item.ProjectItems, ret);
    }
  }
#>
{% endcodeblock %}

<br/>


這個 T4 範本可以遍尋專案內的所有列舉，產生對應的輔助類別與擴充方法，藉此避開列舉操作的 Boxing/UnBoxing 問題。實際使用會像是下面這樣：    

{% codeblock lang:c# %}
using System;
using T4Enum;
using T4Enum.Extensions;

namespace ConsoleApplication7
{
    enum Permission
    {
        Function1,
        Function2,
        Function3
    }
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(Enums.Permission.Function1.Name);
            Console.WriteLine((int)Enums.Permission.Function1.Value);

            Console.WriteLine(Enums.Permission[Permission.Function2].Name);
            Console.WriteLine((int)Enums.Permission[Permission.Function2].Value);

            Console.WriteLine(Enums.Permission.GetName(Permission.Function3));
            Console.WriteLine(Permission.Function3.GetName());

            foreach (var item in Enums.Permission)
            {
                Console.WriteLine(item.Name);
                Console.WriteLine((int)item.Value);
            }

            foreach (var name in Enums.Permission.GetNames())
            {
                Console.WriteLine(name);
            }

            foreach (var value in Enums.Permission.GetValues())
            {
                Console.WriteLine((int)value);
            }
        }
    }

}
{% endcodeblock %}

<br/>


運行結果如下：  

{% img /images/posts/T4Enum/2.png %}

<br/>


目前這版已經能取得列舉名，遍尋列舉名，與遍尋列舉值，但尚未支援 Attribute 的取得。  
