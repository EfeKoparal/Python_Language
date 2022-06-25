"""
strip() , lstrip() ve rstrip()
strip(x) : Stringin başında ve sonunda bulunan x değerlerini siler.

lstrip(x) : Stringin sadece başında bulunan x değerlerini siler.

rstrip(x) : Stringin sadece sonunda bulunan x değerlerini siler.

"                   python                          ".strip() # değer göndermezsek varsayılan olarak boşluk karakteri
'python'
">>>>>>>>>>>>>>Mustafa>>>>>>>>>>>>>>>>>>>>>>>>>>".strip(">")
'Mustafa'
"                            python      ".lstrip()
'python      '
"                            python      ".rstrip()
'                            python'

"""
