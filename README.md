With this template filter you can highlighter syntax using your favorite WYSIWYG editor on Django.

Dependencies:
===

  - Django >= 1.2
  - pygments
  
How To:
===

This templatefilter is based on **django_pygments** but is done to use it when you has written something with a WYSIWYG editor.

You have to copy the templatetag folder in some **app folder** of your Django project. After that, you can use your template filter like that:

{{ your_text|highlighter }}

Any question, send me an email to antoniomartinromero@gmail.com


Thanks!