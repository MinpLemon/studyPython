```text
如果是Series转json，默认的orient是’index’，orient可选参数有 {‘split’,’records’,’index’}
如果是DataFrame转json，默认的orient是’columns’，orient可选参数有 {‘split’,’records’,’index’,’columns’,’values’}
json的格式如下 
split，样式为 {index -> [index], columns -> [columns], data -> [values]}
records，样式为[{column -> value}, … , {column -> value}]
index ，样式为 {index -> {column -> value}}
columns，样式为 {index -> {column -> value}}
values，数组样式
table，样式为{‘schema’: {schema}, ‘data’: {data}}，和records类似
```