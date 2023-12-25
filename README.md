# SorutoBot

修改自[KasumiBot](https://github.com/Kasumi-Games/Kasumi)项目

## dev

**dependencies:**
`python3.10+`

### Windows 安装(powershell)

```bash
python -m venv venv & .\venv\bin\activate # 创建并启用虚拟环境(可选)
pip install -r requirements.txt # 安装依赖环境
```

### Linux 安装

```bash
python -m venv venv && source venv/bin/activate # 创建并启用虚拟环境(可选)
pip install -r requirements.txt # 安装依赖环境
```

### 不使用虚拟环境(不推荐)

```bash
pip install -r requirements.txt # 安装依赖环境
```

Bridge实现针对QQ特性：

-   群聊:

    -   [x] 文字消息（自动被动）
    -   [x] 富媒体消息（自动被动）（暂不支持音频）
    -   [x] 5分钟内爽发（seq自动++）

-   频道:

    -   [x] 文字消息
    -   [x] 富媒体消息
    -   [x] 5分钟内爽发

-   [x] `h()`函数: 主动选择依赖被动消息的msg_id
