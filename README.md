# Contests Calendar

## 项目简介
`Contests Calendar` 是一个用于抓取编程比赛信息的 Python 工具，支持从 Codeforces 和牛客网（NowCoder）获取即将开始的比赛信息，并将比赛的开始时间转换为北京时间，最终将比赛详情保存到桌面的 JSON 文件中。该工具适用于希望以结构化方式跟踪即将开始的比赛的算法竞赛选手。

## 功能
1. **抓取比赛信息**：
   - 从 Codeforces 和牛客网获取比赛详情。
   - 筛选出比赛开始时间在当前日期及之后的比赛。
2. **时间转换**：
   - 将比赛的开始时间从 UTC 转换为北京时间。
3. **数据持久化**：
   - 将比赛信息保存到桌面的 `contests.json` 文件中。
   - 如果文件已存在，会自动合并新数据并去重。

## 使用方法
### 环境依赖
以下库是运行该工具的必要依赖，请确保已安装：

- **Python 3.8 或更高版本**：用于运行脚本。
- **`requests` 库**：用于发送 HTTP 请求，获取比赛信息。
- **`colorama` 库**：用于在终端输出彩色调试信息。
- **`json` 库**：用于处理 JSON 数据，保存比赛信息到文件。
- **`os` 库**：用于操作文件路径。
- **`datetime`、`timezone` 和 `timedelta`**：用于处理时间和时区转换。
安装依赖：
```bash
pip install requests colorama
```
### 配置
1. **替换 API URL**：
   - 在 `get_codeforces_contests()` 函数中，将 `url` 替换为实际的 Codeforces 比赛 API URL。
   - 在 `get_nowcoder_contests()` 函数中，将 `url` 替换为实际的牛客网比赛 API URL。

2. **（可选）修改保存路径**：
   - 默认情况下，比赛信息会保存到桌面的 `contests.json` 文件中。如果需要修改保存路径，请修改 `save_to_json()` 函数中的 `desktop_path`。
### 注意事项
1. **API 限制**：
   - 确保使用的 API URL 是有效的，并且符合目标网站的使用条款。
   - 如果 API 有请求频率限制，请适当调整脚本中的请求间隔。

2. **时间同步**：
   - 该工具将比赛时间从 UTC 转换为北京时间，请确保本地系统时间与网络时间同步。

3. **自动更新**：
   - 如果需要频繁更新比赛信息，可以将脚本设置为定时任务（例如使用 Linux/macOS 的 `cron` 或 Windows 的任务计划程序）。
### 运行脚本
运行脚本：
```bash
python contestsCalendar.py
```
运行后，脚本会抓取比赛信息并保存到桌面的 `contests.json` 文件中。如果文件已存在，会自动合并新数据并去重。
### 输出文件格式
保存的 `contests.json` 文件是一个 JSON 格式的列表，每个比赛信息包含以下字段：
```json
[
    {
        "id": "比赛 ID",
        "name": "比赛名称",
        "startTime": "比赛开始时间（北京时间，格式为 YYYY-MM-DD HH:MM:SS）",
        "type": "比赛类型（例如：Codeforces 或 NowCoder）",
        "phase": "比赛状态（例如：BEFORE）",
        "durationSeconds": "比赛持续时间（格式为 HH:MM:SS）"
    }
]
```
