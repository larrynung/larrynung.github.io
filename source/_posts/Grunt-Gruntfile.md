---
title: Grunt - Gruntfile
date: 2016-09-07 13:53:57
tags: Grunt
---

Gruntfile 的設定可以直接從下面例子來看。  

<!-- More -->

```js
module.exports = function(grunt) { 
  grunt.initConfig({ 
    jshint: { 
      files: ['Gruntfile.js', 'src/**/*.js', 'test/**/*.js'], 
      options: { 
        globals: { 
          jQuery: true 
        } 
      } 
    }
  }); 

  grunt.loadNpmTasks('grunt-contrib-jshint'); 
 
  grunt.registerTask('default', ['jshint']); 
};
```

<br/>


設定大概會分幾個部份，會有 Task 與 Target 的設定，有 npm 套件的載入，以及 Task 的註冊。  

{% asset_img 1.png %}

<br/>


{% asset_img 2.png %}

<br/>


以這例子來說，這邊設定了 jshint task，這個 task 會用 jshint 分析指定的 javascript 的程式。

<br/>


許多套件都會牽扯到檔案的設定，像是上面例子 jshint 要分析的檔案就是要設定的。Grunt 對於檔案設定提供了三種不同的設定方式，分別是 Compact Format、Files Object Format、Files Array Format。  

<br/>


Compact Format 設定方式如下，可指定一組 source 與 destination 檔案。  

```js
grunt.initConfig({ 
  jshint: { 
    foo: { 
      src: ['src/aa.js', 'src/aaa.js'] 
    }, 
  }, 
  concat: { 
    bar: { 
      src: ['src/bb.js', 'src/bbb.js'], 
      dest: 'dest/b.js'
    }, 
  }, 
});
```

<br/>


Files Object Format 設定方式如下，可指定多組 source 與 destination 檔案，`:` 前面是 destination，後面是 source。

```js
grunt.initConfig({ 
  concat: { 
    foo: { 
      files: { 
        'dest/a.js': ['src/aa.js', 'src/aaa.js'],
        'dest/a1.js': ['src/aa1.js', 'src/aaa1.js'], 
      }, 
    }, 
    bar: { 
      files: { 
        'dest/b.js': ['src/bb.js', 'src/bbb.js'], 
        'dest/b1.js': ['src/bb1.js', 'src/bbb1.js'], 
      }, 
    }, 
  }, 
});
```

<br/>


Files Array Format 設定方式如下，除了可指定多組 source 與 destination 檔案外，還能附加額外的屬性。

```js
grunt.initConfig({ 
  concat: { 
    foo: { 
      files: [ 
        {src: ['src/aa.js', 'src/aaa.js'], dest: 'dest/a.js'}, 
        {src: ['src/aa1.js', 'src/aaa1.js'], dest: 'dest/a1.js'}, 
      ], 
    }, 
    bar: { 
      files: [ 
        {src: ['src/bb.js', 'src/bbb.js'], dest: 'dest/b/', nonull: true}, 
        {src: ['src/bb1.js', 'src/bbb1.js'], dest: 'dest/b1/', filter: 'isFile'}, 
      ], 
    }, 
  }, 
});
```

<br/>


Link
----
* [Configuring tasks - Grunt: The JavaScript Task Runner](http://gruntjs.com/configuring-tasks)
