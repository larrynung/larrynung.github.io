---
layout: post
title: "MEF - Handle ReflectionTypeLoadException during MEF composition"
date: 2014-02-17 11:08:00
comments: true
categories: [MEF]
keywords: "MEF, DirectoryCatalog, ReflectionTypeLoadException"
description: "MEF - Handle ReflectionTypeLoadException during MEF composition"
---

使用 MEF 去 Compose 指定目錄下的所有 Part，我們可能會像下面這樣透過 DirectoryCatalog 去提供 Export Parts，讓 CompositionContainer 去做 Compose。  

<!-- More -->

{% codeblock lang:c# %}
        private void ComposeCurrentDirectoryParts()
        {
            using (var catalog = new DirectoryCatalog(Environment.CurrentDirectory))
            using (var container = new CompositionContainer(catalog))
            {
                container.ComposeParts(this);
            }
        }
{% endcodeblock %}

<br/>

多半上面這段程式能夠運行良好。但有的時候會發生不如預期的效果，因為 DirectoryCatalog 會去找目錄下指定的檔案，可能會找到一些組件會相依於其它不存在的組件，導致發生 ReflectionTypeLoadException 錯誤。如果你碰到這樣的問題，可以避開使用 DirectoryCatalog，改成自己去遍巡處理，並用 AssemblyCatalog 載入，載入失敗則將之忽略不予處理。像是下面這樣：  

{% codeblock lang:c# %}
    public class SafeDirectoryCatalog : ComposablePartCatalog
    {
		#region Fields 
        private AggregateCatalog _catalog;
		#endregion Fields 

		#region Properties 
        /// <summary>
        /// Gets the catalog.
        /// </summary>
        /// <value>
        /// The catalog.
        /// </value>
        private AggregateCatalog m_Catalog
        {
            get
            {
                return _catalog ?? (_catalog = new AggregateCatalog());
            }
        }
        /// <summary>
        /// Gets the part definitions that are contained in the directory catalog.
        /// </summary>
        /// <returns>The <see cref="T:System.ComponentModel.Composition.Primitives.ComposablePartDefinition" /> objects that are contained in the <see cref="T:System.ComponentModel.Composition.Hosting.DirectoryCatalog" />.</returns>
        public override IQueryable<ComposablePartDefinition> Parts
        {
            get { return m_Catalog.Parts; }
        }
		#endregion Properties 

		#region Constructors 
        /// <summary>
        /// Initializes a new instance of the <see cref="SafeDirectoryCatalog" /> class.
        /// </summary>
        /// <param name="path">Path to the directory to scan for assemblies to add to the catalog.The path must be absolute or relative to <see cref="P:System.AppDomain.BaseDirectory" />.</param>
        /// <param name="searchPattern">The pattern to search with. The format of the pattern should be the same as specified for <see cref="M:System.IO.Directory.GetFiles(System.String,System.String)" />.</param>
        public SafeDirectoryCatalog(string path, string searchPattern)
        {
            var files = Directory.EnumerateFiles(path, searchPattern, SearchOption.TopDirectoryOnly);

            foreach (var file in files)
            {
                try
                {
                    var ac = new AssemblyCatalog(file);

                    if (ac.Parts.Any())
                        m_Catalog.Catalogs.Add(ac);
                }
                catch (ReflectionTypeLoadException)
                {
                }
            }
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="SafeDirectoryCatalog" /> class.
        /// </summary>
        /// <param name="path">Path to the directory to scan for assemblies to add to the catalog.The path must be absolute or relative to <see cref="P:System.AppDomain.BaseDirectory" />.</param>
        public SafeDirectoryCatalog(string path)
            : this(path, "*.dll")
        {
        }
		#endregion Constructors 
    }
{% endcodeblock %}

<br/>

這邊已參閱[Handle ReflectionTypeLoadException during MEF composition - Stack Overflow](http://stackoverflow.com/questions/4144683/handle-reflectiontypeloadexception-during-mef-composition)，將之整理成可重用的類別，使用時只要將本來的 DirectoryCatalog 改成用 SafeDirectoryCatalog 就可以了。  

{% codeblock lang:c# %}
        private void ComposeCurrentDirectoryParts()
        {
            using (var catalog = new SafeDirectoryCatalog(Environment.CurrentDirectory))
            using (var container = new CompositionContainer(catalog))
            {
                container.ComposeParts(this);
            }
        }
{% endcodeblock %}

<br/>

Link
----
* [Handle ReflectionTypeLoadException during MEF composition - Stack Overflow](http://stackoverflow.com/questions/4144683/handle-reflectiontypeloadexception-during-mef-composition)
