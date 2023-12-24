# SorutoBot

移植自[KasumiBot](https://github.com/Kasumi-Games/Kasumi)项目

## dev

**dependencies:**
`python3.10+`
```bash
pip install flask websocket-client PyYAML requests schedule Pillow bestdori-api fuzzywuzzy
```

Bridge实现针对QQ特性：

- 群聊: 
  - [x] 文字消息（自动被动）
  - [x] 富媒体消息（自动被动）（暂不支持音频）
  - [x] 5分钟内爽发（seq自动++）

- 频道: 
  - [x] 文字消息
  - [x] 富媒体消息
  - [x] 5分钟内爽发


- [x] h()函数: 主动选择依赖被动消息的msg_id


