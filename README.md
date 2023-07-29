# 說明

修改原作，改為使用 STRUCTURED_CHAT Agent ，並且想辦法印出所有的內部過程在終端機上，以利觀察。

新增一個 bash_command_tool.py，用來執行 bash command。


# 執行方法

```
uvicorn main:app --host=0.0.0.0 --port=${PORT:-5000}
```
